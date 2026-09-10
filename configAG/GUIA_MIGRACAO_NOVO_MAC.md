# 🚀 Guia Completo de Migração e Instalação da LLM Wiki em um Novo Mac

Este guia permite que você reproduza **100% da inteligência, automações, watcher, atalhos, auto-evolução de notas, taxonomia canônica e motor de formatação matemática rigorosa** desenvolvidos aqui em qualquer outro MacBook em menos de **2 minutos**, com apenas **1 comando**.

---

## 📦 1. O que compõe o ecossistema da LLM Wiki?

O sistema é dividido em duas partes perfeitamente sincronizadas:

1. **O Cofre do Obsidian (Seus Dados e Conhecimento):**
   * Localizado no iCloud Drive: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me`.
   * **Sincronização 100% Automática:** Ao fazer login com o seu Apple ID no novo Mac, o iCloud já baixa todas as notas, pastas (`raw/`, `queries/`, `wiki/`), PDFs, catálogo `index.md` e o dicionário `configAG/TAXONOMIA_CANONICA.json`.
2. **O Motor de Inteligência e Automações (Scripts & Daemon):**
   * Fica nesta pasta do projeto (ex: `~/llmwiki` ou `~/.gemini/antigravity-ide/scratch`).
   * Contém os scripts Python (`watcher.py`, `query_inplace.py`, `normalize_terms.py`, `contextual_term_engine.py`, `auto_provision_links.py`), o esquema de regras (`SPARK.md`), o higienizador de LaTeX (`perfect_latex_fixer.py`), o ambiente virtual e os serviços nativos do macOS.

---

## ⚡ 2. Passo a Passo para Instalar em um Novo MacBook

### Passo 1: Transferir a pasta do projeto
Envie a pasta deste projeto para o novo Mac via **AirDrop**, pendrive ou repositório Git.  
*(Recomendamos colocar na sua pasta pessoal, por exemplo: `~/llmwiki`)*.

Arquivos essenciais inclusos no pacote:
* `watcher.py` *(Daemon de auto-evolução contínua, ingestão multimodal e taxonomia)*
* `query_inplace.py` *(Executador in-place: zero duplicação + taxonomia + contextualização)*
* `contextual_term_engine.py` *(Motor de análise de recorrência e contextualização no acervo)*
* `normalize_terms.py` *(Normalizador determinístico de vocabulário e aliases)*
* `auto_provision_links.py` *(Motor de varredura e enriquecimento de links órfãos)*
* `perfect_latex_fixer.py` *(Higienizador matemático e estrutural de Markdown)*
* `SPARK.md` *(Esquema mestre e regras da LLM Wiki com tabela de slugs canônicos)*
* `configAG/TAXONOMIA_CANONICA.json` *(Dicionário canônico auto-expansível com aliases)*
* `requirements.txt` *(Dependências Python)*
* `.env` *(Sua chave GEMINI_API_KEY)*
* `setup_new_mac.sh` *(Instalador automático de 1 clique)*
* `Consultar LLM Wiki.workflow` *(Ação rápida para o atalho de teclado)*

---

### Passo 2: Executar o instalador automático
No novo Mac, abra o **Terminal**, navegue até a pasta e execute:

```bash
cd ~/llmwiki   # (ou o caminho onde você colocou a pasta)
./setup_new_mac.sh
```

**O script fará tudo sozinho automaticamente em 30 segundos:**
1. Cria o ambiente virtual Python (`.venv`).
2. Instala todos os pacotes necessários (`google-genai`, `watchdog`, `json5`, etc.).
3. Configura a sua chave `GEMINI_API_KEY`.
4. Instala e ativa o **LaunchAgent** no macOS para iniciar o watcher automaticamente a cada login.
5. Instala a **Quick Action** no menu de Serviços do macOS.

---

### Passo 3: Ativar o atalho `Option + Enter`
1. No novo Mac, abra os **Ajustes do Sistema** (*System Settings*).
2. Vá em **Teclado** ➔ **Atalhos de Teclado...** ➔ **Serviços**.
3. Em **Geral** (ou *Texto*), encontre **`Consultar LLM Wiki`**.
4. Dê dois cliques e pressione as teclas: **`Option + Enter`** (ou `⌥ + Return`).
5. Clique em **Concluído**.

---

## 🛡️ 3. Recursos Avançados e Regras de Negócio Perpétuas

* **Zero Duplicação de Título no Obsidian:**  
  Como o Obsidian já exibe o título da nota nativamente no cabeçalho visual, o corpo do Markdown **NUNCA repete `# Pergunta`**. O texto gerado inicia diretamente na barra de metadados (`> 📅 Data: ... | 🔗 Conexões: ...`) e entra imediatamente em `## 1. Nome da Seção`, mantendo a nota 100% limpa e profissional.
* **Auto-Evolução & Propagação Reversa Contínua:**  
  A cada novo artigo ou documento adicionado na pasta `raw/`, o sistema **analisa todas as dúvidas e consultas anteriores em `queries/`**. Se a nova fonte trouxer dados, evidências empíricas ou respostas que aprimorem uma explicação anterior, a nota é **automaticamente incrementada** com uma subseção `### 🔄 Atualização a partir de [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]`.
* **Regra de Recorrência ($\ge 2$) e Contextualização no Acervo:**  
  Sempre que um conceito for citado $\ge 2$ vezes no acervo, o sistema cria uma nota técnica aprofundada com a seção `## 3. Contexto no Acervo do Pesquisador & Aplicações`, interligando onde e como o conceito é aplicado no projeto.
* **Taxonomia Canônica Dinâmica & Auto-Expansível (Zero Fragmentação):**  
  Novos termos são imediatamente padronizados em slugs únicos (*kebab-case*) e cadastrados no `TAXONOMIA_CANONICA.json` com suas siglas e aliases no frontmatter YAML.
* **Garantia de Conteúdo em 100% dos Links Internos (Zero Links Fantasmas):**  
  Nenhum wikilink no cofre fica vazio ou quebrado. Toda referência possui nota correspondente ativa e rica em `wiki/conceitos/` ou `wiki/tecnologias/`.
* **Trava Anti-Disparo Duplo (Debounce Atômico):** Se você segurar a combinação de teclas por mais tempo, repetições acidentais são descartadas instantaneamente (cooldown de 8s).
* **Parser JSON Inteligente sem Perdas:** Preserva simultaneamente as quebras de linha normais do Markdown e os comandos LaTeX (`\theta`, `\tau`, `\text`, `\frac`, `\left\{`, `\right\}`, `\Delta_x`, `\sigma`, `50\%`).
* **Feedback Multimodal Imediato:** Banner `⏳ Consultando...` inserido na nota em <0.1s, som sutil ao disparar (*Tink*) e sino de conclusão (*Glass*) com notificação do macOS.

---

## 🛠️ 4. Comandos Úteis de Manutenção

* **Verificar se o watcher está rodando no Mac:**
  ```bash
  launchctl list | grep llmwiki
  ```
* **Ver os logs em tempo real:**
  ```bash
  tail -f watcher.log
  ```
* **Pausar o serviço:**
  ```bash
  launchctl unload ~/Library/LaunchAgents/com.wagner.llmwiki-watcher.plist
  ```
* **Reativar o serviço:**
  ```bash
  launchctl load ~/Library/LaunchAgents/com.wagner.llmwiki-watcher.plist
  ```
* **Contextualizar termos recorrentes (>= 2 refs):**
  ```bash
  python3 contextual_term_engine.py
  ```
* **Padronizar todos os termos e links do cofre (Taxonomia):**
  ```bash
  python3 normalize_terms.py
  ```
* **Auto-provisionar todos os links internos pendentes:**
  ```bash
  python3 auto_provision_links.py
  ```
* **Rodar o calibrador de LaTeX e Markdown em todo o cofre:**
  ```bash
  python3 perfect_latex_fixer.py
  ```
