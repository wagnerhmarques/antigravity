# MANUAL DE INSTRUÇÕES E PROCEDIMENTO OPERACIONAL PADRÃO (SOP)
## Projeto de Doutorado Direto — FMUSP / InRad / IFUSP
**Candidato:** Wagner Henrique Marques  
**Orientador:** Prof. Dr. Paulo Roberto Costa  
**Título do Projeto:** *Observadores de aprendizado profundo para a otimização de protocolos de tomografia computadorizada baseada em tarefas*

---

## 🛡️ DIRETRIZ ZERO: Segurança de Dados, Governança Ética e Anonimização

> [!IMPORTANT]
> A conformidade com a LGPD (Lei Federal nº 13.709/2018) e as Resoluções do Conselho Nacional de Saúde (CNS nº 466/2012 e nº 510/2016) é pré-requisito mandatório em todas as etapas que envolvem imagens clínicas e leitores humanos voluntários.
> **Número do Parecer CEP-FMUSP / CAAE:** `27.912.619.6.0000.0068`.

### 1. Protocolo Criptográfico de Anonimização DICOM
Todas as imagens provenientes dos tomógrafos do InRad-HCFMUSP que contenham dados anatômicos de pacientes (utilizados na modelagem prévia ou calibração) devem passar por higienização estrita antes de entrarem no servidor de treinamento:
* **Execução via Script:** Utilizar o perfil de desidentificação estrita baseado no **DICOM PS 3.15 (Anexo E - Basic Application Level Confidentiality Profile)**.
* **Tags Mandatórias de Eliminação/Mascaramento Criptográfico:**
  * `(0010,0010)` *Patient's Name* $\rightarrow$ Anonimizado com hash criptográfico irreversível (ex.: `SUBJ_CRANIO_001`).
  * `(0010,0020)` *Patient ID* $\rightarrow$ Pseudonimizado.
  * `(0010,0030)` *Patient's Birth Date* $\rightarrow$ Removido ou truncado para apenas o ano.
  * `(0008,0080)` *Institution Name* e `(0008,0090)` *Referring Physician* $\rightarrow$ Removidos.
  * `(0010,1010)` *Patient's Age*, `(0010,1030)` *Patient's Weight* $\rightarrow$ Mantidos apenas os parâmetros morfométricos de interesse físico.
* **Tags Físicas Protegidas (NUNCA DELETAR):**
  * Parâmetros do feixe: Tensão `(0018,0060)`, Corrente `(0018,1151)`, Tempo de Exposição `(0018,1152)`, Tempo de Rotação `(0018,1120)`, *Pitch* `(0018,0093)`, Colimação `(0018,9306)`.
  * Dosimetria: $\text{CTDI}_{\text{vol}}$ `(0018,9345)` e $\text{DLP}$ `(0018,9346)`.
  * Reconstrução e Filtros: Algoritmo/Kernel `(0018,1210)` e Espessura de Corte `(0018,0050)`.
  * Carimbos Temporais (para o Eixo 3): *Acquisition Time* `(0008,0032)` e *Content Time* `(0008,0033)`.

### 2. Infraestrutura de Armazenamento e Integridade
* **Armazenamento Primário:** Servidores locais dedicados do InLab/InRad com acesso restrito via VPN institucional, autenticação em dois fatores (2FA) e criptografia em repouso (LUKS/BitLocker).
* **Controle de Integridade:** Toda série DICOM bruta adquirida deve ter seu hash `SHA-256` gerado e registrado em tabela de auditoria imediatamente após a exportação do PACS, prevenindo corrupção silenciosa de arquivos ou alterações não rastreadas.
* **Código e Versões:** Repositório Git institucional com Git LFS (*Large File Storage*) para pesos neurais, bloqueando completamente o envio de arquivos DICOM para repositórios públicos.

---

## 📐 ETAPA 1: Padronização Física e Metrologia Automatizada (Eixo 1 / S1–S3)

### Passo 1.1: Inspeção e Preparação dos Phantoms Híbridos
1. **Phantom de Tórax:** Verificar alinhamento dos nódulos esféricos e de vidro fosco no parênquima pulmonar; checar integridade do módulo geométrico anexo.
2. **Phantom de Abdome:** Inspecionar o encaixe da base elíptica de UHMW maciça (para metrologia pura de ruído) e da versão oca preenchida com as estruturas 3D (fígado, rins e coluna vertebral).
3. **Phantom de Crânio:** Verificar o posicionamento dos inserts parenquimatosos de baixo contraste no interior da calota óssea cortical/trabecular.

### Passo 1.2: Protocolo Físico de Aquisição no Gantry (7 Tomógrafos)
Realizar o agendamento em horários dedicados de pesquisa nos 7 tomógrafos clínicos do InRad (Tabela 1 do projeto: GE Revolution, Optima, Siemens Force, Definition, Philips Brilliance, Incisive e Canon Aquilion).
1. **Posicionamento a Laser:** O phantom deve ser centralizado no isocentro exato do gantry utilizando os lasers de alinhamento coronal, sagital e axial com tolerância $< 1{,}0\text{ mm}$.
2. **Scout View Obrigatório:** Adquirir o topograma/scout frontal e lateral. Extrair a atenuação equivalente em água ($D_w$) de acordo com os relatórios AAPM TG-204 e TG-220.
3. **Série Fatorial:** Executar as combinações planejadas variando tensão (80, 100, 120 kVp), níveis de dose (baixo, padrão e alto mAs), pitch e filtros, contemplando as três famílias de reconstrução de cada fabricante:
   * **FBP:** Retroprojeção Filtrada (controle linear).
   * **HIR:** Reconstrução Iterativa Híbrida (ASiR-V, SAFIRE, iDose4, AIDR 3D).
   * **DLR:** Reconstrução por Deep Learning comercial (TrueFidelity, Precise Image, AiCE).

### Passo 1.3: Pipeline Automatizado de Extração Metrológica (Python)
1. **Segmentação Automática:** O pipeline desenvolvido em Python identifica automaticamente o centro do insert cilíndrico e as regiões homogêneas adjacentes.
2. **Cálculo da TTF (Resolução Espacial Dependente da Tarefa):**
   * Extrair o Perfil de Borda Radial (ESF - *Edge Spread Function*) em torno do insert cilíndrico de tecidos conhecidos.
   * Diferenciar numericamente para obter a Função de Espalhamento de Linha: $\text{LSF}(r) = \frac{d}{dr}\text{ESF}(r)$.
   * Aplicar a Transformada de Fourier 1D para obter $\text{TTF}(f)$.
   * Registrar a frequência espacial de corte a 50% e 10%: $f_{50}$ e $f_{10}$.
3. **Cálculo do NPS 2D (Espectro de Potência de Ruído):**
   * Distribuir uniformemente $N \ge 64$ ROIs quadradas ($128 \times 128$ pixels) no módulo homogêneo.
   * Aplicar detrending polinomial de 2ª ordem em cada ROI para eliminar eventuais gradientes de atenuação residual.
   * Calcular a média dos módulos ao quadrado da FFT 2D normalizada:
     $$\text{NPS}(u, v) = \frac{\Delta x \Delta y}{N_x N_y} \left\langle \left| \mathcal{F}_{2D} \{ I(x, y) - \bar{I}(x, y) \} \right|^2 \right\rangle$$
   * Extrair a frequência de pico espacial ($f_{\text{pico}}$) e a variância total do ruído ($\sigma^2$).
4. **Cálculo dos Observadores Lineares de Linha de Base:**
   * Computar a integral de detectabilidade do observador não-pré-branqueador com filtro do olho humano:
     $$(d'_{\text{NPWE}})^2 = \frac{\left[ \iint |W_{\text{task}}(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot E^2(u, v) \, du \, dv \right]^2}{\iint |W_{\text{task}}(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot \text{NPS}(u, v) \cdot E^4(u, v) \, du \, dv}$$
5. **Critério de Aceite da Etapa (Tabela 2 do Projeto - P1):**
   * Dois físicos médicos independentes executam a extração manual clássica em um subconjunto de 20% das imagens.
   * **Validação formal:** O Coeficiente de Correlação Intraclasse deve ser $\text{ICC} \ge 0{,}90$ e o viés médio no gráfico de Bland-Altman deve ser estatisticamente nulo ($p > 0{,}05$).

---

## 👁️ ETAPA 2: Estudo Psicofísico 2AFC com Radiologistas (Eixo 2 / S3–S6)

### Passo 2.1: Construção da Amostra de ROIs
1. **Extração Padronizada:** A partir das aquisições dos phantoms híbridos, extrair fatias axiais contendo os alvos conhecidos (nódulos de tórax, lesões focais de abdome e meningiomas simulados de crânio).
2. **Geração de Pares de Teste (ROIs $64 \times 64$ pixels):**
   * **ROI Sinal-Presente ($H_1$):** Região anatômica contendo a lesão/alvo centrada.
   * **ROI Sinal-Ausente ($H_0$):** Região anatômica de textura equivalente e mesmo nível de ruído, sem a lesão.

### Passo 2.2: Plataforma Web Psicofísica e Calibração dos Monitores
1. **Interface de Exibição:** Executar os testes através da plataforma web dedicada desenvolvida pelo GDRFM.
2. **Conformidade Médica de Imagem:** A estação de teste dos radiologistas no InRad deve cumprir estritamente as diretrizes **DICOM GSDF (Grayscale Standard Display Function)** e **AAPM TG-18**:
   * Monitor de diagnóstico calibrado com fotômetro (luminância mínima $L_{\min} \ge 1{,}0\text{ cd/m}^2$, luminância máxima $L_{\max} \ge 350\text{ cd/m}^2$).
   * Iluminação ambiente controlada na sala de laudo ($< 25\text{ lux}$).
3. **Randomização Espacial:** O sistema posiciona aleatoriamente a ROI $H_1$ à esquerda ou à direita a cada rodada.

### Passo 2.3: Desenho Experimental e Mitigação de Fadiga (MRMC)
1. **Recrutamento:** Recrutar médicos radiologistas especialistas (tórax, abdome e neuro) e médicos residentes do HCFMUSP.
2. **Fracionamento de Sessões:** Sessões estritamente limitadas a **15 a 20 minutos por bloco** (aproximadamente 100 a 150 pares de imagens por sessão) para evitar viés de fadiga visual e perda de acuidade.
3. **Registro Automático de Dados:** Para cada leitor e cada imagem, registrar:
   * Decisão forçada (Esquerda ou Direita).
   * Acerto ($1$) ou Erro ($0$).
   * Tempo de latência de resposta em milissegundos (desde a renderização na tela até o clique).

### Passo 2.4: Extração da Referência Perceptual Humana
1. Calcular a proporção de escolhas corretas do leitor ($P_C$).
2. No paradigma 2AFC (formalmente livre de critério), $P_C$ equivale à Área sob a Curva ROC ($\text{AUC} = P_C$).
3. Converter para o índice de detectabilidade psicofísico humano:
   $$d'_v = \sqrt{2} \, \Phi^{-1}(P_C)$$
4. Essa base de dados constituirá o padrão-ouro de comparação (*ground truth*) perceptual.

---

## 🧠 ETAPA 3: Engenharia e Treinamento do DLMO com Atenção (Eixo 2 / S3–S6)

### Passo 3.1: Arquitetura de Rede Neural
1. **Modelo Base:** Vision Transformer (ViT) compacto ou Swin Transformer (baseado em janelas deslocadas para capturar dependências locais e globais do ruído de DLR).
2. **Entrada:** Tensores de entrada de 1 canal (escala de cinza de TC convertida de Hounsfield Units para escala normalizada $[-1, 1]$ com janelamento específico de cada tecido).
3. **Mecanismo de Atenção:** Módulos de *Multi-Head Self-Attention* (MHSA) que ponderam o peso relativo das bordas da lesão contra as correlações espaciais complexas do ruído em reconstruções DLR.

### Passo 3.2: Particionamento Rigoroso de Dados
* **Divisão de Conjuntos:** $70\%$ Treinamento, $15\%$ Validação, $15\%$ Teste Independente.
* **Critério Anticontaminação (*No Data Leakage*):** Fatias da mesma aquisição ou fatias consecutivas com sobreposição anatômica NUNCA devem ser divididas entre treino e teste. O conjunto de teste deve conter séries tomográficas retidas que o modelo nunca viu.

### Passo 3.3: Injeção de Ruído Interno Estocástico e Calibração
1. A rede emite o logit de classificação determinístico: $\hat{t} = f_\theta(I)$.
2. Para emular a estocasticidade do olho e do córtex visual humano, injetar o componente de ruído gaussiano:
   $$z = \hat{t} + \varepsilon_{\text{int}}, \quad \varepsilon_{\text{int}} \sim \mathcal{N}(0, \sigma_{\text{int}}^2)$$
3. **Algoritmo de Calibração do $\sigma_{\text{int}}$:**
   * Variar $\sigma_{\text{int}}$ em grade fina $[0{,}01 ; 2{,}00]$.
   * Para cada valor, calcular a curva ROC sintética do DLMO na base de teste.
   * Selecionar o $\sigma_{\text{int}}^*$ que minimiza o erro quadrático médio frente aos índices $d'_v$ humanos obtidos no 2AFC dos radiologistas:
     $$\sigma_{\text{int}}^* = \arg\min_{\sigma} \sum_k \left( d'_{\text{DLMO}}(k; \sigma) - d'_{\text{humano}}(k) \right)^2$$

### Passo 3.4: Teste de Hipótese Formal (Critério H1 da Tabela 2)
* Executar a comparação estatística através de análise MRMC com teste pareado de DeLong:
* **Critério de Sucesso:** O DLMO deve apresentar correlação e concordância com a referência humana significativamente superior aos observadores lineares clássicos (NPWE, HO e CHO) sob reconstruções não lineares DLR com significância estatística $p < 0{,}05$.

---

## ⚡ ETAPA 4: Otimização Multiobjetivo no Espaço $(D, T, W)$ (Eixo 3 / S6–S8)

### Passo 4.1: Extração e Metrificação do Tempo Operacional
Para cada série adquirida nos tomógrafos clínicos, registrar no banco de dados:
1. **Tempo de Aquisição ($T_{\text{acq}}$):**
   $$T_{\text{aquisição}} = \frac{L \cdot t_{\text{rot}}}{P \cdot (N_{\text{col}} \cdot w)}$$
   Extrair $t_{\text{rot}}$ de `(0018,1120)`, $P$ de `(0018,0093)` e verificar contra o log da mesa.
2. **Tempo de Reconstrução ($T_{\text{recon}}$):**
   Calcular a latência computacional do servidor de reconstrução via tags DICOM:
   $$\Delta t_{\text{recon}} = \text{Tag }(0008,0033)\text{ [Content Time]} - \text{Tag }(0008,0032)\text{ [Acquisition Time]}$$
3. **Tempo Total:** $T(\mathbf{p}) = T_{\text{aquisição}}(\mathbf{p}) + T_{\text{reconstrução}}(\mathbf{p})$.

### Passo 4.2: Modelagem Substituta (*Surrogate Modeling*) com Incerteza
Como é impossível irradiar o phantom em todas as infinitas combinações do tomógrafo:
1. Treinar um **Processo Gaussiano (GP)** para mapear o espaço de parâmetros $\mathbf{p} = (\text{kVp}, \text{mA}, t_{\text{rot}}, P, \text{filtro}, \text{DLR})$ para as três respostas:
   * Dose: $\hat{D}(\mathbf{p}) \pm \sigma_D(\mathbf{p})$
   * Tempo Operacional: $\hat{T}(\mathbf{p}) \pm \sigma_T(\mathbf{p})$
   * Detectabilidade DLMO: $\hat{d}'_{\text{DLMO}}(\mathbf{p}) \pm \sigma_{d'}(\mathbf{p})$
2. O Processo Gaussiano fornece a incerteza preditiva experimental em cada região do espaço de parâmetros.

### Passo 4.3: Otimização Genética (NSGA-II) e Fronteira de Pareto
1. Executar o algoritmo **NSGA-II** (*Non-dominated Sorting Genetic Algorithm II*) para resolver o problema tri-objetivo:
   $$\min_{\mathbf{p} \in \Omega} \mathcal{F}(\mathbf{p}) = \left( \text{CTDI}_{\text{vol}}(\mathbf{p}), \; T(\mathbf{p}), \; -d'_{\text{DLMO}}(\mathbf{p}) \right)$$
   sujeito a:
   $$d'_{\text{DLMO}}(\mathbf{p}) \ge d'_{\text{ref}} - \delta_{\text{tol}}$$
2. **Comparação Experimental Obrigatória:**
   * Rodar o **Cenário Baseline (Zou et al., 2026 adaptado)**: Bi-objetivo $\min(\text{Dose})$ com $d'_{\text{NPWE}} \ge d'_{\text{ref}}$ (sem tempo operacional).
   * Rodar o **Cenário Proposto da Tese**: Tri-objetivo $(D, T, W)$ com $d'_{\text{DLMO}}$ e restrições de tempo.
3. **Critério de Sucesso (H2 da Tabela 2):** Identificar pelo menos um protocolo clínico não dominado com redução comprovada de dose e/ou tempo em relação ao protocolo padrão de fábrica do InRad, preservando a detectabilidade diagnóstica dentro do intervalo de incerteza estatística.

---

## 🌐 ETAPA 5: Transferibilidade Inter-Fabricantes e Validação (Eixo 4 / S8–S10)

### Passo 5.1: Desenho Experimental *Leave-One-Scanner-Out*
1. Treinar o modelo DLMO utilizando dados provenientes de 6 tomógrafos clínicos.
2. Testar o modelo diretamente no 7º tomógrafo retido (de fabricante diferente, ex: treinar em GE, Siemens, Philips e testar em Canon).
3. Mensurar a queda de desempenho na Área sob a Curva ($\Delta \text{AUC}$) e na correlação com a referência humana.

### Passo 5.2: Estratégia de Ajuste Fino (*Transfer Learning*)
1. Adquirir um número reduzido e padronizado de fatias de calibração no tomógrafo retido ($N_{\text{calib}} \le 50$ imagens).
2. Congelar os blocos iniciais do Vision Transformer e ajustar (*fine-tuning*) apenas as camadas de atenção final e o cabeçote de classificação.
3. Quantificar o esforço experimental mínimo necessário para restaurar a concordância do DLMO ($r \ge 0{,}90$).
4. **Critério de Sucesso (H3 da Tabela 2):** O modelo deve ser capaz de recuperar o desempenho com esforço experimental reduzido, estabelecendo a transferibilidade do método entre equipamentos e fabricantes concorrentes.

---

## 📅 CHECKLIST OPERACIONAL CRONOLÓGICO RESUMIDO

| Período | Foco Principal | Entregáveis Físicos / Computacionais |
| :--- | :--- | :--- |
| **S1–S2** | Padronização & Ensaios-Piloto | Protocolo de aquisições padronizado; inspeção dos 3 phantoms híbridos; alinhamento no InRad. |
| **S2–S3** | Eixo 1 (Metrologia Automatizada) | Pipeline Python validado com $\text{ICC} \ge 0{,}90$ frente à extração manual de NPS/TTF. |
| **S3–S4** | Eixo 2 (Estudo 2AFC com Radiologistas) | Plataforma web operando; coleta com radiologistas concluída; base $d'_v$ humana gerada. |
| **S4–S5** | Eixo 2 (Desenvolvimento do DLMO) | Rede Vision Transformer treinada; ruído estocástico $\sigma_{\text{int}}$ calibrado; qualificação. |
| **S6–S7** | BEPE / Eixo 3 (Otimização Multiobjetivo) | Estágio na UPenn (PCCT/PixelPrint); algoritmo NSGA-II e Processos Gaussianos rodando. |
| **S7–S8** | Eixo 3 & Eixo 4 (Fronteiras e Transferibilidade)| Comparativo com Zou et al. (2026); validação cruzada entre os 7 tomógrafos clínicos. |
| **S9–S10**| Conclusão & Defesa | Publicação de artigos A1; redação final da tese de Doutorado Direto; defesa pública na FMUSP. |
