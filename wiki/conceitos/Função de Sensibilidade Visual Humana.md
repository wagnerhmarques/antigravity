---
tipo: conceito
titulo: "Função de Sensibilidade Visual Humana (Eye Filter / CSF)"
data_criacao: 2026-08-27
tags: ["psicofisica", "model-observers", "percepcao-visual"]
---

# Função de Sensibilidade Visual Humana (Eye Filter / CSF)

## 1. Fundamentação Psicofísica
O sistema visual humano (olho + córtex visual primário) não responde de forma uniforme a todas as frequências espaciais. A **Função de Sensibilidade ao Contraste** (*Contrast Sensitivity Function* - CSF ou *Eye Filter* $E(u, v)$) modela o comportamento passa-banda da visão humana, com pico de sensibilidade em torno de $2 - 4\text{ ciclos/grau}$ de ângulo visual.

## 2. Formulação Matemática (Modelo de Burgess / Barten):
$$
E(f) = f^n \exp(-c f^m)
$$
Convertendo frequência angular $f_{\text{ang}}$ ($	ext{ciclos/grau}$) para frequência espacial do monitor $f_{\text{esp}}$ ($	ext{mm}^{-1}$):

$$
f_{\text{ang}} = f_{\text{esp}} \cdot d_{\text{visual}} \cdot \tan(1^\circ) \approx f_{\text{esp}} \cdot d_{\text{visual}} \cdot 0{,}01745
$$

onde $d_{\text{visual}}$ é a distância de visualização do radiologista (ex.: $500\text{ mm}$).

## 3. Papel no Observador Modelo NPWE
O filtro $E^2(u, v)$ modula a transferência de contraste e $E^4(u, v)$ modula o ruído de fundo na formulação do [[Índice de Detectabilidade]]:

$$
d'^2_{\text{NPWE}} = \frac{\left[ \iint |W(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot E^2(u, v) \, du \, dv \right]^2}{\iint |W(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot \text{NPS}(u, v) \cdot E^4(u, v) \, du \, dv + \sigma_{\text{int}}^2}
$$

## 4. Conexões
- [[Índice de Detectabilidade]]
- [[Observadores de Modelo (Model Observers)]]
- [[NPWE Model Observer]]
- [[Estudo de Observadores 2AFC]]
