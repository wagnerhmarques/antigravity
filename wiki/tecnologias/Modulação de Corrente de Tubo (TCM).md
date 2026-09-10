---
tipo: tecnologia
aliases: [tube-current-modulation, tcm, TCM, controle-automatico-exposicao, "modulacao de corrente do tubo"]
---
# Modulação de Corrente do Tubo (TCM / AEC)
O sistema de **Controle Automático de Exposição (AEC)** e **Modulação de Corrente do Tubo (TCM)** ajusta dinamicamente a corrente do filamento $mA(\theta, z)$ em função da atenuação angular e longitudinal do paciente:

$$
mA(\theta, z) = mA_{\text{ref}} \cdot \left( \frac{\text{Atenuação}(\theta, z)}{\text{Atenuação}_{\text{ref}}} \right)^p
$$

Garante uniformidade do ruído na imagem ($ext{NPS}$) com redução de dose de até $40\%$ ([[Otimização de Dose em TC|otimizacao-de-dose-em-tc]]).
