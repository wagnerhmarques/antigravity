with open('/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Substituir qualquer bloco com "AVALIAÇÃO BASEADA NA TAREFA" por flow1
text = re.sub(r'```\s*\+[-]+\+\s*\|\s*AVALIAÇÃO BASEADA NA TAREFA.*?```', 
              r"""![Fluxograma 1: Pilares Fundamentais da Avaliação de Qualidade de Imagem Baseada em Tarefa (TBIQ), articulando Resolução ($TTF$), Ruído ($NPS$) e Fisiologia Visual ($E(f)$) no Índice de Detectabilidade ($d'$).](assets/flow1_tbiq_paradigm.png)

<center><em><b>Fluxograma 1:</b> Pilares Fundamentais da Avaliação Baseada em Tarefa (TBIQ).</em></center>""", 
              text, flags=re.DOTALL)

# Substituir qualquer bloco com "Matriz de Canais Corticais T" por flow3
text = re.sub(r'```\s*Imagem Médica g.*?Matriz de Canais Corticais T.*?```', 
              r"""![Fluxograma 2: Fluxo de Redução de Dimensionalidade por Canais Corticais e Decisão no Channelized Hotelling Observer (CHO).](assets/flow3_cho_pipeline.png)

<center><em><b>Fluxograma 2:</b> Decomposição Cortical e Processamento de Decisão no CHO.</em></center>""", 
              text, flags=re.DOTALL)

with open('/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Substituição final aplicada!")
