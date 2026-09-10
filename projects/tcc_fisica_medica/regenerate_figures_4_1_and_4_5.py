import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

target_dirs = [
    '/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile',
    '/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/figuras'
]

def save_fig(fig, filename):
    for d in target_dirs:
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, filename)
        fig.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"Saved: {path} ({os.path.getsize(path)} bytes)")

def draw_arrow(ax, start, end, color='#2C3E50', lw=2.0, style='->'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                shrinkA=2, shrinkB=2, mutation_scale=16))

def draw_exarrow(ax, start, end, color='#C0392B', lw=1.8):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                shrinkA=2, shrinkB=2, mutation_scale=14))

# ==============================================================================
# 1. FIGURA 4.1: FLUXOGRAMA PRISMA 2020 (flow_prisma_flowchart.png)
# ==============================================================================
# Design: Proporção perfeita letra/box, zero espaço ocioso, fontes nítidas e grandes
fig, ax = plt.subplots(figsize=(7.5, 8.2), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Header Box
r_head = patches.FancyBboxPatch((0.10, 9.25), 9.80, 0.65, boxstyle="round,pad=0.01,rounding_size=0.03",
                               facecolor='#0B3C68', edgecolor='#0B3C68', linewidth=1.5)
ax.add_patch(r_head)
ax.text(5.0, 9.68, "FLUXOGRAMA DE SELEÇÃO SISTEMÁTICA (PRISMA 2020)", 
        ha='center', va='center', fontsize=12.5, fontweight='bold', color='white')
ax.text(5.0, 9.40, "Identificação, Triagem, Elegibilidade e Inclusão dos Estudos do Corpus Metrológico", 
        ha='center', va='center', fontsize=9.5, color='#E0EAFC')

# 1. IDENTIFICAÇÃO (y: 6.95 to 9.05)
r_id = patches.FancyBboxPatch((0.10, 6.95), 5.40, 2.10, boxstyle="round,pad=0.01,rounding_size=0.03",
                              facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.6)
ax.add_patch(r_id)
ax.text(2.80, 8.78, "1. IDENTIFICAÇÃO (n = 1.206)", ha='center', va='center', fontsize=11.2, fontweight='bold', color='#154360')
txt_id = "• PubMed / MEDLINE: n = 342\n• Scopus (Elsevier): n = 298\n• Web of Science: n = 215\n• IEEE Xplore Library: n = 187\n• Relatórios AAPM / SPIE: n = 164"
ax.text(0.30, 7.80, txt_id, ha='left', va='center', fontsize=9.8, color='#1B4F72', linespacing=1.35)

r_dup = patches.FancyBboxPatch((5.80, 6.95), 4.10, 2.10, boxstyle="round,pad=0.01,rounding_size=0.03",
                               facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.6)
ax.add_patch(r_dup)
ax.text(7.85, 8.78, "DUPLICATAS (n = 418)", ha='center', va='center', fontsize=11.0, fontweight='bold', color='#922B21')
txt_dup = "• Remoção por DOI / Título\n• Triagem cruzada manual\n• Restante para Triagem:\n  n = 788 registros únicos"
ax.text(5.98, 7.80, txt_dup, ha='left', va='center', fontsize=9.6, color='#78281F', linespacing=1.35)

draw_exarrow(ax, (5.50, 8.00), (5.80, 8.00))

# 2. TRIAGEM (y: 4.65 to 6.75)
r_scr = patches.FancyBboxPatch((0.10, 4.65), 5.40, 2.10, boxstyle="round,pad=0.01,rounding_size=0.03",
                               facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.6)
ax.add_patch(r_scr)
ax.text(2.80, 6.48, "2. TRIAGEM (n = 788)", ha='center', va='center', fontsize=11.2, fontweight='bold', color='#154360')
txt_scr = "• Leitura de Título e Resumo\n• Aplicação do escopo temático\n• Filtragem metodológica cega\n• Registros selecionados: n = 156"
ax.text(0.30, 5.50, txt_scr, ha='left', va='center', fontsize=9.8, color='#1B4F72', linespacing=1.35)

r_ex_scr = patches.FancyBboxPatch((5.80, 4.65), 4.10, 2.10, boxstyle="round,pad=0.01,rounding_size=0.03",
                                  facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.6)
ax.add_patch(r_ex_scr)
ax.text(7.85, 6.48, "EXCLUÍDOS (n = 632)", ha='center', va='center', fontsize=11.0, fontweight='bold', color='#922B21')
txt_ex_scr = "• Modalidades não-TC (n = 328)\n• Estudos clínicos s/ física (n = 214)\n• Resumos sem texto (n = 90)"
ax.text(5.98, 5.50, txt_ex_scr, ha='left', va='center', fontsize=9.6, color='#78281F', linespacing=1.35)

draw_arrow(ax, (2.80, 6.95), (2.80, 6.75))
draw_exarrow(ax, (5.50, 5.70), (5.80, 5.70))

# 3. ELEGIBILIDADE (y: 2.35 to 4.45)
r_el = patches.FancyBboxPatch((0.10, 2.35), 5.40, 2.10, boxstyle="round,pad=0.01,rounding_size=0.03",
                              facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=1.6)
ax.add_patch(r_el)
ax.text(2.80, 4.18, "3. ELEGIBILIDADE (n = 156)", ha='center', va='center', fontsize=11.2, fontweight='bold', color='#154360')
txt_el = "• Recuperação do texto integral\n• Avaliação analítica detalhada\n• Critérios de inclusão (Tab. 3.2)\n• Aprovados para síntese: n = 38"
ax.text(0.30, 3.20, txt_el, ha='left', va='center', fontsize=9.8, color='#1B4F72', linespacing=1.35)

r_ex_el = patches.FancyBboxPatch((5.80, 2.35), 4.10, 2.10, boxstyle="round,pad=0.01,rounding_size=0.03",
                                 facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=1.6)
ax.add_patch(r_ex_el)
ax.text(7.85, 4.18, "EXCLUÍDOS (n = 118)", ha='center', va='center', fontsize=11.0, fontweight='bold', color='#922B21')
txt_ex_el = "• Sem formalismo SDT/Fourier (n = 64)\n• Dados redundantes (n = 32)\n• Dosimetria incompleta (n = 22)"
ax.text(5.98, 3.20, txt_ex_el, ha='left', va='center', fontsize=9.6, color='#78281F', linespacing=1.35)

draw_arrow(ax, (2.80, 4.65), (2.80, 4.45))
draw_exarrow(ax, (5.50, 3.40), (5.80, 3.40))

# 4. INCLUSÃO (y: 0.10 to 2.10)
r_inc = patches.FancyBboxPatch((0.10, 0.10), 9.80, 2.00, boxstyle="round,pad=0.01,rounding_size=0.03",
                               facecolor='#D4EFDF', edgecolor='#27AE60', linewidth=2.0)
ax.add_patch(r_inc)
ax.text(5.0, 1.78, "4. CORPUS INCLUÍDO NA SÍNTESE FINAL (n = 38 PUBLICAÇÕES)", 
        ha='center', va='center', fontsize=12.0, fontweight='bold', color='#145A32')

txt_inc_1 = "• Artigos Indexados (n = 26)\n  Med. Phys., IEEE TMI, Radiology\n  PMB, European Radiology"
txt_inc_2 = "• Relatórios Normativos (n = 8)\n  AAPM TG-233, ICRU 54, ICRP 103\n  ANVISA RDC 611/2022"
txt_inc_3 = "• Obras Seminais (n = 4)\n  Barrett & Myers, Bushberg\n  Rose, Attix (Física Médica)"

ax.text(0.35, 0.85, txt_inc_1, ha='left', va='center', fontsize=9.6, color='#0E6251', linespacing=1.30)
ax.text(3.70, 0.85, txt_inc_2, ha='left', va='center', fontsize=9.6, color='#0E6251', linespacing=1.30)
ax.text(7.15, 0.85, txt_inc_3, ha='left', va='center', fontsize=9.6, color='#0E6251', linespacing=1.30)

draw_arrow(ax, (2.80, 2.35), (2.80, 2.10))

save_fig(fig, 'flow_prisma_flowchart.png')
plt.close(fig)


# ==============================================================================
# 2. FIGURA 4.5: PIPELINE DO OBSERVADOR CHO (flow3_cho_pipeline.png)
# ==============================================================================
# Design: Letras grandes, alta legibilidade, fórmulas matemáticas nítidas, proporção compacta
fig, ax = plt.subplots(figsize=(7.5, 4.6), constrained_layout=True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

cho_boxes = [
    (0.10, 5.50, 4.75, 4.35, "1. IMAGEM MÉDICA (g)", "Vetor de Pixels — Dimensão N",
     "• Matriz tomográfica 2D / 3D discretizada\n• Ruído quântico de fótons de raios X\n• Fundo anatômico complexo estruturado\n• Hipóteses: H0 (ruído) vs. H1 (sinal + ruído)",
     '#EBF5FB', '#2980B9', '#154360', '#1B4F72'),
    
    (5.15, 5.50, 4.75, 4.35, "2. CANAIS CORTICAIS (T)", "Decomposição V1 — Dimensão P ≪ N",
     "• Filtros de frequência e orientação angular\n• Canais D-DOG (diferença de gaussianas)\n• Canais de Gabor 2D / Laguerre-Gauss\n• Redução drástica: N ~ 10⁴ → P ≤ 10",
     '#FEF9E7', '#F39C12', '#7D6608', '#5B4600'),
    
    (0.10, 2.45, 4.75, 2.80, "3. VETOR CANALIZADO (v)", "v = T · g  |  Matriz de Covariância Kv",
     "• Respostas dos canais: v ∈ ℝᴾ\n• Covariância: Kv = T · K · Tᵀ  (P × P)\n• Inversão matricial estável e direta (Kv⁻¹)",
     '#E8F8F5', '#1ABC9C', '#0E6251', '#0B4F42'),
    
    (5.15, 2.45, 4.75, 2.80, "4. DECISÃO ESCALAR (t)", "t = wᵀ · v  |  Filtro Ótimo de Hotelling",
     "• Template ótimo: w = Kv⁻¹ · ⟨vs⟩\n• Escalar de decisão: t = wᵀ · v\n• Teste de decisão binária e curva ROC",
     '#EAF2F8', '#34495E', '#1A5276', '#2C3E50')
]

for x, y, w, h, tit, sub, txt, bg, bc, tc, txc in cho_boxes:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.03",
                              facecolor=bg, edgecolor=bc, linewidth=1.6)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.45, tit, ha='center', va='center', fontsize=11.5, fontweight='bold', color=tc)
    ax.text(x + w/2, y + h - 0.95, sub, ha='center', va='center', fontsize=9.6, fontweight='bold', fontstyle='italic', color=txc)
    ax.text(x + 0.25, y + (h - 1.30)/2, txt, ha='left', va='center', fontsize=9.6, color=txc, linespacing=1.35)

# Setas de fluxo
draw_arrow(ax, (4.85, 7.68), (5.15, 7.68), lw=2.2) # 1 -> 2
draw_arrow(ax, (7.52, 5.50), (7.52, 5.25), lw=2.2) # 2 -> 4
draw_arrow(ax, (5.15, 3.85), (4.85, 3.85), lw=2.2) # 4 -> 3

# Box de Síntese Inferior (Fórmula do Índice de Detectabilidade)
r_bot3 = patches.FancyBboxPatch((0.10, 0.10), 9.80, 2.05, boxstyle="round,pad=0.01,rounding_size=0.03",
                                facecolor='#EAFAF1', edgecolor='#27AE60', linewidth=2.0)
ax.add_patch(r_bot3)
ax.text(5.0, 1.55, "ÍNDICE DE DETECTABILIDADE:  d'_CHO = √[ ⟨vs⟩ᵀ · Kv⁻¹ · ⟨vs⟩ ]", 
        ha='center', va='center', fontsize=12.5, fontweight='bold', color='#196F3D')
ax.text(5.0, 0.70, "Máxima correlação objetiva (r > 0,90) com o desempenho psicofísico de médicos radiologistas\nem fundos anatômicos complexos com ruído estruturado em lei de potência.", 
        ha='center', va='center', fontsize=9.6, color='#145A32', linespacing=1.30)

draw_arrow(ax, (2.48, 2.45), (2.48, 2.15), lw=2.2) # 3 -> Bot

save_fig(fig, 'flow3_cho_pipeline.png')
plt.close(fig)

print("Todas as figuras foram regeneradas com sucesso!")
