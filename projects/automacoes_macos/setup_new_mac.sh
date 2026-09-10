#!/usr/bin/env zsh
# ==============================================================================
# Script de Instalação Automática da LLM Wiki para um Novo MacBook (macOS)
# Executa tudo em menos de 1 minuto!
# ==============================================================================

set -e

echo "================================================================="
echo "🚀 INICIANDO INSTALAÇÃO DA LLM WIKI NO NOVO MACBOOK"
echo "================================================================="

CURRENT_DIR=$(pwd)
USER_HOME=$HOME
VAULT_DIR="$USER_HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me"

echo "📂 Diretório do Projeto: $CURRENT_DIR"
echo "📂 Diretório do Vault:   $VAULT_DIR"

# 1. Verificar Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado! Por favor, instale o Python 3 antes de continuar."
    exit 1
fi

# 2. Criar ambiente virtual
echo "\n📦 Configurando ambiente virtual Python (.venv)..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate

# 3. Instalar dependências
echo "📦 Instalando pacotes necessários (google-genai, watchdog, json5...)..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# 4. Verificar arquivo .env
echo "\n🔑 Verificando GEMINI_API_KEY (.env)..."
if [ ! -f ".env" ]; then
    echo "⚠️ Arquivo .env não encontrado!"
    echo -n "👉 Digite a sua GEMINI_API_KEY: "
    read API_KEY_INPUT
    echo "GEMINI_API_KEY=$API_KEY_INPUT" > .env
    echo "✅ Arquivo .env criado com sucesso!"
else
    echo "✅ Arquivo .env já existe."
fi

# 5. Configurar o LaunchAgent em segundo plano
echo "\n⚙️ Configurando daemon LaunchAgent no macOS..."
mkdir -p "$USER_HOME/Library/LaunchAgents"

PLIST_CONTENT="<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">
<plist version=\"1.0\">
<dict>
    <key>Label</key>
    <string>com.wagner.llmwiki-watcher</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/zsh</string>
        <string>-c</string>
        <string>cd $CURRENT_DIR && source .venv/bin/activate && export PYTHONUNBUFFERED=1 && exec python3 watcher.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>$CURRENT_DIR</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>$CURRENT_DIR/watcher.log</string>
    <key>StandardErrorPath</key>
    <string>$CURRENT_DIR/watcher_err.log</string>
</dict>
</plist>"

echo "$PLIST_CONTENT" > "$USER_HOME/Library/LaunchAgents/com.wagner.llmwiki-watcher.plist"

# Recarregar daemon
launchctl unload "$USER_HOME/Library/LaunchAgents/com.wagner.llmwiki-watcher.plist" 2>/dev/null || true
launchctl load "$USER_HOME/Library/LaunchAgents/com.wagner.llmwiki-watcher.plist"
echo "✅ LaunchAgent registrado e ativo no macOS!"

# 6. Instalar Serviço / Ação Rápida de Atalho
echo "\n⌨️ Configurando Quick Action em ~/Library/Services..."
mkdir -p "$USER_HOME/Library/Services"
if [ -d "Consultar LLM Wiki.workflow" ]; then
    cp -r "Consultar LLM Wiki.workflow" "$USER_HOME/Library/Services/"
    killall pbs 2>/dev/null || true
    echo "✅ Serviço 'Consultar LLM Wiki' instalado em ~/Library/Services!"
fi

echo "\n================================================================="
echo "🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO NO SEU MACBOOK!"
echo "================================================================="
echo "👉 Próximo passo no novo Mac:"
echo "   1. Abra Ajustes do Sistema ➔ Teclado ➔ Atalhos de Teclado ➔ Serviços."
echo "   2. Em 'Consultar LLM Wiki', atribua o atalho: Option + Enter."
echo "================================================================="
