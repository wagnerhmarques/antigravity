---
aliases: ["niveis-de-referencia-diagnostica-drl", "DRL", "DRLs", "Diagnostic Reference Levels", "Níveis de Referência Diagnóstica"]
---

# Níveis de Referência Diagnóstica (DRL)

## Definição Conceitual e Fundamentação Física

Os **Níveis de Referência Diagnóstica (DRLs)** constitui uma ferramenta de investigação em radiologia diagnóstica e intervencionista, aplicada para otimizar a proteção radiológica dos pacientes. Na prática da Tomografia Computadorizada (TC) e outras modalidades de imagem médica, os DRLs não devem ser confundidos com limites de dose regulatórios ou restrições de dose estritos para indivíduos; trata-se de valores de orientação estabelecidos para exames típicos de grupos de pacientes de tamanho padrão ou para fantomas padrão para procedimentos específicos.

A fundamentação estatística dos DRLs baseia-se tipicamente na distribuição das doses administradas em populações amplas ou em redes de serviços de saúde, sendo comumente definidos no **percentil 75** da distribuição de métricas de dose como o $CTDI_{vol}$ (Índice de Dose da Tomografia Computadorizada Volumétrico) e o $DLP$ (Produto Dose-Comprimento). Quando a prática clínica de um serviço excede consistentemente estes valores de referência sem justificativa clínica para a variação, isso indica a necessidade de uma investigação imediata e de ações corretivas de [[Otimização de Dose em TC|otimizacao-de-dose-em-tc]].

## Formulações Matemáticas

Matematicamente, a determinação de DRLs populacionais envolve a análise da distribuição de frequências das métricas de dose obtidas em um conjunto de $N$ instalações ou exames. Seja $\left\{ D_1, D_2, \dots, D_N \right\}$ o conjunto ordenado de valores representativos de dose (por exemplo, a média ou mediana do $CTDI_{vol}$ por procedimento em cada centro):

$$
\text{DRL} = P_{75}\left( \left\{ D_i \right\}_{i=1}^{N} \right)
$$

Onde $P_{75}$ representa o 75º percentil da distribuição acumulada empírica. Para avaliações de conformidade e auditorias de dose em tomografia computadorizada, a dose média de um protocolo institucional ($\overline{D}_{\text{inst}}$) é comparada ao DRL nacional ou regional:

$$\Delta_{\text{dose}} = \frac{\overline{D}_{\text{inst}} - \text{DRL}}{\text{DRL}} \times 100\%$

Onde desvios positivos acentuados ($\Delta_{\text{dose}} > 0$) sinalizam protocolos ineficientes ou parâmetros de aquisição inadequados, enquanto reduções recentes documentadas na literatura demonstram quedas expressivas, como a redução média de $21,8\%$ no $CTDI_{vol}$ e $19,8\%$ no $DLP$ reportadas em estudos de grande impacto.

## Aplicação no Acervo de Pesquisa e Documentos

No escopo da pesquisa em Física Médica e Tomografia Computadorizada desenvolvida no acervo (USP/FAPESP), os DRLs exercem um papel central na garantia de conformidade regulatória e na busca contínua pela excelência em dosimetria clínica. Suas principais aplicações documentadas englobam:

1. **Otimização e Princípio ALARA:** Os DRLs funcionam como parâmetros quantitativos norteadores para alinhar a prática diária ao princípio [[Radioproteção|alara]] (*As Low As Reasonably Achievable*), assegurando que a qualidade diagnóstica seja mantida com a menor dose de radiação ionizante possível.
2. **Auditorias de Dose e Métricas de TC:** Atuam em conjunto direto com as [[Métricas de Dose em TC|metricas-de-dose-tc]] ($CTDI_{vol}$, $DLP$, $SSDE$), permitindo comparar a produção institucional com os limiares estabelecidos por órgãos reguladores nacionais e internacionais.
3. **Revisões Históricas e Epidemiológicas:** Análises recentes de dados de dose demonstram uma tendência contínua de revisão para baixo dos valores de corte globais e nacionais de DRLs, refletindo avanços tecnológicos em filtragem, algoritmos de reconstrução iterativa e inteligência artificial aplicada à imagem.

## Conexões Relacionadas

- [[Otimização de Dose em TC|otimizacao-de-dose-em-tc]]
- [[Métricas de Dose em TC|metricas-de-dose-tc]]
- [[Radioproteção|alara]]
- [[Risco Oncológico e Epidemiologia da Radiação em TC|risco-oncologico-radiacao-tc]]