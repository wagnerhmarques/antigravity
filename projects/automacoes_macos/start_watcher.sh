#!/usr/bin/env bash
cd "$(dirname "$0")"
source .venv/bin/activate
export PYTHONUNBUFFERED=1
python3 watcher.py
