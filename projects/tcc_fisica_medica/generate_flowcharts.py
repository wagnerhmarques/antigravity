import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

assets_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/assets"
os.makedirs(assets_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300

def draw_box(ax, xy, width, height, title, text, bg_color='#EBF3FB', border_color='#1E5F9E', title_color='#0B3C68', text_color='#1C2833', radius=0.03):
    x, y = xy
    # Caixa principal com bordas arredondadas
    rect = patches.FancyBboxPatch((x, y), width, height,
                                 boxstyle=f"round,pad={radius}",
                                 facecolor=bg_color, edgecolor=border_color, linewidth=1.6)
    ax.add_patch(rect)
    
    # Texto
    if title:
        ax.text(x + width/2, y + height - 0.08, title, ha='center', va='top',
                fontsize=9.5, fontweight='bold', color=title_color)
    if text:
        ax.text(x + width/2, y + (height/2 if not title else height/2 - 0.04), text,
                ha='center', va='center', fontsize=8.5, color=text_color, multialignment='center')

def draw_arrow(ax, start, end, color='#1E5F9E', width=1.8, style='->'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=width, shrinkA=3, shrinkB=3))

# ==============================================================================
# FLUXO 1: Pilares da Avaliação Baseada em Tarefa (TBIQ)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.2)
ax.axis('off')

# Título do Fluxo
draw_box(ax, (1.5, 4.3), 7.0, 0.7, "AVALIAÇÃO DE QUALIDADE DE IMAGEM BASEADA EM TAREFA (TBIQ)", 
         "Definição da qualidade pela eficácia diagnóstica do observador", bg_color='#0B3C68', border_color='#0B3C68', title_color='white', text_color='#D0E1F9')

# 3 Pilares
draw_box(ax, (0.3, 2.1), 2.8, 1.4, "RESOLUÇÃO DO SISTEMA", "Função de Transferência\nda Tarefa: TTF(f)\n(Borda circular / Contraste)", bg_color='#EAF2F8', border_color='#2980B9', title_color='#1B4F72')
draw_box(ax, (3.6, 2.1), 2.8, 1.4, "TEXTURA DO RUÍDO", "Espectro de Potência\ndo Ruído: NPS(f)\n(Magnitude & Correlação)", bg_color='#EAF2F8', border_color='#2980B9', title_color='#1B4F72')
draw_box(ax, (6.9, 2.1), 2.8, 1.4, "BIOLOGIA VISUAL", "Filtro Ocular CSF: E(f)\n& Espectro da Lesão:\nW_task(f)", bg_color='#EAF2F8', border_color='#2980B9', title_color='#1B4F72')

# Setas de cima para os 3 pilares
draw_arrow(ax, (3.5, 4.3), (1.7, 3.5))
draw_arrow(ax, (5.0, 4.3), (5.0, 3.5))
draw_arrow(ax, (6.5, 4.3), (8.3, 3.5))

# Métrica Central Final
draw_box(ax, (2.5, 0.2), 5.0, 1.1, "ÍNDICE DE DETECTABILIDADE (d')", 
         "d' = Separação estatística entre as distribuições H0 e H1\n(Síntese biofísica e computacional da qualidade)", 
         bg_color='#D4EFDF', border_color='#27AE60', title_color='#145A32', text_color='#1E8449')

# Setas dos 3 pilares para a métrica central
draw_arrow(ax, (1.7, 2.1), (3.7, 1.3))
draw_arrow(ax, (5.0, 2.1), (5.0, 1.3))
draw_arrow(ax, (8.3, 2.1), (6.3, 1.3))

plt.savefig(os.path.join(assets_dir, 'flow1_tbiq_paradigm.png'))
plt.close()
print("Gerado: flow1_tbiq_paradigm.png")


# ==============================================================================
# FLUXO 2: Comparativo de Paradigmas (Clássico vs Baseado em Tarefa)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 4.8), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis('off')

# Cabeçalho
draw_box(ax, (0.5, 4.1), 4.8, 0.7, "PARADIGMA CLÁSSICO (Linear / Escalar)", "Métricas físicas descontextualizadas", bg_color='#FDEDEC', border_color='#C0392B', title_color='#922B21', text_color='#78281F')
draw_box(ax, (5.7, 4.1), 4.8, 0.7, "PARADIGMA BASEADO EM TAREFA (TBIQ)", "Desempenho diagnóstico contextualizado", bg_color='#EAFAF1', border_color='#27AE60', title_color='#196F3D', text_color='#145A32')

# Conteúdo Clássico
draw_box(ax, (0.5, 0.4), 4.8, 3.5, "", 
         "• Métricas: Desvio padrão (HU), SNR, CNR, MTF global\n\n"
         "• Phantoms: Cilindros homogêneos de água / acrílico\n\n"
         "• Premissa: Linearidade estrita e ruído estacionário\n\n"
         "• Observador: Desconsiderado (avaliação pontual)\n\n"
         "• Falha Crítica: Falsa otimização por filtros de blur e\n  incapacidade de avaliar algoritmos não lineares (DLR)", 
         bg_color='#FADBD8', border_color='#E74C3C', title_color='#922B21', text_color='#641E16', radius=0.02)

# Conteúdo TBIQ
draw_box(ax, (5.7, 0.4), 4.8, 3.5, "", 
         "• Métrica Central: Índice de Detectabilidade (d')\n\n"
         "• Phantoms: Antropomórficos e Híbridos (FREDDIE)\n\n"
         "• Premissa: Não linearidade, dependente da tarefa clínica\n\n"
         "• Observador: Modelos Matemáticos e IA (NPWE, CHO, DLMO)\n\n"
         "• Validação Rigorosa: Alta correlação com radiologistas\n  em testes psicofísicos 2AFC e comissão AAPM TG-233", 
         bg_color='#D5F5E3', border_color='#2ECC71', title_color='#196F3D', text_color='#0E6251', radius=0.02)

plt.savefig(os.path.join(assets_dir, 'flow2_comparativo_paradigmas.png'))
plt.close()
print("Gerado: flow2_comparativo_paradigmas.png")


# ==============================================================================
# FLUXO 3: Processamento do Channelized Hotelling Observer (CHO)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 4.2), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 4.2)
ax.axis('off')

draw_box(ax, (0.3, 1.4), 2.2, 1.4, "IMAGEM MÉDICA g", "Vetor discreto de pixels\n(N pixels, ex: 16.384)\nRuído + Fundo Estruturado", bg_color='#EBF5FB', border_color='#2980B9', title_color='#154360')

draw_box(ax, (3.2, 1.4), 2.6, 1.4, "CANAIS CORTICAIS (T)", "Decomposição em V1\n(C canais, C << N)\nGabor / Laguerre-Gauss / DOG", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')

draw_box(ax, (6.5, 1.4), 2.0, 1.4, "VETOR CANALIZADO v", "v = T * g\nDimensão Reduzida (C x 1)\nCovariância Kv (C x C)", bg_color='#E8F8F5', border_color='#1ABC9C', title_color='#0E6251')

draw_box(ax, (9.1, 1.4), 1.6, 1.4, "DECISÃO (t)", "t = w^T * v\nw = Kv^-1 * <vs>\nEstatística Escalar", bg_color='#EAF2F8', border_color='#34495E', title_color='#1A5276')

draw_arrow(ax, (2.5, 2.1), (3.2, 2.1))
draw_arrow(ax, (5.8, 2.1), (6.5, 2.1))
draw_arrow(ax, (8.5, 2.1), (9.1, 2.1))

# Caixa inferior do d' CHO
draw_box(ax, (3.0, 0.1), 5.0, 0.9, "ÍNDICE DE DETECTABILIDADE DO CHO", 
         "d'_CHO = sqrt( <vs>^T * Kv^-1 * <vs> )", bg_color='#EAFAF1', border_color='#27AE60', title_color='#196F3D', text_color='#145A32')

draw_arrow(ax, (7.5, 1.4), (7.0, 1.0))

plt.savefig(os.path.join(assets_dir, 'flow3_cho_pipeline.png'))
plt.close()
print("Gerado: flow3_cho_pipeline.png")


# ==============================================================================
# FLUXO 4: Phantoms Híbridos e Metodologia 2AFC
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 5.8), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5.8)
ax.axis('off')

# Topo: Aquisição
draw_box(ax, (2.0, 4.6), 7.0, 1.0, "AQUISIÇÃO TOMOGRÁFICA DO PHANTOM FÍSICO REAL (FREDDIE)", 
         "Phantoms antropomórficos de Tórax, Abdome e Crânio com materiais equivalentes a tecidos biológicos\nVarreduras clínicas em múltiplos níveis de dose e tomógrafos", 
         bg_color='#EBF5FB', border_color='#2980B9', title_color='#154360')

# Nível Médio: Fundo H0
draw_box(ax, (3.0, 3.2), 5.0, 0.8, "BANCO DE IMAGENS DE FUNDO ANATÔMICO REAL (H0)", 
         "ROIs anatômicas reais sem lesão física", bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')

draw_arrow(ax, (5.5, 4.6), (5.5, 4.0))

# Bifurcação H0 e H1
draw_box(ax, (0.5, 1.6), 4.5, 1.1, "CASOS DE SINAL AUSENTE (H0)", "Fundo anatômico puro + ruído quântico real", bg_color='#FDEDEC', border_color='#E74C3C', title_color='#922B21')

draw_box(ax, (6.0, 1.6), 4.5, 1.1, "INSERÇÃO DIGITAL HÍBRIDA DE LESÕES (H1)", 
         "Modelagem 3D de nódulos / metástases\nConvolução com a PSF 3D do tomógrafo", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')

draw_arrow(ax, (4.5, 3.2), (2.7, 2.7))
draw_arrow(ax, (6.5, 3.2), (8.3, 2.7))

# Base: 2AFC
draw_box(ax, (1.5, 0.1), 8.0, 1.1, "PLATAFORMA DE TESTE PSICOFÍSICO CEGO 2AFC", 
         "Apresentação simultânea aos pares (H0 vs. H1) em monitores diagnósticos calibrados GSDF\nValidação e Calibração Perceptual: Painel de Radiologistas Especialistas vs. Observadores DLMO", 
         bg_color='#D4EFDF', border_color='#27AE60', title_color='#145A32', text_color='#196F3D')

draw_arrow(ax, (2.7, 1.6), (4.0, 1.2))
draw_arrow(ax, (8.3, 1.6), (7.0, 1.2))

plt.savefig(os.path.join(assets_dir, 'flow4_phantom_hibrido_2afc.png'))
plt.close()
print("Gerado: flow4_phantom_hibrido_2afc.png")


# ==============================================================================
# FLUXO 5: Arquitetura do Observador DLMO com Auto-Atenção (Vision Transformer)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 4.2), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 4.2)
ax.axis('off')

draw_box(ax, (0.3, 1.4), 2.2, 1.4, "IMAGEM MÉDICA g", "ROI de entrada (ex: 128x128)\nTextura não-estacionária DLR\nSinal H0 / H1", bg_color='#EBF5FB', border_color='#2980B9', title_color='#154360')

draw_box(ax, (3.0, 1.4), 2.5, 1.4, "EXTRATOR HIERÁRQUICO", "Camadas Convolucionais / Patches\nProjeção Linear e Posição 2D\nExtração de bordas e texturas", bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')

draw_box(ax, (6.0, 1.4), 2.5, 1.4, "AUTO-ATENÇÃO (ViT)", "Multi-Head Self-Attention (MHSA)\nPonderação de correlações globais\nEmulação da atenção foveal", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')

draw_box(ax, (9.0, 1.4), 1.7, 1.4, "DECISÃO (t)", "Camadas Densas\nEstatística Escalar t\nEstimativa de d'_DL", bg_color='#EAFAF1', border_color='#27AE60', title_color='#196F3D')

draw_arrow(ax, (2.5, 2.1), (3.0, 2.1))
draw_arrow(ax, (5.5, 2.1), (6.0, 2.1))
draw_arrow(ax, (8.5, 2.1), (9.0, 2.1))

# Caixa inferior da perda perceptual
draw_box(ax, (2.5, 0.1), 6.0, 0.9, "TREINAMENTO COM FUNÇÃO DE PERDA PERCEPTUAL MULTITAREFA", 
         "L_total = L_classificacao(y, y_hat) + lambda * ( d'_DL - d'_humano )^2", bg_color='#FADBD8', border_color='#E74C3C', title_color='#922B21', text_color='#78281F')

draw_arrow(ax, (9.8, 1.4), (8.5, 0.8))

plt.savefig(os.path.join(assets_dir, 'flow5_dlmo_architecture.png'))
plt.close()
print("Gerado: flow5_dlmo_architecture.png")


# ==============================================================================
# FLUXO 6: Pipeline Integrado de Software Metrológico
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.2), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 6.2)
ax.axis('off')

# Entrada
draw_box(ax, (0.5, 5.1), 4.8, 0.9, "MÓDULO 1: ENTRADA DICOM & PARSER", "Leitura de imagens tomográficas e validação de metadados\n(kVp, mA, tempo rotação, pitch, kernel, DLR)", bg_color='#EBF5FB', border_color='#2980B9', title_color='#154360')

# Segmentação
draw_box(ax, (5.7, 5.1), 4.8, 0.9, "MÓDULO 2: SEGMENTAÇÃO AUTOMÁTICA", "Localização precisa de insertos do phantom e amostragem\nde mosaicos de ROIs anatômicas (M >= 100)", bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')

draw_arrow(ax, (5.3, 5.55), (5.7, 5.55))

# Bifurcação Resolução e Ruído
draw_box(ax, (0.5, 3.4), 4.8, 1.3, "MÓDULO 3A: RESOLUÇÃO ESPACIAL", "• Técnica da borda circular em insertos\n• ESF(r) -> LSF(r) -> TTF(f)\n• Extração do descritor de resolução f50", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')

draw_box(ax, (5.7, 3.4), 4.8, 1.3, "MÓDULO 3B: TEXTURA E RUÍDO", "• Detrending polinomial 2D P2(x, y)\n• Janelamento Hanning 2D -> NPS 2D/1D\n• Extração de frequência de pico f_peak e f_av", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')

draw_arrow(ax, (8.1, 5.1), (2.9, 4.7))
draw_arrow(ax, (8.1, 5.1), (8.1, 4.7))

# Observadores
draw_box(ax, (1.5, 1.8), 8.0, 1.2, "MÓDULO 4: OBSERVADORES COMPUTACIONAIS DE MODELO", 
         "• Observadores Lineares Clássicos: NPWE e CHO (Canais Gabor, Laguerre-Gauss, D-DOG)\n• Observadores de Aprendizado Profundo: DLMO (CNNs residuais e Vision Transformers)", 
         bg_color='#EAFAF1', border_color='#27AE60', title_color='#196F3D')

draw_arrow(ax, (2.9, 3.4), (4.5, 3.0))
draw_arrow(ax, (8.1, 3.4), (6.5, 3.0))

# Incerteza e Otimização
draw_box(ax, (1.0, 0.2), 9.0, 1.2, "MÓDULO 5: INCERTEZA E OTIMIZAÇÃO MULTIOBJETIVO (NSGA-II)", 
         "• Determinação de incerteza por Bootstrap Não-Paramétrico (B = 2000 reamostragens)\n• Algoritmo Genético NSGA-II para mapeamento da Fronteira de Pareto Tridimensional (D, T, -W)\n• Tomada de Decisão Multicritério (TOPSIS) para seleção do protocolo clínico ideal", 
         bg_color='#FADBD8', border_color='#E74C3C', title_color='#922B21')

draw_arrow(ax, (5.5, 1.8), (5.5, 1.4))

plt.savefig(os.path.join(assets_dir, 'flow6_software_pipeline.png'))
plt.close()
print("Gerado: flow6_software_pipeline.png")

print("TODOS OS 6 FLUXOGRAMAS FORAM GERADOS COM SUCESSO EM ALTA RESOLUÇÃO!")
