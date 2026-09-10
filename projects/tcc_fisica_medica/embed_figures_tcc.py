import os

target_path = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md"

with open(target_path, "r", encoding="utf-8") as f:
    text = f.read()

# Vamos verificar a presença dos marcadores dos capítulos e inserir as figuras com legendas formais

# 1. Inserção da Figura 1 no Capítulo 2 (após a dedução de 2.4)
fig1_markdown = """
![Figura 1: Fundamentos da Teoria de Detecção de Sinais (SDT), Curvas ROC e Psicofísica 2AFC. (A) Distribuições condicionais de probabilidade $p(t|H_0)$ e $p(t|H_1)$, ilustrando o limiar de decisão $t_c$, a taxa de verdadeiros positivos (TPF) e falsos positivos (FPF), e a separação $d'$. (B) Família de curvas ROC para diferentes índices de detectabilidade ($d' = 0{,}5$ a $4{,}5$). (C) Relação psicofísica formal $P_C = \\Phi(d'/\\sqrt{2})$ no paradigma 2AFC, destacando o limiar clínico e o critério de Rose.](assets/fig1_sdt_roc_2afc.png)

<center><em><b>Figura 1:</b> Fundamentos da Teoria de Detecção de Sinais (SDT), Curvas ROC e Psicofísica 2AFC.</em></center>
<br>
"""

# 2. Inserção da Figura 2 no Capítulo 2 (após a seção 2.3)
fig2_markdown = """
![Figura 2: Métricas Espectrais de Qualidade de Imagem Baseada em Tarefas. (A) Função de Transferência da Tarefa $TTF(f)$ para insertos de diferentes contrastes e materiais, evidenciando a dependência não linear e o ponto de modulação de 50% ($f_{50}$). (B) Espectro de Potência do Ruído $NPS(f)$ comparando FBP (rampa de alta frequência), HIR, DLR e MBIR com deslocamento de $f_{\\text{peak}}$ ("plastic look"). (C) Filtro Ocular Humano $E(f)$ (Função de Sensibilidade ao Contraste). (D) Espectro de Potência da Tarefa Diagnóstica $W_{\\text{task}}(f)$ para lesões nodulares esféricas de diferentes diâmetros ($\varnothing = 3, 5, 8, 12\\text{ mm}$).](assets/fig2_spectral_metrics.png)

<center><em><b>Figura 2:</b> Métricas Espectrais de Resolução ($TTF$), Ruído ($NPS$), Filtro Ocular ($E$) e Espectro da Tarefa ($W_{\\text{task}}$).</em></center>
<br>
"""

# 3. Inserção da Figura 3 no Capítulo 3 (seção 3.3)
fig3_markdown = """
![Figura 3: Modelagem de Canais Corticais no Channelized Hotelling Observer (CHO). (A) Resposta em frequência dos canais passa-faixa Dense Difference of Gaussians (D-DOG) com espaçamento de meia oitava. (B) Perfis espaciais dos canais Laguerre-Gauss radiais ($LG_0$ a $LG_3$). (C) Mapa de sensibilidade bidimensional de um canal de Gabor orientado a $\\theta = 45^\\circ$. (D) Comportamento da detectabilidade $d'$ do modelo CHO em ruído anatômico estruturado comparado ao colapso do modelo NPWE não-canalizado.](assets/fig3_cho_cortical_channels.png)

<center><em><b>Figura 3:</b> Modelagem dos Canais Corticais (Gabor, Laguerre-Gauss, D-DOG) e desempenho do observador CHO.</em></center>
<br>
"""

# 4. Inserção da Figura 4 no Capítulo 4 (seções 4.2 e 4.4)
fig4_markdown = """
![Figura 4: Não-Linearidade em Algoritmos DLR, Falha dos Modelos Lineares e Metodologia de Detrending. (A) Detectabilidade $d'$ em função do nível de dose $\\text{CTDI}_{\\text{vol}}$ para FBP, HIR e DLR. (B) Dispersão e quebra de correlação linear do modelo NPWE ($r = 0{,}68$) versus a alta correlação do modelo DLMO ancorado na percepção de radiologistas ($r = 0{,}98$). (C) Esquema didático do processo de Detrending Polinomial 2D: remoção do gradiente anatômico macroscópico $P_2(x, y)$ para isolamento do ruído quântico estocástico puro $\\delta I(x, y)$.](assets/fig4_dlr_non_linearity_detrending.png)

<center><em><b>Figura 4:</b> Impacto da não-linearidade em DLR, colapso de modelos analíticos lineares e metodologia de detrending em fundos anatômicos.</em></center>
<br>
"""

# 5. Inserção da Figura 5 no Capítulo 5 (seção 5.3)
fig5_markdown = """
![Figura 5: Otimização Multiobjetivo em Tomografia Computadorizada e Fronteira de Pareto. (A) Trade-off bidimensional entre Dose e Detectabilidade, ilustrando soluções ótimas na fronteira e protocolos dominados ineficientes. (B) Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando Dose de Radiação ($D$), Tempo Operacional total ($T$) e Detectabilidade Diagnóstica ($W = d'$).](assets/fig5_dlmo_pareto_3d.png)

<center><em><b>Figura 5:</b> Fronteira de Pareto Tridimensional $(D, T, -W)$ para Otimização Multiobjetivo de Protocolos de TC.</em></center>
<br>
"""

# Inserção estratégica nos pontos exatos do texto

# 1. Inserir Figura 1 logo após a dedução da fórmula 2AFC
alvo_1 = "Essa dedução demonstra rigorosamente a origem do fator $\\sqrt{2}$, estabelecendo a ponte metrológica direta entre a porcentagem empírica de acertos de um médico radiologista em tela diagnóstica e o índice de detectabilidade físico $d'$."
if alvo_1 in text and "fig1_sdt_roc_2afc.png" not in text:
    text = text.replace(alvo_1, alvo_1 + "\n\n" + fig1_markdown)

# 2. Inserir Figura 2 logo após a seção 2.3.4 (Critério de Rose)
alvo_2 = "enquanto $d' \\approx 1{,}5 \\text{ a } 2{,}0$ estabelece o limiar de discriminação clínica mínima aceitável."
if alvo_2 in text and "fig2_spectral_metrics.png" not in text:
    text = text.replace(alvo_2, alvo_2 + "\n\n" + fig2_markdown)

# 3. Inserir Figura 3 logo após a seção 3.3.2 (Canais D-DOG)
alvo_3 = "onde $\\sigma_j = \\sigma_0 \\alpha^j$ com $\\alpha = 1{,}4$ (espaçamento de meia oitava) e $a = 1{,}6$."
if alvo_3 in text and "fig3_cho_cortical_channels.png" not in text:
    text = text.replace(alvo_3, alvo_3 + "\n\n" + fig3_markdown)

# 4. Inserir Figura 4 logo após a seção 4.4 (Incerteza Bootstrap)
alvo_4 = "Garante-se assim a rastreabilidade e o rigor metrológico dos resultados experimentais."
if alvo_4 in text and "fig4_dlr_non_linearity_detrending.png" not in text:
    text = text.replace(alvo_4, alvo_4 + "\n\n" + fig4_markdown)

# 5. Inserir Figura 5 logo após a seção 5.3 (Dominância de Pareto)
alvo_5 = "Isso permite à equipe multiprofissional (físicos médicos, radiologistas e administradores hospitalares) selecionar analiticamente o protocolo ótimo ideal para cada contexto: protocolos de dose ultra-baixa para rastreamento pediátrico, protocolos de velocidade máxima para emergência ou protocolos de detectabilidade máxima para oncologia de alta complexidade."
if alvo_5 in text and "fig5_dlmo_pareto_3d.png" not in text:
    text = text.replace(alvo_5, alvo_5 + "\n\n" + fig5_markdown)

with open(target_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Figuras embutidas com sucesso em TCC - Documento.md!")
