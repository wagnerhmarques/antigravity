"""
Módulo Utilitário para Extração de Transcrições e Metadados do YouTube
Compatível com Obsidian Vault e Karpathy LLM Wiki
"""

import os
import re
import json
import urllib.parse
import urllib.request
from typing import Optional, Dict, Any, List
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def extract_video_id(url_or_id: str) -> Optional[str]:
    """Extrai o ID do vídeo do YouTube a partir de diversos formatos de URL ou ID direto."""
    if not url_or_id:
        return None
    url_or_id = url_or_id.strip()
    if len(url_or_id) == 11 and re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id

    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/live\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/.*[?&]v=([a-zA-Z0-9_-]{11})'
    ]

    for p in patterns:
        m = re.search(p, url_or_id)
        if m:
            return m.group(1)
    return None

def sanitize_filename(title: str, max_len: int = 80) -> str:
    """Limpa caracteres inválidos para nomes de arquivos no macOS/Obsidian."""
    clean = re.sub(r'[\\/*?:"<>|#^\[\]]', '', title)
    clean = re.sub(r'\s+', ' ', clean).strip()
    if len(clean) > max_len:
        clean = clean[:max_len].strip()
    return clean or "video_youtube"

def fetch_video_metadata(video_id: str) -> Dict[str, Any]:
    """Obtém metadados do vídeo (título, autor) usando a API oEmbed oficial do YouTube."""
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    
    metadata = {
        "video_id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "title": f"Vídeo do YouTube ({video_id})",
        "author_name": "Canal do YouTube",
        "author_url": "",
        "thumbnail_url": f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    }

    try:
        req = urllib.request.Request(
            oembed_url,
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        )
        with urllib.request.urlopen(req, timeout=8) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                metadata["title"] = data.get("title", metadata["title"])
                metadata["author_name"] = data.get("author_name", metadata["author_name"])
                metadata["author_url"] = data.get("author_url", metadata["author_url"])
                metadata["thumbnail_url"] = data.get("thumbnail_url", metadata["thumbnail_url"])
    except Exception as e:
        print(f"⚠️ Aviso ao obter metadados via oEmbed para {video_id}: {e}")

    return metadata

def format_timestamp(seconds: float) -> str:
    """Converte segundos em formato HH:MM:SS ou MM:SS."""
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"

def fetch_youtube_transcript(video_id: str) -> Dict[str, Any]:
    """
    Obtém a transcrição do vídeo com agrupamento inteligente de parágrafos por timestamp.
    Tenta idiomas preferenciais (pt, en, es) com suporte a tradução automática.
    """
    preferred_languages = ['pt', 'pt-BR', 'en', 'es']
    transcript_obj = None
    language_used = "desconhecido"
    is_generated = False
    fetched_snippets = []

    api = YouTubeTranscriptApi()

    try:
        transcript_list = api.list(video_id)
        
        # 1. Tentar transcrição manual em idioma preferencial
        try:
            transcript_obj = transcript_list.find_manually_created_transcript(preferred_languages)
            language_used = transcript_obj.language_code
            is_generated = False
        except Exception:
            # 2. Tentar transcrição automática em idioma preferencial
            try:
                transcript_obj = transcript_list.find_generated_transcript(preferred_languages)
                language_used = transcript_obj.language_code
                is_generated = True
            except Exception:
                # 3. Pegar a primeira disponível e tentar traduzir para português
                for t in transcript_list:
                    try:
                        if t.is_translatable:
                            transcript_obj = t.translate('pt')
                            language_used = "pt (traduzido)"
                            is_generated = t.is_generated
                            break
                        else:
                            transcript_obj = t
                            language_used = t.language_code
                            is_generated = t.is_generated
                            break
                    except Exception:
                        continue

        if transcript_obj:
            fetched_snippets = transcript_obj.fetch()
        else:
            fetched_snippets = api.fetch(video_id, languages=preferred_languages)
            language_used = "auto"

    except Exception as e:
        try:
            fetched_snippets = api.fetch(video_id, languages=preferred_languages)
            language_used = "auto"
        except Exception as e2:
            raise RuntimeError(f"Não foi possível obter a transcrição do vídeo {video_id}: {e2}")

    if not fetched_snippets:
        raise RuntimeError(f"Nenhuma legenda ou transcrição encontrada para o vídeo {video_id}.")

    # Agrupar falas em blocos de ~30 a 60 segundos ou quebras naturais para facilitar leitura
    grouped_blocks = []
    current_block_start = None
    current_block_texts = []
    
    full_text_pieces = []

    for snippet in fetched_snippets:
        start_sec = getattr(snippet, "start", 0.0) if hasattr(snippet, "start") else snippet.get("start", 0.0)
        text = getattr(snippet, "text", "") if hasattr(snippet, "text") else snippet.get("text", "")
        text = text.strip()
        if not text:
            continue
        
        full_text_pieces.append(text)

        if current_block_start is None:
            current_block_start = start_sec
            current_block_texts.append(text)
        else:
            # Se acumulou mais de 45 segundos ou mais de 50 palavras no bloco, fecha o parágrafo
            time_diff = start_sec - current_block_start
            words_count = sum(len(t.split()) for t in current_block_texts)
            if time_diff >= 45 or words_count >= 50:
                ts_str = format_timestamp(current_block_start)
                yt_link = f"https://youtu.be/{video_id}?t={int(current_block_start)}"
                paragraph = " ".join(current_block_texts)
                grouped_blocks.append(f"- **[{ts_str}]({yt_link})** {paragraph}")
                
                current_block_start = start_sec
                current_block_texts = [text]
            else:
                current_block_texts.append(text)

    # Adicionar o último bloco restante
    if current_block_start is not None and current_block_texts:
        ts_str = format_timestamp(current_block_start)
        yt_link = f"https://youtu.be/{video_id}?t={int(current_block_start)}"
        paragraph = " ".join(current_block_texts)
        grouped_blocks.append(f"- **[{ts_str}]({yt_link})** {paragraph}")

    return {
        "video_id": video_id,
        "language": language_used,
        "is_generated": is_generated,
        "snippets_count": len(fetched_snippets),
        "formatted_transcript": "\n\n".join(grouped_blocks),
        "full_text": " ".join(full_text_pieces)
    }

def build_raw_markdown(metadata: Dict[str, Any], transcript_info: Dict[str, Any]) -> str:
    """Gera o documento markdown estruturado para a pasta raw/."""
    title = metadata.get("title", "Vídeo do YouTube")
    video_id = metadata.get("video_id", "")
    url = metadata.get("url", f"https://www.youtube.com/watch?v={video_id}")
    author = metadata.get("author_name", "Desconhecido")
    author_url = metadata.get("author_url", "")
    lang = transcript_info.get("language", "pt")
    is_gen = "Sim (Automática)" if transcript_info.get("is_generated") else "Não (Oficial/Manual)"

    channel_md = f"[{author}]({author_url})" if author_url else author

    md = f"""# {title}

- **Tipo:** Vídeo do YouTube (Transcrição Completa)
- **URL Oficial:** {url}
- **Canal / Autor:** {channel_md}
- **ID do Vídeo:** `{video_id}`
- **Idioma da Transcrição:** {lang}
- **Legenda Gerada Automaticamente:** {is_gen}

---

## 📺 Link Direto
> 🔗 [Clique aqui para assistir ao vídeo no YouTube: **{title}**]({url})

---

## 📜 Transcrição Completa com Timestamps

{transcript_info.get("formatted_transcript", "")}
"""
    return md
