import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

fig, ax = plt.subplots(figsize=(10, 11), dpi=300)
ax.axis('off')

# Color palette
box_face = '#F8FAFC'
box_edge = '#0284C7'
header_face = '#0369A1'
text_color = '#0F172A'
subtext_color = '#334155'
arrow_color = '#0284C7'

# Phases on the left
phases = [
    ("IDENTIFICAÇÃO", 0.88),
    ("TRIAGEM", 0.64),
    ("ELEGIBILIDADE", 0.40),
    ("INCLUSÃO", 0.16)
]

for title, y_pos in phases:
    # Phase banner
    ax.text(0.04, y_pos, title, fontsize=10, fontweight='bold', color='#0369A1', 
            rotation=90, va='center', ha='center',
            bbox=dict(boxstyle='square,pad=0.4', facecolor='#E0F2FE', edgecolor='#BAE6FD', lw=1.5))

def draw_box(ax, x, y, w, h, title, lines, is_excluded=False):
    edge = '#EF4444' if is_excluded else box_edge
    face = '#FEF2F2' if is_excluded else box_face
    
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.02",
                                  facecolor=face, edgecolor=edge, lw=1.5)
    ax.add_patch(rect)
    
    # Title
    t_color = '#991B1B' if is_excluded else '#0369A1'
    ax.text(x + w/2, y + h - 0.025, title, fontsize=9.5, fontweight='bold',
            color=t_color, ha='center', va='top')
    
    # Text lines
    cur_y = y + h - 0.055
    for line in lines:
        ax.text(x + 0.015, cur_y, line, fontsize=8.2, color=text_color, ha='left', va='top')
        cur_y -= 0.024

# 1. Identification Box
draw_box(ax, 0.12, 0.77, 0.45, 0.20, 
         "Registros Identificados nas Bases (n = 1.206)", 
         [
             "• PubMed / MEDLINE (n = 342)",
             "• Scopus - Elsevier (n = 298)",
             "• Web of Science Core Collection (n = 215)",
             "• IEEE Xplore Digital Library (n = 187)",
             "• AAPM Reports & SPIE Digital Library (n = 164)"
         ])

# Duplicates Removed Box
draw_box(ax, 0.62, 0.77, 0.35, 0.14,
         "Duplicatas Removidas (n = 418)",
         [
             "• Identificação algorítmica e",
             "  triagem manual cruzada",
             "• Registros únicos: n = 788"
         ], is_excluded=True)

# 2. Screening Box
draw_box(ax, 0.12, 0.53, 0.45, 0.16,
         "Registros Triados (n = 788)",
         [
             "• Avaliação de Título e Resumo",
             "• Aplicação preliminar de escopo",
             "• Triagem por pares independentes"
         ])

# Excluded Screening Box
draw_box(ax, 0.62, 0.51, 0.35, 0.20,
         "Registros Excluídos (n = 632)",
         [
             "• Modalidades não tomográficas",
             "  (RM, US, SPECT) (n = 328)",
             "• Estudos clínicos sem metrologia",
             "  ou física de imagens (n = 214)",
             "• Resumos de congressos sem texto",
             "  integral analítico (n = 90)"
         ], is_excluded=True)

# 3. Eligibility Box
draw_box(ax, 0.12, 0.29, 0.45, 0.16,
         "Texto Completo Recuperado (n = 156)",
         [
             "• Artigos recuperados na íntegra",
             "• Avaliação aprofundada contra",
             "  critérios de elegibilidade (Tab. 3.2)"
         ])

# Excluded Eligibility Box
draw_box(ax, 0.62, 0.27, 0.35, 0.20,
         "Artigos Excluídos na Íntegra (n = 118)",
         [
             "• Ausência de formalismo SDT,",
             "  Fourier ou observadores (n = 64)",
             "• Dados duplicados de coortes (n = 32)",
             "• Falta de parametrização física",
             "  e dosimétrica rigorosa (n = 22)"
         ], is_excluded=True)

# 4. Inclusion Box
draw_box(ax, 0.12, 0.05, 0.45, 0.18,
         "Corpus Incluído na Síntese (n = 38)",
         [
             "• Artigos em periódicos revisados (n = 26)",
             "• Relatórios normativos internacionais",
             "  (AAPM, ICRU, ICRP, ANVISA) (n = 8)",
             "• Obras seminais e livros-texto (n = 4)"
         ])

# Synthesis Box (Right side of inclusion)
draw_box(ax, 0.62, 0.05, 0.35, 0.18,
         "Síntese e Modelagem Teórica",
         [
             "• Deduções contínuas de SDT/Fourier",
             "• Parametrização em Python (Tab. 3.3)",
             "• Síntese metrológica TG-233",
             "• Otimização multiobjetivo Pareto"
         ])

# Arrows
arrow_kw = dict(arrowstyle="->", color=arrow_color, lw=2, mutation_scale=15)
arrow_ex_kw = dict(arrowstyle="->", color='#EF4444', lw=2, mutation_scale=15)

# Identification -> Screening
ax.annotate("", xy=(0.345, 0.69), xytext=(0.345, 0.77), arrowprops=arrow_kw)
# Identification -> Duplicates
ax.annotate("", xy=(0.62, 0.84), xytext=(0.57, 0.84), arrowprops=arrow_ex_kw)

# Screening -> Eligibility
ax.annotate("", xy=(0.345, 0.45), xytext=(0.345, 0.53), arrowprops=arrow_kw)
# Screening -> Excluded Screening
ax.annotate("", xy=(0.62, 0.61), xytext=(0.57, 0.61), arrowprops=arrow_ex_kw)

# Eligibility -> Inclusion
ax.annotate("", xy=(0.345, 0.23), xytext=(0.345, 0.29), arrowprops=arrow_kw)
# Eligibility -> Excluded Eligibility
ax.annotate("", xy=(0.62, 0.37), xytext=(0.57, 0.37), arrowprops=arrow_ex_kw)

# Inclusion -> Synthesis
ax.annotate("", xy=(0.62, 0.14), xytext=(0.57, 0.14), arrowprops=arrow_kw)

plt.tight_layout()
out_fig = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/figuras/flow_prisma_flowchart.png"
plt.savefig(out_fig, bbox_inches='tight', dpi=300)
print("PRISMA Flowchart created at:", out_fig)
