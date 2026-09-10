# Instruções do Agente Antigravity

> Este projeto implementa uma **LLM Wiki (Karpathy Pattern)** gerenciada por agente.  
> As regras canônicas de operação, crescimento e manutenção estão definidas em [SPARK.md](file:///Users/user/.gemini/antigravity-ide/scratch/configAG/SPARK.md).

## Diretriz de Execução
- **Sempre leia [SPARK.md](file:///Users/user/.gemini/antigravity-ide/scratch/configAG/SPARK.md) no início de qualquer interação.**
- Nunca crie pastas ou estruturas por antecipação.
- Mantenha `raw/` imutável.
- Aplique rigorosamente a regra de crescimento de páginas soltas na raiz de `wiki/` e a regra dos 3+ para subpastas.
- Registre todas as operações (`ingest`, `query`, `lint`, `refactor`) em [log.md](file:///Users/user/.gemini/antigravity-ide/scratch/configAG/log.md).
- Mantenha [index.md](file:///Users/user/.gemini/antigravity-ide/scratch/configAG/index.md) atualizado com links para todas as páginas da wiki.

