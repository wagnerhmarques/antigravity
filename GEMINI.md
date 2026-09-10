# Diretrizes do Projeto & Fluxo de Trabalho

## Planejamento e Execução
1. **Passo a Passo Prévio**:
   - Antes de iniciar a implementação ou execução de qualquer tarefa, o agente deve sempre apresentar um plano claro e detalhado com o passo a passo do que será feito.

## Regras de Versionamento e Git
1. **Commit & Push Automático**:
   - Sempre que arquivos forem criados, modificados ou excluídos durante uma tarefa, o agente deve automaticamente:
     1. Adicionar os arquivos ao stage (`git add .`).
     2. Criar um commit com mensagem clara e em português (ou padrão convencional de commits).
     3. Fazer o envio para o repositório remoto (`git push origin main`).
2. Se a resposta for apenas informativa (sem alterações de código/arquivos), nenhuma ação de Git é necessária.

---

# Regras Permanentes de Perfil do Usuário

## 1. Google Planilhas & Formatação Regional (Brasil - PT-BR)
* **Separador Decimal:** Usar ESTRITAMENTE **vírgula (`,`)** em todas as cotações, múltiplos, percentuais e números.
* **Separador de Argumentos em Fórmulas:** Usar **ponto e vírgula (`;`)**, como em `=SE(D50>0; H50/D50; 0)` e `=SOMA(I53:I59)`.
* **Célula de Entrada de Aporte:** Injetar como número puro (`1500,00`), nunca com strings como `"R$ 1.500,00"`, para não quebrar fórmulas matemáticas com `#VALUE!`.
* **Nome da Planilha vs Nome da Aba:**
  * O nome do arquivo/planilha no Google Drive é e deve permanecer ESTRITAMENTE: **`P$ - Gestão & Aportes`**.
  * Sempre que criar uma nova aba semanal, renomeie ESTRITAMENTE a **aba inferior (sheet tab)** com a data do dia no formato **`DDMM`** (ex: `3108`).
  * **Regra de 1 Aba Única:** Criar apenas 1 nova aba datada por execução semanal a partir da célula **`A1`**, contendo o layout executivo completo (KPIs, Ações, FIIs, Teste de Estresse Selic, Radar de Proventos e Simulador Inteligente).

## 2. Carteira Real de Ativos Monitorados (Total: 19 Ativos)
* **13 Ações:** `RADL3`, `KLBN11`, `TOTS3`, `WEGE3`, `ITSA4`, `BBAS3`, `GOAU4`, `CMIG4`, `ABEV3`, `VALE3`, `PETR4`, `EGIE3`, `BBSE3`.
* **6 Fundos Imobiliários (FIIs):** `XPML11`, `HGLG11`, `MXRF11`, `BTHF11`, `BTLG11`, `KNCR11`.
* **Exclusões Definitivas:** Não monitorar `VISC11`, `TRXF11`, `ITUB4`, `BBDC4`, `TAEE11`, `CPLE6`, `SAPR11`, `CXSE3`, `VIVT3`.

## 3. Gestão e Organização no Apple Reminders (4 Eixos)
* **4 Listas Exclusivas:** `USP`, `SOFTSET`, `ME`, `TUTORMUNDI`.
* **Regra de Ouro:** Tutormundi nunca deve se misturar com Softset.
* **Seções Pré-existentes:** Alocar cada lembrete nas seções pré-existentes de cada lista (ex: `CoC`, `Graduação`, `CRP`, `Doutorado`), evitando a seção `Other`.

## 4. Automação Semanal macOS
* **Frequência:** Toda segunda-feira às **09h00** via LaunchAgent (`~/Library/LaunchAgents/com.user.investidor10_weekly_analysis.plist`).
* **Áudio Briefing:** Voz nativa do macOS `say -v Luciana`.
* **Relatórios:** PDF com gráficos vetoriais (`relatorio_executivo_carteira.pdf`) e Markdown (`relatorio_semanal_carteira.md`).
