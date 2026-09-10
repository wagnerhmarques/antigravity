---tipo: conceito
titulo: "Métricas de Dose em Tomografia Computadorizada (CTDIvol e DLP)"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags: ["dosimetria", "ctdi", "dlp", "metrologia", "fisica-medica"]
fontes_origem: ["[[McCollough 2026 - Evolução das Doses de Radiação em TC|mccollough-2026-good-news-ct-doses]]"]
aliases: [metricas-de-dose-tc, ctdivol, CTDIvol, ssde, SSDE\, dlp, DLP, "metricas de dose"]
---

# Métricas de Dose em Tomografia Computadorizada ($CTDI_{vol}$ e $DLP$)

## 1. O que são $CTDI_{vol}$ e $DLP$?
Na Tomografia Computadorizada (TC), a dosimetria clínica padronizada internacionalmente baseia-se em duas métricas principais geradas e reportadas diretamente pelo equipamento (e extraídas via relatórios estruturados DICOM SR):

- **$CTDI_{vol}$ (Volume CT Dose Index - mGy):** Mede a intensidade média de radiação entregue por unidade de volume dentro da área escaneada, utilizando simuladores padronizados de acrílico (phantoms de 16 cm para crânio/pediátrico ou 32 cm para corpo). Representa a densidade da dose ao longo do eixo z.
- **$DLP$ (Dose-Length Product - mGy·cm):** Produto do $CTDI_{vol}$ pelo comprimento total varrido na varredura ($L$ em cm). Representa a energia radiante total depositada no paciente:
  

$$
DLP = CTDI_{vol} \times L
$$

---

## 2. Aplicação Prática & Benchmarking
- Ambas as métricas são utilizadas pela ICRP e ACR para estabelecer [[Níveis de Referência Diagnóstica (DRL)|Níveis de Referência Diagnóstica (DRLs)]] e **Doses Atingíveis (Achievable Doses)**.
- **Importante:** $CTDI_{vol}$ e $DLP$ representam doses em phantoms de referência, servindo de base para estimativas de dose absorvida em órgãos e dose efetiva ($E$) em pacientes de portes específicos.

---

## 3. Tendência Histórica
Conforme demonstrado por [[McCollough 2026 - Evolução das Doses de Radiação em TC|mccollough-2026-good-news-ct-doses]], entre 2017 e 2025/2026:
- O DRL do $CTDI_{vol}$ médio caiu **21,8%**.
- O DRL do $DLP$ médio caiu **19,8%**.
- No caso de abdome de rotina, o $CTDI_{vol}$ de referência caiu de 25 mGy (2002) para 11 mGy (2025).

---

## 🔗 Páginas Relacionadas
- [[Níveis de Referência Diagnóstica (DRL)|niveis-de-referencia-diagnostica-drl]]
- [[Otimização de Dose em TC|otimizacao-de-dose-em-tc]]
- [[McCollough 2026 - Evolução das Doses de Radiação em TC|mccollough-2026-good-news-ct-doses]]
