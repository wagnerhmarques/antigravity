#!/usr/bin/env python3
"""
Watcher Daemon para LLM Wiki (Karpathy Pattern - Multimodal & In-Place Query Responders)
Monitora as pastas:
  - raw/     -> Ingestão automática de fontes (Markdown, TXT e PDF)
  - queries/ -> Resposta contextual incorporada DIRETAMENTE na própria nota

Blindagens e Otimizações de Alto Nível:
1. RAG Semântico Híbrido (semantic_retriever.py): Seleção precisa de Top-K documentos relevantes.
2. Git Auto-Snapshot (git_backup.py): Versionamento local silencioso para restauração em 1 clique.
3. Propagação Reversa com Filtro Inteligente de Relevância e Fila Anti-Rate-Limit (Zero Erros 429).
4. Blindagem contra arquivos virtuais desidratados .icloud e travas [Errno 1] do macOS.
5. ZERO DUPLICAÇÃO DE TÍTULO: O corpo do arquivo inicia DIRETO na barra de metadados.
6. Rigor LaTeX Absoluto: Preservação e fechamento perfeito de comandos KaTeX.
"""

import os
import re
import sys
import time
import json
import datetime
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv
import json5

# Importações seguras do SDK Google GenAI
from google import genai
from google.genai import types

# Carregar variáveis de ambiente
load_dotenv()

VAULT_DIR = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me")
SCRATCH_DIR = Path("/Users/user/.gemini/antigravity-ide/scratch")
TAXONOMIA_FILE = SCRATCH_DIR / "configAG" / "TAXONOMIA_CANONICA.json"

try:
    from semantic_retriever import retrieve_relevant_context, update_vault_embeddings
except Exception:
    retrieve_relevant_context = None
    update_vault_embeddings = None

try:
    from git_backup import run_git_snapshot
except Exception:
    run_git_snapshot = None

# Garantir diretórios base no Vault e Scratch
for base in [VAULT_DIR, SCRATCH_DIR]:
    (base / "configAG").mkdir(parents=True, exist_ok=True)
    (base / "raw" / "assets").mkdir(parents=True, exist_ok=True)
    (base / "queries").mkdir(parents=True, exist_ok=True)
    (base / "wiki" / "fontes").mkdir(parents=True, exist_ok=True)
    (base / "wiki" / "conceitos").mkdir(parents=True, exist_ok=True)
    (base / "wiki" / "tecnologias").mkdir(parents=True, exist_ok=True)
    (base / "wiki" / "sinteses").mkdir(parents=True, exist_ok=True)

PROCESSED_RAW_LOG = SCRATCH_DIR / ".processed_files.json"
PROCESSED_QUERY_LOG = SCRATCH_DIR / ".processed_queries.json"

def get_processed_list(log_path: Path):
    if log_path.exists():
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def mark_item_processed(log_path: Path, item: str):
    items = get_processed_list(log_path)
    if item not in items:
        items.append(item)
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)

def safe_atomic_write(target_path: Path, content: str):
    """Escreve via arquivo temporário com substituição atômica (resistente a travas do iCloud Drive)."""
    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        temp_file = target_path.parent / f".tmp_{target_path.name}_{int(time.time()*1000)}"
        temp_file.write_text(content, encoding="utf-8")
        os.replace(temp_file, target_path)
    except Exception:
        try:
            target_path.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"⚠️ Erro ao salvar arquivo {target_path}: {e}")

def load_taxonomy():
    if not TAXONOMIA_FILE.exists():
        return {}
    try:
        with open(TAXONOMIA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_taxonomy(tax: dict):
    for base in [SCRATCH_DIR, VAULT_DIR]:
        dest = base / "configAG" / "TAXONOMIA_CANONICA.json"
        try:
            safe_atomic_write(dest, json.dumps(tax, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"Aviso ao salvar taxonomia em {dest}: {e}")

def build_alias_map():
    tax = load_taxonomy()
    alias_map = {}
    for canonical, data in tax.items():
        alias_map[canonical.lower()] = canonical
        for a in data.get("aliases", []):
            alias_map[a.lower().strip()] = canonical
            norm = re.sub(r'[^a-zA-Z0-9]', '', a.lower())
            if norm:
                alias_map[norm] = canonical
    return alias_map

def normalize_links(text: str) -> str:
    alias_map = build_alias_map()
    if not alias_map:
        return text

    def replace_link(match):
        full_match = match.group(0)
        inner = match.group(1).strip()
        if not inner or inner.startswith("queries/") or inner.startswith("http"):
            return full_match
        parts = inner.split("|")
        target = parts[0].split("#")[0].strip()
        anchor = ("#" + parts[0].split("#")[1].strip()) if "#" in parts[0] else ""
        alias = parts[1].strip() if len(parts) > 1 else None

        target_lower = target.lower()
        target_norm = re.sub(r'[^a-zA-Z0-9]', '', target_lower)
        canonical = alias_map.get(target_lower) or alias_map.get(target_norm)
        if canonical:
            if alias:
                return f"[[{canonical}{anchor}|{alias}]]"
            elif target != canonical:
                return f"[[{canonical}{anchor}|{target}]]"
            else:
                return f"[[{canonical}{anchor}]]"
        return full_match

    return re.sub(r'\[\[(.*?)\]\]', replace_link, text)

# ==========================================
# SANITIZADOR DE LATEX RIGOROSO
# ==========================================
MATH_RESTORATION_MAP = [
    (r'\\heta\b', r'\\theta'),
    (r'\\au\b', r'\\tau'),
    (r'\\imes\b', r'\\times'),
    (r'\\ext\{', r'\\text{'),
    (r'\\rac\{', r'\\frac{'),
    (r'\\ilde\{', r'\\tilde{'),
    (r'\\egin\{', r'\\begin{'),
    (r'\\abla\b', r'\\nabla'),
    (r'\\ight\b', r'\\right'),
    (r'\\op\b', r'\\top'),
    (r'\\an\b', r'\\tan'),
    (r'\\anh\b', r'\\tanh'),
    (r'\\ag\b', r'\\tag'),
    (r'\\riangle\b', r'\\triangle'),
    (r'\\herefore\b', r'\\therefore'),
    (r'\\left\s*\{', r'\\left\\{'),
    (r'\\right\s*\}', r'\\right\\}'),
]

LATEX_COMMANDS = [
    "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta",
    "theta", "vartheta", "iota", "kappa", "lambda", "mu", "nu", "xi",
    "pi", "varpi", "rho", "varrho", "sigma", "varsigma", "tau", "upsilon",
    "phi", "varphi", "chi", "psi", "omega",
    "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Upsilon", "Phi", "Psi", "Omega",
    "sum", "prod", "coprod", "int", "iint", "iiint", "oint", "sqrt",
    "frac", "tfrac", "dfrac", "partial", "nabla", "infty",
    "sin", "cos", "tan", "cot", "sec", "csc", "arcsin", "arccos", "arctan",
    "sinh", "cosh", "tanh", "coth", "exp", "log", "ln", "det", "dim",
    "max", "min", "sup", "inf", "lim", "liminf", "limsup",
    "cdot", "times", "div", "pm", "mp", "circ", "bullet", "approx", "sim", "simeq",
    "cong", "equiv", "le", "leq", "ge", "geq", "neq", "ne", "in", "notin",
    "subset", "subseteq", "supset", "supseteq", "to", "rightarrow", "leftarrow",
    "Rightarrow", "Leftarrow", "Leftrightarrow", "leftrightarrow", "mapsto",
    "forall", "exists", "neg", "vee", "wedge", "oplus", "otimes",
    "left", "right", "mathbf", "mathit", "mathrm", "mathcal", "mathbb", "text",
    "Big", "big", "Bigg", "bigg", "begin", "end", "tilde", "bar", "top", "tag"
]

def sanitize_math_expression(math_str: str) -> str:
    for pat, repl in MATH_RESTORATION_MAP:
        math_str = re.sub(pat, repl, math_str)

    math_str = re.sub(r'\\left\s*\{', r'\\left\\{', math_str)
    math_str = re.sub(r'\\right\s*\}', r'\\right\\}', math_str)
    math_str = re.sub(r'\\righta\b', r'\\rightarrow', math_str)

    math_str = re.sub(r',\s*,', ',', math_str)
    math_str = re.sub(r'\\\\,', r'\\,', math_str)
    math_str = re.sub(r'\s*,\s*d([a-zA-Z])', r'\\, d\1', math_str)
    math_str = re.sub(r'd\\theta', r'\\, d\\theta', math_str)

    parts = re.split(r'(\\text\{.*?\})', math_str)
    new_parts = []
    for p in parts:
        if p.startswith(r'\text{'):
            new_parts.append(p)
        else:
            cur = p
            for cmd in LATEX_COMMANDS:
                cur = re.sub(r'(?<![\\a-zA-Z])' + cmd + r'(?![a-zA-Z])', r'\\' + cmd, cur)
            new_parts.append(cur)
    math_str = "".join(new_parts)

    math_str = re.sub(r'\\\\([a-zA-Z]+)', r'\\\1', math_str)
    math_str = re.sub(r'\\delta_x', r'\\Delta_x', math_str)
    math_str = re.sub(r'\\delta_y', r'\\Delta_y', math_str)
    math_str = re.sub(r'\\int\s*\\int', r'\\iint', math_str)

    return math_str.strip()

def fix_all_latex_in_text(text: str) -> str:
    text = text.replace(r"\n", "\n")

    def replace_display_math(match):
        inner = match.group(1).strip()
        lines = [l.strip() for l in inner.split("\n") if l.strip()]
        if len(lines) > 1 and not any(env in inner for env in ["aligned", "matrix", "cases", "array", "begin", "gather"]):
            return "\n\n".join([f"$$\n{sanitize_math_expression(l)}\n$$" for l in lines])
        cleaned = sanitize_math_expression(inner)
        return f"\n$$\n{cleaned}\n$$\n"

    text = re.sub(r'\$\$(.*?)\$\$', replace_display_math, text, flags=re.DOTALL)

    def replace_inline_math(match):
        inner = match.group(1)
        if re.match(r'^\d+(\.\d+)?$', inner.strip()):
            return f"${inner}$"
        cleaned = sanitize_math_expression(inner)
        return f"${cleaned}$"

    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', replace_inline_math, text)
    text = re.sub(r'\n\$\$\s*\$\$\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def robust_parse_json(raw_text: str):
    text = raw_text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    # Pre-process JSON text: double backslashes on all LaTeX commands so JSON parser preserves them
    for cmd in sorted(LATEX_COMMANDS, key=len, reverse=True):
        pattern = r"(?<!\\)\\" + cmd + r"(?![a-zA-Z])"
        text = re.sub(pattern, r"\\\\" + cmd, text)

    # Double backslash on isolated LaTeX operators
    text = re.sub(r"(?<!\\)\\{", r"\\\\{", text)
    text = re.sub(r"(?<!\\)\\}", r"\\\\}", text)
    text = re.sub(r"(?<!\\)\\,", r"\\\\,", text)

    try:
        return json.loads(text, strict=False)
    except Exception:
        pass

    try:
        return json5.loads(text)
    except Exception as e:
        raise ValueError(f"Falha ao decodificar JSON: {e}")

def sync_to_all(rel_path: str, content: str):
    sanitized = fix_all_latex_in_text(normalize_links(content))
    for base in [VAULT_DIR, SCRATCH_DIR]:
        target = base / rel_path
        safe_atomic_write(target, sanitized)

def append_to_log(action_str: str, details: str):
    today = datetime.date.today().isoformat()
    entry = f"\n\n---\n\n## [{today}] {action_str}\n{details}"
    for base in [VAULT_DIR, SCRATCH_DIR]:
        for loc in [base / "configAG" / "log.md", base / "log.md"]:
            if loc.exists():
                try:
                    txt = loc.read_text(encoding="utf-8")
                    safe_atomic_write(loc, txt + entry)
                except Exception:
                    pass

def update_index_sources(slug: str, titulo: str, resumo: str):
    for base in [SCRATCH_DIR, VAULT_DIR]:
        for idx in [base / "configAG" / "index.md", base / "index.md"]:
            if not idx.exists():
                continue
            try:
                content = idx.read_text(encoding="utf-8")
                nova_linha = f"\n- [[{slug}]] — *{titulo}*: {resumo}"
                if f"[[{slug}]]" in content:
                    continue
                if "## 📚 Fontes Ingeridas" in content:
                    parts = content.split("## 📚 Fontes Ingeridas (`wiki/fontes/`)")
                    if len(parts) == 2:
                        updated = parts[0] + "## 📚 Fontes Ingeridas (`wiki/fontes/`)" + nova_linha + parts[1]
                    else:
                        updated = content + nova_linha
                else:
                    updated = content + nova_linha
                safe_atomic_write(idx, updated)
            except Exception:
                pass

def update_index_queries(note_title: str, resumo: str):
    for base in [SCRATCH_DIR, VAULT_DIR]:
        for idx in [base / "configAG" / "index.md", base / "index.md"]:
            if not idx.exists():
                continue
            try:
                content = idx.read_text(encoding="utf-8")
                nova_linha = f"\n- [[queries/{note_title}]] — {resumo}"
                if f"[[queries/{note_title}]]" in content or f"[[{note_title}]]" in content:
                    continue
                if "## 💡 Consultas & Sínteses" in content:
                    parts = content.split("## 💡 Consultas & Sínteses (`queries/`)")
                    if len(parts) == 2:
                        updated = parts[0] + "## 💡 Consultas & Sínteses (`queries/`)" + nova_linha + parts[1]
                    else:
                        updated = content + nova_linha
                else:
                    section_header = "\n\n---\n\n## 💡 Consultas & Sínteses (`queries/`)\n"
                    updated = content + section_header + nova_linha
                safe_atomic_write(idx, updated)
            except Exception:
                pass

def notify_user(title: str, message: str):
    try:
        script = f'display notification "{message}" with title "{title}"'
        subprocess.Popen(["osascript", "-e", script])
    except Exception:
        pass

# ==========================================
# PROPAGAÇÃO INTELIGENTE COM FILTRO E FILA ANTI-RATE-LIMIT
# ==========================================
def propagate_source_to_existing_notes(client, slug_fonte: str, titulo_fonte: str, conteudo_fonte: str):
    print(f"\n🔄 [Auto-Evolução] Analisando relevância de '{titulo_fonte}' para dúvidas do pesquisador...")

    queries_dir = VAULT_DIR / "queries"
    if not queries_dir.exists():
        queries_dir = SCRATCH_DIR / "queries"

    query_files = [f for f in queries_dir.glob("*.md") if not f.name.startswith(".") and not f.name.endswith(".icloud")]
    if not query_files:
        return

    # Pré-filtro léxico e temático para classificar relevância e evitar chamadas desnecessárias
    fonte_tokens = set(re.findall(r'[a-zA-Z0-9_\-]{4,}', (titulo_fonte + " " + conteudo_fonte[:2000]).lower()))
    
    scored_queries = []
    for qfile in query_files:
        try:
            q_stem = qfile.stem.strip()
            q_txt = qfile.read_text(encoding="utf-8")

            if f"Atualização a partir de [[{slug_fonte}]]" in q_txt:
                continue

            q_tokens = set(re.findall(r'[a-zA-Z0-9_\-]{4,}', (q_stem + " " + q_txt[:1000]).lower()))
            overlap = len(fonte_tokens.intersection(q_tokens))
            scored_queries.append((overlap, qfile, q_stem, q_txt))
        except Exception:
            continue

    # Avaliar apenas as Top-4 consultas com maior sobreposição temática
    scored_queries.sort(key=lambda x: x[0], reverse=True)
    top_candidates = [item for item in scored_queries[:4] if item[0] >= 2]

    if not top_candidates:
        print("ℹ️ [Auto-Evolução] Nenhuma consulta existente requer incremento direto desta fonte.")
        return

    print(f"🎯 [Auto-Evolução] Avaliando as {len(top_candidates)} consultas mais correlacionadas com intervalo seguro...")

    for _, qfile, q_stem, q_txt in top_candidates:
        try:
            prompt_eval = f"""Você é o pesquisador assistente e mantenedor da LLM Wiki de Física Médica & TC.

NOTA DE CONSULTA EXISTENTE:
TÍTULO: "{q_stem}"
CONTEÚDO:
{q_txt[:2500]}

---

NOVA FONTE CIENTÍFICA NO ACERVO:
TÍTULO: "{titulo_fonte}"
SLUG: "{slug_fonte}"
CONTEÚDO:
{conteudo_fonte[:4000]}

Sua tarefa:
Avalie se esta NOVA FONTE traz dados novos, métricas, algoritmos ou evidências que ENRIQUEÇAM a nota "{q_stem}".

Regras:
1. Se não agregar valor técnico específico: retorne "relevante": false.
2. Se agregar: retorne "relevante": true e forneça um incremento conciso em "incremento_markdown".
   Comece EXATAMENTE com: ### 🔄 Atualização a partir de [[{slug_fonte}]] ({titulo_fonte}):

Retorne um JSON ESTRUTURADO:
{{
  "relevante": true,
  "incremento_markdown": "### 🔄 Atualização a partir de [[{slug_fonte}]] ({titulo_fonte}):\\n\\n- ..."
}}
"""

            response = None
            for candidate in ["gemini-3.7-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite"]:
                try:
                    response = client.models.generate_content(
                        model=candidate,
                        contents=prompt_eval,
                        config=types.GenerateContentConfig(response_mime_type="application/json")
                    )
                    break
                except Exception:
                    continue

            if not response or not response.text:
                time.sleep(2.0)
                continue

            data = robust_parse_json(response.text)
            if data.get("relevante") and data.get("incremento_markdown"):
                inc_text = fix_all_latex_in_text(normalize_links(data["incremento_markdown"].strip()))
                
                updated_txt = q_txt
                if "> 📅 **Data:**" in updated_txt and f"[[{slug_fonte}]]" not in updated_txt:
                    updated_txt = re.sub(
                        r"(> 📅 \*\*Data:\*\*.*?\| 🔗 \*\*Conexões:\*\*.*?)\n",
                        r"\1, [[" + slug_fonte + "]]\n",
                        updated_txt
                    )
                
                updated_txt = updated_txt.strip() + "\n\n" + inc_text + "\n"
                sync_to_all(f"queries/{qfile.name}", updated_txt)
                append_to_log(f"evolution | queries/{q_stem}", f"- Enriquecida com novos achados de `[[{slug_fonte}]]`")
                print(f"✨ [Auto-Evolução] Nota '{q_stem}' enriquecida com achados de [[{slug_fonte}]]!")
                notify_user("LLM Wiki 💡", f"Nota '{q_stem[:30]}' enriquecida!")

            # Pausa de segurança anti-rate-limit entre requisições
            time.sleep(2.5)

        except Exception as e:
            print(f"Aviso na propagação para {qfile.name}: {e}")

# ==========================================
# 1. PROCESSAMENTO DE FONTES BRUTAS (raw/)
# ==========================================
def process_raw_file(raw_file_path: Path):
    valid_exts = [".md", ".txt", ".pdf"]
    if not raw_file_path.exists() or raw_file_path.suffix.lower() not in valid_exts:
        return

    filename = raw_file_path.name
    if filename.startswith(".") or filename.endswith(".icloud") or filename in get_processed_list(PROCESSED_RAW_LOG):
        return

    print(f"\n[Watcher - Raw] 🔍 Novo documento bruto detectado: {filename}")
    time.sleep(2.0)

    try:
        scratch_raw = SCRATCH_DIR / "raw" / filename
        if not scratch_raw.exists():
            scratch_raw.parent.mkdir(parents=True, exist_ok=True)
            scratch_raw.write_bytes(raw_file_path.read_bytes())
    except Exception as sync_err:
        print(f"[Watcher - Raw] Aviso ao sincronizar cópia local: {sync_err}")

    is_pdf = raw_file_path.suffix.lower() == ".pdf"
    content_text = ""
    pdf_bytes = None

    if is_pdf:
        try:
            pdf_bytes = raw_file_path.read_bytes()
            if len(pdf_bytes) == 0:
                return
        except Exception as e:
            print(f"[Watcher - Raw] Erro ao ler PDF: {e}")
            return
    else:
        for _ in range(5):
            try:
                content_text = raw_file_path.read_text(encoding="utf-8")
                break
            except Exception:
                time.sleep(0.5)

        if not content_text.strip():
            return

        # Detecção e enriquecimento automático de links do YouTube
        if not is_pdf and "## 📜 Transcrição Completa" not in content_text:
            try:
                from youtube_helper import extract_video_id, fetch_video_metadata, fetch_youtube_transcript, build_raw_markdown
                yt_id = extract_video_id(content_text.strip())
                if yt_id:
                    print(f"[Watcher - Raw] 🎬 Link do YouTube detectado: {yt_id}. Baixando transcrição...")
                    yt_meta = fetch_video_metadata(yt_id)
                    yt_trans = fetch_youtube_transcript(yt_id)
                    content_text = build_raw_markdown(yt_meta, yt_trans)
                    safe_atomic_write(raw_file_path, content_text)
                    if scratch_raw != raw_file_path:
                        safe_atomic_write(scratch_raw, content_text)
                    print(f"[Watcher - Raw] ✅ Transcrição do YouTube incorporada com sucesso ao raw.")
            except Exception as yt_err:
                print(f"[Watcher - Raw] Aviso na extração do YouTube: {yt_err}")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[Watcher] ⚠️ GEMINI_API_KEY não configurada!")
        return

    try:
        client = genai.Client(api_key=api_key)

        print("[Watcher - Raw] ⚡ Analisando documento e gerando ficha analítica...")

        spark_path = SCRATCH_DIR / "configAG" / "SPARK.md"
        if not spark_path.exists():
            spark_path = SCRATCH_DIR / "SPARK.md"
        spark_content = spark_path.read_text(encoding="utf-8") if spark_path.exists() else ""

        system_instruction = f"""Você é o mantenedor de uma LLM Wiki científica pessoal seguindo o paradigma Karpathy.
Siga rigorosamente as instruções do SPARK.md:

---
{spark_content}
---
"""

        prompt_task = f"""FONTE BRUTA RECEBIDA: `{filename}`

Sua tarefa:
1. Analisar profundamente o documento (seja artigo/projeto em PDF ou notas em Markdown).
2. Criar a ficha analítica da fonte em markdown para `wiki/fontes/<slug-da-fonte>.md` com YAML frontmatter completo (`tipo: fonte`, etc.), Resumo Executivo, Dados Quantitativos, Fórmulas e Wikilinks `[[...]]`.
3. Extrair conceitos essenciais, grandezas ou inovações tecnológicas, gerando páginas dedicadas com wikilinks `[[Nome-da-Pagina]]` e `tipo: conceito` ou `tipo: tecnologia`.
4. Formatar equações matemáticas em LaTeX rigoroso ($...$ para inline e $$...$$ para blocos isolados).
5. TAXONOMIA PADRONIZADA: Utilize os slugs canônicos do SPARK.md.
6. Retornar um JSON ESTRUTURADO.
"""

        contents = []
        if is_pdf:
            pdf_part = types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")
            contents = [pdf_part, system_instruction + "\n\n" + prompt_task]
        else:
            contents = [system_instruction + "\n\n" + f"CONTEÚDO DA FONTE BRUTA ({filename}):\n\n{content_text}\n\n" + prompt_task]

        response = None
        for candidate in ["gemini-3.7-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite"]:
            try:
                response = client.models.generate_content(
                    model=candidate,
                    contents=contents,
                    config=types.GenerateContentConfig(response_mime_type="application/json")
                )
                print(f"[Watcher - Raw] 🎯 Processado pelo modelo: {candidate}")
                break
            except Exception as model_err:
                err_str = str(model_err)
                if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                    time.sleep(10)
                continue

        if not response or not response.text:
            return

        data = robust_parse_json(response.text)

        fonte_info = data["arquivo_fonte"]
        sync_to_all(fonte_info["caminho"], fonte_info["conteudo"])
        print(f"[Watcher - Raw] ✅ Ficha criada: {fonte_info['caminho']}")

        for page in data.get("paginas_conceitos", []):
            tipo = page.get("tipo", "conceito")
            caminho = f"wiki/{tipo}s/{page['slug']}.md"
            sync_to_all(caminho, page["conteudo"])
            print(f"[Watcher - Raw] 📄 Página criada: {caminho}")

        update_index_sources(data["slug_fonte"], data["titulo_fonte"], data.get("resumo_index", ""))
        log_text = f"- **Fonte processada:** `{filename}`\n" + data.get("log_detalhes", "")
        append_to_log(f"ingest | {data['titulo_fonte']}", log_text)

        # Atualizar cache RAG e disparar snapshot Git
        if update_vault_embeddings:
            update_vault_embeddings(client)

        # Propagação com filtro e fila inteligente
        propagate_source_to_existing_notes(client, data["slug_fonte"], data["titulo_fonte"], fonte_info["conteudo"])

        if run_git_snapshot:
            run_git_snapshot(f"ingest source: {data['slug_fonte']}")

        mark_item_processed(PROCESSED_RAW_LOG, filename)
        print(f"[Watcher - Raw] ✨ Ingestão e Auto-Evolução concluídas para: {filename}\n")

    except Exception as e:
        print(f"[Watcher - Raw] ❌ Erro: {e}")

# ==========================================
# 2. PROCESSAMENTO DE CONSULTAS (queries/)
# ==========================================
def process_query_file(query_file_path: Path):
    if not query_file_path.exists() or query_file_path.suffix.lower() not in [".md", ".txt"]:
        return

    filename = query_file_path.name
    if filename.startswith(".") or filename.endswith(".icloud"):
        return

    time.sleep(1.5)

    query_text = ""
    for _ in range(5):
        try:
            query_text = query_file_path.read_text(encoding="utf-8")
            break
        except Exception:
            time.sleep(0.5)

    if "> 📅 **Data:**" in query_text or "⏳ **LLM Wiki:**" in query_text:
        return

    clean_stem = query_file_path.stem.strip()
    if clean_stem.lower() in ["sem título", "untitled"] and not query_text.strip():
        return

    print(f"\n[Watcher - Query] 💬 Nova pergunta detectada: {filename}")

    # Verificar se a nota contém link do YouTube
    from youtube_helper import (
        extract_video_id,
        fetch_video_metadata,
        fetch_youtube_transcript
    )

    yt_id = extract_video_id(query_text) or extract_video_id(clean_stem)
    is_youtube = yt_id is not None
    yt_meta = None
    yt_trans = None

    if is_youtube:
        print(f"[Watcher - Query] 🎬 Link do YouTube detectado: {yt_id}. Baixando transcrição...")
        try:
            yt_meta = fetch_video_metadata(yt_id)
            yt_trans = fetch_youtube_transcript(yt_id)
            print(f"[Watcher - Query] ✅ Transcrição do vídeo obtida ({len(yt_trans.get('raw_entries', []))} falas).")
        except Exception as yt_err:
            print(f"[Watcher - Query] ⚠️ Erro ao obter transcrição do YouTube: {yt_err}")
            is_youtube = False

    cleaned_user_notes = query_text.strip()
    if cleaned_user_notes.startswith("# "):
        parts = cleaned_user_notes.split("\n", 1)
        first_h1 = parts[0].replace("# ", "").strip()
        if first_h1.lower() == clean_stem.lower() or first_h1.lower() in clean_stem.lower():
            cleaned_user_notes = parts[1].strip() if len(parts) > 1 else ""

    if is_youtube and yt_meta:
        effective_query = f"Interpretação e Análise do Vídeo: {yt_meta.get('title', clean_stem)}"
        if cleaned_user_notes:
            effective_query += f"\n\nObservações e perguntas do pesquisador sobre o vídeo:\n{cleaned_user_notes}"
    else:
        effective_query = f"Pergunta: {clean_stem}"
        if cleaned_user_notes:
            effective_query += f"\n\nContexto adicional fornecido pelo pesquisador:\n{cleaned_user_notes}"

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[Watcher] ⚠️ GEMINI_API_KEY não configurada!")
        return

    try:
        client = genai.Client(api_key=api_key)

        print("[Watcher - Query] ⚡ Consultando acervo via RAG Semântico...")

        spark_path = SCRATCH_DIR / "configAG" / "SPARK.md"
        if not spark_path.exists():
            spark_path = SCRATCH_DIR / "SPARK.md"
        spark_content = spark_path.read_text(encoding="utf-8") if spark_path.exists() else ""

        if retrieve_relevant_context:
            wiki_context = retrieve_relevant_context(effective_query, top_k=10, client=client)
        else:
            wiki_context = ""
            for wf in (SCRATCH_DIR / "wiki").rglob("*.md"):
                if not wf.name.startswith(".") and not wf.name.endswith(".icloud"):
                    try:
                        rel = wf.relative_to(SCRATCH_DIR)
                        txt = wf.read_text(encoding="utf-8")
                        wiki_context += f"\n\n--- DOCUMENTO: `{rel}` ---\n{txt}\n"
                    except Exception:
                        pass

        today_str = datetime.date.today().isoformat()

        if is_youtube and yt_meta and yt_trans:
            prompt_query = f"""Você é o pesquisador assistente e mantenedor desta LLM Wiki de Física Médica, Ciência de Dados & Tomografia Computadorizada.

ESQUEMA DA WIKI E TAXONOMIA PADRONIZADA (SPARK.md):
{spark_content}

DOCUMENTOS MAIS RELEVANTES RECUPERADOS DO COFRE:
{wiki_context}

---

VÍDEO DO YOUTUBE PARA INTERPRETAÇÃO IN-PLACE NA NOTA:
- Título: {yt_meta.get('title')}
- Canal/Autor: {yt_meta.get('author_name')}
- URL Oficial: {yt_meta.get('url')}
- ID do Vídeo: `{yt_id}`

NOTAS / PERGUNTAS ADICIONAIS DO PESQUISADOR (se houver):
{cleaned_user_notes}

TRANSCRIÇÃO COMPLETA DO VÍDEO (COM TIMESTAMPS):
{yt_trans.get('formatted_transcript', '')}

---

DIRETRIZES DE INTERPRETAÇÃO E SÍNTESE DO VÍDEO:
1. NÃO CRIE TÍTULO `# H1` NEM REPITA O TÍTULO DA NOTA:
   - Comece DIRETO na primeira seção com `## 1. Síntese Executiva & Tese Principal`.
2. ESTRUTURAÇÃO COMPLETA:
   - `## 1. Síntese Executiva & Tese Principal`: Resumo claro e objetivo do propósito e conclusão do vídeo.
   - `## 2. Momentos-Chave & Roteiro do Vídeo`: Tópicos cronológicos com links de timestamps clicáveis no formato `[MM:SS]({yt_meta.get('url')}?t=SEGUNDOS)`.
   - `## 3. Análise Conceitual, Métodos & Modelagem`: Aprofundamento técnico em algoritmos, arquiteturas, matemática, física, código e hipóteses explicadas.
   - `## 4. Conexões com o Acervo & Aplicações Práticas`: Como o conteúdo se conecta ao cofre e pesquisas em andamento.
3. TAXONOMIA PADRONIZADA: Utilize os slugs canônicos do SPARK.md com wikilinks `[[...]]`.
4. FÓRMULAS EM LATEX: Blocos `$$` fechados e autocontidos, comandos rigorosos KaTeX.

Retorne um JSON ESTRUTURADO:
{{
  "titulo_sintese": "{yt_meta.get('title', clean_stem)}",
  "conceitos_chave": ["[[conceito-1]]", "[[conceito-2]]"],
  "resposta_markdown": "conteúdo técnico detalhado começando direto em ## 1. Síntese Executiva...",
  "resumo_index": "Resumo de 1 linha sobre o vídeo para o index.md",
  "log_detalhes": "- Vídeo do YouTube interpretado in-place: `{yt_meta.get('title', clean_stem)}`"
}}
"""
        else:
            prompt_query = f"""Você é o pesquisador assistente e mantenedor desta LLM Wiki de Física Médica & Tomografia Computadorizada.

ESQUEMA DA WIKI E TAXONOMIA PADRONIZADA (SPARK.md):
{spark_content}

DOCUMENTOS MAIS RELEVANTES RECUPERADOS DO ACERVO:
{wiki_context}

---

PERGUNTA / SOLICITAÇÃO DO PESQUISADOR:
{effective_query}

---

DIRETRIZES FUNDAMENTAIS DE ESTRUTURAÇÃO E REDAÇÃO:
1. NÃO MENCIONE NEM REPITA A PERGUNTA NO CORPO DO TEXTO:
   - O título da nota já é exibido nativamente pelo Obsidian.
   - NUNCA crie título `# H1`. Inicie DIRETO na primeira seção temática com `## 1. Título Temático`.
   - NUNCA use frases introdutórias do tipo "Em resposta à sua pergunta...", "A questão sobre...", "Neste documento abordamos a pergunta...".
2. TAXONOMIA PADRONIZADA: Utilize os slugs canônicos padronizados do SPARK.md.
3. Fórmulas em LaTeX:
   - Blocos de equação: use `$$` isolados em suas próprias linhas. Cada fórmula em um bloco $$ fechado.
   - Delimitadores de chaves: NUNCA use `\\left{{` ou `\\right}}`. Use OBRIGATORIAMENTE `\\left\\{{` e `\\right\\}}`.
   - Letras Gregas e Comandos: Preserve comandos como \\theta, \\tau, \\text{{...}}, \\times, \\nabla, \\Delta_x, \\sigma, \\iint, \\, d\\theta.
4. Responda com máximo rigor acadêmico, tabelas comparativas e clareza didática.

Retorne um JSON ESTRUTURADO:
{{
  "titulo_sintese": "Título claro da resposta",
  "conceitos_chave": ["[[conceito-1]]", "[[conceito-2]]"],
  "resposta_markdown": "conteúdo técnico detalhado começando direto em ## 1. Nome da Seção...",
  "resumo_index": "Resumo de 1 linha para o index.md",
  "log_detalhes": "- Consulta processada via RAG: `{filename}`"
}}
"""

        response = None
        for candidate in ["gemini-3.7-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite"]:
            try:
                response = client.models.generate_content(
                    model=candidate,
                    contents=prompt_query,
                    config=types.GenerateContentConfig(response_mime_type="application/json")
                )
                print(f"[Watcher - Query] 🎯 Resposta gerada pelo modelo: {candidate}")
                break
            except Exception as model_err:
                err_str = str(model_err)
                if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                    time.sleep(8)
                continue

        if not response or not response.text:
            return

        data = robust_parse_json(response.text)

        raw_conceitos = data.get("conceitos_chave", [])
        norm_conceitos = [normalize_links(c) for c in raw_conceitos]
        conceitos_links = ", ".join(norm_conceitos)

        raw_markdown = data.get('resposta_markdown', '').strip()

        if raw_markdown.startswith("# "):
            lines_m = raw_markdown.split("\n", 1)
            raw_markdown = lines_m[1].strip() if len(lines_m) > 1 else ""

        raw_markdown = re.sub(r'^(Em resposta à (sua )?pergunta|A pergunta sobre|Neste documento abordamos).*?\n+', '', raw_markdown, flags=re.IGNORECASE).strip()

        sanitized_markdown = fix_all_latex_in_text(normalize_links(raw_markdown))
        user_notes_block = f"{cleaned_user_notes}\n\n" if cleaned_user_notes else ""
        
        # CORPO DA NOTA SEM TÍTULO # DUPLICADO
        if is_youtube and yt_meta and yt_trans:
            yt_link_str = f"[{yt_meta.get('title')}]({yt_meta.get('url')})"
            meta_channel = f" | 👤 **Canal:** {yt_meta.get('author_name')}" if yt_meta.get('author_name') else ""
            meta_header = f"> 📅 **Data:** {today_str} | 🔗 **Conexões:** {conceitos_links} | 📺 **Vídeo:** {yt_link_str}{meta_channel}"
            
            transcript_collapsible = f"""

---

<details>
<summary>📜 <b>Ver Transcrição Completa com Timestamps</b></summary>

{yt_trans.get('formatted_transcript', '')}
</details>
"""
            full_note_content = f"""{user_notes_block}{meta_header}

{sanitized_markdown}{transcript_collapsible}"""
        else:
            full_note_content = f"""{user_notes_block}> 📅 **Data:** {today_str} | 🔗 **Conexões:** {conceitos_links}

{sanitized_markdown}
"""

        sync_to_all(f"queries/{filename}", full_note_content)
        print(f"[Watcher - Query] ✅ Resposta incorporada diretamente em: queries/{filename}")

        update_index_queries(clean_stem, data.get("resumo_index", data.get("titulo_sintese", clean_stem)))
        append_to_log(f"query | {data.get('titulo_sintese', clean_stem)}", data.get("log_detalhes", ""))

        if run_git_snapshot:
            run_git_snapshot(f"query watcher: {clean_stem[:30]}")

        mark_item_processed(PROCESSED_QUERY_LOG, filename)
        print(f"[Watcher - Query] ✨ Consulta concluída com sucesso: {filename}\n")

    except Exception as e:
        print(f"[Watcher - Query] ❌ Erro na consulta: {e}")

# ==========================================
# 3. HANDLERS E START DO OBSERVER
# ==========================================
class RawFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            process_raw_file(Path(event.src_path))
    def on_modified(self, event):
        if not event.is_directory:
            process_raw_file(Path(event.src_path))
    def on_moved(self, event):
        if not event.is_directory:
            process_raw_file(Path(event.dest_path))

class QueryFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            process_query_file(Path(event.src_path))
    def on_modified(self, event):
        if not event.is_directory:
            process_query_file(Path(event.src_path))
    def on_moved(self, event):
        if not event.is_directory:
            process_query_file(Path(event.dest_path))

def start_watcher():
    print("=" * 65)
    print("🚀 LLM WIKI WATCHER ATIVO COM RAG SEMÂNTICO & GIT BACKUP")
    print(f"📁 Monitorando Raw:     {VAULT_DIR / 'raw'}")
    print(f"💬 Monitorando Queries: {VAULT_DIR / 'queries'}")
    print("🧠 Motor RAG:          Ativo (Busca Semântica Top-K + Taxonomia)")
    print("🛡️ Backup Git:         Ativo (Snapshots automáticos no Cofre)")
    print("🔄 Auto-Evolução:       Fila inteligente anti-rate-limit")
    print("📐 Rigor LaTeX:        100% Lossless KaTeX")
    print("=" * 65)

    for ext in ["*.md", "*.txt", "*.pdf"]:
        for f in (VAULT_DIR / "raw").glob(ext):
            process_raw_file(f)

    for ext in ["*.md", "*.txt"]:
        for f in (VAULT_DIR / "queries").glob(ext):
            process_query_file(f)

    observer = Observer()
    observer.schedule(RawFolderHandler(), str(VAULT_DIR / "raw"), recursive=False)
    observer.schedule(QueryFolderHandler(), str(VAULT_DIR / "queries"), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watcher()
