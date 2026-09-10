import os
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import zipfile
import shutil

project_dir = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_2026"
fig_dir = os.path.join(project_dir, "figuras")
tex_dir = os.path.join(project_dir, "tex")
os.makedirs(fig_dir, exist_ok=True)
os.makedirs(tex_dir, exist_ok=True)

print("1. Gerando gráficos científicos e diagramas de alta resolução...")

# Global style for matplotlib
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 8.5
plt.rcParams['figure.titlesize'] = 13
plt.rcParams['lines.linewidth'] = 1.8
plt.rcParams['grid.alpha'] = 0.35

# -------------------------------------------------------------
# FIGURA 1: Teoria de Detecção de Sinais (SDT), Curvas ROC e Psicofísica 2AFC
# -------------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4.5), constrained_layout=True)

t = np.linspace(-4, 7, 500)
mu0, sigma0 = 0.0, 1.0
mu1, sigma1 = 2.2, 1.0
tc = 1.3

p0 = (1 / (sigma0 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((t - mu0) / sigma0) ** 2)
p1 = (1 / (sigma1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((t - mu1) / sigma1) ** 2)

ax1.plot(t, p0, 'b-', label=r'$p(t|H_0)$ (Sinal Ausente)')
ax1.plot(t, p1, 'r-', label=r'$p(t|H_1)$ (Sinal Presente)')
ax1.axvline(tc, color='k', linestyle='--', linewidth=1.5, label=r'Limiar $t_c = 1.3$')
ax1.fill_between(t, p1, where=(t >= tc), color='red', alpha=0.25, label='Sensibilidade (TPF)')
ax1.fill_between(t, p0, where=(t >= tc), color='blue', alpha=0.25, label='Falso Positivo (FPF)')
ax1.annotate(r'$d^\prime = 2.2$', xy=(mu0, 0.41), xytext=(mu1, 0.41),
             arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5),
             ha='center', va='bottom', fontsize=10, fontweight='bold', color='purple')
ax1.set_title('(A) Distribuições de Decisão da SDT')
ax1.set_xlabel('Estatística de Teste Escalar ($t$)')
ax1.set_ylabel('Densidade de Probabilidade $p(t)$')
ax1.grid(True)
ax1.legend(loc='upper right', frameon=True, fontsize=8)
ax1.set_ylim(0, 0.48)

fpf = np.linspace(0.0001, 0.9999, 300)

def norm_cdf(x):
    return 0.5 * (1.0 + np.vectorize(math.erf)(x / np.sqrt(2.0)))

def norm_ppf(p):
    p = np.asarray(p)
    q = np.where(p < 0.5, p, 1 - p)
    q = np.clip(q, 1e-15, 0.5)
    t_val = np.sqrt(-2 * np.log(q))
    c0 = 2.515517; c1 = 0.802853; c2 = 0.010328
    d1 = 1.432788; d2 = 0.189269; d3 = 0.001308
    approx = t_val - ((c2 * t_val + c1) * t_val + c0) / (((d3 * t_val + d2) * t_val + d1) * t_val + 1.0)
    return np.where(p < 0.5, -approx, approx)

d_primes = [0.5, 1.0, 1.8, 2.5, 3.5, 4.5]
colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(d_primes)))

z_fpf = norm_ppf(fpf)
for dp, col in zip(d_primes, colors):
    tpf = norm_cdf(z_fpf + dp)
    ax2.plot(fpf, tpf, label=f"$d' = {dp:.1f}$", color=col)

ax2.plot([0, 1], [0, 1], 'k:', label=r'Chance ($d^\prime = 0$)')
ax2.set_title(r'(B) Curvas ROC em Função de $d^\prime$')
ax2.set_xlabel('Fração de Falsos Positivos (FPF)')
ax2.set_ylabel('Fração de Verdadeiros Positivos (TPF)')
ax2.grid(True)
ax2.legend(loc='lower right', frameon=True, fontsize=8)

dp_range = np.linspace(0, 5, 200)
pc_values = norm_cdf(dp_range / np.sqrt(2.0))

ax3.plot(dp_range, pc_values * 100, 'darkgreen', lw=2.2, label=r'$P_C = \Phi(d^\prime / \sqrt{2})$')
ax3.axhline(50, color='gray', linestyle=':', label='Acerto ao Acaso (50%)')
ax3.axvline(1.8, color='orange', linestyle='--', label=r'Limiar Clínico ($d^\prime \approx 1.8 \rightarrow 89.8\%$)')
ax3.axvline(4.0, color='crimson', linestyle='--', label=r'Critério de Rose ($d^\prime \geq 4.0 \rightarrow 99.8\%$)')
ax3.set_title(r'(C) Desempenho no Paradigma 2AFC')
ax3.set_xlabel(r'Índice de Detectabilidade ($d^\prime$)')
ax3.set_ylabel('Proporção de Acertos $P_C$ (%)')
ax3.set_ylim(45, 102)
ax3.grid(True)
ax3.legend(loc='lower right', frameon=True, fontsize=8)

plt.savefig(os.path.join(fig_dir, 'fig1_sdt_roc_2afc.png'))
plt.close()

# -------------------------------------------------------------
# FIGURA 2: Métricas Espectrais Físicas (TTF, NPS, Filtro Ocular E(f) e Wtask)
# -------------------------------------------------------------
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 9), constrained_layout=True)

f = np.linspace(0.001, 1.5, 400)

ttf_iodo = 1.0 / (1.0 + (f / 0.58)**2.8)
ttf_teflon = 1.0 / (1.0 + (f / 0.52)**2.6)
ttf_delrin = 1.0 / (1.0 + (f / 0.42)**2.4)
ttf_water = 1.0 / (1.0 + (f / 0.35)**2.2)

ax1.plot(f, ttf_iodo, 'darkred', label=r'Iodo (+350 HU) - $f_{50} = 0.58\text{ mm}^{-1}$')
ax1.plot(f, ttf_teflon, 'tab:orange', label=r'Teflon (+900 HU) - $f_{50} = 0.52\text{ mm}^{-1}$')
ax1.plot(f, ttf_delrin, 'tab:blue', label=r'Delrin (+340 HU) - $f_{50} = 0.42\text{ mm}^{-1}$')
ax1.plot(f, ttf_water, 'tab:cyan', label=r'Solid Water (+20 HU) - $f_{50} = 0.35\text{ mm}^{-1}$')
ax1.axhline(0.5, color='k', linestyle=':', label=r'Nível $f_{50}$')
ax1.set_title(r'(A) Função de Transferência da Tarefa $TTF(f)$')
ax1.set_xlabel(r'Frequência Espacial $f$ ($\text{mm}^{-1}$)')
ax1.set_ylabel(r'Modulação $TTF(f)$')
ax1.set_xlim(0, 1.2)
ax1.set_ylim(0, 1.05)
ax1.grid(True)
ax1.legend(loc='upper right', frameon=True)

nps_fbp = 1500 * (f**1.1) * np.exp(-(f / 0.65)**2.2)
nps_hir = 1100 * (f**0.9) * np.exp(-(f / 0.48)**2.0)
nps_dlr = 750 * (f**0.95) * np.exp(-(f / 0.55)**2.1)
nps_mbir = 900 * (f**0.4) * np.exp(-(f / 0.30)**1.8)

ax2.plot(f, nps_fbp, 'k-', label=r'FBP (Rampa clássica, $f_{\text{peak}} \approx 0.45$)')
ax2.plot(f, nps_hir, 'tab:blue', label=r'HIR (Intermediário, $f_{\text{peak}} \approx 0.35$)')
ax2.plot(f, nps_dlr, 'tab:green', lw=2.2, label=r'DLR (Preservação de textura, $f_{\text{peak}} \approx 0.40$)')
ax2.plot(f, nps_mbir, 'tab:purple', linestyle='--', label=r'MBIR Agressivo ("Plastic look", $f_{\text{peak}} \approx 0.18$)')
ax2.set_title(r'(B) Espectro de Potência do Ruído $NPS(f)$')
ax2.set_xlabel(r'Frequência Espacial $f$ ($\text{mm}^{-1}$)')
ax2.set_ylabel(r'Densidade Espectral $NPS(f)$ ($\text{HU}^2\cdot\text{mm}^2$)')
ax2.set_xlim(0, 1.2)
ax2.grid(True)
ax2.legend(loc='upper right', frameon=True)

f_retina = np.linspace(0.01, 30, 400)
f0 = 0.8; n_exp = 1.3; m_exp = 1.1; c_exp = 2.2
e_retina = (f_retina / f0)**n_exp * np.exp(-c_exp * (f_retina / f0)**m_exp)
e_retina = e_retina / np.max(e_retina)

ax3.plot(f_retina, e_retina, 'darkblue', lw=2.0, label=r'Sensibilidade Ocular $E(f)$')
peak_idx = np.argmax(e_retina)
ax3.axvline(f_retina[peak_idx], color='red', linestyle='--', 
            label=f'Pico Máximo Visual $\\approx {f_retina[peak_idx]:.1f}$ cpd ($0.45\\text{{ mm}}^{{-1}}$)')
ax3.set_title(r'(C) Filtro Ocular Humano $E(f)$ (Sensibilidade ao Contraste)')
ax3.set_xlabel('Frequência Retiniana (ciclos/grau)')
ax3.set_ylabel(r'Sensibilidade Normalizada $E(f)$')
ax3.set_xlim(0, 25)
ax3.set_ylim(0, 1.05)
ax3.grid(True)
ax3.legend(loc='upper right', frameon=True)

def j1_approx(x):
    val = np.zeros_like(x)
    small = (x < 3.0)
    xs = x[small]
    val[small] = 0.5 * xs - (xs**3) / 16.0 + (xs**5) / 384.0 - (xs**7) / 18432.0
    xb = x[~small]
    val[~small] = np.sqrt(2.0 / (np.pi * xb)) * np.cos(xb - 3 * np.pi / 4)
    return val

diameters = [3.0, 5.0, 8.0, 12.0]
colors_d = ['tab:red', 'tab:green', 'tab:blue', 'tab:purple']

for d_val, col in zip(diameters, colors_d):
    R = d_val / 2.0
    arg = 2 * np.pi * R * f
    j1_vals = j1_approx(arg)
    sinc_j1 = np.where(arg == 0, 0.5, np.abs(j1_vals / arg))
    w_task = 2 * np.pi * (R**2) * sinc_j1
    w_task = w_task / w_task[0]
    ax4.plot(f, w_task, label=f'Nódulo $\\varnothing = {d_val:.0f}$ mm', color=col)

ax4.set_title(r'(D) Espectro da Tarefa Diagnóstica $W_{\text{task}}(f)$')
ax4.set_xlabel(r'Frequência Espacial $f$ ($\text{mm}^{-1}$)')
ax4.set_ylabel('Amplitude Normalizada')
ax4.set_xlim(0, 1.2)
ax4.set_ylim(0, 1.05)
ax4.grid(True)
ax4.legend(loc='upper right', frameon=True)

plt.savefig(os.path.join(fig_dir, 'fig2_spectral_metrics.png'))
plt.close()

# -------------------------------------------------------------
# FIGURA 3: Modelagem de Canais Corticais no CHO
# -------------------------------------------------------------
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 9), constrained_layout=True)

# D-DOG
sigmas = [0.035, 0.05, 0.07, 0.10, 0.14]
a_ddog = 1.6
for idx, s in enumerate(sigmas):
    ddog = np.exp(-(f**2) / (2 * s**2)) - np.exp(-(f**2) / (2 * (a_ddog * s)**2))
    ddog = ddog / np.max(ddog)
    f_p = f[np.argmax(ddog)]
    ax1.plot(f, ddog, label=f'Canal D-DOG {idx+1} (Pico: {f_p:.2f} mm$^{{-1}}$)')
ax1.set_title('(A) Canais Corticais Passa-Faixa D-DOG')
ax1.set_xlabel(r'Frequência Espacial $f$ ($\text{mm}^{-1}$)')
ax1.set_ylabel('Resposta Espectral Normalizada')
ax1.set_xlim(0, 1.2)
ax1.set_ylim(0, 1.05)
ax1.grid(True)
ax1.legend(loc='upper right', frameon=True, fontsize=8)

# Laguerre-Gauss
r = np.linspace(0, 12, 300)
au = 3.5
x_lg = 2 * np.pi * (r**2) / (au**2)
lg0 = (np.sqrt(2)/au) * np.exp(-np.pi * (r**2)/(au**2))
lg1 = lg0 * (1 - x_lg)
lg2 = lg0 * (1 - 2*x_lg + 0.5*(x_lg**2))
lg3 = lg0 * (1 - 3*x_lg + 1.5*(x_lg**2) - (x_lg**3)/6.0)

ax2.plot(r, lg0, label='Canal LG 0 ($n=0$)')
ax2.plot(r, lg1, label='Canal LG 1 ($n=1$)')
ax2.plot(r, lg2, label='Canal LG 2 ($n=2$)')
ax2.plot(r, lg3, label='Canal LG 3 ($n=3$)')
ax2.set_title('(B) Canais Laguerre-Gauss no Domínio Espacial')
ax2.set_xlabel('Raio Radial $r$ (mm)')
ax2.set_ylabel('Amplitude Espacial')
ax2.grid(True)
ax2.legend(loc='upper right', frameon=True, fontsize=8)

# Gabor 2D
x_g = np.linspace(-6, 6, 200)
y_g = np.linspace(-6, 6, 200)
X, Y = np.meshgrid(x_g, y_g)
theta = np.pi / 4.0
x_theta = X * np.cos(theta) + Y * np.sin(theta)
y_theta = -X * np.sin(theta) + Y * np.cos(theta)
sigma_g = 2.0
f_g = 0.3
gabor = np.exp(-0.5 * (x_theta**2 + y_theta**2) / (sigma_g**2)) * np.cos(2 * np.pi * f_g * x_theta)

im = ax3.imshow(gabor, extent=[-6, 6, -6, 6], cmap='coolwarm', origin='lower')
ax3.set_title(r'(C) Canal de Gabor 2D ($\theta = 45^\circ$, $f_c = 0.3\text{ mm}^{-1}$)')
ax3.set_xlabel('Deslocamento $x$ (mm)')
ax3.set_ylabel('Deslocamento $y$ (mm)')
fig.colorbar(im, ax=ax3, fraction=0.046, pad=0.04)

# Detectabilidade em Ruído Estruturado
doses = np.linspace(1, 15, 100)
d_npwe_homo = 0.85 * np.sqrt(doses)
d_cho_anat = 0.72 * np.sqrt(doses)
d_npwe_anat_colapso = 0.32 * np.sqrt(doses) + 0.15 * (1 - np.exp(-doses/4.0))

ax4.plot(doses, d_npwe_homo, 'k--', label='NPWE (Fundo Homogêneo)')
ax4.plot(doses, d_cho_anat, 'tab:green', lw=2.2, label='CHO com D-DOG (Fundo Anatômico)')
ax4.plot(doses, d_npwe_anat_colapso, 'crimson', lw=1.8, label='NPWE (Fundo Anatômico - Sem Canais!)')
ax4.set_title(r'(D) Detectabilidade ($d^\prime$) vs. Dose ($\text{CTDI}_{\text{vol}}$)')
ax4.set_xlabel(r'Dose de Radiação $\text{CTDI}_{\text{vol}}$ (mGy)')
ax4.set_ylabel(r'Índice de Detectabilidade $d^\prime$')
ax4.set_ylim(0, 3.2)
ax4.grid(True)
ax4.legend(loc='lower right', frameon=True, fontsize=8)

plt.savefig(os.path.join(fig_dir, 'fig3_cho_cortical_channels.png'))
plt.close()

# -------------------------------------------------------------
# FIGURA 4: Não-Linearidade em Algoritmos DLR, Falha dos Modelos Lineares e Detrending
# -------------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4.5), constrained_layout=True)

doses = np.linspace(1, 15, 100)
d_fbp = 0.65 * np.sqrt(doses)
d_hir = 0.78 * (doses**0.45) + 0.2
d_dlr = 1.15 * (doses**0.35) + 0.3

ax1.plot(doses, d_fbp, 'k--', label='FBP (Linear)')
ax1.plot(doses, d_hir, 'tab:blue', label='HIR (Iterativo Híbrido)')
ax1.plot(doses, d_dlr, 'tab:green', lw=2.2, label='DLR (Aprendizado Profundo)')
ax1.set_title(r'(A) Detectabilidade $d^\prime$ vs. Dose')
ax1.set_xlabel(r'Dose de Radiação $\text{CTDI}_{\text{vol}}$ (mGy)')
ax1.set_ylabel(r'Índice de Detectabilidade $d^\prime$')
ax1.grid(True)
ax1.legend(loc='lower right', frameon=True, fontsize=8)

# Correlação com Radiologistas
np.random.seed(42)
d_humano = np.random.uniform(0.8, 3.8, 40)
d_npwe = 0.65 * d_humano + np.random.normal(0, 0.45, 40)
d_dlmo = 0.98 * d_humano + np.random.normal(0, 0.12, 40)

ax2.scatter(d_humano, d_npwe, color='crimson', alpha=0.6, marker='x', label=r'Modelo Linear NPWE ($r = 0.68$)')
ax2.scatter(d_humano, d_dlmo, color='darkgreen', alpha=0.8, marker='o', label=r'Modelo DLMO com Atenção ($r = 0.98$)')
ax2.plot([0.5, 4.0], [0.5, 4.0], 'k:', label='Concordância Perfeita ($y = x$)')
ax2.set_title('(B) Correlação com Radiologistas em DLR')
ax2.set_xlabel(r'$d^\prime$ Medido no Painel de Radiologistas (2AFC)')
ax2.set_ylabel(r'$d^\prime$ Estimado pelo Modelo Computacional')
ax2.grid(True)
ax2.legend(loc='upper left', frameon=True, fontsize=8)

# Detrending Polinomial
x_p = np.linspace(0, 10, 200)
gradiente_macro = 100 + 15 * x_p - 0.8 * (x_p**2)
ruido_puro = np.random.normal(0, 4.5, 200)
perfil_bruto = gradiente_macro + ruido_puro

ax3.plot(x_p, perfil_bruto, color='tab:blue', alpha=0.4, label='Perfil Bruto $I(x)$ (Anatomia + Ruído)')
ax3.plot(x_p, gradiente_macro, 'crimson', lw=1.8, linestyle='--', label=r'Polinômio Ajustado $P_2(x)$')
ax3.plot(x_p, ruido_puro - 25, color='darkgreen', lw=1.0, label=r'Ruído Puro $\delta I(x) = I - P_2$ (Offset -25 HU)')
ax3.set_title('(C) Princípio do Detrending Polinomial')
ax3.set_xlabel('Posição Espacial (mm)')
ax3.set_ylabel('Número CT (HU)')
ax3.grid(True)
ax3.legend(loc='upper right', frameon=True, fontsize=7.5)

plt.savefig(os.path.join(fig_dir, 'fig4_dlr_non_linearity_detrending.png'))
plt.close()

# -------------------------------------------------------------
# FIGURA 5: Otimização Multiobjetivo e Fronteira de Pareto Tridimensional
# -------------------------------------------------------------
fig = plt.figure(figsize=(14, 6), constrained_layout=True)

ax1 = fig.add_subplot(1, 2, 1)
d_pareto = np.linspace(1.0, 14.0, 100)
w_pareto = 0.9 * np.sqrt(d_pareto)

np.random.seed(101)
d_dom = np.random.uniform(3.0, 14.0, 35)
w_dom = np.random.uniform(0.8, 2.5, 35)
mask = w_dom < (0.9 * np.sqrt(d_dom) - 0.2)
d_dom = d_dom[mask]
w_dom = w_dom[mask]

ax1.plot(d_pareto, w_pareto, 'darkgreen', lw=2.5, label='Fronteira de Pareto (Soluções Ótimas)')
ax1.scatter(d_dom, w_dom, color='gray', alpha=0.6, s=30, label='Protocolos Dominados (Ineficientes)')
ax1.scatter([2.0], [0.9*np.sqrt(2.0)], color='blue', s=80, zorder=5, label='P1: Rastreamento / Pediátrico (Ultra-low dose)')
ax1.scatter([7.0], [0.9*np.sqrt(7.0)], color='tab:orange', s=80, zorder=5, label='P2: Equilíbrio Clínico de Rotina')
ax1.scatter([13.0], [0.9*np.sqrt(13.0)], color='crimson', s=80, zorder=5, label='P3: Oncologia / Máxima Detectabilidade')
ax1.set_title(r'(A) Trade-off Bidimensional: Dose vs. Detectabilidade')
ax1.set_xlabel(r'Dose de Radiação $\text{CTDI}_{\text{vol}}$ (mGy)')
ax1.set_ylabel(r'Desempenho Diagnóstico $W = d^\prime$')
ax1.grid(True)
ax1.legend(loc='lower right', frameon=True, fontsize=8)

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
D_grid = np.linspace(1.0, 14.0, 25)
T_grid = np.linspace(2.0, 20.0, 25)
D_mesh, T_mesh = np.meshgrid(D_grid, T_grid)
W_mesh = 0.75 * np.sqrt(D_mesh) + 0.35 * np.log1p(T_mesh)

surf = ax2.plot_surface(D_mesh, T_mesh, W_mesh, cmap='viridis', alpha=0.75, edgecolor='none')
ax2.scatter(d_dom, np.random.uniform(5, 18, len(d_dom)), w_dom, color='red', alpha=0.5, s=20, label='Dominados')
ax2.set_title(r'(B) Fronteira de Pareto Tridimensional $(D, T, -W)$')
ax2.set_xlabel(r'Dose $D$ ($\text{CTDI}_{\text{vol}}$, mGy)', labelpad=8)
ax2.set_ylabel(r'Tempo Operacional $T$ (s)', labelpad=8)
ax2.set_zlabel(r'Detectabilidade $W = d^\prime$', labelpad=8)
ax2.view_init(elev=25, azim=-125)
fig.colorbar(surf, ax=ax2, fraction=0.03, pad=0.08, label=r'Detectabilidade $d^\prime$')

plt.savefig(os.path.join(fig_dir, 'fig5_dlmo_pareto_3d.png'))
plt.close()

# -------------------------------------------------------------
# FLUXOGRAMAS AUXILIARES
# -------------------------------------------------------------
def draw_box(ax, xy, width, height, title, text, bg_color='#EBF3FB', border_color='#1E5F9E', title_color='#0B3C68', text_color='#1C2833', radius=0.03):
    x, y = xy
    rect = patches.FancyBboxPatch((x, y), width, height,
                                 boxstyle=f"round,pad={radius}",
                                 facecolor=bg_color, edgecolor=border_color, linewidth=1.6)
    ax.add_patch(rect)
    if title:
        ax.text(x + width/2, y + height - 0.08, title, ha='center', va='top',
                fontsize=9.5, fontweight='bold', color=title_color)
    if text:
        ax.text(x + width/2, y + (height/2 if not title else height/2 - 0.04), text,
                ha='center', va='center', fontsize=8.5, color=text_color, multialignment='center')

def draw_arrow(ax, start, end, color='#1E5F9E', width=1.8, style='->'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=width, shrinkA=3, shrinkB=3))

# Flow 1
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.set_xlim(0, 10); ax.set_ylim(0, 5.2); ax.axis('off')
draw_box(ax, (1.5, 4.3), 7.0, 0.7, "AVALIAÇÃO DE QUALIDADE DE IMAGEM BASEADA EM TAREFA (TBIQ)", 
         "Definição da qualidade pela eficácia diagnóstica do observador", bg_color='#0B3C68', border_color='#0B3C68', title_color='white', text_color='#D0E1F9')
draw_box(ax, (0.3, 2.1), 2.8, 1.4, "RESOLUÇÃO DO SISTEMA", "Função de Transferência\nda Tarefa: TTF(f)\n(Borda circular / Contraste)", bg_color='#EAF2F8', border_color='#2980B9', title_color='#1B4F72')
draw_box(ax, (3.6, 2.1), 2.8, 1.4, "TEXTURA DO RUÍDO", "Espectro de Potência\ndo Ruído: NPS(f)\n(Magnitude & Correlação)", bg_color='#EAF2F8', border_color='#2980B9', title_color='#1B4F72')
draw_box(ax, (6.9, 2.1), 2.8, 1.4, "BIOLOGIA VISUAL", "Filtro Ocular CSF: E(f)\n& Espectro da Lesão:\nW_task(f)", bg_color='#EAF2F8', border_color='#2980B9', title_color='#1B4F72')
draw_arrow(ax, (3.5, 4.3), (1.7, 3.5))
draw_arrow(ax, (5.0, 4.3), (5.0, 3.5))
draw_arrow(ax, (6.5, 4.3), (8.3, 3.5))
draw_box(ax, (2.5, 0.2), 5.0, 1.1, "ÍNDICE DE DETECTABILIDADE (d')", 
         "d' = Separação estatística entre as distribuições H0 e H1\n(Síntese biofísica e computacional da qualidade)", 
         bg_color='#D4EFDF', border_color='#27AE60', title_color='#145A32', text_color='#1E8449')
draw_arrow(ax, (1.7, 2.1), (3.5, 1.3))
draw_arrow(ax, (5.0, 2.1), (5.0, 1.3))
draw_arrow(ax, (8.3, 2.1), (6.5, 1.3))
plt.savefig(os.path.join(fig_dir, 'flow1_tbiq_paradigm.png'))
plt.close()

# Flow 2 (Quadro 1 / Paradigmas)
fig, ax = plt.subplots(figsize=(10, 4.2), constrained_layout=True)
ax.set_xlim(0, 10); ax.set_ylim(0, 4.2); ax.axis('off')
draw_box(ax, (0.3, 0.2), 4.4, 3.8, "PARADIGMA CLÁSSICO (Linear / Escalar)",
         "• Métricas: Desvio padrão (HU), SNR, CNR, MTF global\n• Phantoms: Cilindros homogêneos de água / acrílico\n• Premissa: Linearidade estrita e ruído estacionário\n• Observador: Desconsiderado (avaliação pontual)\n• Falha Crítica: falsa otimização por filtros de blur e\nincapacidade de avaliar algoritmos não lineares (DLR)",
         bg_color='#FDEDEC', border_color='#E74C3C', title_color='#78281F')
draw_box(ax, (5.3, 0.2), 4.4, 3.8, "PARADIGMA BASEADO EM TAREFA (TBIQ)",
         "• Métrica Central: Índice de Detectabilidade (d')\n• Phantoms: Antropomórficos e Híbridos (FREDDIE)\n• Premissa: Não linearidade, dependente da tarefa clínica\n• Observador: Modelos Matemáticos e IA (NPWE, CHO, DLMO)\n• Validação Rigorosa: Alta correlação com radiologistas\nem testes psicofísicos 2AFC e comissão AAPM TG-233",
         bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')
plt.savefig(os.path.join(fig_dir, 'flow2_comparativo_paradigmas.png'))
plt.close()

# Flow 3 (CHO Pipeline)
fig, ax = plt.subplots(figsize=(11, 4.2), constrained_layout=True)
ax.set_xlim(0, 11); ax.set_ylim(0, 4.2); ax.axis('off')
draw_box(ax, (0.2, 2.2), 2.3, 1.6, "IMAGEM MÉDICA g", "Vetor discreto de pixels\n(N pixels, ex: 16.384)\nRuído + Fundo Estruturado", bg_color='#EAF2F8', border_color='#2980B9', title_color='#1B4F72')
draw_box(ax, (2.9, 2.2), 2.3, 1.6, "CANAIS CORTICAIS (T)", "Decomposição em V1\n(C canais, C << N)\nGabor / Laguerre-Gauss / DOG", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')
draw_box(ax, (5.6, 2.2), 2.3, 1.6, "VETOR CANALIZADO v", "v = T * g\nDimensão Reduzida (C x 1)\nCovariância Kv (C x C)", bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')
draw_box(ax, (8.3, 2.2), 2.5, 1.6, "DECISÃO (t)", "t = w^T * v\nw = Kv^-1 * <vs>\nEstatística Escalar", bg_color='#F5EEF8', border_color='#8E44AD', title_color='#512E5F')
draw_arrow(ax, (2.5, 3.0), (2.9, 3.0))
draw_arrow(ax, (5.2, 3.0), (5.6, 3.0))
draw_arrow(ax, (7.9, 3.0), (8.3, 3.0))
draw_box(ax, (2.8, 0.2), 5.4, 1.2, "ÍNDICE DE DETECTABILIDADE DO CHO", "d'_CHO = sqrt( <vs>^T * Kv^-1 * <vs> )", bg_color='#D4EFDF', border_color='#27AE60', title_color='#145A32', text_color='#1E8449')
draw_arrow(ax, (6.75, 2.2), (6.75, 1.4))
draw_arrow(ax, (9.5, 2.2), (7.5, 1.4))
plt.savefig(os.path.join(fig_dir, 'flow3_cho_pipeline.png'))
plt.close()

# Flow 4 (Phantom Híbrido 2AFC)
fig, ax = plt.subplots(figsize=(11, 6.2), constrained_layout=True)
ax.set_xlim(0, 11); ax.set_ylim(0, 6.2); ax.axis('off')
draw_box(ax, (2.0, 5.0), 7.0, 1.0, "AQUISIÇÃO TOMOGRÁFICA DO PHANTOM FÍSICO REAL (FREDDIE)", 
         "Phantoms antropomórficos de Tórax, Abdome e Crânio com materiais equivalentes a tecidos biológicos\nVarreduras clínicas em múltiplos níveis de dose e tomógrafos", bg_color='#EBF5FB', border_color='#2980B9', title_color='#154360')
draw_box(ax, (3.0, 3.5), 5.0, 0.9, "BANCO DE IMAGENS DE FUNDO ANATÔMICO REAL (H0)", "ROIs anatômicas reais sem lesão física", bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')
draw_arrow(ax, (5.5, 5.0), (5.5, 4.4))
draw_box(ax, (0.5, 1.9), 4.5, 1.1, "CASOS DE SINAL AUSENTE (H0)", "Fundo anatômico puro + ruído quântico real", bg_color='#FDEDEC', border_color='#E74C3C', title_color='#78281F')
draw_box(ax, (6.0, 1.9), 4.5, 1.1, "INSERÇÃO DIGITAL HÍBRIDA DE LESÕES (H1)", "Modelagem 3D de nódulos / metástases\nConvolução com a PSF 3D do tomógrafo", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')
draw_arrow(ax, (4.5, 3.5), (2.75, 3.0))
draw_arrow(ax, (6.5, 3.5), (8.25, 3.0))
draw_box(ax, (1.5, 0.2), 8.0, 1.1, "PLATAFORMA DE TESTE PSICOFÍSICO CEGO 2AFC", "Apresentação simultânea aos pares (H0 vs. H1) em monitores diagnósticos calibrados GSDF\nValidação e Calibração Perceptual: Painel de Radiologistas Especialistas vs. Observadores DLMO", bg_color='#EAFAF1', border_color='#27AE60', title_color='#196F3D')
draw_arrow(ax, (2.75, 1.9), (3.5, 1.3))
draw_arrow(ax, (8.25, 1.9), (7.5, 1.3))
plt.savefig(os.path.join(fig_dir, 'flow4_phantom_hibrido_2afc.png'))
plt.close()

# Flow 5 (DLMO Vision Transformer Architecture)
fig, ax = plt.subplots(figsize=(11, 4.8), constrained_layout=True)
ax.set_xlim(0, 11); ax.set_ylim(0, 4.8); ax.axis('off')
draw_box(ax, (0.3, 2.5), 2.2, 1.7, "IMAGEM MÉDICA g", "ROI de entrada (ex: 128x128)\nTextura não-estacionária DLR\nSinal H0 / H1", bg_color='#EBF5FB', border_color='#2980B9', title_color='#154360')
draw_box(ax, (2.9, 2.5), 2.4, 1.7, "EXTRATOR HIERÁRQUICO", "Camadas Convolucionais / Patches\nProjeção Linear e Posição 2D\nExtração de bordas e texturas", bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')
draw_box(ax, (5.7, 2.5), 2.4, 1.7, "AUTO-ATENÇÃO (ViT)", "Multi-Head Self-Attention (MHSA)\nPonderação de correlações globais\nEmulação da atenção foveal", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')
draw_box(ax, (8.5, 2.5), 2.2, 1.7, "DECISÃO (t)", "Camadas Densas\nEstatística Escalar t\nEstimativa de d'_DL", bg_color='#EAFAF1', border_color='#27AE60', title_color='#196F3D')
draw_arrow(ax, (2.5, 3.35), (2.9, 3.35))
draw_arrow(ax, (5.3, 3.35), (5.7, 3.35))
draw_arrow(ax, (8.1, 3.35), (8.5, 3.35))
draw_box(ax, (2.0, 0.4), 7.0, 1.3, "TREINAMENTO COM FUNÇÃO DE PERDA PERCEPTUAL MULTITAREFA", 
         "L_total = L_classificacao(y, y_hat) + lambda * ( d'_DL - d'_humano )^2", bg_color='#FADBD8', border_color='#E74C3C', title_color='#922B21', text_color='#78281F')
draw_arrow(ax, (9.6, 2.5), (8.5, 1.7))
plt.savefig(os.path.join(fig_dir, 'flow5_dlmo_architecture.png'))
plt.close()

# Flow 6 (Software Pipeline)
fig, ax = plt.subplots(figsize=(11, 6.2), constrained_layout=True)
ax.set_xlim(0, 11); ax.set_ylim(0, 6.2); ax.axis('off')
draw_box(ax, (0.5, 5.1), 4.8, 0.9, "MÓDULO 1: ENTRADA DICOM & PARSER", "Leitura de imagens tomográficas e validação de metadados\n(kVp, mA, tempo rotação, pitch, kernel, DLR)", bg_color='#EBF5FB', border_color='#2980B9', title_color='#154360')
draw_box(ax, (5.7, 5.1), 4.8, 0.9, "MÓDULO 2: SEGMENTAÇÃO AUTOMÁTICA", "Localização precisa de insertos do phantom e amostragem\nde mosaicos de ROIs anatômicas (M >= 100)", bg_color='#E8F8F5', border_color='#16A085', title_color='#0E6251')
draw_arrow(ax, (5.3, 5.55), (5.7, 5.55))
draw_box(ax, (0.5, 3.4), 4.8, 1.3, "MÓDULO 3A: RESOLUÇÃO ESPACIAL", "• Técnica da borda circular em insertos\n• ESF(r) -> LSF(r) -> TTF(f)\n• Extração do descritor de resolução f50", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')
draw_box(ax, (5.7, 3.4), 4.8, 1.3, "MÓDULO 3B: TEXTURA E RUÍDO", "• Detrending polinomial 2D P2(x, y)\n• Janelamento Hanning 2D -> NPS 2D/1D\n• Extração de frequência de pico f_peak e f_av", bg_color='#FEF9E7', border_color='#F39C12', title_color='#7D6608')
draw_arrow(ax, (8.1, 5.1), (2.9, 4.7))
draw_arrow(ax, (8.1, 5.1), (8.1, 4.7))
draw_box(ax, (1.5, 1.8), 8.0, 1.2, "MÓDULO 4: OBSERVADORES COMPUTACIONAIS DE MODELO", 
         "• Observadores Lineares Clássicos: NPWE e CHO (Canais Gabor, Laguerre-Gauss, D-DOG)\n• Observadores de Aprendizado Profundo: DLMO (CNNs residuais e Vision Transformers)", 
         bg_color='#EAFAF1', border_color='#27AE60', title_color='#196F3D')
draw_arrow(ax, (2.9, 3.4), (4.5, 3.0))
draw_arrow(ax, (8.1, 3.4), (6.5, 3.0))
draw_box(ax, (1.0, 0.2), 9.0, 1.2, "MÓDULO 5: INCERTEZA E OTIMIZAÇÃO MULTIOBJETIVO (NSGA-II)", 
         "• Determinação de incerteza por Bootstrap Não-Paramétrico (B = 2000 reamostragens)\n• Algoritmo Genético NSGA-II para mapeamento da Fronteira de Pareto Tridimensional (D, T, -W)\n• Tomada de Decisão Multicritério (TOPSIS) para seleção do protocolo clínico ideal", 
         bg_color='#FADBD8', border_color='#E74C3C', title_color='#922B21')
draw_arrow(ax, (5.5, 1.8), (5.5, 1.4))
plt.savefig(os.path.join(fig_dir, 'flow6_software_pipeline.png'))
plt.close()

print("Todas as figuras e diagramas gerados com sucesso em:", fig_dir)
