> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Tomografia Computadorizada]], [[Unidades Hounsfield]], [[Transformada de Radon]], [[Retroprojeção Filtrada (FBP)]], [[Photon Counting Detector CT (PCD-CT)]]

## 1. Origem Histórica e o Desenvolvimento da Tomografia Computadorizada

A **[[Tomografia Computadorizada]] (TC)** surgiu no início da década de 1970, como fruto do trabalho pioneiro do engenheiro eletricista britânico **Sir Godfrey Hounsfield** nos laboratórios da *Electric and Musical Industries* (EMI Laboratories), no Reino Unido.

O arcabouço conceitual e experimental desenvolveu-se através dos seguintes marcos temporais e científicos:

- **Bases Matemáticas (1917):** O matemático austríaco Johann Radon demonstrou teoricamente que uma função bidimensional ou tridimensional contínua pode ser reconstruída univocamente a partir de um conjunto infinito de suas projeções integrais (a [[Transformada de Radon]]). 
- **Modelagem Teórica Aplicada (1963–1964):** O físico sul-africano Allan Cormack publicou de forma independente os fundamentos matemáticos e físicos da reconstrução de imagens por atenuação de raios X, realizando experimentos teóricos sobre medição de coeficientes de atenuação linear.
- **Desenvolvimento do Protótipo (1967–1971):** Hounsfield concebeu e construiu o primeiro scanner funcional em escala de laboratório para varreduras intracranianas.
- **Primeiro Exame Clínico (1º de Outubro de 1971):** Realizou-se a primeira varredura tomográfica em um paciente vivo no *Atkinson Morley's Hospital*, em Wimbledon, Londres. A paciente apresentava uma suspeita de cisto no lóbulo frontal do cérebro, cuja lesão foi claramente demonstrada no corte tomográfico.
- **Anúncio Oficial e Lançamento Comercial (1972):** A invenção foi oficialmente apresentada durante o congresso anual do *British Institute of Radiology* (BIR) em abril de 1972.
- **Reconhecimento Científico (1979):** Godfrey Hounsfield e Allan Cormack foram laureados conjuntamente com o Prêmio Nobel de Fisiologia ou Medicina pelas contribuições no desenvolvimento da tomografia computadorizada.

---

## 2. Cronologia e Evolução Tecnológica por Gerações

A evolução técnica dos tomógrafos é categorizada por gerações de arquitetura de aquisição e arranjo de detectores:

| Geração | Período de Introdução | Geometria do Feixe | Configuração e Movimento | Tempo de Aquisição por Corte |
| :--- | :--- | :--- | :--- | :--- |
| **1ª Geração** | 1971–1972 | Feixe em lápis (*Pencil Beam*) | Translação-Rotação (1 a 2 detectores por corte) | 4,5 a 5,0 minutos |
| **2ª Geração** | 1974 | Feixe em leque estreito (*Narrow Fan-Beam*) | Translação-Rotação (Matriz linear de 3 a 30 detectores) | 20 a 60 segundos |
| **3ª Geração** | 1975–1976 | Feixe em leque largo (*Wide Fan-Beam*) | Rotação-Rotação (Matriz curva de centenas de detectores) | 1,0 a 5,0 segundos |
| **4ª Geração** | 1978 | Feixe em leque largo | Rotação-Estacionária (Anel fixo 360° de 1000+ detectores) | 1,0 a 2,0 segundos |
| **TC Helicoidal / Multislice** | Década de 1990–2000 | Feixe cônico (*Cone-Beam*) | Rotação Contínua (*Slip-Ring*) com múltiplas fileiras de detectores | Subsegundo por volume completo |
| **PCD-CT (Contagem de Fótons)** | Década de 2020 | Feixe cônico e espectral | Detectores de conversão direta em semicondutor (CdTe/CZT) | Dezenas de milissegundos |

---

## 3. Fundamentação Matemática da Formação de Imagem e Unidades Hounsfield

A reconstrução de imagem tomográfica baseia-se na inversão de projeções de atenuação. A intensidade emergente $I$ de um feixe monocromático ao atravessar o corpo obedece à Lei de Beer-Lambert:

$$
I = I_0 \exp \left( - \int_L \mu(x, y) \\, dl \right)
$$

A projeção $P_{\theta}(t)$, correspondente à Transformada de Radon do coeficiente de atenuação linear espacial $\mu(x, y)$, é definida por:

$$
P_{\theta}(t) = \mathcal{R}\{\mu(x, y)\} = \iint_{-\infty}^{\infty} \mu(x, y) \delta(x \cos\theta + y \sin\theta - t) \\, dx \\, dy
$$

Para quantificar a atenuação tecidual de maneira reprodutível e independente dos parâmetros do tubo, Hounsfield definiu a escala estandardizada em **[[Unidades Hounsfield]] ($\text{UH}$)**:

$$
\text{UH} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Onde $\mu_{\text{água}}$ e $\mu_{\text{ar}}$ representam os coeficientes de atenuação linear da água e do ar sob condições idênticas de feixe.

---

## 4. Relevância Contemporânea e Impacto na Física Médica

A transição histórica dos primeiros algoritmos de reconstrução algébrica (ART) para a **[[Retroprojeção Filtrada (FBP)]]**, e posteriormente para a **[[Reconstrução Iterativa]]** e métodos de **[[Deep Learning Image Reconstruction (DLR)]]**, redefiniu os parâmetros de qualidade de imagem e proteção contra radiação.

Atualmente, o surgimento da tomografia de contagem de fótons (**[[Photon Counting Detector CT (PCD-CT)]]**) representa o maior avanço tecnológico desde a invenção da TC em 1971, eliminando o ruído eletrônico residual, aumentando a resolução espacial e permitindo quantificação espectral direta do tecido biológico.

---

## 5. Conexões e Wikilinks

- [[Tomografia Computadorizada]]
- [[Unidades Hounsfield]]
- [[Transformada de Radon]]
- [[Retroprojeção Filtrada (FBP)]]
- [[Reconstrução Iterativa]]
- [[Deep Learning Image Reconstruction (DLR)]]
- [[Photon Counting Detector CT (PCD-CT)]]
