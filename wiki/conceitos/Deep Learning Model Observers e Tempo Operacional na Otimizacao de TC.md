# Deep Learning Model Observers (DLMO) e Tempo Operacional na Otimização de TC

> [!NOTE]
> Nota conceitual de alinhamento metodológico do projeto de Doutorado Direto (FMUSP/InRad - IFUSP), conectando as fronteiras teóricas de ensaios virtuais (ex.: [[Zou 2026 - Otimizacao de Protocolos de TC com RL e VIT]]) com a metodologia experimental baseada em phantoms físicos híbridos e observadores profundos com atenção.

---

## 1. Superação do "Mundo Perfeito Virtual" via Phantoms Híbridos

Simulações computacionais puras de ensaios virtuais de imagem (VIT - *Virtual Imaging Trials*), como a arquitetura XCAT + CatSim empregada por Zou et al. (2026), enfrentam a barreira crítica do **Sim-to-Real Gap** quando confrontadas com a prática radiológica contemporânea:
- **Aproximações físicas analíticas:** Modelos de simulação simplificam espectros de raios X polienergéticos, espalhamento (*scatter*) e consideram detectores com respostas lineares uniformes sem a modelagem de ruído eletrônico real.
- **Opacidade dos algoritmos de Reconstrução por Deep Learning (DLR):** Motores comerciais de última geração (*TrueFidelity*, *AiCE*, *Precise Image*) operam como "caixas-pretas" proprietárias com pesos inacessíveis a simuladores abertos. O comportamento do ruído frente à modulação de dose não é reproduzível computacionalmente com fidelidade absoluta.

### A Solução Adotada na Tese (Costa et al., 2025; Boiset et al., 2023)
O projeto ancora-se em **três phantoms físicos híbridos** (tórax, abdome e crânio), que combinam no mesmo dispositivo físico:
1. **Módulo Geométrico/Metrológico:** Inserts cilíndricos calibrados em fundo homogêneo para extração padronizada e automatizada de métricas físicas conforme AAPM TG-233 ($\text{TTF}(f)$, $\text{NPS}(f)$ e $d'_{\text{NPWE}} / d'_{\text{CHO}}$).
2. **Módulo Antropomórfico (Manufatura Aditiva 3D):** Confeccionado com polímeros radiodensos equivalentes a tecidos biológicos (parênquima, osso cortical/trabecular e tecidos moles), gerando espalhamento real, endurecimento de feixe (*beam hardening*) e ruído estrutural anatômico (*anatomical clutter*).
3. **Ancoragem Multicêntrica Real:** Aquisições físicas padronizadas em **7 tomógrafos clínicos de 4 fabricantes** (GE, Siemens, Philips e Canon) no parque tecnológico do InRad-HCFMUSP, capturando a física real da interação da radiação e os motores DLR comerciais.

---

## 2. Estruturação do DLMO (Deep Learning Model Observer)

Zou et al. (2026) empregaram Deep Learning apenas na codificação de imagens *scout* (via ViT) e na política do PPO, mantendo a estimativa de qualidade restrita a equações lineares analíticas. Sob DLR, contudo, o ruído deixa de ser Gaussiano e estacionário, invalidando premissas lineares do TG-233.

O **DLMO com Mecanismo de Atenção** proposto no Eixo 2 supera essa limitação:

### A. Formulação da Tarefa Psicofísica (Task-Based)
- **Classificação Binária:** $H_0$ (fundo anatômico / sinal ausente) vs. $H_1$ (fundo com lesão/insert / sinal presente).
- **Entrada:** Pares de ROIs de $64 \times 64$ extraídos de fatias axiais do phantom nas configurações geométrica e antropomórfica.

### B. Arquitetura e Mimetização Humana
- **Modelo:** Vision Transformer (ViT / Swin Transformer) com autoatenuação espacial para ponderar características contextuais da lesão e da textura do ruído.
- **Injeção de Ruído Interno Estocástico:** Para reproduzir a incerteza e o limiar de decisão perceptual do leitor humano, a variável de decisão é perturbada por:
  $$z = \hat{t} + \varepsilon_{\text{int}}, \quad \varepsilon_{\text{int}} \sim \mathcal{N}(0, \sigma_{\text{int}}^2)$$
  onde $\hat{t} = f_\theta(I)$ representa o logit emitido pela rede.

### C. Calibração Perceptual via 2AFC (InRad-HCFMUSP)
- Experimento psicofísico de escolha forçada entre duas alternativas (2AFC), formalmente *criterion-free*, com radiologistas especialistas e residentes:
  $$d'_v = \sqrt{2} \Phi^{-1}(P_C)$$
- O hiperparâmetro $\sigma_{\text{int}}$ é ajustado empiricamente para maximizar a concordância e a correlação ($R^2 \ge 0,90$) entre o índice $d'_{\text{DLMO}}$ e a detectabilidade humana real.

---

## 3. Metrificação e Modelagem do Tempo Operacional ($T$)

O tempo total de exame não é meramente administrativo; ele determina a viabilidade física de protocolos clínicos de alto fluxo (rastreamento de câncer de pulmão) e limitações térmicas de hardware:

$$T(\mathbf{p}) = T_{\text{aquisição}}(\mathbf{p}) + T_{\text{reconstrução}}(\mathbf{p})$$

### A. Tempo de Aquisição ($T_{\text{acq}}$)
$$T_{\text{aquisição}} = \frac{L \cdot t_{\text{rot}}}{P \cdot (N_{\text{col}} \cdot w)}$$
- **Restrições Físicas:** Reduções drásticas em $t_{\text{rot}}$ ou aumentos no pitch $P$ demandam correntes de tubo (mA) excessivas para manter a fluência de fótons, esbarrando no limite de dissipação de potência e aquecimento anódico do tubo de raios X.

### B. Tempo de Reconstrução ($T_{\text{recon}}$)
- **Custo Computacional DLR:** Algoritmos iterativos densos e redes neurais de reconstrução exigem processamento intensivo em GPUs dedicadas. Em exames de alta resolução, o tempo de reconstrução pode saltar de 5 segundos (FBP) para mais de 90 a 180 segundos por série, criando filas no processador e atraso na liberação do paciente.
- **Extração Empírica via DICOM:**
  $$\Delta t_{\text{recon}} = \text{Content Time } (0008,0033) - \text{Acquisition Time } (0008,0032)$$

### C. Otimização Multiobjetivo no Espaço $(D, T, W)$
A função objetivo a ser explorada via Algoritmos Genéticos (NSGA-II) e Modelos Substitutos (*Surrogate Models* via Processos Gaussianos) busca a Fronteira de Pareto:
$$\min_{\mathbf{p} \in \Omega} \mathcal{F}(\mathbf{p}) = \left( \text{CTDI}_{\text{vol}}(\mathbf{p}), \; T(\mathbf{p}), \; -d'_{\text{DLMO}}(\mathbf{p}) \right)$$
sujeito a $d'_{\text{DLMO}}(\mathbf{p}) \ge d'_{\text{ref}} - \delta_{\text{tol}}$, garantindo suficiência diagnóstica sem gargalos de produtividade hospitalar.

---

## 🔗 Conexões e Referências Cruzadas
- [[Zou 2026 - Otimizacao de Protocolos de TC com RL e VIT]] (Benchmark teórico internacional de RL para TC).
- [[COSTA et al. 2025 - Hybrid Phantom for Lung CT Design and Validation]] (Base metrológica dos phantoms do GDRFM).
- AAPM Task Group Report 233 (2019/2021) - Metodologia de métricas baseadas em tarefa.
