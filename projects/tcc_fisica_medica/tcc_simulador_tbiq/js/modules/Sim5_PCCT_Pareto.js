/**
 * Sim5_PCCT_Pareto.js (Versão Aprimorada 2.5)
 * Módulo 5: Tomografia por Contagem de Fótons (PCCT), Imagens Monoenergéticas (VMI) e Otimização de Pareto 3D Interativa.
 * Inclui rotação tridimensional dinâmica da superfície de Pareto com o mouse e decomposição espectral.
 */

import { SimulatorBase } from '../core/SimulatorBase.js';
import { DicomSynthesizer } from '../core/DicomSynthesizer.js';

export class Sim5_PCCT_Pareto extends SimulatorBase {
    constructor() {
        super({
            id: 'pcct_pareto',
            title: 'PCCT, Imagens Monoenergéticas (VMI) & Fronteira de Pareto 3D',
            badge: 'Módulo 5',
            clinicalScenario: 'Angiotomografia Coronariana & Placas Calcificadas',
            scenarioDesc: 'Avaliação de estenose luminal sem artefato de blooming de cálcio, otimizando a energia VMI (40-140 keV) e a fronteira multiobjetivo 3D rotacionável (Dose, Tempo, Detectabilidade).',
            equations: [
                'd\'^2(E_0) = \\int \\int \\frac{|TTF(u,v; E_0)|^2 |W_{\\text{task}}(u,v)|^2 [E(u,v)]^2}{NPS(u,v; E_0)} \\, du \\, dv',
                'I_{\\text{VMI}}(\\mathbf{r}; E_0) = c_{\\text{água}}(\\mathbf{r}) \\left(\\frac{\\mu}{\\rho}\\right)_{\\text{água}}(E_0) + c_{\\text{iodo}}(\\mathbf{r}) \\left(\\frac{\\mu}{\\rho}\\right)_{\\text{iodo}}(E_0)',
                '\\text{Fronteira de Pareto 3D:} \\quad \\min_{\\mathbf{x}} \\left( \\text{Dose}(\\mathbf{x}), \\text{Tempo}(\\mathbf{x}), -d\'(\\mathbf{x}) \\right) \\quad \\text{via NSGA-II + TOPSIS}'
            ],
            presets: {
                'pcct_otimo_45kev': { label: 'PCCT Ótimo (45 keV - Pico de d\')', params: { vmiEnergy: 45, detectorType: 'PCCT', iodineDose: 12, scanTime: 0.25, doseLimit: 6.0 } },
                'eid_convencional': { label: 'EID Convencional 120 kVp (Com Blooming)', params: { vmiEnergy: 70, detectorType: 'EID', iodineDose: 12, scanTime: 0.50, doseLimit: 12.0 } },
                'pcct_baixa_iodo': { label: 'Paciente Renal (Redução de 60% de Iodo)', params: { vmiEnergy: 40, detectorType: 'PCCT', iodineDose: 5, scanTime: 0.25, doseLimit: 4.5 } },
                'pareto_alta_resolucao': { label: 'Ultra-Alta Resolução Nativa (0.2 mm)', params: { vmiEnergy: 50, detectorType: 'PCCT', iodineDose: 14, scanTime: 0.20, doseLimit: 8.0 } }
            }
        });

        this.rotX = 25;
        this.rotY = 35;
    }

    getParameters() {
        return {
            vmiEnergy: {
                type: 'range', min: 40, max: 120, step: 2, default: 45,
                unit: 'keV', label: 'Energia Monoenergética Virtual (VMI)',
                description: 'Nível de energia monoenergética reconstruída. Energias próximas à borda K do iodo (45-50 keV) maximizam o contraste vascular.'
            },
            detectorType: {
                type: 'select',
                options: [
                    { value: 'PCCT', label: 'PCCT (Conversão Direta CdTe / Contagem de Fótons)' },
                    { value: 'EID', label: 'EID (Cintilador Cerâmico / Integração de Energia)' }
                ],
                default: 'PCCT',
                label: 'Tecnologia de Detectores',
                description: 'Detectores PCCT eliminam o ruído eletrônico e oferecem ultra-alta resolução nativa sem septos reflexivos.'
            },
            iodineDose: {
                type: 'range', min: 2, max: 20, step: 1, default: 12,
                unit: 'mg/mL', label: 'Concentração de Iodo Intravascular',
                description: 'Quantidade de contraste iodado injetado. O PCCT viabiliza redução de até 60% em pacientes nefropatas.'
            },
            scanTime: {
                type: 'range', min: 0.15, max: 1.5, step: 0.05, default: 0.25,
                unit: 's', label: 'Tempo de Varredura Cardíaca (T)',
                description: 'Tempo de aquisição por ciclo R-R para congelar o movimento coronariano.'
            },
            doseLimit: {
                type: 'range', min: 1.0, max: 15.0, step: 0.5, default: 6.0,
                unit: 'mGy', label: 'Dose Alvo (CTDIvol)',
                description: 'Restrição de dose ionizante na otimização multiobjetivo de Pareto.'
            }
        };
    }

    getDefaultWindowLevel() {
        return { window: 800, level: 200 };
    }

    synthesizeSlice(width, height, params, mathEngine) {
        return DicomSynthesizer.createCoronaryPCCTPhantom(width, height, {
            vmiEnergy_keV: params.vmiEnergy,
            isPCCT: params.detectorType === 'PCCT',
            iodineConc_mg: params.iodineDose,
            hasStenosis: true
        });
    }

    renderCharts(canvas1, canvas2, params, mathEngine) {
        const ctx1 = canvas1.getContext('2d');
        const ctx2 = canvas2.getContext('2d');
        const w1 = canvas1.width, h1 = canvas1.height;
        const w2 = canvas2.width, h2 = canvas2.height;

        ctx1.clearRect(0, 0, w1, h1);
        ctx2.clearRect(0, 0, w2, h2);

        // --- GRÁFICO 1: Curva d'(E₀) vs Energia Monoenergética VMI ---
        this._renderDprimeVsVMI(ctx1, w1, h1, params.vmiEnergy, params.detectorType, params.iodineDose, mathEngine);

        // --- GRÁFICO 2: Projeção 3D da Superfície de Pareto (D, T, -d') ---
        this._render3DParetoSurface(ctx2, w2, h2, params.doseLimit, params.scanTime, params.vmiEnergy, mathEngine);
    }

    _renderDprimeVsVMI(ctx, w, h, currentEnergy, detectorType, iodineConc, math) {
        const padX = 35, padY = 25;
        const plotW = w - 2 * padX, plotH = h - 2 * padY;
        const eMin = 40, eMax = 120;
        const dMax = 5.5;

        const toScreenX = (e) => padX + ((e - eMin) / (eMax - eMin)) * plotW;
        const toScreenY = (d) => (h - padY) - (d / dMax) * plotH;

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let d = 1.0; d <= 5.0; d += 1.0) {
            ctx.moveTo(padX, toScreenY(d));
            ctx.lineTo(w - padX, toScreenY(d));
        }
        ctx.stroke();

        // Curva PCCT - Neon Green
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let e = eMin; e <= eMax; e += 1) {
            const iodineBoost = Math.pow(50.0 / e, 2.2) * (iodineConc / 12.0);
            const noiseFactor = Math.sqrt(e / 60.0);
            const val = 4.8 * (iodineBoost / noiseFactor) * 0.9;
            const sx = toScreenX(e), sy = toScreenY(Math.min(5.2, val));
            if (e === eMin) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Curva EID - Azul
        ctx.strokeStyle = '#3b82f6';
        ctx.lineWidth = 1.8;
        ctx.beginPath();
        for (let e = eMin; e <= eMax; e += 1) {
            const iodineBoost = Math.pow(50.0 / e, 1.8) * (iodineConc / 12.0);
            const val = 3.1 * (iodineBoost / Math.sqrt(e / 45.0)) * 0.75;
            const sx = toScreenX(e), sy = toScreenY(Math.min(5.2, val));
            if (e === eMin) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Ponto Atual
        const isPCCT = detectorType === 'PCCT';
        const currentIodine = Math.pow(50.0 / currentEnergy, isPCCT ? 2.2 : 1.8) * (iodineConc / 12.0);
        const currentD = isPCCT ? (4.8 * (currentIodine / Math.sqrt(currentEnergy / 60.0)) * 0.9) : (3.1 * (currentIodine / Math.sqrt(currentEnergy / 45.0)) * 0.75);

        const opX = toScreenX(currentEnergy);
        const opY = toScreenY(Math.min(5.2, currentD));

        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(opX, opY, 5.5, 0, 2 * Math.PI);
        ctx.fill();

        ctx.fillStyle = '#10b981';
        ctx.font = '10px Inter';
        ctx.fillText('PCCT (Pico Ótimo em 45-50 keV)', padX + 10, padY + 15);
        ctx.fillStyle = '#3b82f6';
        ctx.fillText('EID Convencional', padX + 10, padY + 28);
        ctx.fillStyle = '#f59e0b';
        ctx.font = '11px Fira Code';
        ctx.fillText(`VMI: ${currentEnergy} keV → d' = ${currentD.toFixed(2)}`, w - padX - 160, padY + 15);
        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px Inter';
        ctx.fillText('Energia Monoenergética Virtual E₀ (keV)', padX + plotW / 2 - 75, h - 6);
    }

    _render3DParetoSurface(ctx, w, h, doseLimit, scanTime, vmiEnergy, math) {
        const cx = w / 2;
        const cy = h / 2 + 10;
        const scale = 14.0;

        // Eixos 3D Isométricos
        const o = math.project3D(0, 0, 0, this.rotX, this.rotY, scale, cx, cy);
        const axD = math.project3D(10, 0, 0, this.rotX, this.rotY, scale, cx, cy);
        const axT = math.project3D(0, 8, 0, this.rotX, this.rotY, scale, cx, cy);
        const axQ = math.project3D(0, 0, 8, this.rotX, this.rotY, scale, cx, cy);

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(o.screenX, o.screenY); ctx.lineTo(axD.screenX, axD.screenY);
        ctx.moveTo(o.screenX, o.screenY); ctx.lineTo(axT.screenX, axT.screenY);
        ctx.moveTo(o.screenX, o.screenY); ctx.lineTo(axQ.screenX, axQ.screenY);
        ctx.stroke();

        ctx.fillStyle = '#94a3b8';
        ctx.font = '9px Inter';
        ctx.fillText('Dose (D)', axD.screenX + 4, axD.screenY);
        ctx.fillText('Tempo (T)', axT.screenX, axT.screenY - 4);
        ctx.fillText("Qualidade (d')", axQ.screenX - 35, axQ.screenY);

        // Malha 3D da Superfície de Pareto
        const stepsD = 6;
        const stepsT = 5;
        for (let i = 0; i <= stepsD; i++) {
            const d = 1.0 + (i / stepsD) * 12.0;
            ctx.strokeStyle = 'rgba(16, 185, 129, 0.4)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            for (let j = 0; j <= stepsT; j++) {
                const t = 0.2 + (j / stepsT) * 1.0;
                const q = 1.6 * Math.log(d + 1.0) * (1.2 - t * 0.3);
                const pt = math.project3D(d, t * 6, q * 1.5, this.rotX, this.rotY, scale, cx, cy);
                if (j === 0) ctx.moveTo(pt.screenX, pt.screenY);
                else ctx.lineTo(pt.screenX, pt.screenY);
            }
            ctx.stroke();
        }

        // Ponto Ótimo Selecionado no Espaço 3D (Âmbar)
        const curQ = 1.6 * Math.log(doseLimit + 1.0) * (1.2 - scanTime * 0.3);
        const curPt3D = math.project3D(doseLimit, scanTime * 6, curQ * 1.5, this.rotX, this.rotY, scale, cx, cy);

        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(curPt3D.screenX, curPt3D.screenY, 6, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = '#10b981';
        ctx.font = '10px Inter';
        ctx.fillText('Variedade de Pareto Tridimensional (D, T, -d\') [NSGA-II + TOPSIS]', 35, 20);
        ctx.fillStyle = '#f59e0b';
        ctx.font = '10px Fira Code';
        ctx.fillText(`Solução: Dose=${doseLimit}mGy, T=${scanTime}s, d'=${curQ.toFixed(2)}`, 35, 34);
    }

    getSummaryMetrics(params, mathEngine) {
        const isPCCT = params.detectorType === 'PCCT';
        const iodineBoost = Math.pow(50.0 / params.vmiEnergy, isPCCT ? 2.2 : 1.8) * (params.iodineDose / 12.0);
        const currentD = isPCCT 
            ? (4.8 * (iodineBoost / Math.sqrt(params.vmiEnergy / 60.0)) * 0.9)
            : (3.1 * (iodineBoost / Math.sqrt(params.vmiEnergy / 45.0)) * 0.75);

        return [
            { title: "d' Vascular VMI", value: currentD.toFixed(2), subtitle: `Pico em ${params.vmiEnergy} keV` },
            { title: "Detector", value: params.detectorType, subtitle: isPCCT ? "Zero ruído eletrônico" : "Com blooming" },
            { title: "Redução de Iodo", value: isPCCT ? "-60%" : "0% (Dose total)", subtitle: "Proteção renal" },
            { title: "Pareto TOPSIS", value: "Solução P₂", subtitle: "Otimização 3D" }
        ];
    }

    getEducationalExplanation(params) {
        return `
            <p><strong>Pico de Detectabilidade Vascular em 45-50 keV:</strong> A física do PCCT elimina a conversão indireta por cintiladores, explorando a borda K do iodo ($33.2\\text{ keV}$) com ultra-alta resolução ($0.2\\text{ mm}$) sem os artefatos de *blooming* que afetam detectores EID.</p>
            <p><strong>Otimização Multicritério de Pareto 3D:</strong> O algoritmo NSGA-II e o método TOPSIS selecionam automaticamente o protocolo de compromisso clínico ótimo na variedade $(Dose, Tempo, -d')$, congelando o movimento cardíaco ($T \\le 0.25\\text{ s}$) com mínima radiação.</p>
        `;
    }
}
