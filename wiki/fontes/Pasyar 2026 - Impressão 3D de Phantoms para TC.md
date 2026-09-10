---
tipo: fonte
titulo: "Dual-Filament 3D Printing of Patient-Specific CT Phantoms with Embedded Implants and Tunable Metal-Artifact Intensity"
autores: "Pouyan Pasyar, Kai Mei, Jessica Y. Im, Leonid Roshkovan, Michael Geagan, Peter B. Noël"
ano: 2026
veiculo: "medRxiv preprint (doi: 10.64898/2026.07.17.26358319)"
doi: "10.64898/2026.07.17.26358319"
fonte_bruta: "raw/2026.07.17.26358319v1.full.pdf"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags: ["3d-printing", "computed-tomography", "metal-artifacts", "phantom-design", "pixelprint", "spectral-ct"]
fontes_origem: []
---

# Dual-Filament 3D Printing of Patient-Specific CT Phantoms with Embedded Implants and Tunable Metal-Artifact Intensity

## Resumo Executivo
O artigo apresenta um método inovador de [[Impressão 3D com Duplo Filamento|impressao-3d-duplo-filamento]] baseado em uma extensão do arcabouço [[Pixelprint]], permitindo a fabricação de fantomas de tomografia computadorizada (TC) específicos para pacientes com implantes metálicos embutidos e intensidades de artefatos controláveis e referenciadas à verdade fundamental. O método utiliza deposição voxel a voxel intercalada de dois filamentos: um ácido polilático (PLA) dopado com cálcio para tecidos moles e ósseos, e um PLA dopado com aço inoxidável 17-4 PH para implantes metálicos. Três fantomas de coluna cervical com parafusos espinhais embutidos (0% de inflição metálica como referência, 50% de inflição média e 85% de inflição alta) foram fabricados e avaliados em um sistema de TC espectral clínico.

## Principais Achados & Dados Quantitativos
- **Acurácia HU:** Os valores de Hounsfield Unit (HU) nos tecidos moles e osso trabecular concordaram com os dados clínicos do paciente dentro de $\pm25$ HU. O osso cortical apresentou subestimação (atingindo máximo de $\approx 620$ HU frente a $>1000$ HU no paciente) devido ao limite superior do filamento de PLA dopado com cálcio utilizado.
- **Modulação de Artefatos (Parâmetro Gumbel):** O parâmetro de localização de Gumbel $\mu$ (que quantifica a severidade de estrias e artefatos) escalou monotonicamente de $46.7$ HU (fundo sem metal, 0%) para $57.1$ HU (infill de 50%) e $90.5$ HU (infill de 85%) em imagens virtuais monoenergéticas (VMI) de $70$ keV.
- **Índice p-index Normalizado:** Aumentou de $0.252$ (inflição de 50%) para $0.932$ (inflição de 85%), representando um aumento de aproximadamente $3,7$ vezes na severidade do artefato.
- **Dependência Energética (VMI):** O uso de energias monoenergéticas elevadas ($130-190$ keV) reduziu drasticamente os artefatos de endurecimento de feixe e estrias, preservando a delineação dos contornos dos parafusos.

## Conceitos, Métodos e Tecnologias Relacionadas
- [[Pixelprint]]
- [[Impressão 3D com Duplo Filamento|impressao-3d-duplo-filamento]]
- [[Redução de Artefatos Metálicos|reducao-de-artefatos-metalicos]]
- [[Tomografia Computadorizada Espectral|tomografia-computadorizada-espectral]]
- [[Métrica Gumbel p-index para Quantificação de Artefatos|metrica-gumbel-p-index]]
