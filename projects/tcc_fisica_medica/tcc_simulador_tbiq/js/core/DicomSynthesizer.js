/**
 * DicomSynthesizer.js
 * Sintetizador de fatias tomográficas virtuais em Unidades Hounsfield (HU).
 * Gera modelos anatômicos sintéticos realistas de tórax, abdome, encéfalo, trabeculado ósseo e artérias coronárias,
 * aplicando ruído quântico de Poisson, convolução de PSF e filtragens não-lineares.
 */

export class DicomSynthesizer {
    /**
     * Gera uma fatia de Tórax / Parênquima Pulmonar (Caso LDCT / Nódulo Pulmonar)
     * @param {number} width
     * @param {number} height
     * @param {Object} params
     * @returns {Float32Array}
     */
    static createLungPhantom(width, height, {
        dose = 2.5,          // CTDIvol em mGy (escalona o ruído)
        lesionContrast = 200,// ΔC em HU (ex: vidro fosco = +180 HU sobre fundo de -800 HU)
        lesionRadius = 3.5,  // mm
        lesionType = 'ggn',  // 'ggn' (vidro fosco) ou 'solid' (sólido)
        hasSignal = true,    // H1 (com lesão) ou H0 (sem lesão)
        blurSigma = 1.0,     // Efeito da PSF/Kernel
        isDLR = false        // Reconstrução DLR não-linear
    } = {}) {
        const slice = new Float32Array(width * height);
        const cx = width / 2;
        const cy = height / 2;
        const scale = width / 240.0; // ~240 mm FOV

        // Desvio padrão do ruído escalonado com a dose (σ ∝ 1/√dose para FBP)
        const baseNoise = isDLR ? (18.0 / Math.sqrt(Math.max(0.5, dose))) * 0.55 : (32.0 / Math.sqrt(Math.max(0.5, dose)));

        // Semente aleatória para ruído coerente
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                const idx = y * width + x;
                const dx = (x - cx) / scale;
                const dy = (y - cy) / scale;
                const r = Math.sqrt(dx * dx + dy * dy);

                let hu = -1000.0; // Ar ambiente externo

                // 1. Contorno Corporal (Elipse)
                const bodyEl = (dx * dx) / (105 * 105) + (dy * dy) / (85 * 85);
                if (bodyEl <= 1.0) {
                    hu = 40.0; // Parede torácica / músculo intercostal

                    // Tecido adiposo subcutâneo
                    if (bodyEl > 0.88) hu = -90.0;

                    // Costelas (Osso cortical / medular)
                    const angle = Math.atan2(dy, dx);
                    const ribFreq = Math.cos(angle * 6.0);
                    if (bodyEl > 0.75 && bodyEl < 0.86 && ribFreq > 0.4) {
                        hu = 750.0; // Costela
                    }

                    // Coluna vertebral
                    const spineDist = Math.sqrt(dx * dx + (dy - 60) * (dy - 60));
                    if (spineDist < 18) hu = 800.0;

                    // Mediastino e Coração (Centro-anterior)
                    const heartDist = Math.sqrt((dx + 15) * (dx + 15) + (dy - 10) * (dy - 10));
                    if (heartDist < 35) hu = 45.0;

                    // 2. Pulmão Direito e Esquerdo
                    const rightLung = ((dx - 45) * (dx - 45)) / (38 * 38) + ((dy + 5) * (dy + 5)) / (55 * 55);
                    const leftLung = ((dx + 48) * (dx + 48)) / (34 * 34) + ((dy + 12) * (dy + 12)) / (50 * 50);

                    if (rightLung <= 1.0 && spineDist >= 18 && heartDist >= 35) {
                        hu = -800.0; // Parênquima pulmonar direito
                        // Vasos broncovasculares normais
                        if (Math.sin(dx * 0.35) * Math.cos(dy * 0.35) > 0.72) hu = -150.0;
                    } else if (leftLung <= 1.0 && spineDist >= 18 && heartDist >= 35) {
                        hu = -800.0; // Parênquima pulmonar esquerdo
                        if (Math.cos(dx * 0.4) * Math.sin(dy * 0.4) > 0.74) hu = -150.0;
                    }

                    // 3. Inserção do Nódulo Pulmonar (Hipótese H1) no pulmão direito
                    if (hasSignal && rightLung <= 0.8) {
                        const noduleX = 35.0;
                        const noduleY = -10.0;
                        const distToNodule = Math.sqrt((dx - noduleX) * (dx - noduleX) + (dy - noduleY) * (dy - noduleY));

                        if (distToNodule <= lesionRadius * 1.5) {
                            // Perfil de vidro fosco (Gaussiano atenuado) ou sólido
                            const profile = lesionType === 'ggn'
                                ? Math.exp(-(distToNodule * distToNodule) / (2 * (lesionRadius * 0.6) * (lesionRadius * 0.6)))
                                : (distToNodule <= lesionRadius ? 1.0 : Math.exp(-(distToNodule - lesionRadius) * 2.0));

                            hu += lesionContrast * profile;
                        }
                    }
                }

                // 4. Adição de Ruído Estocástico (dependente da atenuação/dose)
                const localNoiseStd = hu < -500 ? baseNoise * 0.85 : baseNoise * 1.15;
                let noiseVal = (Math.random() + Math.random() + Math.random() - 1.5) * localNoiseStd * 1.732;

                // Suavização DLR se ativa
                if (isDLR) {
                    noiseVal *= 0.65;
                }

                slice[idx] = hu + noiseVal;
            }
        }

        return slice;
    }

    /**
     * Gera uma fatia de Fígado / Abdome com Metástase Hipoatenuante (Módulo Fourier TG-233)
     */
    static createLiverPhantom(width, height, {
        dose = 10.0,
        deltaC = 25.0,        // HU (contraste tumor-fígado sutil: 15-35 HU)
        lesionRadius = 5.0,   // mm
        hasSignal = true,
        isCatphanMode = false,// Mostra insertos padrão Catphan (+300 Iodo, +900 Teflon, etc)
        isDLR = false
    } = {}) {
        const slice = new Float32Array(width * height);
        const cx = width / 2;
        const cy = height / 2;
        const scale = width / 260.0;

        const baseNoise = isDLR ? (12.0 / Math.sqrt(Math.max(1.0, dose))) * 0.6 : (22.0 / Math.sqrt(Math.max(1.0, dose)));

        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                const idx = y * width + x;
                const dx = (x - cx) / scale;
                const dy = (y - cy) / scale;
                const r = Math.sqrt(dx * dx + dy * dy);

                let hu = -1000.0;

                if (isCatphanMode) {
                    // Fantoma Cilíndrico Catphan (Água Sólida + Insertos)
                    if (r <= 100.0) {
                        hu = 20.0; // Fundo de água
                        // 4 Insertos circulares
                        const pIodine = Math.sqrt((dx - 50)*(dx - 50) + dy*dy);
                        const pTeflon = Math.sqrt(dx*dx + (dy - 50)*(dy - 50));
                        const pDelrin = Math.sqrt((dx + 50)*(dx + 50) + dy*dy);
                        const pWater  = Math.sqrt(dx*dx + (dy + 50)*(dy + 50));

                        if (pIodine <= 15) hu = 300.0;  // Iodo
                        if (pTeflon <= 15) hu = 900.0;  // Teflon
                        if (pDelrin <= 15) hu = 340.0;  // Delrin
                        if (pWater  <= 15) hu = 25.0;   // Solid Water
                    }
                } else {
                    // Anatomia Abdominal Hepática Real
                    const bodyEl = (dx * dx) / (120 * 120) + (dy * dy) / (95 * 95);
                    if (bodyEl <= 1.0) {
                        hu = -90.0; // Gordura subcutânea
                        if (bodyEl <= 0.85) {
                            hu = 45.0; // Tecido mole geral

                            // Fígado no quadrante superior direito (dx < 0 na convenção radiológica)
                            const liverEl = ((dx + 35) * (dx + 35)) / (60 * 60) + ((dy + 10) * (dy + 10)) / (50 * 50);
                            if (liverEl <= 1.0) {
                                hu = 110.0; // Parênquima hepático na fase portal

                                // Veia porta / veias hepáticas
                                const vDist = Math.sqrt((dx + 30) * (dx + 30) + (dy + 15) * (dy + 15));
                                if (vDist < 8.0) hu = 160.0;

                                // Metástase Hipoatenuante (H1)
                                if (hasSignal) {
                                    const metaDist = Math.sqrt((dx + 45) * (dx + 45) + (dy + 5) * (dy + 5));
                                    if (metaDist <= lesionRadius) {
                                        // Atenuação menor (ex: 110 HU - 25 HU = 85 HU)
                                        const profile = Math.cos((metaDist / lesionRadius) * (Math.PI / 2));
                                        hu -= deltaC * profile;
                                    }
                                }
                            }

                            // Baço
                            const spleenEl = ((dx - 65) * (dx - 65)) / (30 * 30) + ((dy + 10) * (dy + 10)) / (35 * 35);
                            if (spleenEl <= 1.0) hu = 100.0;

                            // Vértebra
                            const spineDist = Math.sqrt(dx * dx + (dy - 65) * (dy - 65));
                            if (spineDist < 20) hu = 850.0;
                            // Aorta com contraste
                            const aortaDist = Math.sqrt((dx + 8) * (dx + 8) + (dy - 45) * (dy - 45));
                            if (aortaDist < 12) hu = 280.0;
                        }
                    }
                }

                const noise = (Math.random() + Math.random() + Math.random() - 1.5) * baseNoise * 1.732;
                slice[idx] = hu + noise;
            }
        }
        return slice;
    }

    /**
     * Gera uma fatia de Crânio / AVC Isquêmico Hiperagudo (Módulo CHO & Canais V1)
     */
    static createBrainPhantom(width, height, {
        dose = 40.0,         // CTDIvol alto típico de crânio (~40-60 mGy)
        ischemicDelta = 4.0, // Apenas 3-5 HU de perda de contraste no edema citotóxico
        hasSignal = true,
        useCHO = true,
        isDLR = false
    } = {}) {
        const slice = new Float32Array(width * height);
        const cx = width / 2;
        const cy = height / 2;
        const scale = width / 200.0;

        const baseNoise = isDLR ? 2.5 : 4.8; // Baixo ruído em crânio

        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                const idx = y * width + x;
                const dx = (x - cx) / scale;
                const dy = (y - cy) / scale;
                const r = Math.sqrt(dx * dx + dy * dy);

                let hu = -1000.0;

                // Calota Craniana
                const headEl = (dx * dx) / (75 * 75) + (dy * dy) / (90 * 90);
                if (headEl <= 1.0) {
                    if (headEl > 0.84) {
                        hu = 1400.0; // Osso cortical denso
                    } else {
                        // Parênquima Encefálico
                        hu = 30.0; // Substância branca padrão

                        // Córtex e Núcleos da Base (Substância Cinzenta: ~38 HU)
                        if (headEl > 0.72) {
                            hu = 38.0; // Fita cortical insular e córtex cerebral
                        }

                        // Núcleos lentiformes e caudado
                        const lentL = Math.sqrt((dx - 22) * (dx - 22) + (dy + 5) * (dy + 5));
                        const lentR = Math.sqrt((dx + 22) * (dx + 22) + (dy + 5) * (dy + 5));
                        if (lentL < 12 || lentR < 12) hu = 39.0;

                        // Ventrículos Laterais (Líquor: ~5 HU)
                        const ventDist = Math.sqrt(dx * dx * 4.0 + dy * dy);
                        if (ventDist < 25 && Math.abs(dy) < 30) {
                            hu = 5.0; // CSF
                        }

                        // Edema Citotóxico / AVC Isquêmico no Córtex Insular Direito (dx > 0)
                        if (hasSignal && dx > 25 && dx < 55 && dy > -20 && dy < 25) {
                            hu -= ischemicDelta; // Apagamento da fita insular (de 38 HU para 34 HU)
                        }
                    }
                }

                // Textura anatômica cerebral + ruído
                const anatomicalClutter = Math.sin(dx * 0.8) * Math.cos(dy * 0.8) * 1.5;
                const noise = (Math.random() + Math.random() + Math.random() - 1.5) * baseNoise * 1.732;
                slice[idx] = hu + anatomicalClutter + noise;
            }
        }
        return slice;
    }

    /**
     * Gera uma fatia de Osso Esponjoso Trabecular / Microfratura (Módulo DLR Não-Linear)
     */
    static createTrabecularBonePhantom(width, height, {
        dlrStrength = 0,    // 0: FBP, 50: DLR Medium, 100: DLR Ultra-High
        hasFracture = true,
        fractureGap_um = 180 // Micrômetros (fenda submilimétrica)
    } = {}) {
        const slice = new Float32Array(width * height);
        const cx = width / 2;
        const cy = height / 2;
        const scale = width / 60.0; // Alta resolução (60 mm FOV)

        const noiseLevel = dlrStrength > 0 ? 15.0 * (1.0 - dlrStrength * 0.007) : 35.0;

        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                const idx = y * width + x;
                const dx = (x - cx) / scale;
                const dy = (y - cy) / scale;
                const r = Math.sqrt(dx * dx + dy * dy);

                let hu = -100.0; // Gordura externa

                if (r < 25.0) {
                    if (r > 21.0) {
                        hu = 1200.0; // Cortical óssea
                    } else {
                        // Rede Trabecular de Alta Frequência
                        const grid1 = Math.sin(dx * 5.0) * Math.cos(dy * 5.0);
                        const grid2 = Math.sin(dx * 7.0 + dy * 7.0);
                        const trabecularPattern = (grid1 + grid2) > 0.4 ? 400.0 : -30.0; // Espícula mineralizada vs medula

                        hu = trabecularPattern;

                        // Se DLR alto estiver ativo, simula a fusão/obliteração plástica (efeito ceroso)
                        if (dlrStrength > 40) {
                            const blurWeight = (dlrStrength - 40) / 60.0;
                            hu = hu * (1.0 - blurWeight * 0.75) + 180.0 * (blurWeight * 0.75);
                        }

                        // Fenda de microfratura incompleta (largura submilimétrica)
                        if (hasFracture) {
                            const fractureLine = Math.abs(dx * 0.7 + dy * 0.7 - 2.0);
                            const gapMm = fractureGap_um / 1000.0;
                            if (fractureLine < gapMm && r < 18.0) {
                                hu = -40.0; // Fenda preenchida por sangue/gordura

                                // DLR excessivo preenche a fenda apagando a fratura
                                if (dlrStrength > 60) {
                                    hu = 220.0; // Fusão cerosa falsa
                                }
                            }
                        }
                    }
                }

                const noise = (Math.random() + Math.random() + Math.random() - 1.5) * noiseLevel * 1.732;
                slice[idx] = hu + noise;
            }
        }
        return slice;
    }

    /**
     * Gera uma fatia de Artéria Coronária com Placa Calcificada (Módulo PCCT & Pareto 3D)
     */
    static createCoronaryPCCTPhantom(width, height, {
        vmiEnergy_keV = 50,  // keV (40 a 140 keV)
        isPCCT = true,       // true: PCCT (sem blooming, 0.2 mm), false: EID (com blooming)
        iodineConc_mg = 12,  // mg/mL
        hasStenosis = true
    } = {}) {
        const slice = new Float32Array(width * height);
        const cx = width / 2;
        const cy = height / 2;
        const scale = width / 40.0; // 40 mm FOV ultra-zoom vascular

        // Atenuação mássica do iodo em função de VMI (borda K em 33.2 keV)
        const iodineAttenuation = Math.pow(60.0 / vmiEnergy_keV, 2.8) * 35.0 * iodineConc_mg;
        const lumenHU = 50.0 + iodineAttenuation;

        // Detector EID vs PCCT
        const noiseLevel = isPCCT ? 12.0 : 26.0;
        const bloomingRadius = isPCCT ? 0.2 : 1.4; // Alargamento da calcificação no EID

        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                const idx = y * width + x;
                const dx = (x - cx) / scale;
                const dy = (y - cy) / scale;
                const r = Math.sqrt(dx * dx + dy * dy);

                let hu = -80.0; // Gordura epicárdica

                // Miocárdio de fundo
                if (dx > 5.0) hu = 45.0;

                // Parede da artéria coronária (diâmetro ~ 3.5 mm => r ~ 1.75 mm)
                const lumenRadius = 1.75;
                if (r <= lumenRadius * 1.4) {
                    hu = 40.0; // Parede vascular

                    // Luz vascular com iodo contrastado
                    if (r <= lumenRadius) {
                        hu = lumenHU;
                    }

                    // Placa de ateroma calcificada na parede lateral
                    if (hasStenosis) {
                        const plaqueDist = Math.sqrt((dx - 1.0)*(dx - 1.0) + dy*dy);
                        if (plaqueDist <= 1.1 + bloomingRadius) {
                            const intensity = isPCCT ? 1000.0 : 1000.0 * Math.exp(-(plaqueDist - 0.8) / bloomingRadius);
                            hu = Math.max(hu, intensity);
                        }
                    }
                }

                const noise = (Math.random() + Math.random() + Math.random() - 1.5) * noiseLevel * 1.732;
                slice[idx] = hu + noise;
            }
        }
        return slice;
    }
}
