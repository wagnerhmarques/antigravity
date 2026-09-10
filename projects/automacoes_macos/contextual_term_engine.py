#!/usr/bin/env python3
"""
Motor de Contextualização Automática de Termos Recorrentes (Regra de Recorrência >= 2)
1. Identifica termos que aparecem >= 2 vezes no acervo.
2. Coleta os trechos de contexto reais de todos os documentos onde o termo aparece.
3. Gera uma nota profunda que explica o termo FÍSICA e CONTEXTUALMENTE dentro do acervo do pesquisador.
"""

import os
import re
import sys
import time
import json
import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SCRATCH_DIR = Path("/Users/user/.gemini/antigravity-ide/scratch")
VAULT_DIR = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me")

from perfect_latex_fixer import fix_all_latex_in_text

def get_recurring_terms():
    alias_map = {}
    tax_path = SCRATCH_DIR / "configAG" / "TAXONOMIA_CANONICA.json"
    if tax_path.exists():
        try:
            with open(tax_path, "r", encoding="utf-8") as f:
                tax = json.load(f)
            for canon, d in tax.items():
                alias_map[canon.lower()] = canon
                for a in d.get("aliases", []):
                    alias_map[a.lower().strip()] = canon
                    norm = re.sub(r'[^a-zA-Z0-9]', '', a.lower())
                    if norm:
                        alias_map[norm] = canon
        except Exception:
            pass

    term_contexts = {}
    for base in [VAULT_DIR, SCRATCH_DIR]:
        for p in base.rglob("*.md"):
            if p.name.startswith(".") or "configAG" in str(p):
                continue
            try:
                rel = str(p.relative_to(base))
                txt = p.read_text(encoding="utf-8")
                links = re.findall(r"\[\[(.*?)\]\]", txt)
                for link in links:
                    inner = link.split("|")[0].split("#")[0].strip()
                    if not inner or inner.startswith("queries/") or inner.startswith("http"):
                        continue
                    
                    target_lower = inner.lower()
                    target_norm = re.sub(r'[^a-zA-Z0-9]', '', target_lower)
                    canon = alias_map.get(target_lower) or alias_map.get(target_norm) or inner

                    if canon not in term_contexts:
                        term_contexts[canon] = []
                    
                    # Extract surrounding context snippet (200 chars)
                    m = re.search(re.escape(link), txt)
                    snippet = ""
                    if m:
                        st = max(0, m.start() - 100)
                        en = min(len(txt), m.end() + 100)
                        snippet = txt[st:en].replace("\n", " ").strip()
                    
                    # Store if from unique file
                    if not any(item[0] == rel for item in term_contexts[canon]):
                        term_contexts[canon].append((rel, snippet))
            except Exception:
                pass

    return {t: ctxs for t, ctxs in term_contexts.items() if len(ctxs) >= 2}

def generate_contextualized_note(client, term_name: str, contexts: list):
    slug = re.sub(r'[^a-zA-Z0-9_\-]+', '-', term_name.lower().strip()).strip('-')
    if not slug:
        return None

    # Contextos onde o termo apareceu
    formatted_contexts = ""
    for fpath, snip in contexts[:8]:
        formatted_contexts += f"- **No documento `{fpath}`:** \"{snip}\"\n"

    prompt = f"""Você é o pesquisador assistente e mantenedor da LLM Wiki de Física Médica & Tomografia Computadorizada (USP/FAPESP).

O termo "{term_name}" apareceu múltiplas vezes ({len(contexts)} ocorrências) no acervo de notas e artigos do pesquisador.

TRECHOS ONDE O TERMO É CITADO NO ACERVO:
{formatted_contexts}

Sua tarefa:
Gerar uma nota de conhecimento PROFUNDA, TÉCNICA e RIGOROSA em Markdown, estruturada segundo o SPARK.md:
---
tipo: conceito (ou tecnologia)
aliases: [{term_name}]
tags: [fisica-medica, tomografia-computadorizada]
data: {datetime.date.today().isoformat()}
---

# {term_name}

## 1. Definição Conceitual e Fundamentação Física
Explicação acadêmica, rigorosa e aprofundada do conceito...

## 2. Formulação Matemática e Propriedades
Equações rigorosas em LaTeX ($...$ para inline, $$...$$ para blocos, com \\Delta_x, \\sigma, \\iint, \\left\\{{ e \\right\\}}).

## 3. Contexto no Acervo do Pesquisador & Aplicações
Explique COMO este conceito se conecta aos documentos e pesquisas do usuário (citando os documentos de onde ele foi extraído com wikilinks [[...]], como controle de qualidade, dose, detectabilidade, DLR ou fantomas).

## 4. Conexões e Wikilinks
Liste os wikilinks essenciais relacionados.

Retorne APENAS o código Markdown completo.
"""

    response = None
    for candidate in ["gemini-3.7-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite"]:
        try:
            response = client.models.generate_content(
                model=candidate,
                contents=prompt,
            )
            break
        except Exception:
            continue

    if not response or not response.text:
        return None

    raw_text = response.text.strip()
    if raw_text.startswith("```markdown"):
        raw_text = raw_text[11:]
    elif raw_text.startswith("```"):
        raw_text = raw_text[3:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]

    clean_content = fix_all_latex_in_text(raw_text.strip())
    tipo = "tecnologia" if any(k in term_name.lower() for k in ["deep-learning", "detector", "nsga", "transformer", "network", "scanner", "observer", "algoritmo"]) else "conceito"
    caminho_rel = f"wiki/{tipo}s/{slug}.md"

    return caminho_rel, clean_content

def update_index_entry(slug: str, titulo: str, tipo: str):
    resumo = f"Página de referência técnica sobre {titulo}."
    for base in [SCRATCH_DIR, VAULT_DIR]:
        for idx in [base / "configAG" / "index.md", base / "index.md"]:
            if not idx.exists():
                continue
            try:
                content = idx.read_text(encoding="utf-8")
                nova_linha = f"\n- [[{slug}]] — *{titulo}*: {resumo}"
                if f"[[{slug}]]" in content:
                    continue
                if tipo == "tecnologia" and "## 🛠️ Tecnologias & Algoritmos" in content:
                    parts = content.split("## 🛠️ Tecnologias & Algoritmos (`wiki/tecnologias/`)")
                    if len(parts) == 2:
                        content = parts[0] + "## 🛠️ Tecnologias & Algoritmos (`wiki/tecnologias/`)" + nova_linha + parts[1]
                elif "## 🧠 Conceitos & Métricas" in content:
                    parts = content.split("## 🧠 Conceitos & Métricas (`wiki/conceitos/`)")
                    if len(parts) == 2:
                        content = parts[0] + "## 🧠 Conceitos & Métricas (`wiki/conceitos/`)" + nova_linha + parts[1]
                else:
                    content = content + nova_linha
                idx.write_text(content, encoding="utf-8")
            except Exception:
                pass

def process_all_recurring_terms():
    recurring = get_recurring_terms()
    print(f"Identificados {len(recurring)} termos recorrentes (>= 2 ocorrências) no acervo.")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("⚠️ GEMINI_API_KEY não configurada!")
        return

    from google import genai
    client = genai.Client(api_key=api_key)

    for i, (term, contexts) in enumerate(sorted(recurring.items(), key=lambda x: len(x[1]), reverse=True), 1):
        slug = re.sub(r'[^a-zA-Z0-9_\-]+', '-', term.lower()).strip('-')
        
        # Verificar se já existe nota com tamanho substancial
        already_detailed = False
        for base in [VAULT_DIR, SCRATCH_DIR]:
            for p in [base / "wiki" / "conceitos" / f"{slug}.md", base / "wiki" / "tecnologias" / f"{slug}.md", base / "wiki" / f"{slug}.md"]:
                if p.exists() and p.stat().st_size > 1200:
                    already_detailed = True
                    break
        
        if already_detailed:
            continue

        print(f"[{i}/{len(recurring)}] ⚡ Contextualizando termo recorrente ({len(contexts)} refs): [[{term}]]...")
        res = generate_contextualized_note(client, term, contexts)
        if res:
            caminho_rel, content = res
            for base in [VAULT_DIR, SCRATCH_DIR]:
                dest = base / caminho_rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding="utf-8")
            tipo = "tecnologia" if "tecnologia" in caminho_rel else "conceito"
            update_index_entry(slug, term, tipo)
            print(f"✅ Nota contextualizada salva: {caminho_rel}")
            time.sleep(1.0)

if __name__ == "__main__":
    process_all_recurring_terms()
