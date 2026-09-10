> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[ICRU Report 95]], [[Grandezas Operacionais de Dosimetria]], [[Dose Efetiva]], [[Radioproteção]]

## 1. Visão Geral e Contexto Histórico do ICRU Report 95

O **ICRU Report 95** (*Operational Quantities for Radiation Protection External Exposure*), publicado em 2020 pela *International Commission on Radiation Units and Measurements* (ICRU) em conjunto com a *International Commission on Radiological Protection* (ICRP), representa a revisão mais profunda e significativa no sistema de metrologia das radiações ionizantes para **[[radioprotecao]]** nas últimas três décadas.

Historicamente, o sistema de dosimetria operacional estabelecido nos relatórios ICRU 39, 43 e 51 baseava-se no conceito de equivalente de dose em profundidades fixas ($d = 10\text{ mm}$, $d = 3\text{ mm}$ e $d = 0,07\text{ mm}$) dentro de um phantom simplificado de geometria esférica (*ICRU sphere*) ou plana (esfera de 30 cm de diâmetro com composição equivalente a tecido). Essas grandezas — como o **Equivalente de Dose Ambiental** $H^*(10)$ e o **Equivalente de Dose Pessoal** $H_p(10)$ — foram concebidas como estimadores práticos e conservadores da [[metricas-de-dose-tc|dose-efetiva]] ($E$) e das doses em órgãos críticos ($H_T$).

Contudo, o avanço do conhecimento radiobiológico (formalizado na ICRP Publ. 103), a introdução de fantasmas antropomórficos computacionais de referência (*voxel-based phantoms*) e simulações avançadas por [[monte-carlo-simulation|Monte Carlo]] evidenciaram desvios severos:
1. **Superestimação / Subestimação Extrema:** Em baixas energias de fótons ($< 30\text{ keV}$, comuns em mamografia e espalhamento de [[Tomografia Computadorizada]]) e em energias muito elevadas ($> 10\text{ MeV}$), $H^*(10)$ e $H_p(10)$ falham em estimar com precisão a verdadeira dose efetiva $E$, podendo superestimá-la por fatores superiores a 2 ou subestimá-la perigosamente em feixes de nêutrons e fótons de alta energia.
2. **Incompatibilidade Teórica:** O uso da grandeza "equivalente de dose" (baseada no fator de qualidade $Q(L)$ da ICRU) divergia do formalismo moderno da dose efetiva $E$ (baseado nos fatores de ponderação da radiação $w_R$ e tecidual $w_T$ da ICRP 103).

Para resolver essas discrepâncias, o **ICRU 95 redefiniu inteiramente as grandezas operacionais**, alinhando-as diretamente com as grandezas de proteção da ICRP.

---

## 2. A Nova Taxonomia das Grandezas Operacionais

O ICRU Report 95 abandona a profundidade física na esfera de tecido ($10\text{ mm}$, $3\text{ mm}$) e passa a definir as grandezas operacionais como **produtos direta e rigorosamente calibrados da fluência ($\Phi$) ou do kerma no ar livre no ar ($K_a$) por coeficientes de conversão para a Dose Efetiva ou Dose Absorvida em Órgãos Específicos**, calculados em fantasmas antropomórficos padronizados.

### A. Monitoramento de Área (Grandezas Ambientais)
* **Dose Efetiva Ambiental ($E^*$):** Replaces $H^*(10)$. Define a dose efetiva que seria recebida por um fantasma antropomórfico adulto de referência situado no campo de radiação expandido e alinhado.
* **Dose Absorvida Ambiental no Cristalino ($D_{\text{lens}}^*$):** Replaces $H'(3,\Omega)$. Mede a dose absorvida média no cristalino ocular para monitoramento de área.
* **Dose Absorvida Ambiental na Pele Local ($D_{\text{local skin}}^*$):** Replaces $H'(0.07,\Omega)$. Mede a dose absorvida na camada basal da pele local.

### B. Monitoramento Individual / Pessoal (Dosimetria de Trabalhadores)
* **Dose Efetiva Pessoal ($E_p$):** Replaces $H_p(10)$. Representa a estimativa direta da [[metricas-de-dose-tc|dose-efetiva]] ($E$) recebida pelo trabalhador ocupacionalmente exposto, medida por um dosímetro individual posicionado na superfície do corpo.
* **Dose Absorvida Pessoal no Cristalino ($D_p(\text{lens})$):** Replaces $H_p(3)$. Quantifica a dose absorvida no cristalino do trabalhador.
* **Dose Absorvida Pessoal na Pele Local ($D_p(\text{local skin})$):** Replaces $H_p(0.07)$. Quantifica a dose em tecidos cutâneos locais.
* **Dose Absorvida Pessoal nas Mãos e Pés ($D_p(\text{hands/feet})$):** Nova grandeza específica para dosimetria de extremidades.

---

## 3. Matriz Comparativa: Sistema Antigo (ICRU 39/51) vs. Novo Sistema (ICRU 95)

| Parâmetro Metrológico | Sistema Antigo (ICRU 39 / 43 / 51) | Novo Sistema (ICRU Report 95) |
| :--- | :--- | :--- |
| **Objeto de Referência** | Esfera ICRU (30 cm) / Placa homogênea | Fantasmas Antropomórficos Coxelizados ICRP (Homem/Mulher Adultos) |
| **Monitoramento de Área (Corpo Inteiro)** | Equivalente de Dose Ambiental $H^*(10)$ | **Dose Efetiva Ambiental ($E^*$)** |
| **Monitoramento Pessoal (Corpo Inteiro)** | Equivalente de Dose Pessoal $H_p(10)$ | **Dose Efetiva Pessoal ($E_p$)** |
| **Dosimetria de Cristalino Ocular** | $H'(3)$ / $H_p(3)$ [Sv] | **$D_{\text{lens}}^*$ / $D_p(\text{lens})$ [Gy]** |
| **Unidade Fundamental** | Sievert (Sv) - via Fator $Q(L)$ | **Sv** para $E^*$ / $E_p$; **Gy** para $D_{\text{lens}}$, $D_{\text{skin}}$ |
| **Aproximação com a Dose Efetiva Real** | Variável; superestima em até $+200\%$ em baixas energias | **Exata por definição** sob condições de referência |

---

## 4. Formalismo Matemático e Coeficientes de Conversão

No ICRU 95, o cálculo da Dose Efetiva Ambiental $E^*$ para um espectro de energia $\Phi_E(E)$ é dado por:

$$
E^* = \int_0^{E_{\max}} \Phi_E(E) \cdot c_E^*(E) \, dE
$$

Onde:
* $\Phi_E(E) = \frac{d\Phi}{dE}$ é a distribuição espectral da fluência de partículas;
* $c_E^*(E)$ é o **coeficiente de conversão de fluência para Dose Efetiva Ambiental** (expresso em $\text{pSv}\cdot\text{cm}^2$), tabelado rigorosamente no ICRU 95 para fótons, nêutrons, elétrons e pósitrons em geometrias de irradiação padronizadas (AP - Antero-Posterior, PA - Postero-Anterior, LAT, ROT e ISO).

Para dosimetria individual de fótons em termos do Kerma no Ar Livre no Ar ($K_a$):

$$
E_p = K_a \cdot C_{K_a, E_p}(E, \alpha)
$$

Onde $C_{K_a, E_p}(E, \alpha)$ é o coeficiente de conversão do Kerma no ar para a Dose Efetiva Pessoal, variando em função da energia do fóton $E$ e do ângulo de incidência $\alpha$ no tronco do indivíduo.

---

## 5. Relevância e Impacto na Física Médica, Radioproteção e Tomografia Computadorizada

1. **Redefinição dos Limites de Cristalino Ocular:** A aprovação pelo ICRP (Publ. 118) da redução do limite anual de dose no cristalino de $150\text{ mSv/ano}$ para $20\text{ mSv/ano}$ exigiu uma grandeza dosimétrica mais precisa. O ICRU 95 introduz $D_p(\text{lens})$ expressa diretamente em Gray (Gy), eliminando ambiguidades da conversão $H_p(3)$ em exames de radiologia intervencionista e salas de tomografia tomográfica guiada por fluoroscopia.
2. **Calibração de Instrumentos e Dosímetros:** Instrumentos de monitoramento de área (câmaras de ionização pressurizadas, detectores Geiger-Müller) e dosímetros individuais (TLD, OSL) estão passando por um processo global de recalibração de suas respostas em energia para responder diretamente em $E^*$ e $E_p$.
3. **Mapeamento de Dose Espalhada em TC:** Na Tomografia Computadorizada, a radiação espalhada no ambiente tem espectro focado entre $30\text{ keV}$ e $120\text{ keV}$. As antigas grandezas $H^*(10)$ superestimavam a dose ocupacional da equipe nessa faixa. O ICRU 95 proporciona uma estimativa realista da [[metricas-de-dose-tc|dose-efetiva]] recebida por físicos médicos, radiologistas e tecnólogos.

---

## 🔗 Conexões e Wikilinks no Acervo
- [[radioprotecao]]
- [[metricas-de-dose-tc|dose-efetiva]]
- [[radiation-dosimetry]]
- [[efeitos-biologicos-da-radiacao]]
- [[metricas-de-dose-tc]]
- [[niveis-de-referencia-diagnostica-drl]]
