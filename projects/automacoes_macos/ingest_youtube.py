#!/usr/bin/env python3
"""
CLI de Ingestão de Vídeos do YouTube para a LLM Wiki (Karpathy Pattern)
Extrai transcrição completa com timestamps, salva o documento bruto em raw/
e aciona a análise profunda via Gemini gerando fichas e conceitos no Obsidian.

Uso:
    python ingest_youtube.py "https://www.youtube.com/watch?v=VMj-3S1tku0"
    python ingest_youtube.py --raw-only "https://youtu.be/VMj-3S1tku0"
"""

import sys
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

SCRATCH_DIR = Path("/Users/user/.gemini/antigravity-ide/scratch")
VAULT_DIR = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me")

from youtube_helper import (
    extract_video_id,
    fetch_video_metadata,
    fetch_youtube_transcript,
    build_raw_markdown,
    sanitize_filename
)

def ingest_video(url_or_id: str, raw_only: bool = False):
    video_id = extract_video_id(url_or_id)
    if not video_id:
        print(f"❌ Erro: URL ou ID de vídeo do YouTube inválido: '{url_or_id}'")
        sys.exit(1)

    print(f"\n🎬 [YouTube Ingest] 1/3 Identificado Vídeo ID: {video_id}")
    print("📡 Obtendo metadados oficiais do YouTube...")
    metadata = fetch_video_metadata(video_id)
    title = metadata.get("title", f"Vídeo YouTube {video_id}")
    author = metadata.get("author_name", "Desconhecido")
    print(f"   ▶️ Título: {title}")
    print(f"   👤 Canal: {author}")

    print("\n📜 [YouTube Ingest] 2/3 Baixando e estruturando transcrição com timestamps...")
    try:
        transcript_info = fetch_youtube_transcript(video_id)
        snippets_count = transcript_info.get("snippets_count", 0)
        lang = transcript_info.get("language", "pt")
        print(f"   ✅ Transcrição obtida ({snippets_count} falas sincronizadas, idioma: {lang})")
    except Exception as e:
        print(f"❌ Erro ao obter transcrição: {e}")
        sys.exit(1)

    # Construir Markdown
    raw_markdown = build_raw_markdown(metadata, transcript_info)

    # Definir nome do arquivo
    clean_title = sanitize_filename(title, max_len=60)
    filename = f"YouTube - {clean_title} [{video_id}].md"

    # Salvar em raw/ nos diretórios de scratch e vault
    saved_paths = []
    for base in [SCRATCH_DIR, VAULT_DIR]:
        if base.exists():
            raw_target = base / "raw" / filename
            raw_target.parent.mkdir(parents=True, exist_ok=True)
            try:
                raw_target.write_text(raw_markdown, encoding="utf-8")
                saved_paths.append(raw_target)
            except Exception as e:
                print(f"⚠️ Erro ao salvar em {raw_target}: {e}")

    print(f"\n💾 [YouTube Ingest] 3/3 Arquivo bruto salvo com sucesso em raw/:")
    for p in saved_paths:
        print(f"   📄 {p}")

    if raw_only:
        print("\n✨ Modo --raw-only ativado. O documento bruto está pronto em raw/.")
        return

    # Iniciar análise completa na LLM Wiki
    print("\n🧠 [YouTube Ingest] Acionando análise de inteligência artificial (Gemini)...")
    try:
        import watcher
        scratch_target = SCRATCH_DIR / "raw" / filename
        if scratch_target.exists():
            watcher.process_raw_file(scratch_target)
            print("\n🎉 [YouTube Ingest] Concluído com sucesso!")
            print(f"   - Ficha analítica gerada em: wiki/fontes/")
            print(f"   - Conceitos e conexões criados em: wiki/")
            print(f"   - Catálogo e log atualizados.")
        else:
            print("⚠️ Arquivo não encontrado no scratch para processamento imediato.")
    except Exception as e:
        print(f"⚠️ Processamento imediato pelo watcher falhou: {e}")
        print("💡 O daemon watcher processará este arquivo em segundo plano.")

def main():
    parser = argparse.ArgumentParser(
        description="Ingestão de vídeos do YouTube para o Obsidian e LLM Wiki."
    )
    parser.add_argument(
        "url",
        nargs="?",
        help="URL ou ID do vídeo do YouTube (ex: https://www.youtube.com/watch?v=...)"
    )
    parser.add_argument(
        "--raw-only",
        action="store_true",
        help="Apenas baixa e formata a transcrição em raw/, sem executar a análise do LLM imediatamente."
    )

    args = parser.parse_args()

    url = args.url
    if not url:
        print("📺 Ingestão de Vídeo do YouTube para o Obsidian")
        url = input("👉 Digite ou cole o link do vídeo: ").strip()

    if not url:
        print("❌ Nenhuma URL fornecida.")
        sys.exit(1)

    ingest_video(url, raw_only=args.raw_only)

if __name__ == "__main__":
    main()
