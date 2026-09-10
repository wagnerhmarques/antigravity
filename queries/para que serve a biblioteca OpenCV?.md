> 📅 **Data:** 2026-08-29 | 🔗 **Conexões:** [[Tomografia Computadorizada]], [[Qualidade de Imagem em TC]], [[Observadores de Modelo (Model Observers)]], [[Processamento Digital de Imagens]]

> 📅 **Data:** 2026-03-30 | 🔗 **Conexões:** [[Tomografia Computadorizada]], [[Qualidade de Imagem em TC]], [[Deep Learning Image Reconstruction (DLR)]], [[Observadores de Modelo (Model Observers)]]

## 1. Visão Geral e Arquitetura da OpenCV

A **OpenCV** (*Open Source Computer Vision Library*) é uma biblioteca de código aberto, de alto desempenho, projetada para processamento de imagens, visão computacional e aprendizado de máquina. Desenvolvida originalmente pela Intel e mantida pela comunidade open-source e pela OpenCV.org, a biblioteca oferece interfaces otimizadas para linguagens como C++, Python, Java e Julia, alavancando instruções SIMD (AVX, NEON) e aceleração por GPU (CUDA/OpenCL).

No contexto da **Física Médica** e da **Tomografia Computadorizada (TC)**, a OpenCV atua como a infraestrutura de pré-processamento, segmentação, extração de Regiões de Interesse (ROIs) e manipulação matricial para pipelines de avaliação quantitativa de qualidade de imagem e testes de percepção (como o suporte computacional a [[Observadores de Modelo (Model Observers)]]).

## 2. Funcionalidades Essenciais no Processamento de Imagens Médicas

A biblioteca fornece primitivas matemáticas e computacionais fundamentais para lidar com matrizes de atenuação e dados de imagem:

1. **Filtragem Espacial e Operações Frequenciais:**
   - Implementação de filtros lineares e não-lineares (filtro Gaussiano, filtro mediano, filtro bilateral).
   - Cálculo de gradientes e detecção de bordas ($Sobel$, $Laplaciano$, $Canny$) cruciais para delineamento de contornos e fantasmas (*phantoms*).
   - Transformada Discreta de Fourier (DFT) bidimensional para análises de frequências espaciais relacionadas ao [[Noise Power Spectrum]].

2. **Operações Morfológicas e Segmentação de ROIs:**
   - Correção de desalinhamentos e extração de estruturas anatômicas ou patológicas (ex.: nódulos pulmonares, tecidos moles) utilizando operações morfológicas (abertura, fechamento) e algoritmos de binarização adaptativa ($Otsu$, limiarização local).

3. **Transformações Geométricas e Registro:**
   - Rotação, translação, redimensionamento isotrópico e transformações afins/homográficas essenciais para alinhar varreduras sequenciais de TC ou registrar cortes de tomografia com modelos teóricos (*phantoms* computacionais).

## 3. Aplicação no Pipeline de Análise em Tomografia Computadorizada

Em tarefas de metrologia e qualidade de imagem em TC, a OpenCV é combinada com bibliotecas médicas (como `pydicom` e `SimpleITK`) para realizar etapas operacionais de alto impacto:

$$
\mathbf{I}_{\text{proc}}(x, y) = \mathcal{T} \left\{ \mathbf{I}_{\text{raw}}(x, y) \right\}
$$

Onde $\mathcal{T}$ representa uma cadeia de transformações lineares ou não-lineares aplicadas sobre as matrizes de unidades Hounsfield (HU).

### Aplicações Práticas:
- **Extração Automática de ROIs:** Recorte preciso de regiões centrais e periféricas em fantasmas (ex.: Fantasma Catphan®) para o cálculo da Função de Transferência de Modulação ([[Task Transfer Function]]) e do Espectro de Potência de Ruído ([[Noise Power Spectrum]]).
- **Preparo de Dados para Observadores de Modelo:** Geração e alinhamento de vetores de imagem para modelos como o [[Channelized Hotelling Observer (CHO)]] e o [[NPWE Model Observer]].
- **Redes de Aprendizado Profundo:** Pré-processamento e normalização de tensores de entrada para redes de reconstrução e classificação ([[Deep Learning Image Reconstruction (DLR)]]).

## 4. Tabela Comparativa de Módulos e Uso na Física Médica

| Módulo OpenCV | Função Principal | Aplicação em TC e Física Médica |
| :--- | :--- | :--- |
| `imgproc` | Processamento de imagens (filtros, transformações, limiarização) | Extração de ROIs, cálculo de perfis de borda para MTF e isolamento de sinal. |
| `core` | Estruturas de dados escalares e matriciais (`cv::Mat` / `numpy.ndarray`) | Manipulação direta de matrizes de atenuação e coeficientes de TC. |
| `dnn` | Módulo de inferência para redes neurais profundas | Execução rápida de modelos DLR para redução de ruído e segmentação. |
| `features2d` | Detecção e descrição de pontos de interesse (SIFT, ORB) | Registro de imagens de TC e rastreamento de marcadores fiduciais em radioterapia. |
