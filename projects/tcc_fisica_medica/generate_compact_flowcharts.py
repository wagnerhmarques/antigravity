import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Directories to save images
output_dirs = [
    "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/figuras",
    "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile",
]

for d in output_dirs:
    os.makedirs(d, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300

def draw_arrow(ax, start, end, color='#1E5F9E', width=1.8, style='->'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=width, shrinkA=2, shrinkB=2))

def draw_exarrow(ax, start, end, color='#C0392B', width=1.8, style='->'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=width, shrinkA=2, shrinkB=2))

def save_compact(fig, filename):
    for d in output_dirs:
        out_path = os.path.join(d, filename)
        fig.savefig(out_path, dpi=300, bbox_inches='tight', pad_inches=0.01)
    plt.close(fig)
    print(f"Gerado com sucesso e proporção 1:1: {filename}")


# ==============================================================================
# FIGURA 1.1: Comparativo entre Paradigmas (flow2_comparativo_paradigmas.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 5.4), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Left Header (Clássico)
r_h1 = patches.FancyBboxPatch((0.15, 8.85), 4.75, 1.0, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#78281F', edgecolor='#78281F', linewidth=1.5)
ax.add_patch(r_h1)
ax.text(2.525, 9.48, "PARADIGMA CLÁSSICO", ha='center', va='center', fontsize=11.5, fontweight='bold', color='white')
ax.text(2.525, 9.10, "Métricas pontuais em meios homogêneos", ha='center', va='center', fontsize=9.2, color='#FADBD8')

# Left Body
r_b1 = patches.FancyBboxPatch((0.15, 1.45), 4.75, 7.25, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.5)
ax.add_patch(r_b1)

items_c = [
    ("Métricas Centrais:", "Desvio padrão (HU), SNR e CNR\nescalares, MTF global única."),
    ("Fantomas Físicos:", "Cilindros homogêneos de água e\nacrílico (PMMA) sem anatomia."),
    ("Premissas Físicas:", "Linearidade estrita, invariância\nespacial e ruído estacionário WSS."),
    ("Papel do Observador:", "Desconsiderado (avaliação física\npuramente instrumental)."),
    ("Limitação Crítica:", "Falsa otimização por filtros e\ncolapso total sob IA / DLR.")
]

y_pos = 8.45
for label, val in items_c:
    ax.text(0.35, y_pos, label, fontsize=10.0, fontweight='bold', color='#922B21', va='top')
    y_pos -= 0.36
    ax.text(0.50, y_pos, val, fontsize=9.0, color='#4A148C', va='top', multialignment='left')
    y_pos -= 1.00

# Right Header (TBIQ)
r_h2 = patches.FancyBboxPatch((5.10, 8.85), 4.75, 1.0, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#145A32', edgecolor='#145A32', linewidth=1.5)
ax.add_patch(r_h2)
ax.text(7.475, 9.48, "PARADIGMA BASEADO EM TAREFA (TBIQ)", ha='center', va='center', fontsize=11.0, fontweight='bold', color='white')
ax.text(7.475, 9.10, "Eficácia diagnóstica do observador na tarefa", ha='center', va='center', fontsize=9.2, color='#D5F5E3')

# Right Body
r_b2 = patches.FancyBboxPatch((5.10, 1.45), 4.75, 7.25, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#EAFAF1', edgecolor='#27AE60', linewidth=1.5)
ax.add_patch(r_b2)

items_t = [
    ("Métricas Centrais:", "Índice de Detectabilidade (d') e\nárea sob a curva ROC (AUC)."),
    ("Fantomas Físicos:", "Simuladores antropomórficos e\nhíbridos clínicos (FREDDIE)."),
    ("Premissas Físicas:", "Não-linearidade, resolução TTF(f; ΔC)\ndependente de contraste e não-WSS."),
    ("Papel do Observador:", "Modelos Perceptuais e Redes\nNeurais (NPWE, CHO, DLMO)."),
    ("Validação Rigorosa:", "Forte correlação com radiologistas\nem testes psicofísicos 2AFC.")
]

y_pos = 8.45
for label, val in items_t:
    ax.text(5.30, y_pos, label, fontsize=10.0, fontweight='bold', color='#145A32', va='top')
    y_pos -= 0.36
    ax.text(5.45, y_pos, val, fontsize=9.0, color='#0E6251', va='top', multialignment='left')
    y_pos -= 1.00

# Bottom Synthesis Banner
r_bot_c = patches.FancyBboxPatch((0.15, 0.10), 9.70, 1.20, boxstyle="round,pad=0.01,rounding_size=0.04",
                                 facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.5)
ax.add_patch(r_bot_c)
ax.text(5.0, 0.85, "TRANSIÇÃO METROLÓGICA FUNDAMENTAL", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#154360')
ax.text(5.0, 0.45, "Da avaliação instrumental em fantomas homogêneos para a capacidade real de detecção clínica de lesões.",
        ha='center', va='center', fontsize=8.8, color='#1B4F72')

save_compact(fig, 'flow2_comparativo_paradigmas.png')


# ==============================================================================
# FIGURA 1.2: Pilares do Paradigma TBIQ (flow1_tbiq_paradigm.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 4.6), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Top Banner
r_top = patches.FancyBboxPatch((0.15, 8.20), 9.70, 1.65, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor='#0B3C68', edgecolor='#0B3C68', linewidth=1.5)
ax.add_patch(r_top)
ax.text(5.0, 9.20, "AVALIAÇÃO DE QUALIDADE BASEADA EM TAREFA (TBIQ)", 
        ha='center', va='center', fontsize=12.0, fontweight='bold', color='white')
ax.text(5.0, 8.60, "Qualidade metrológica definida pelo desempenho do observador em tarefa diagnóstica clínica", 
        ha='center', va='center', fontsize=9.2, color='#E0EAFC')

# 3 Pillars
pillars = [
    (0.15, 3.40, 3.05, 4.40, "RESOLUÇÃO ESPACIAL", "Função de Transferência\nda Tarefa\n\nTTF(f; ΔC)\n\nAvaliada em bordas\ncirculares de insertos\nem fantomas clínicos.", '#154360', '#1B4F72', '#EBF5FB', '#2980B9'),
    (3.475, 3.40, 3.05, 4.40, "TEXTURA DO RUÍDO", "Espectro de Potência\ndo Ruído\n\nNPS(f)\n\nVariância e correlação\nespacial 2D no domínio\ncontínuo de Fourier.", '#154360', '#1B4F72', '#EBF5FB', '#2980B9'),
    (6.80, 3.40, 3.05, 4.40, "BIOLOGIA VISUAL", "Filtro Ocular Humano\nE(f) (Burgess)\n&\nEspectro da Lesão\nW_task(f) (Bessel J1)\nPerfil clínico do alvo.", '#154360', '#1B4F72', '#EBF5FB', '#2980B9')
]

for x, y, w, h, tit, txt, c_tit, c_txt, bg, bc in pillars:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor=bg, edgecolor=bc, linewidth=1.5)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.45, tit, ha='center', va='center', fontsize=10.5, fontweight='bold', color=c_tit)
    ax.text(x + w/2, y + 1.85, txt, ha='center', va='center', fontsize=9.0, color=c_txt, multialignment='center')

draw_arrow(ax, (2.5, 8.20), (1.675, 7.80))
draw_arrow(ax, (5.0, 8.20), (5.0, 7.80))
draw_arrow(ax, (7.5, 8.20), (8.325, 7.80))

# Bottom Synthesis Box
r_bot = patches.FancyBboxPatch((0.15, 0.10), 9.70, 2.90, boxstyle="round,pad=0.01,rounding_size=0.04",
                               facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=1.8)
ax.add_patch(r_bot)
ax.text(5.0, 2.30, "ÍNDICE DE DETECTABILIDADE (d')", 
        ha='center', va='center', fontsize=12.0, fontweight='bold', color='#145A32')
ax.text(5.0, 1.55, "d' = [ ∫ (|W(f)|² · TTF²(f) / NPS(f)) · E²(f) df ]¹/²", 
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0E6251')
ax.text(5.0, 0.70, "Separação estatística contínua entre as hipóteses H0 (ruído puro) e H1 (sinal + ruído).\nSíntese biofísica e matemática contínua da qualidade de imagem em tomografia.", 
        ha='center', va='center', fontsize=8.8, color='#145A32', multialignment='center')

draw_arrow(ax, (1.675, 3.40), (3.0, 3.00))
draw_arrow(ax, (5.0, 3.40), (5.0, 3.00))
draw_arrow(ax, (8.325, 3.40), (7.0, 3.00))

save_compact(fig, 'flow1_tbiq_paradigm.png')


# ==============================================================================
# FIGURA 3.1: Etapas Metodológicas da Pesquisa (flow_metodologia_etapas.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 5.0), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# 4 Stages in 2x2 Grid with connecting arrows
boxes_met = [
    (0.15, 5.40, 4.70, 4.40, "1. REVISÃO PRISMA 2020", "Busca em 6 Bases Científicas",
     "• Protocolo PRISMA 2020 rigoroso\n• 1.206 registros identificados\n• 38 estudos incluídos na síntese\n• Corpus normativo AAPM e ANVISA",
     '#EBF5FB', '#2980B9', '#154360', '#1B4F72'),
    
    (5.15, 5.40, 4.70, 4.40, "2. DEDUÇÕES TEÓRICAS", "Formalismo Matemático SDT",
     "• Teoria de Detecção de Sinais (SDT)\n• Métricas espectrais em Fourier\n• Deduções: Hotelling, NPWE, CHO\n• Redes profundas e Vision Transformers",
     '#FEF9E7', '#F39C12', '#7D6608', '#5B4600'),
    
    (0.15, 1.70, 4.70, 3.30, "3. MODELAGEM EM PYTHON", "Simulações Numéricas Controladas",
     "• Scripts originais em Python (Tab. 3.3)\n• Curvas ROC, canais corticais V1\n• Otimização de Pareto 3D (NSGA-II)",
     '#E8F8F5', '#16A085', '#0E6251', '#0B4F42'),
    
    (5.15, 1.70, 4.70, 3.30, "4. SÍNTESE CLÍNICA", "Problematizações Hospitalares",
     "• Discussões clínicas: AVC, Nódulo, Fígado\n• Validação com testes psicofísicos 2AFC\n• Diretrizes para dosimetria ALARA",
     '#EAFAF1', '#27AE60', '#196F3D', '#145A32')
]

for x, y, w, h, tit, sub, txt, bg, bc, tc, txc in boxes_met:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor=bg, edgecolor=bc, linewidth=1.5)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.40, tit, ha='center', va='center', fontsize=10.8, fontweight='bold', color=tc)
    ax.text(x + w/2, y + h - 0.85, sub, ha='center', va='center', fontsize=8.8, fontstyle='italic', color=txc)
    ax.text(x + 0.30, y + (h - 1.20)/2, txt, ha='left', va='center', fontsize=8.8, color=txc, multialignment='left')

draw_arrow(ax, (4.85, 7.60), (5.15, 7.60)) # 1 -> 2
draw_arrow(ax, (7.50, 5.40), (7.50, 5.00)) # 2 -> 4
draw_arrow(ax, (5.15, 3.35), (4.85, 3.35)) # 4 -> 3
draw_arrow(ax, (2.50, 5.40), (2.50, 5.00)) # 1 -> 3

# Bottom Box
r_bot_m = patches.FancyBboxPatch((0.15, 0.10), 9.70, 1.30, boxstyle="round,pad=0.01,rounding_size=0.04",
                                 facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=1.8)
ax.add_patch(r_bot_m)
ax.text(5.0, 0.90, "INTEGRAÇÃO METROLÓGICA E GARANTIA DA QUALIDADE BASEADA EM TAREFA", 
        ha='center', va='center', fontsize=10.2, fontweight='bold', color='#145A32')
ax.text(5.0, 0.45, "Unificação entre física dosimétrica, detectores avançados e percepção visual diagnóstica para a clínica.", 
        ha='center', va='center', fontsize=8.6, color='#0E6251')

draw_arrow(ax, (2.50, 1.70), (2.50, 1.40))
draw_arrow(ax, (7.50, 1.70), (7.50, 1.40))

save_compact(fig, 'flow_metodologia_etapas.png')


# ==============================================================================
# FIGURA 4.1: Fluxograma PRISMA 2020 (flow_prisma_flowchart.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 7.8), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Top Header
r_top_p = patches.FancyBboxPatch((0.15, 9.20), 9.70, 0.70, boxstyle="round,pad=0.01,rounding_size=0.04",
                                facecolor='#0B3C68', edgecolor='#0B3C68', linewidth=1.5)
ax.add_patch(r_top_p)
ax.text(5.0, 9.62, "FLUXOGRAMA DE SELEÇÃO SISTEMÁTICA (PRISMA 2020)", 
        ha='center', va='center', fontsize=11.5, fontweight='bold', color='white')
ax.text(5.0, 9.35, "Processo de identificação, triagem, elegibilidade e inclusão dos estudos", 
        ha='center', va='center', fontsize=8.8, color='#E0EAFC')

# 1. IDENTIFICAÇÃO (y: 6.85 to 9.00)
r_id = patches.FancyBboxPatch((0.15, 6.85), 5.30, 2.15, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.5)
ax.add_patch(r_id)
ax.text(2.80, 8.75, "1. REGISTROS IDENTIFICADOS (n = 1.206)", ha='center', va='center', fontsize=10.2, fontweight='bold', color='#154360')
txt_id = "• PubMed / MEDLINE (n = 342)\n• Scopus - Elsevier (n = 298)\n• Web of Science Core Collection (n = 215)\n• IEEE Xplore Digital Library (n = 187)\n• Relatórios AAPM e SPIE (n = 164)"
ax.text(0.35, 7.75, txt_id, ha='left', va='center', fontsize=8.6, color='#1B4F72')

r_dup = patches.FancyBboxPatch((5.65, 6.85), 4.20, 2.15, boxstyle="round,pad=0.01,rounding_size=0.04",
                               facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.5)
ax.add_patch(r_dup)
ax.text(7.75, 8.75, "DUPLICATAS REMOVIDAS (n = 418)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#922B21')
txt_dup = "• Remoção algorítmica por DOI\n• Triagem manual cruzada\n• Registros únicos restantes:\n  n = 788 registros para triagem"
ax.text(5.85, 7.75, txt_dup, ha='left', va='center', fontsize=8.6, color='#78281F')

draw_exarrow(ax, (5.45, 7.92), (5.65, 7.92))

# 2. TRIAGEM (y: 4.55 to 6.60)
r_scr = patches.FancyBboxPatch((0.15, 4.55), 5.30, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                               facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.5)
ax.add_patch(r_scr)
ax.text(2.80, 6.35, "2. REGISTROS TRIADOS (n = 788)", ha='center', va='center', fontsize=10.2, fontweight='bold', color='#154360')
txt_scr = "• Avaliação cega de Título e Resumo\n• Aplicação preliminar de critérios de escopo\n• Triagem metodológica de pertinência"
ax.text(0.35, 5.40, txt_scr, ha='left', va='center', fontsize=8.6, color='#1B4F72')

r_ex_scr = patches.FancyBboxPatch((5.65, 4.55), 4.20, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                                  facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.5)
ax.add_patch(r_ex_scr)
ax.text(7.75, 6.35, "REGISTROS EXCLUÍDOS (n = 632)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#922B21')
txt_ex_scr = "• Modalidades não-TC (n = 328)\n• Estudos clínicos sem física (n = 214)\n• Resumos sem texto completo (n = 90)"
ax.text(5.85, 5.40, txt_ex_scr, ha='left', va='center', fontsize=8.6, color='#78281F')

draw_arrow(ax, (2.80, 6.85), (2.80, 6.60))
draw_exarrow(ax, (5.45, 5.57), (5.65, 5.57))

# 3. ELEGIBILIDADE (y: 2.25 to 4.30)
r_el = patches.FancyBboxPatch((0.15, 2.25), 5.30, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.5)
ax.add_patch(r_el)
ax.text(2.80, 4.05, "3. TEXTO COMPLETO AVALIADO (n = 156)", ha='center', va='center', fontsize=10.2, fontweight='bold', color='#154360')
txt_el = "• Recuperação integral dos textos completos\n• Avaliação analítica contra critérios PICOS\n• Conformidade com Tabela 3.2 do TCC"
ax.text(0.35, 3.10, txt_el, ha='left', va='center', fontsize=8.6, color='#1B4F72')

r_ex_el = patches.FancyBboxPatch((5.65, 2.25), 4.20, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                                 facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.5)
ax.add_patch(r_ex_el)
ax.text(7.75, 4.05, "ARTIGOS EXCLUÍDOS (n = 118)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#922B21')
txt_ex_el = "• Sem formalismo SDT/Fourier (n = 64)\n• Coortes redundantes/duplicadas (n = 32)\n• Falta de dosimetria padronizada (n = 22)"
ax.text(5.85, 3.10, txt_ex_el, ha='left', va='center', fontsize=8.6, color='#78281F')

draw_arrow(ax, (2.80, 4.55), (2.80, 4.30))
draw_exarrow(ax, (5.45, 3.27), (5.65, 3.27))

# 4. INCLUSÃO (y: 0.10 to 2.00)
r_inc = patches.FancyBboxPatch((0.15, 0.10), 9.70, 1.90, boxstyle="round,pad=0.01,rounding_size=0.04",
                               facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=1.8)
ax.add_patch(r_inc)
ax.text(5.0, 1.65, "4. CORPUS INCLUÍDO NA SÍNTESE FINAL (n = 38 ESTUDOS E RELATÓRIOS)", 
        ha='center', va='center', fontsize=10.8, fontweight='bold', color='#145A32')

txt_inc_1 = "• Artigos em Periódicos Indexados (n = 26)\n  (Med. Phys., IEEE TMI, Radiology, PMB)"
txt_inc_2 = "• Relatórios Normativos (n = 8)\n  (AAPM TG-233, ICRU 54, ICRP 103, ANVISA)"
txt_inc_3 = "• Obras Seminais (n = 4)\n  (Barrett, Bushberg, Rose, Attix)"

ax.text(0.45, 0.75, txt_inc_1, ha='left', va='center', fontsize=8.5, color='#0E6251')
ax.text(3.65, 0.75, txt_inc_2, ha='left', va='center', fontsize=8.5, color='#0E6251')
ax.text(7.15, 0.75, txt_inc_3, ha='left', va='center', fontsize=8.5, color='#0E6251')

draw_arrow(ax, (2.80, 2.25), (2.80, 2.00))

save_compact(fig, 'flow_prisma_flowchart.png')


# ==============================================================================
# FIGURA 4.5: Pipeline do Observador CHO (flow3_cho_pipeline.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 4.4), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

cho_boxes = [
    (0.15, 5.60, 4.70, 4.20, "1. IMAGEM MÉDICA (g)", "Vetor de Pixels (Dimensão N)",
     "• Matriz tomográfica 2D ou 3D\n• Ruído quântico de raios X\n• Fundo anatômico estruturado\n• Hipóteses H0 (ruído) e H1 (sinal+ruído)",
     '#EBF5FB', '#2980B9', '#154360', '#1B4F72'),
    
    (5.15, 5.60, 4.70, 4.20, "2. CANAIS CORTICAIS (T)", "Decomposição V1 (Dimensão P << N)",
     "• Filtros de frequência e orientação\n• Canais D-DOG (diferença de gaussianas)\n• Canais de Gabor 2D e Laguerre-Gauss\n• Redução drástica de dimensionalidade",
     '#FEF9E7', '#F39C12', '#7D6608', '#5B4600'),
    
    (0.15, 2.50, 4.70, 2.80, "3. VETOR CANALIZADO (v)", "v = T · g  (Dimensão P)",
     "• Estatística das respostas dos canais\n• Matriz de Covariância: Kv = T · K · T^T\n• Inversão numérica estável (P pequeno)",
     '#E8F8F5', '#1ABC9C', '#0E6251', '#0B4F42'),
    
    (5.15, 2.50, 4.70, 2.80, "4. DECISÃO ESCALAR (t)", "t = w^T · v  (Filtro Ótimo)",
     "• Filtro ótimo: w = Kv^-1 · <vs>\n• Estatística escalar de decisão diagnóstica\n• Classificação binária da lesão",
     '#EAF2F8', '#34495E', '#1A5276', '#2C3E50')
]

for x, y, w, h, tit, sub, txt, bg, bc, tc, txc in cho_boxes:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor=bg, edgecolor=bc, linewidth=1.5)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.40, tit, ha='center', va='center', fontsize=10.8, fontweight='bold', color=tc)
    ax.text(x + w/2, y + h - 0.85, sub, ha='center', va='center', fontsize=8.8, fontstyle='italic', color=txc)
    ax.text(x + 0.30, y + (h - 1.20)/2, txt, ha='left', va='center', fontsize=8.8, color=txc, multialignment='left')

draw_arrow(ax, (4.85, 7.70), (5.15, 7.70))
draw_arrow(ax, (7.50, 5.60), (7.50, 5.30))
draw_arrow(ax, (5.15, 3.90), (4.85, 3.90))

# Bottom Synthesis Box
r_bot3 = patches.FancyBboxPatch((0.15, 0.10), 9.70, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                                facecolor='#EAFAF1', edgecolor='#27AE60', linewidth=1.8)
ax.add_patch(r_bot3)
ax.text(5.0, 1.60, "ÍNDICE DE DETECTABILIDADE:  d'_CHO = √[ ⟨vs⟩ᵀ · Kv⁻¹ · ⟨vs⟩ ]", 
        ha='center', va='center', fontsize=11.5, fontweight='bold', color='#196F3D')
ax.text(5.0, 0.80, "Máxima correlação objetiva com o desempenho de radiologistas humanos diante de fundos anatômicos complexos.", 
        ha='center', va='center', fontsize=8.8, color='#145A32', multialignment='center')

draw_arrow(ax, (7.50, 2.50), (7.50, 2.15))

save_compact(fig, 'flow3_cho_pipeline.png')


# ==============================================================================
# FIGURA 4.7: Phantoms Híbridos e Metodologia 2AFC (flow4_phantom_hibrido_2afc.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Top Box
r_t4 = patches.FancyBboxPatch((0.15, 8.00), 9.70, 1.85, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.5)
ax.add_patch(r_t4)
ax.text(5.0, 9.15, "AQUISIÇÃO DO PHANTOM FÍSICO REAL (FREDDIE)", 
        ha='center', va='center', fontsize=11.8, fontweight='bold', color='#154360')
ax.text(5.0, 8.50, "Simuladores antropomórficos clínicos em múltiplos níveis de dose, detectores e algoritmos DLR", 
        ha='center', va='center', fontsize=9.0, color='#1B4F72')

# Middle 2 Branches
r_b4_1 = patches.FancyBboxPatch((0.15, 3.20), 4.75, 4.40, boxstyle="round,pad=0.01,rounding_size=0.04",
                                facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.5)
ax.add_patch(r_b4_1)
ax.text(2.525, 7.15, "CASOS DE SINAL AUSENTE (H0)", ha='center', va='center', fontsize=10.8, fontweight='bold', color='#922B21')
ax.text(2.525, 5.20, "• Fundo anatômico autêntico\n• Textura de ruído quântico real\n• Variabilidade estocástica do\n  parênquima biológico normal\n• Amostragem aleatória de ROIs", 
        ha='center', va='center', fontsize=9.0, color='#78281F', multialignment='left')

r_b4_2 = patches.FancyBboxPatch((5.10, 3.20), 4.75, 4.40, boxstyle="round,pad=0.01,rounding_size=0.04",
                                facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=1.5)
ax.add_patch(r_b4_2)
ax.text(7.475, 7.15, "INSERÇÃO HÍBRIDA DE LESÕES (H1)", ha='center', va='center', fontsize=10.8, fontweight='bold', color='#7D6608')
ax.text(7.475, 5.20, "• Modelagem matemática 3D da lesão\n• Convolução com a PSF 3D real do scanner\n• Inserção do perfil atenuador no fundo\n• Alvos com contraste e tamanho clínicos", 
        ha='center', va='center', fontsize=9.0, color='#5B4600', multialignment='left')

draw_arrow(ax, (3.0, 8.00), (2.525, 7.60))
draw_arrow(ax, (7.0, 8.00), (7.475, 7.60))

# Bottom Box
r_bot4 = patches.FancyBboxPatch((0.15, 0.10), 9.70, 2.70, boxstyle="round,pad=0.01,rounding_size=0.04",
                                facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=1.8)
ax.add_patch(r_bot4)
ax.text(5.0, 2.20, "PLATAFORMA DE TESTE PSICOFÍSICO CEGO 2AFC", 
        ha='center', va='center', fontsize=11.8, fontweight='bold', color='#145A32')
ax.text(5.0, 1.45, "Apresentação pareada aleatória (H0 vs H1) em monitores calibrados no padrão DICOM GSDF.", 
        ha='center', va='center', fontsize=9.2, color='#0E6251')
ax.text(5.0, 0.70, "Validação cruzada direta: Radiologistas Especialistas vs Observadores Computacionais (DLMO).", 
        ha='center', va='center', fontsize=8.8, color='#145A32')

draw_arrow(ax, (2.525, 3.20), (3.8, 2.80))
draw_arrow(ax, (7.475, 3.20), (6.2, 2.80))

save_compact(fig, 'flow4_phantom_hibrido_2afc.png')


# ==============================================================================
# FIGURA 4.8: Arquitetura DLMO Vision Transformer (flow5_dlmo_architecture.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 4.6), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

dlmo_boxes = [
    (0.15, 5.60, 4.70, 4.20, "1. IMAGEM MÉDICA (g)", "ROI Tomográfica 2D/3D",
     "• Textura não-linear gerada por DLR\n• Ruído anisotrópico não-estacionário\n• Presença de sinal H0 (ausente) ou H1",
     '#EBF5FB', '#2980B9', '#154360', '#1B4F72'),
    
    (5.15, 5.60, 4.70, 4.20, "2. RETALHOS & EMBEDDINGS", "Divisão em Patches 2D",
     "• Quebra da ROI em retalhos espaciais\n• Projeção linear e positional embeddings\n• Captura simultânea de bordas e texturas",
     '#E8F8F5', '#16A085', '#0E6251', '#0B4F42'),
    
    (0.15, 2.50, 4.70, 2.80, "3. AUTO-ATENÇÃO (ViT)", "Multi-Head Self-Attention",
     "• Ponderação contextual global e local\n• Modelagem de atenção foveal e periférica\n• Invariância a distorções não-lineares",
     '#FEF9E7', '#F39C12', '#7D6608', '#5B4600'),
    
    (5.15, 2.50, 4.70, 2.80, "4. DECISÃO (d'_DL)", "Classificador Perceptual MLP",
     "• Vetor de características semânticas\n• Estatística escalar de decisão diagnóstica\n• Extração do índice de detectabilidade d'_DL",
     '#EAFAF1', '#27AE60', '#196F3D', '#145A32')
]

for x, y, w, h, tit, sub, txt, bg, bc, tc, txc in dlmo_boxes:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor=bg, edgecolor=bc, linewidth=1.5)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.40, tit, ha='center', va='center', fontsize=10.8, fontweight='bold', color=tc)
    ax.text(x + w/2, y + h - 0.85, sub, ha='center', va='center', fontsize=8.8, fontstyle='italic', color=txc)
    ax.text(x + 0.30, y + (h - 1.20)/2, txt, ha='left', va='center', fontsize=8.8, color=txc, multialignment='left')

draw_arrow(ax, (4.85, 7.70), (5.15, 7.70))
draw_arrow(ax, (7.50, 5.60), (7.50, 5.30))
draw_arrow(ax, (5.15, 3.90), (4.85, 3.90))

# Bottom Loss Box
r_bot5 = patches.FancyBboxPatch((0.15, 0.10), 9.70, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                                facecolor='#FADBD8', edgecolor='#E74C3C', linewidth=1.8)
ax.add_patch(r_bot5)
ax.text(5.0, 1.55, "FUNÇÃO DE PERDA PERCEPTUAL:  L_total = L_class + λ · ( d'_DL - d'_humano )²", 
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#922B21')
ax.text(5.0, 0.75, "Ancoragem matemática do observador computacional ao córtex visual dos médicos radiologistas.", 
        ha='center', va='center', fontsize=8.8, color='#78281F')

draw_arrow(ax, (7.50, 2.50), (7.50, 2.15))

save_compact(fig, 'flow5_dlmo_architecture.png')


# ==============================================================================
# FIGURA 4.10: Pipeline Integrado de Software Metrológico (flow6_software_pipeline.png)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.2, 5.5), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Module 1 & 2 (Top Row)
r_m1 = patches.FancyBboxPatch((0.15, 7.80), 4.75, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.5)
ax.add_patch(r_m1)
ax.text(2.525, 9.35, "MÓDULO 1: ENTRADA DICOM", ha='center', va='center', fontsize=10.8, fontweight='bold', color='#154360')
ax.text(2.525, 8.55, "Leitura de imagens e metadados\n(kVp, mA, tempo, dose CTDI, kernel, DLR)", ha='center', va='center', fontsize=8.8, color='#1B4F72', multialignment='center')

r_m2 = patches.FancyBboxPatch((5.10, 7.80), 4.75, 2.05, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#E8F8F5', edgecolor='#16A085', linewidth=1.5)
ax.add_patch(r_m2)
ax.text(7.475, 9.35, "MÓDULO 2: SEGMENTAÇÃO ROIs", ha='center', va='center', fontsize=10.8, fontweight='bold', color='#0E6251')
ax.text(7.475, 8.55, "Localização de insertos e amostragem\nautomática de ROIs homogêneas (M ≥ 100)", ha='center', va='center', fontsize=8.8, color='#0B4F42', multialignment='center')

draw_arrow(ax, (4.90, 8.82), (5.10, 8.82))

# Module 3A & 3B (Second Row)
r_m3a = patches.FancyBboxPatch((0.15, 5.35), 4.75, 2.15, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=1.5)
ax.add_patch(r_m3a)
ax.text(2.525, 6.95, "MÓDULO 3A: RESOLUÇÃO TTF(f)", ha='center', va='center', fontsize=10.8, fontweight='bold', color='#7D6608')
ax.text(2.525, 6.10, "• Borda circular em insertos de calibração\n• ESF(r) → LSF(r) → TTF(f) → f50 e f10", ha='center', va='center', fontsize=8.8, color='#5B4600')

r_m3b = patches.FancyBboxPatch((5.10, 5.35), 4.75, 2.15, boxstyle="round,pad=0.01,rounding_size=0.04",
                              facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=1.5)
ax.add_patch(r_m3b)
ax.text(7.475, 6.95, "MÓDULO 3B: TEXTURA NPS(f)", ha='center', va='center', fontsize=10.8, fontweight='bold', color='#7D6608')
ax.text(7.475, 6.10, "• Detrending polinomial 2D P2(x, y)\n• Janela Hanning 2D → NPS 2D/1D → f_peak", ha='center', va='center', fontsize=8.8, color='#5B4600')

draw_arrow(ax, (2.525, 7.80), (2.525, 7.50))
draw_arrow(ax, (7.475, 7.80), (7.475, 7.50))

# Module 4 (Third Row)
r_m4 = patches.FancyBboxPatch((0.15, 2.80), 9.70, 2.25, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#EAFAF1', edgecolor='#27AE60', linewidth=1.5)
ax.add_patch(r_m4)
ax.text(5.0, 4.45, "MÓDULO 4: OBSERVADORES COMPUTACIONAIS DE MODELO", ha='center', va='center', fontsize=11.2, fontweight='bold', color='#196F3D')
ax.text(5.0, 3.55, "• Observadores Lineares: NPWE e CHO (Canais D-DOG, Laguerre-Gauss, Gabor 2D)\n• Observadores Profundos: DLMO (Vision Transformers com auto-atenção multi-cabeça)", 
        ha='center', va='center', fontsize=9.0, color='#145A32', multialignment='center')

draw_arrow(ax, (2.525, 5.35), (3.8, 5.05))
draw_arrow(ax, (7.475, 5.35), (6.2, 5.05))

# Module 5 (Bottom Row)
r_m5 = patches.FancyBboxPatch((0.15, 0.10), 9.70, 2.40, boxstyle="round,pad=0.01,rounding_size=0.04",
                             facecolor='#FADBD8', edgecolor='#E74C3C', linewidth=1.8)
ax.add_patch(r_m5)
ax.text(5.0, 1.85, "MÓDULO 5: INCERTEZA E OTIMIZAÇÃO MULTIOBJETIVO (PARETO)", ha='center', va='center', fontsize=11.2, fontweight='bold', color='#922B21')
ax.text(5.0, 0.95, "• Incerteza estatística por Bootstrap (B = 2000 reamostragens)\n• Algoritmo Genético NSGA-II (Fronteira 3D) e Ranqueamento Multicritério TOPSIS", 
        ha='center', va='center', fontsize=9.0, color='#78281F', multialignment='center')

draw_arrow(ax, (5.0, 2.80), (5.0, 2.50))

save_compact(fig, 'flow6_software_pipeline.png')

print("TODAS AS FIGURAS (INCLUINDO 4.1 PRISMA) REGERADAS COM SUCESSO!")
