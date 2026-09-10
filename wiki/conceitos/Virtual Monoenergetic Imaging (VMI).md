---tipo: conceito
titulo: "Virtual Monoenergetic Imaging (VMI) e Espectrometria em TC"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags:
  - fisica-medica
  - monoenergetico
  - reconstrucao
  - tomografia-computadorizada
fontes_origem:
  - "[[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]"
aliases: [virtual-monoenergetic-imaging, vmi, VMI, "monoenergetic imaging"]
---

# Virtual Monoenergetic Imaging (VMI) e Espectrometria em TC

## 1. Definição Conceitual: $kV$ vs. $keV$
Uma das confusões conceituais mais frequentes na radiologia moderna reside na equivalência equivocada entre $kV$ e $keV$:
- **$kV$ (Kilovoltagem de Tubo):** Grandeza física prospectiva aplicada ao tubo de raios X. Estabelece a energia cinética máxima que os elétrons atingem ao colidir com o anodo, gerando um espectro **policromático** contínuo (*bremsstrahlung*) acrescido de linhas de emissão característica. Um exame a 120 kV contém fótons que variam de dezenas de keV até o teto de 120 keV, com energia média dependente da filtração adicional (tipicamente entre 60 e 75 keV).
- **$keV$ (Kiloelectronvolt em VMI):** Unidade de energia que rotula uma imagem **monoenergética virtual sintetizada**. O VMI não representa um feixe físico monocromático real, mas sim uma simulação matemática que calcula como cada vóxel atenuaria se fosse atravessado por um feixe composto exclusivamente por fótons de uma única energia discreta $E_{mono}$.

$$
\text{Espectro } kV \xrightarrow{\text{Aquisicao Espectral}} \text{Decomposicao de Materiais} \xrightarrow{\text{Reconstrucao}} \text{VMI}(E_{mono} \text{ em } keV)
$$

---

## 2. Formulação Matemática da Decomposição Espectral

A atenuação de um feixe de raios X através da matéria segue a lei de Beer-Lambert:

$$
I = I_0 \cdot e^{-\mu(E) \cdot x}
$$

Onde $\mu(E)$ é o coeficiente de atenuação linear na energia $E$ e $x$ é a espessura do meio atravessado.

Na faixa de energias diagnósticas da TC (30 a 140 keV), as interações predominantes são o **efeito fotoelétrico** (dependência $\propto Z^3/E^3$) e o **espalhamento Compton** (dependência com a densidade eletrônica $\rho_e$, fracamente dependente de $E$). Devido a essa dimensionalidade bidimensional, a atenuação de qualquer tecido biológico em um vóxel pode ser expressa como uma combinação linear de dois materiais de base conhecidos (ex.: iodo e água/tecido mole):

$$
\mu(E) = w_1 \cdot \mu_1(E) + w_2 \cdot \mu_2(E)
$$

Onde:
- $\mu_1(E)$ e $\mu_2(E)$ são as curvas conhecidas de atenuação dos materiais base;
- $w_1$ e $w_2$ são os pesos/concentrações desconhecidos calculados resolvendo o sistema linear obtido de pelo menos dois canais de energia distintos.

Uma vez determinados $w_1$ e $w_2$, a imagem VMI para qualquer energia monocromática $E_{mono}$ é gerada diretamente por:

$$
\mu_{\text{VMI}}(E_{mono}) = w_1 \cdot \mu_1(E_{mono}) + w_2 \cdot \mu_2(E_{mono})
$$

Ou equivalentemente expressa como soma ponderada das imagens de baixa e alta energia:

$$
\mu_{\text{VMI}}(E_{mono}) = w(E_{mono}) \cdot \mu_{\text{low}} + \left(1 - w(E_{mono})\right) \cdot \mu_{\text{high}}
$$

---

## 3. Dinâmica de Contraste e Ruído em Função do $keV$

1. **Baixo $keV$ (40 a 60 keV):**
   - *Vantagem:* Acentuado aumento na atenuação fotoelétrica do iodo ($K\text{-edge} = 33,2\text{ keV}$), maximizando o contraste vascular e parenquimatoso.
   - *Desafio Teórico:* Amplificação matemática do ruído estocástico pela ponderação dos termos de decomposição. Contudo, no [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]], algoritmos avançados de denoising espectral preservam a relação contraste-ruído ($CNR$), tornando níveis de 50–55 keV clinicamente superiores.
2. **Alto $keV$ (70 a 140 keV):**
   - *Vantagem:* Atenuação de artefatos de endurecimento de feixe (*beam hardening*) e mitigação parcial de artefatos metálicos causados por próteses ou clipes cirúrgicos.
   - *Comportamento:* A convergência das curvas de atenuação para o regime Compton reduz as diferenças de contraste entre tecidos moles e contraste iodado.

---

## Referências Cruzadas
- [[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]
- [[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]]
- [[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]]