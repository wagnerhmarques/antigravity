---
tipo: conceito
titulo: "Efeito Fotoelétrico em Radiodiagnóstico e Tomografia Computadorizada"
data_criacao: 2026-08-27
data_atualizacao: 2026-08-27
tags:
  - "interacao-radiacao-materia"
  - "efeito-fotoeletrico"
  - "qualidade-de-imagem"
  - "fisica-medica"
  - "tomografia-espectral"
---

# Efeito Fotoelétrico em Radiodiagnóstico e Tomografia Computadorizada

## 1. Definição e Mecanismo Físico

O **Efeito Fotoelétrico** é o processo de interação quântica no qual um fóton de radiação X incidente colide inelasticamente com um elétron orbital fortemente ligado (tipicamente da camada K ou L) de um átomo do meio absorvedor. O fóton transfere **integralmente** toda a sua energia $h\nu$ para o elétron e deixa de existir.

O elétron é ejetado da eletrosfera com energia cinética $E_k$, passando a ser denominado **fotoelétron**:

$$
E_k = h\nu - E_b
$$

Onde:
- $h\nu$ é a energia do fóton incidente ($h$ é a constante de Planck e $\nu$ a frequência eletromagnética);
- $E_b$ é a energia de ligação do elétron à sua camada orbital atômica específica (função de trabalho / *binding energy*);
- $E_k$ é a energia cinética inicial com que o fotoelétron é ejetado.

A vacância orbital criada é imediatamente preenchida por elétrons de camadas mais externas, resultando na emissão de **radiação característica** (fótons fluorescentes com energias discretas $\Delta E$) ou na ejeção de **elétrons Auger**.

---

## 2. Dependência Paramétrica e Coeficiente de Atenuação Mássico

A probabilidade de ocorrência do efeito fotoelétrico por unidade de massa, representada pelo coeficiente de atenuação linear fotoelétrico $\tau$ ou coeficiente mássico $\frac{\tau}{\rho}$, exibe uma dependência extrema com o número atômico efetivo ($Z$) do meio e com a energia ($E$) do feixe incidente:

$$
\frac{\tau}{\rho} \propto \frac{Z^k}{E^n} \approx \frac{Z^3 \text{ a } Z^4}{E^3 \text{ a } E^{3{,}5}}
$$

### Propriedades e Características Fundamentais:
1. **Bordas de Absorção K (*K-edge*):** A probabilidade de absorção aumenta abruptamente quando a energia do fóton incidente atinge exatamente a energia de ligação dos elétrons da camada K ($E \ge E_{b,K}$).
   - **Iodo ($Z=53$):** Borda K em $33{,}2\text{ keV}$;
   - **Bário ($Z=56$):** Borda K em $37{,}4\text{ keV}$;
   - **Gadolínio ($Z=64$):** Borda K em $50{,}2\text{ keV}$.
2. **Diferenciação Tecidual:** Como o osso cortical ($Z_{\text{ef}} \approx 13{,}8$) possui número atômico efetivo substancialmente maior que o tecido mole ($Z_{\text{ef}} \approx 7{,}4$), a absorção fotoelétrica no osso é cerca de $(13{,}8 / 7{,}4)^3 \approx 6{,}5$ vezes mais intensa por unidade de massa em baixas energias.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada

| Aplicação / Tecnologia | Mecanismo Físico | Impacto Clínico e Diagnóstico |
| :--- | :--- | :--- |
| **Contraste Iodado em Baixo kVp** | Operação em $70-80\text{ kVp}$ aproxima o espectro da borda K do iodo ($33{,}2\text{ keV}$). | Aumento drástico do coeficiente $\mu$, permitindo reduzir a carga de contraste ou a dose. |
| **TC Espectral ([[Tomografia Computadorizada Espectral|tomografia-computadorizada-espectral]])** | Decomposição de base por pares fotoelétrico + Compton. | Geração de mapas quantitativos de concentração de iodo ($\text{mg/mL}$) e imagens virtuais sem contraste. |
| **Detectores de Contagem de Fótons ([[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]])** | Separação em patamares energéticos (*bins*) sem ruído de integração. | Exploração máxima do sinal fotoelétrico de baixa energia, elevando o [[Índice de Detectabilidade|indice-de-detectabilidade]] ($d'$). |

---

## 4. Conexões no Acervo

- [[Espalhamento Compton|espalhamento-compton]]
- [[Atenuação|atenuacao]]
- [[Unidades Hounsfield|unidades-hounsfield]]
- [[Tomografia Computadorizada Espectral|tomografia-computadorizada-espectral]]
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
- [[Radioproteção|radioprotecao]]
