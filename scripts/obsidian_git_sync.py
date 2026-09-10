#!/usr/bin/env python3
"""
Módulo de Sincronização Contínua: Obsidian Vault -> Repositório Git (GitHub)

Funcionalidades:
1. Sincroniza pastas do cofre Obsidian (USP, wiki, raw, queries, configAG) com o repositório Git local.
2. Executa auto-commit semântico e git push para o GitHub (origin main).
3. Mecanismo de Debounce inteligente (5s) para evitar commits fragmentados durante a digitação.
4. Watchdog em tempo real observando todo o cofre do Obsidian.
"""

import os
import sys
import time
import shutil
import logging
import datetime
import threading
import subprocess
from pathlib import Path

# Caminhos padrão
VAULT_DIR = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me")
REPO_DIR = Path("/Users/user/antigravity")
LOG_FILE = Path("/Users/user/.gemini/antigravity-ide/scratch/obsidian_sync.log")

# Pastas a serem sincronizadas
SYNCED_FOLDERS = ["USP", "wiki", "raw", "queries", "configAG"]

# Configuração de Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(str(LOG_FILE)),
        logging.StreamHandler(sys.stdout)
    ]
)

class DebouncedSync:
    """Gerencia execuções de sincronização com debounce para agrupar modificações rápidas."""
    def __init__(self, delay_seconds: float = 5.0):
        self.delay = delay_seconds
        self.timer = None
        self.lock = threading.Lock()
        self.last_trigger = "alteração detectada"

    def trigger(self, reason: str = "alteração detectada"):
        with self.lock:
            self.last_trigger = reason
            if self.timer is not None:
                self.timer.cancel()
            self.timer = threading.Timer(self.delay, self._execute)
            self.timer.start()

    def _execute(self):
        with self.lock:
            reason = self.last_trigger
            self.timer = None
        sync_and_push(trigger_reason=reason)


_debouncer = DebouncedSync(delay_seconds=5.0)


def sync_vault_to_repo() -> bool:
    """Copia as pastas do cofre Obsidian para o repositório git local usando rsync."""
    if not VAULT_DIR.exists():
        logging.error(f"Cofre Obsidian não encontrado em: {VAULT_DIR}")
        return False

    if not REPO_DIR.exists():
        logging.error(f"Repositório local não encontrado em: {REPO_DIR}")
        return False

    logging.info("Iniciando sincronização de pastas do Obsidian para o repositório...")

    try:
        for folder_name in SYNCED_FOLDERS:
            src = VAULT_DIR / folder_name
            dest = REPO_DIR / folder_name

            if not src.exists():
                continue

            dest.mkdir(parents=True, exist_ok=True)

            cmd = [
                "rsync", "-a", "--delete",
                "--exclude=.DS_Store",
                "--exclude=*.icloud",
                "--exclude=.git",
                "--exclude=.obsidian",
                "--exclude=.smart-env",
                "--exclude=.claudian",
                f"{str(src)}/",
                f"{str(dest)}/"
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                logging.warning(f"Aviso no rsync da pasta {folder_name}: {res.stderr}")

        # Sincronizar arquivos .md soltos na raiz do Vault (se houver)
        for item in VAULT_DIR.glob("*.md"):
            if not item.name.startswith("."):
                shutil.copy2(item, REPO_DIR / item.name)

        logging.info("Sincronização de arquivos concluída com sucesso.")
        return True
    except Exception as e:
        logging.error(f"Erro ao sincronizar arquivos do Obsidian: {e}")
        return False


def commit_and_push(trigger_reason: str = "atualização de notas") -> bool:
    """Verifica alterações no repositório git, faz commit e push para o GitHub."""
    try:
        status_res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(REPO_DIR),
            capture_output=True,
            text=True,
            check=True
        )

        changes = status_res.stdout.strip()
        if not changes:
            logging.info("Nenhuma alteração detectada no repositório. Push não necessário.")
            return True

        logging.info(f"Alterações detectadas no Git ({len(changes.splitlines())} arquivos). Realizando commit...")

        # Git add
        subprocess.run(["git", "add", "."], cwd=str(REPO_DIR), check=True, capture_output=True)

        # Git commit
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_msg = f"docs(obsidian): auto-sync [{now_str}] - {trigger_reason}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(REPO_DIR), check=True, capture_output=True)
        logging.info(f"Commit registrado: '{commit_msg}'")

        # Git push
        logging.info("Enviando alterações para o GitHub (origin main)...")
        push_res = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=str(REPO_DIR),
            capture_output=True,
            text=True
        )

        if push_res.returncode == 0:
            logging.info("✅ Push realizado com sucesso no GitHub!")
            return True
        else:
            logging.error(f"❌ Falha ao enviar para o GitHub: {push_res.stderr}")
            return False

    except Exception as e:
        logging.error(f"Erro durante commit/push no Git: {e}")
        return False


def sync_and_push(trigger_reason: str = "manual") -> bool:
    """Executa a sincronização completa e o envio para o GitHub."""
    if sync_vault_to_repo():
        return commit_and_push(trigger_reason)
    return False


def trigger_debounced_sync(reason: str = "alteração detectada"):
    """Dispara uma sincronização agrupada via debounce."""
    _debouncer.trigger(reason)


def start_vault_watcher():
    """Inicia o observador de arquivos em tempo real no cofre do Obsidian."""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        logging.error("Biblioteca 'watchdog' não instalada. Execute: pip install watchdog")
        return

    class VaultEventHandler(FileSystemEventHandler):
        IGNORED_PATTERNS = [".git", ".obsidian", ".smart-env", ".claudian", ".DS_Store", ".icloud"]

        def _is_ignored(self, path_str: str) -> bool:
            return any(ignored in path_str for ignored in self.IGNORED_PATTERNS)

        def on_any_event(self, event):
            if event.is_directory:
                return
            src_path = getattr(event, "src_path", "")
            if self._is_ignored(src_path):
                return

            event_type = event.event_type
            rel_name = Path(src_path).name
            logging.info(f"Evento no Obsidian [{event_type}]: {rel_name}")
            trigger_debounced_sync(reason=f"{event_type} {rel_name}")

    logging.info(f"Iniciando monitoramento do cofre Obsidian: {VAULT_DIR}")
    event_handler = VaultEventHandler()
    observer = Observer()
    observer.schedule(event_handler, str(VAULT_DIR), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Parando monitoramento...")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Obsidian to GitHub Sync Engine")
    parser.add_argument("--sync-now", action="store_true", help="Executa uma sincronização e push imediato")
    parser.add_argument("--watch", action="store_true", help="Inicia o observador em tempo real contínuo")
    parser.add_argument("--reason", type=str, default="execução manual", help="Motivo do commit")

    args = parser.parse_args()

    if args.watch:
        sync_and_push(trigger_reason="inicialização do watcher")
        start_vault_watcher()
    elif args.sync_now:
        sync_and_push(trigger_reason=args.reason)
    else:
        sync_and_push(trigger_reason="execução direta")
