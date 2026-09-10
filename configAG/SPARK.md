# SPARK.md - Especificação Técnica e Diretrizes da LLM Wiki (Karpathy Pattern)

Este documento define a arquitetura, regras de formatação, taxonomia padronizada e padrões de engenharia da **LLM Wiki Científica Pessoal** (USP / FAPESP).

---

## 🏛️ Arquitetura dos 5 Pilares de Robustez

1. **RAG Semântico Híbrido (`semantic_retriever.py`):**
   - Combina embeddings vetoriais locais (`gemini-embedding-001`) com a Taxonomia Canônica.
   - Recupera os 8 a 12 documentos mais relevantes por consulta, mantendo o tempo de resposta em <3 segundos e eliminando diluição de contexto.
2. **Backup Git Silencioso e Versionamento Atômico (`git_backup.py`):**
   - Cria snapshots automáticos do cofre no Git local a cada ingestão e consulta.
   - Permite desfazer qualquer alteração indesejada instantaneamente (`python git_backup.py restore`).
3. **Propagação Inteligente com Fila Anti-Rate-Limit (`watcher.py`):**
   - Ao receber novo artigo em `raw/`, ranqueia e atualiza apenas as notas de `queries/` com sobreposição real, espaçando requisições para evitar erros `429`.
4. **Blindagem contra iCloud Drive e Concorrência:**
   - Filtro ativo contra arquivos desidratados `.icloud` e arquivos temporários `.`.
   - Escrita atômica segura via `safe_atomic_write` para evitar travas de sincronização `[Errno 1]`.
5. **Auditoria Contínua de Integridade (`vault_audit.py`):**
   - Varredura de links órfãos, sintaxe matemática KaTeX e coerência de taxonomia.

---

## 🏷️ Padrão Estético de Nomenclatura: Nomes Naturais com Espaços

- **PROIBIDO** o uso de identificadores em *kebab-case* com traços (ex.: `[[indice-de-detectabilidade]]`).
- **OBRIGATÓRIO** o uso de **Nomes Acadêmicos Naturais com Espaços, Acentuação Correta e Siglas em Caixa Alta**:
  - `[[Índice de Detectabilidade]]`
  - `[[Task Transfer Function]]`
  - `[[Noise Power Spectrum]]`
  - `[[Efeito Fotoelétrico]]`
  - `[[Espalhamento Compton]]`
  - `[[Tomografia Computadorizada]]`
  - `[[Qualidade de Imagem em TC]]`
  - `[[Reconstrução Iterativa]]`
  - `[[Deep Learning Image Reconstruction (DLR)]]`
  - `[[Photon Counting Detector CT (PCD-CT)]]`
  - `[[Retroprojeção Filtrada (FBP)]]`
  - `[[Observadores de Modelo (Model Observers)]]`
  - `[[Métricas de Dose em TC]]`
  - `[[Radioproteção]]`

---

## 📐 Regras de Formatação Visual e LaTeX no Obsidian

### 1. Início de Notas de Consulta (`queries/`):
- **PROIBIDO** criar cabeçalhos `# H1` duplicados no corpo do arquivo (o Obsidian já exibe o nome do arquivo como título).
- O arquivo deve iniciar DIRETO na barra de metadados:
  ```markdown
  > 📅 **Data:** YYYY-MM-DD | 🔗 **Conexões:** [[Conceito 1]], [[Conceito 2]]
  ```
- **PROIBIDO** colocar `---` solto na primeira linha.

### 2. Sintaxe KaTeX Rigorosa:
- Equações em display math devem ficar em blocos `$$` dedicados:
  ```latex
  $$
  d'^2_{\text{NPWE}} = \frac{\left[ \iint_{-\infty}^{\infty} |W(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot E^2(u, v) \, du \, dv \right]^2}{\iint_{-\infty}^{\infty} |W(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot \text{NPS}(u, v) \cdot E^4(u, v) \, du \, dv + \sigma_{\text{int}}^2}
  $$
  ```
- Delimitadores de chaves: use OBRIGATORIAMENTE `\left\{` e `\right\}`.
- Letras gregas e operadores: preservar `\theta`, `\tau`, `\text{...}`, `\times`, `\nabla`, `\iint`.
