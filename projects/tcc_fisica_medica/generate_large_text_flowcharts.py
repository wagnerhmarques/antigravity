import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

output_dirs = [
    "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/figuras",
]

for d in output_dirs:
    os.makedirs(d, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300

def draw_arrow(ax, start, end, color='#1E5F9E', width=2.2, style='->'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=width, shrinkA=4, shrinkB=4))

def save_all(fig, filename):
    for d in output_dirs:
        out_path = os.path.join(d, filename)
        fig.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Gerado com proporção otimizada: {filename}")

# ==============================================================================
# FLUXO 1: Pilares da Avaliação Baseada em Tarefa (TBIQ) (Figura 1.2)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 5.4), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5.4)
ax.axis('off')

# Top Banner (Compact, Large Text)
rect_top = patches.FancyBboxPatch((0.8, 4.3), 9.4, 0.95, boxstyle="round,pad=0.02",
                                 facecolor='#0B3C68', edgecolor='#0B3C68', linewidth=2.0)
ax.add_patch(rect_top)
ax.text(5.5, 4.95, "AVALIAÇÃO DE QUALIDADE BASEADA EM TAREFA (TBIQ)", 
        ha='center', va='center', fontsize=14.0, fontweight='bold', color='white')
ax.text(5.5, 4.55, "Qualidade definida pelo desempenho diagnóstico de um observador em tarefa clínica", 
        ha='center', va='center', fontsize=11.5, color='#E0EAFC')

# 3 Pillars (Tighter height, much larger text)
p_data = [
    (0.4, 2.1, 3.2, 1.85, "RESOLUÇÃO ESPACIAL", 
     "Função de Transferência\nda Tarefa: TTF(f)\n\n(Borda circular / Contraste ΔC)", '#154360', '#1B4F72'),
    (3.9, 2.1, 3.2, 1.85, "TEXTURA DO RUÍDO", 
     "Espectro de Potência\ndo Ruído: NPS(f)\n\n(Variância & Correlação 2D)", '#154360', '#1B4F72'),
    (7.4, 2.1, 3.2, 1.85, "BIOLOGIA VISUAL", 
     "Filtro Ocular Humano: E(f)\n&\nEspectro da Lesão: W_task(f)", '#154360', '#1B4F72')
]

for x, y, w, h, tit, txt, c_tit, c_txt in p_data:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                              facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=2.0)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.28, tit, ha='center', va='center', fontsize=13.0, fontweight='bold', color=c_tit)
    ax.text(x + w/2, y + 0.72, txt, ha='center', va='center', fontsize=11.5, color=c_txt, multialignment='center')

# Arrows Top -> Pillars
draw_arrow(ax, (3.2, 4.3), (2.0, 3.95))
draw_arrow(ax, (5.5, 4.3), (5.5, 3.95))
draw_arrow(ax, (7.8, 4.3), (9.0, 3.95))

# Central Metric Box
rect_bot = patches.FancyBboxPatch((1.5, 0.15), 8.0, 1.45, boxstyle="round,pad=0.02",
                                  facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=2.2)
ax.add_patch(rect_bot)
ax.text(5.5, 1.15, "ÍNDICE DE DETECTABILIDADE (d')", 
        ha='center', va='center', fontsize=14.0, fontweight='bold', color='#145A32')
ax.text(5.5, 0.60, "Separação estatística entre as hipóteses H0 (ruído puro) e H1 (sinal + ruído)\nSíntese biofísica e matemática contínua da qualidade de imagem", 
        ha='center', va='center', fontsize=11.5, color='#0E6251', multialignment='center')

# Arrows Pillars -> Central Metric
draw_arrow(ax, (2.0, 2.1), (3.8, 1.6))
draw_arrow(ax, (5.5, 2.1), (5.5, 1.6))
draw_arrow(ax, (9.0, 2.1), (7.2, 1.6))

save_all(fig, 'flow1_tbiq_paradigm.png')

# ==============================================================================
# FLUXO 2: Comparativo de Paradigmas (Figura 1.1)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.0), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 6.0)
ax.axis('off')

# Header Cards
r_h1 = patches.FancyBboxPatch((0.4, 4.95), 5.0, 0.9, boxstyle="round,pad=0.02",
                             facecolor='#FDEDEC', edgecolor='#C0392B', linewidth=2.0)
ax.add_patch(r_h1)
ax.text(2.9, 5.55, "PARADIGMA CLÁSSICO", ha='center', va='center', fontsize=14.0, fontweight='bold', color='#922B21')
ax.text(2.9, 5.20, "Métricas lineares e escalares descontextualizadas", ha='center', va='center', fontsize=11.0, color='#78281F')

r_h2 = patches.FancyBboxPatch((5.6, 4.95), 5.0, 0.9, boxstyle="round,pad=0.02",
                             facecolor='#EAFAF1', edgecolor='#27AE60', linewidth=2.0)
ax.add_patch(r_h2)
ax.text(8.1, 5.55, "PARADIGMA BASEADO EM TAREFA", ha='center', va='center', fontsize=14.0, fontweight='bold', color='#196F3D')
ax.text(8.1, 5.20, "Eficácia diagnóstica do observador na tarefa clínica", ha='center', va='center', fontsize=11.0, color='#145A32')

# Content Classical
r_c1 = patches.FancyBboxPatch((0.4, 0.2), 5.0, 4.55, boxstyle="round,pad=0.02",
                             facecolor='#FADBD8', edgecolor='#E74C3C', linewidth=2.0)
ax.add_patch(r_c1)

items_c = [
    ("• Métricas Principais:", "Desvio padrão (HU), SNR, CNR, MTF global"),
    ("• Fantomas Utilizados:", "Cilindros homogêneos de água / acrílico"),
    ("• Premissas Físicas:", "Linearidade estrita e ruído estacionário (WSS)"),
    ("• Papel do Observador:", "Desconsiderado (avaliação puramente física)"),
    ("• Falha Crítica:", "Falsa otimização por filtros de suavização e\nincapacidade de avaliar algoritmos DLR / IA")
]

y_pos = 4.35
for label, val in items_c:
    ax.text(0.65, y_pos, label, fontsize=12.0, fontweight='bold', color='#78281F', va='top')
    y_pos -= 0.32
    ax.text(0.85, y_pos, val, fontsize=11.0, color='#4A148C', va='top')
    y_pos -= 0.52

# Content TBIQ
r_c2 = patches.FancyBboxPatch((5.6, 0.2), 5.0, 4.55, boxstyle="round,pad=0.02",
                             facecolor='#D5F5E3', edgecolor='#2ECC71', linewidth=2.0)
ax.add_patch(r_c2)

items_t = [
    ("• Métrica Central:", "Índice de Detectabilidade (d') e AUC-ROC"),
    ("• Fantomas Utilizados:", "Antropomórficos e Híbridos (FREDDIE)"),
    ("• Premissas Físicas:", "Não-linearidade e textura não-estacionária"),
    ("• Papel do Observador:", "Modelos Perceptuais e IA (NPWE, CHO, DLMO)"),
    ("• Validação Rigorosa:", "Alta correlação com radiologistas humanos\nem testes psicofísicos 2AFC / AAPM TG-233")
]

y_pos = 4.35
for label, val in items_t:
    ax.text(5.85, y_pos, label, fontsize=12.0, fontweight='bold', color='#145A32', va='top')
    y_pos -= 0.32
    ax.text(6.05, y_pos, val, fontsize=11.0, color='#0E6251', va='top')
    y_pos -= 0.52

save_all(fig, 'flow2_comparativo_paradigmas.png')

# ==============================================================================
# FLUXO 3: Pipeline do Observador CHO (Figuras 3.1 e 4.5)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 4.6), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 4.6)
ax.axis('off')

# 4 Pipeline Boxes
cho_boxes = [
    (0.3, 1.8, 2.3, 2.5, "IMAGEM MÉDICA g", 
     "Vetor discreto de pixels\n(N pixels, ex: 16.384)\n\nRuído Quântico +\nFundo Estruturado", 
     '#EBF5FB', '#2980B9', '#154360', '#1B4F72'),
    (2.9, 1.8, 2.6, 2.5, "CANAIS CORTICAIS (T)", 
     "Decomposição em V1\n(P canais, P << N)\n\nD-DOG, Gabor 2D,\nLaguerre-Gauss", 
     '#FEF9E7', '#F39C12', '#7D6608', '#5B4600'),
    (5.8, 1.8, 2.5, 2.5, "VETOR CANALIZADO v", 
     "v = T · g\nDimensão Reduzida (P x 1)\n\nMatriz de Covariância\nKv = T · K · T^T", 
     '#E8F8F5', '#1ABC9C', '#0E6251', '#0B4F42'),
    (8.6, 1.8, 2.1, 2.5, "DECISÃO (t)", 
     "t = w^T · v\nw = Kv^-1 · <vs>\n\nEstatística Escalar\nde Decisão", 
     '#EAF2F8', '#34495E', '#1A5276', '#2C3E50')
]

for x, y, w, h, tit, txt, bg, bc, tc, txc in cho_boxes:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                              facecolor=bg, edgecolor=bc, linewidth=2.0)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.35, tit, ha='center', va='center', fontsize=12.5, fontweight='bold', color=tc)
    ax.text(x + w/2, y + 1.0, txt, ha='center', va='center', fontsize=11.2, color=txc, multialignment='center')

# Horizontal Arrows
draw_arrow(ax, (2.6, 3.05), (2.9, 3.05))
draw_arrow(ax, (5.5, 3.05), (5.8, 3.05))
draw_arrow(ax, (8.3, 3.05), (8.6, 3.05))

# Bottom Detectability Box
r_bot = patches.FancyBboxPatch((2.2, 0.15), 6.6, 1.35, boxstyle="round,pad=0.02",
                               facecolor='#EAFAF1', edgecolor='#27AE60', linewidth=2.2)
ax.add_patch(r_bot)
ax.text(5.5, 1.05, "ÍNDICE DE DETECTABILIDADE DO CHO", 
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#196F3D')
ax.text(5.5, 0.55, "d'_CHO = √[ ⟨vs⟩ᵀ · Kv⁻¹ · ⟨vs⟩ ]\n(Máxima correlação com radiologistas humanos em fundos anatômicos)", 
        ha='center', va='center', fontsize=11.5, color='#145A32', multialignment='center')

draw_arrow(ax, (9.65, 1.8), (8.6, 1.05))

save_all(fig, 'flow3_cho_pipeline.png')

# ==============================================================================
# FLUXO 4: Phantoms Híbridos e Metodologia 2AFC (Figura 4.7)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 5.8), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5.8)
ax.axis('off')

# Top Box
r_top4 = patches.FancyBboxPatch((1.2, 4.5), 8.6, 1.15, boxstyle="round,pad=0.02",
                                facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=2.0)
ax.add_patch(r_top4)
ax.text(5.5, 5.25, "AQUISIÇÃO DO PHANTOM FÍSICO REAL (FREDDIE)", 
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#154360')
ax.text(5.5, 4.80, "Simuladores antropomórficos com materiais equivalentes a tecidos biológicos\nVarreduras clínicas em múltiplos níveis de dose, detectores e algoritmos", 
        ha='center', va='center', fontsize=11.5, color='#1B4F72', multialignment='center')

# Middle Box
r_mid4 = patches.FancyBboxPatch((2.2, 3.0), 6.6, 1.0, boxstyle="round,pad=0.02",
                                facecolor='#E8F8F5', edgecolor='#16A085', linewidth=2.0)
ax.add_patch(r_mid4)
ax.text(5.5, 3.65, "BANCO DE IMAGENS DE FUNDO ANATÔMICO REAL (H0)", 
        ha='center', va='center', fontsize=13.0, fontweight='bold', color='#0E6251')
ax.text(5.5, 3.25, "Mosaico de ROIs anatômicas autênticas sem lesão física", 
        ha='center', va='center', fontsize=11.5, color='#0B4F42', multialignment='center')

draw_arrow(ax, (5.5, 4.5), (5.5, 4.0))

# Left/Right Branches
r_b1 = patches.FancyBboxPatch((0.4, 1.55), 4.8, 1.15, boxstyle="round,pad=0.02",
                             facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=2.0)
ax.add_patch(r_b1)
ax.text(2.8, 2.30, "CASOS DE SINAL AUSENTE (H0)", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#922B21')
ax.text(2.8, 1.85, "Fundo anatômico puro + ruído quântico real\n(Variabilidade anatômica estocástica)", ha='center', va='center', fontsize=11.0, color='#78281F', multialignment='center')

r_b2 = patches.FancyBboxPatch((5.8, 1.55), 4.8, 1.15, boxstyle="round,pad=0.02",
                             facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=2.0)
ax.add_patch(r_b2)
ax.text(8.2, 2.30, "INSERÇÃO HÍBRIDA DE LESÕES (H1)", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#7D6608')
ax.text(8.2, 1.85, "Modelagem matemática 3D de nódulos/tumores\nConvolução com a PSF 3D real do tomógrafo", ha='center', va='center', fontsize=11.0, color='#5B4600', multialignment='center')

draw_arrow(ax, (4.5, 3.0), (2.8, 2.7))
draw_arrow(ax, (6.5, 3.0), (8.2, 2.7))

# Bottom Box
r_bot4 = patches.FancyBboxPatch((0.8, 0.15), 9.4, 1.15, boxstyle="round,pad=0.02",
                                facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=2.2)
ax.add_patch(r_bot4)
ax.text(5.5, 0.90, "PLATAFORMA DE TESTE PSICOFÍSICO CEGO 2AFC", 
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#145A32')
ax.text(5.5, 0.45, "Apresentação simultânea aos pares (H0 vs. H1) em monitores diagnósticos calibrados (GSDF)\nValidação Perceptual: Painel de Radiologistas Especialistas vs. Observadores DLMO", 
        ha='center', va='center', fontsize=11.5, color='#0E6251', multialignment='center')

draw_arrow(ax, (2.8, 1.55), (4.2, 1.3))
draw_arrow(ax, (8.2, 1.55), (6.8, 1.3))

save_all(fig, 'flow4_phantom_hibrido_2afc.png')

# ==============================================================================
# FLUXO 5: Arquitetura DLMO Vision Transformer (Figura 4.8)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 4.6), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 4.6)
ax.axis('off')

dlmo_boxes = [
    (0.3, 1.75, 2.3, 2.55, "IMAGEM MÉDICA g", 
     "ROI tomográfica 2D/3D\n(ex: 128 x 128)\n\nTextura Não-Linear DLR\nSinal H0 / H1", 
     '#EBF5FB', '#2980B9', '#154360', '#1B4F72'),
    (2.9, 1.75, 2.6, 2.55, "EXTRATOR DE RETALHOS", 
     "Divisão em Patches 2D\nProjeção Linear + Embedding\n\nExtração de Bordas\ne Texturas Locais", 
     '#E8F8F5', '#16A085', '#0E6251', '#0B4F42'),
    (5.8, 1.75, 2.6, 2.55, "AUTO-ATENÇÃO (ViT)", 
     "Multi-Head Self-Attention\n(MHSA)\n\nPonderação Global &\nAtenção Foveal-Periférica", 
     '#FEF9E7', '#F39C12', '#7D6608', '#5B4600'),
    (8.7, 1.75, 2.0, 2.55, "DECISÃO (t)", 
     "Classificador MLP\n\nEstatística Escalar t\n&\nDetectabilidade d'_DL", 
     '#EAFAF1', '#27AE60', '#196F3D', '#145A32')
]

for x, y, w, h, tit, txt, bg, bc, tc, txc in dlmo_boxes:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                              facecolor=bg, edgecolor=bc, linewidth=2.0)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.35, tit, ha='center', va='center', fontsize=12.5, fontweight='bold', color=tc)
    ax.text(x + w/2, y + 1.0, txt, ha='center', va='center', fontsize=11.2, color=txc, multialignment='center')

draw_arrow(ax, (2.6, 3.0), (2.9, 3.0))
draw_arrow(ax, (5.5, 3.0), (5.8, 3.0))
draw_arrow(ax, (8.4, 3.0), (8.7, 3.0))

# Bottom Loss Box
r_bot5 = patches.FancyBboxPatch((1.2, 0.15), 8.6, 1.35, boxstyle="round,pad=0.02",
                                facecolor='#FADBD8', edgecolor='#E74C3C', linewidth=2.2)
ax.add_patch(r_bot5)
ax.text(5.5, 1.05, "TREINAMENTO COM FUNÇÃO DE PERDA PERCEPTUAL MULTITAREFA", 
        ha='center', va='center', fontsize=13.0, fontweight='bold', color='#922B21')
ax.text(5.5, 0.55, "L_total = L_classificação(y, ŷ) + λ · ( d'_DL - d'_humano )²\n(Alinhamento estrito do observador computacional ao córtex visual dos especialistas)", 
        ha='center', va='center', fontsize=11.5, color='#78281F', multialignment='center')

draw_arrow(ax, (9.7, 1.75), (8.8, 1.1))

save_all(fig, 'flow5_dlmo_architecture.png')

# ==============================================================================
# FLUXO 6: Pipeline Integrado de Software Metrológico (Figura 4.10)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.2), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 6.2)
ax.axis('off')

# Module 1 & 2
r_m1 = patches.FancyBboxPatch((0.4, 4.95), 5.0, 1.1, boxstyle="round,pad=0.02",
                             facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=2.0)
ax.add_patch(r_m1)
ax.text(2.9, 5.65, "MÓDULO 1: ENTRADA DICOM & PARSER", ha='center', va='center', fontsize=13.0, fontweight='bold', color='#154360')
ax.text(2.9, 5.25, "Leitura de imagens tomográficas e extração de metadados\n(kVp, mA, tempo rotação, pitch, kernel, nível DLR)", ha='center', va='center', fontsize=11.0, color='#1B4F72', multialignment='center')

r_m2 = patches.FancyBboxPatch((5.6, 4.95), 5.0, 1.1, boxstyle="round,pad=0.02",
                             facecolor='#E8F8F5', edgecolor='#16A085', linewidth=2.0)
ax.add_patch(r_m2)
ax.text(8.1, 5.65, "MÓDULO 2: SEGMENTAÇÃO AUTOMÁTICA", ha='center', va='center', fontsize=13.0, fontweight='bold', color='#0E6251')
ax.text(8.1, 5.25, "Localização de insertos e amostragem de mosaicos\nde ROIs homogêneas e anatômicas (M ≥ 100)", ha='center', va='center', fontsize=11.0, color='#0B4F42', multialignment='center')

draw_arrow(ax, (5.4, 5.5), (5.6, 5.5))

# Module 3A & 3B
r_m3a = patches.FancyBboxPatch((0.4, 3.25), 5.0, 1.4, boxstyle="round,pad=0.02",
                              facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=2.0)
ax.add_patch(r_m3a)
ax.text(2.9, 4.25, "MÓDULO 3A: RESOLUÇÃO ESPACIAL TTF(f)", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#7D6608')
ax.text(2.9, 3.65, "• Técnica da borda circular em insertos de calibração\n• ESF(r)  →  LSF(r)  →  TTF(f)\n• Extração das frequências de corte f50 e f10", ha='center', va='center', fontsize=11.0, color='#5B4600')

r_m3b = patches.FancyBboxPatch((5.6, 3.25), 5.0, 1.4, boxstyle="round,pad=0.02",
                              facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=2.0)
ax.add_patch(r_m3b)
ax.text(8.1, 4.25, "MÓDULO 3B: TEXTURA E RUÍDO NPS(f)", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#7D6608')
ax.text(8.1, 3.65, "• Detrending polinomial 2D P2(x, y) de 2ª ordem\n• Janelamento Hanning 2D  →  NPS 2D / 1D\n• Extração da frequência de pico f_peak e f_av", ha='center', va='center', fontsize=11.0, color='#5B4600')

draw_arrow(ax, (8.1, 4.95), (2.9, 4.65))
draw_arrow(ax, (8.1, 4.95), (8.1, 4.65))

# Module 4
r_m4 = patches.FancyBboxPatch((0.8, 1.7), 9.4, 1.25, boxstyle="round,pad=0.02",
                             facecolor='#EAFAF1', edgecolor='#27AE60', linewidth=2.0)
ax.add_patch(r_m4)
ax.text(5.5, 2.50, "MÓDULO 4: OBSERVADORES COMPUTACIONAIS DE MODELO", ha='center', va='center', fontsize=13.5, fontweight='bold', color='#196F3D')
ax.text(5.5, 2.05, "• Observadores Lineares Clássicos: NPWE e CHO (Canais D-DOG, Laguerre-Gauss, Gabor 2D)\n• Observadores Baseados em Aprendizado Profundo: DLMO (Vision Transformers com MHSA)", ha='center', va='center', fontsize=11.5, color='#145A32', multialignment='center')

draw_arrow(ax, (2.9, 3.25), (4.5, 2.95))
draw_arrow(ax, (8.1, 3.25), (6.5, 2.95))

# Module 5
r_m5 = patches.FancyBboxPatch((0.4, 0.15), 10.2, 1.25, boxstyle="round,pad=0.02",
                             facecolor='#FADBD8', edgecolor='#E74C3C', linewidth=2.2)
ax.add_patch(r_m5)
ax.text(5.5, 0.95, "MÓDULO 5: INCERTEZA E OTIMIZAÇÃO MULTIOBJETIVO (PARETO)", ha='center', va='center', fontsize=13.5, fontweight='bold', color='#922B21')
ax.text(5.5, 0.50, "• Determinação de incerteza por Bootstrap Não-Paramétrico (B = 2000 reamostragens)\n• Algoritmo Genético NSGA-II para mapeamento da Fronteira de Pareto 3D (Dose, Tempo, -d')\n• Tomada de Decisão Multicritério (TOPSIS) para seleção do protocolo clínico ótimo", ha='center', va='center', fontsize=11.5, color='#78281F', multialignment='center')

draw_arrow(ax, (5.5, 1.7), (5.5, 1.4))

save_all(fig, 'flow6_software_pipeline.png')

# ==============================================================================
# FLUXO METODOLOGIA: Diagrama Conceitual de Etapas (Figura 3.1)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 4.6), constrained_layout=True)
ax.set_xlim(0, 11)
ax.set_ylim(0, 4.6)
ax.axis('off')

stages = [
    (0.3, 1.75, 2.3, 2.55, "1. REVISÃO PRISMA", 
     "Protocolo PRISMA 2020\nBusca em 6 bases (n=1206)\n\nTriagem e Elegibilidade\nCorpus final de 38 estudos", 
     '#EBF5FB', '#2980B9', '#154360', '#1B4F72'),
    (2.9, 1.75, 2.6, 2.55, "2. DEDUÇÕES TEÓRICAS", 
     "Fundamentação SDT\nÓptica de Fourier e Metrologia\n\nModelagem de Observadores\n(Hotelling, NPWE, CHO, DLMO)", 
     '#FEF9E7', '#F39C12', '#7D6608', '#5B4600'),
    (5.8, 1.75, 2.6, 2.55, "3. MODELAGEM PYTHON", 
     "Scripts originais em Python\nSimulações sintéticas (Tab. 3.3)\n\nCurvas ROC, Espectros,\nCanais e Variedade Pareto", 
     '#E8F8F5', '#16A085', '#0E6251', '#0B4F42'),
    (8.7, 1.75, 2.0, 2.55, "4. SÍNTESE CLÍNICA", 
     "Problematizações reais\n(AVC, Pulmão, Fígado)\n\nHarmonização com normas\nAAPM TG-233 e ANVISA", 
     '#EAFAF1', '#27AE60', '#196F3D', '#145A32')
]

for x, y, w, h, tit, txt, bg, bc, tc, txc in stages:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                              facecolor=bg, edgecolor=bc, linewidth=2.0)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.35, tit, ha='center', va='center', fontsize=12.5, fontweight='bold', color=tc)
    ax.text(x + w/2, y + 1.0, txt, ha='center', va='center', fontsize=11.2, color=txc, multialignment='center')

draw_arrow(ax, (2.6, 3.0), (2.9, 3.0))
draw_arrow(ax, (5.5, 3.0), (5.8, 3.0))
draw_arrow(ax, (8.4, 3.0), (8.7, 3.0))

# Bottom Synthesis Box
r_bot_met = patches.FancyBboxPatch((1.2, 0.15), 8.6, 1.35, boxstyle="round,pad=0.02",
                                   facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=2.2)
ax.add_patch(r_bot_met)
ax.text(5.5, 1.05, "INTEGRAÇÃO METROLÓGICA E CONTROLE DE QUALIDADE BASEADO EM TAREFA", 
        ha='center', va='center', fontsize=13.0, fontweight='bold', color='#145A32')
ax.text(5.5, 0.55, "Unificação dos domínios da dosimetria, física de detectores e percepção visual\npara garantia da segurança do paciente e otimização dosimétrica em tomografia", 
        ha='center', va='center', fontsize=11.5, color='#0E6251', multialignment='center')

draw_arrow(ax, (9.7, 1.75), (8.8, 1.1))

save_all(fig, 'flow_metodologia_etapas.png')

print("TODOS OS 7 FLUXOGRAMAS FORAM REGERADOS COM SUCESSO!")
