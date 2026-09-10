---
tipo: conceito
titulo: "Espectro de Raios X e Modulação de Feixe"
data_criacao: 2026-08-27
tags: ["espectro-raios-x", "dosimetria", "qualidade-de-imagem"]
---

# Espectro de Raios X e Modulação de Feixe

## 1. Estrutura do Espectro Clínico
O espectro de raios X emitido por um tubo diagnóstico é a superposição da **Radiação de Frenamento** contínua com os **Picos de Radiação Característica**, filtrados pela janela do tubo, óleo de isolamento e filtros adicionais (ex.: alumínio, cobre e [[Filtragem Bowtie]]).

$$
\Phi(E) = \Phi_{\text{brems}}(E) + \sum_i \Phi_{\text{carac}, i} \delta(E - E_i)
$$

## 2. Fatores Moduladores:
- **Tensão de Tubo ($kVp$):** Determina a energia máxima dos fótons ($E_{\max} = e \cdot kVp$), a energia média do feixe e a eficiência de produção de raios X ($\propto kVp^2$).
- **Produto Corrente-Tempo ($mAs$):** Modula linearmente a quantidade total de fótons (fluência) sem alterar a distribuição energética relativa.
- **Filtração:** Atenua exponencialmente os fótons de baixa energia, reduzindo a dose desnecessária na pele do paciente.

## 3. Conexões
- [[Radiação de Frenamento (Bremsstrahlung)]]
- [[Radiação Característica]]
- [[Endurecimento do Feixe]]
- [[Filtragem Bowtie]]
- [[Unidades Hounsfield]]
