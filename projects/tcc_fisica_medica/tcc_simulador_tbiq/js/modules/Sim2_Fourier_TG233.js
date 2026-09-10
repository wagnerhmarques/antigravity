/**
 * Sim2_Fourier_TG233.js
 * Módulo 2: Métricas no Domínio de Fourier segundo o Relatório AAPM TG-233.
 * Conceitos: Resolução TTF(f), Espectro de Potência do Ruído NPS(f), Filtro Ocular E(f) e Espectro da Tarefa Wtask(f).
 * Caso Clínico: Detecção de Metástases Hepáticas Hipoatenuantes (ΔC ≤ 25 HU) em TC de Abdome.
 */

import { SimulatorBase } from '../core/SimulatorBase.js';
import { DicomSynthesizer } from '../core/DicomSynthesizer.js';

export class Sim2_Fourier_TG233 extends SimulatorBase {
    constructor() {
        super({
            id: 'fourier_tg233',
            title: 'Métricas Espectrais em Fourier (AAPM TG-233)',
            badge: 'Módulo 2',
            clinicalScenario: 'Metástase Hepática Hipoatenuante (Fase Portal)',
            scenarioDesc: 'Avaliação de lesão oncológica hepática hipovascular (+85 HU) contra parênquima contrastado (+110 HU) com ΔC sutil de 25 HU.',
            equations: [
                'd\'^2 = \\int_0^\\infty \\frac{[TTF(f; \\Delta C)]^2 \\cdot [W_{\\text{task}}(f)]^2 \\cdot [E(f)]^2}{NPS(f)} \\, f \\, df',
                'TTF(f; \\Delta C) = \\left[ 1 + \\left(\\frac{f}{f_{50}(\\Delta C)}\\right)^\\alpha \\right]^{-1}',
                'NPS_{\\text{FBP}}(f) = \\frac{\\pi}{N_{\\text{proj}} \\bar{\\Phi}} \\cdot |f| \\cdot MTF^2(f)'
            ],
            presets: {
                'padrao_portal': { label: 'Fígado Portal (Dose Padrão)', params: { dose: 10.0, deltaC: 25.0, lesionRadius: 5.0, insertType: 'water', viewingDist: 50 } },
                'catphan_insert': { label: 'Fantoma Cilíndrico Catphan (Insertos)', params: { dose: 12.0, deltaC: 300.0, lesionRadius: 7.5, insertType: 'iodine', viewingDist: 50 } },
                'micro_metastase': { label: 'Micrometástase Sutil (Raio 2.5 mm)', params: { dose: 8.0, deltaC: 18.0, lesionRadius: 2.5, insertType: 'water', viewingDist: 50 } },
                'baixa_dose_abdome': { label: 'Abdome Baixa Dose (Ruído Alto)', params: { dose: 3.5, deltaC: 22.0, lesionRadius: 4.0, insertType: 'water', viewingDist: 60 } }
            }
        });
    }

    getParameters() {
        return {
            dose: {
                type: 'range', min: 1.0, max: 25.0, step: 0.5, default: 10.0,
                unit: 'mGy', label: 'Dose Absorvida (CTDIvol)',
                description: 'Impacta diretamente a densidade integrada do espectro de ruído NPS(f).'
            },
            deltaC: {
                type: 'range', min: 10.0, max: 100.0, step: 5.0, default: 25.0,
                unit: 'HU', label: 'Contraste da Metástase (ΔC)',
                description: 'Diferença de atenuação alvo-fundo. Alvos de baixo contraste degradam a frequência de corte f50 da TTF.'
            },
            lesionRadius: {
                type: 'range', min: 1.5, max: 12.0, step: 0.5, default: 5.0,
                unit: 'mm', label: 'Raio da Patologia (R)',
                description: 'Define a distribuição de frequências do espectro da tarefa Wtask(f) via Bessel J1.'
            },
            insertType: {
                type: 'select',
                options: [
                    { value: 'water', label: 'Parênquima Hepático / Água (+25 HU)' },
                    { value: 'iodine', label: 'Inserto de Iodo (+300 HU)' },
                    { value: 'teflon', label: 'Inserto de Teflon (+900 HU)' }
                ],
                default: 'water',
                label: 'Tipo de Inserto / Alvo',
                description: 'Define a frequência f50 e o decaimento da TTF(f).'
            },
            viewingDist: {
                type: 'range', min: 30, max: 100, step: 5, default: 50,
                unit: 'cm', label: 'Distância Olho-Monitor (d)',
                description: 'Converte frequências espaciais físicas (mm⁻¹) em ciclos por grau (cpd) na retina via E(f).'
            }
        };
    }

    getDefaultWindowLevel() {
        return { window: 400, level: 50 }; // Janela típica de Abdome / Fígado
    }

    synthesizeSlice(width, height, params, mathEngine) {
        const isCatphan = params.insertType !== 'water';
        return DicomSynthesizer.createLiverPhantom(width, height, {
            dose: params.dose,
            deltaC: params.deltaC,
            lesionRadius: params.lesionRadius,
            hasSignal: params.hasSignal !== undefined ? params.hasSignal : true,
            isCatphanMode: isCatphan,
            isDLR: false
        });
    }

    renderCharts(canvas1, canvas2, params, mathEngine) {
        const ctx1 = canvas1.getContext('2d');
        const ctx2 = canvas2.getContext('2d');
        const w1 = canvas1.width, h1 = canvas1.height;
        const w2 = canvas2.width, h2 = canvas2.height;

        ctx1.clearRect(0, 0, w1, h1);
        ctx2.clearRect(0, 0, w2, h2);

        // Parâmetros da TTF dependentes do contraste do inserto
        let f50 = 0.35;
        let alpha = 2.8;
        if (params.insertType === 'iodine') { f50 = 0.58; alpha = 3.2; }
        else if (params.insertType === 'teflon') { f50 = 0.52; alpha = 3.0; }

        // Parâmetros do NPS escalonados pela dose
        const npsAmp = (350.0 * 10.0) / Math.max(1.0, params.dose);
        const fpeak = 0.45;

        // Cálculo de d' contínuo de Fourier
        const dPrime = mathEngine.integrateDPrime({
            f50: f50,
            alpha: alpha,
            fpeak: fpeak,
            npsAmp: npsAmp,
            lesionRadius: params.lesionRadius,
            deltaC: params.deltaC,
            viewingDist: params.viewingDist,
            observerType: 'NPWE'
        });

        // --- GRÁFICO 1: TTF(f) e NPS(f) Normalizado ---
        this._renderTTF_NPS(ctx1, w1, h1, f50, alpha, fpeak, npsAmp, mathEngine);

        // --- GRÁFICO 2: Filtro Ocular E(f) e Espectro da Tarefa Wtask(f) ---
        this._renderEye_Task(ctx2, w2, h2, params.lesionRadius, params.deltaC, params.viewingDist, dPrime, mathEngine);
    }

    _renderTTF_NPS(ctx, w, h, f50, alpha, fpeak, npsAmp, math) {
        const padX = 35, padY = 25;
        const plotW = w - 2 * padX, plotH = h - 2 * padY;
        const fMax = 1.2;

        const toScreenX = (f) => padX + (f / fMax) * plotW;
        const toScreenY = (normY) => (h - padY) - normY * plotH;

        // Grid
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let y = 0.2; y <= 1.0; y += 0.2) {
            ctx.moveTo(padX, toScreenY(y));
            ctx.lineTo(w - padX, toScreenY(y));
        }
        ctx.stroke();

        // Linha f50 tracejada
        const sx50 = toScreenX(f50);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(sx50, toScreenY(0));
        ctx.lineTo(sx50, toScreenY(0.5));
        ctx.lineTo(padX, toScreenY(0.5));
        ctx.stroke();
        ctx.setLineDash([]);

        // Curva TTF(f) - Ciano
        ctx.strokeStyle = '#00f0ff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let f = 0; f <= fMax; f += 0.02) {
            const val = math.ttf(f, f50, alpha);
            const sx = toScreenX(f), sy = toScreenY(val);
            if (f === 0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Curva NPS(f) Normalizada - Âmbar
        const maxNPS = math.nps(fpeak, fpeak, npsAmp);
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2.0;
        ctx.beginPath();
        for (let f = 0; f <= fMax; f += 0.02) {
            const val = math.nps(f, fpeak, npsAmp) / maxNPS;
            const sx = toScreenX(f), sy = toScreenY(val);
            if (f === 0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Rótulos
        ctx.fillStyle = '#00f0ff';
        ctx.font = '10px Inter';
        ctx.fillText(`TTF(f) [f₅₀ = ${f50.toFixed(2)} mm⁻¹]`, padX + 10, padY + 15);
        ctx.fillStyle = '#f59e0b';
        ctx.fillText(`NPS(f) [Pico Rampa = ${fpeak.toFixed(2)} mm⁻¹]`, padX + 10, padY + 30);
        ctx.fillStyle = '#94a3b8';
        ctx.fillText('Frequência Espacial f (mm⁻¹)', padX + plotW / 2 - 55, h - 6);
    }

    _renderEye_Task(ctx, w, h, radius, deltaC, viewingDist, dPrime, math) {
        const padX = 35, padY = 25;
        const plotW = w - 2 * padX, plotH = h - 2 * padY;
        const fMax = 1.2;

        const toScreenX = (f) => padX + (f / fMax) * plotW;
        const toScreenY = (normY) => (h - padY) - normY * plotH;

        // Curva Filtro Ocular E(f) Normalizado - Verde
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2.0;
        ctx.beginPath();
        let maxE = 0;
        for (let f = 0; f <= fMax; f += 0.01) {
            const e = math.eyeFilterBurgess(f, viewingDist);
            if (e > maxE) maxE = e;
        }
        for (let f = 0; f <= fMax; f += 0.01) {
            const val = (math.eyeFilterBurgess(f, viewingDist) / (maxE || 1.0));
            const sx = toScreenX(f), sy = toScreenY(val);
            if (f === 0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Curva Espectro da Tarefa Wtask(f) Normalizado - Coral/Roxo
        ctx.strokeStyle = '#a855f7';
        ctx.lineWidth = 2.0;
        ctx.beginPath();
        const maxW = math.taskSpectrumSphere(0, radius, deltaC);
        for (let f = 0; f <= fMax; f += 0.01) {
            const val = math.taskSpectrumSphere(f, radius, deltaC) / (maxW || 1.0);
            const sx = toScreenX(f), sy = toScreenY(val);
            if (f === 0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Rótulos
        ctx.fillStyle = '#10b981';
        ctx.font = '10px Inter';
        ctx.fillText(`E(f) Burgess [Olho a ${viewingDist} cm]`, padX + 10, padY + 15);
        ctx.fillStyle = '#a855f7';
        ctx.fillText(`W_task(f) [Lesão R = ${radius.toFixed(1)} mm]`, padX + 10, padY + 30);
        ctx.fillStyle = '#00f0ff';
        ctx.font = '11px Fira Code';
        ctx.fillText(`d' Espectral = ${dPrime.toFixed(2)}`, w - padX - 140, padY + 15);
    }

    getSummaryMetrics(params, mathEngine) {
        let f50 = 0.35;
        let alpha = 2.8;
        if (params.insertType === 'iodine') { f50 = 0.58; alpha = 3.2; }
        else if (params.insertType === 'teflon') { f50 = 0.52; alpha = 3.0; }

        const npsAmp = (350.0 * 10.0) / Math.max(1.0, params.dose);
        const dPrime = mathEngine.integrateDPrime({
            f50: f50, alpha: alpha, fpeak: 0.45, npsAmp: npsAmp,
            lesionRadius: params.lesionRadius, deltaC: params.deltaC,
            viewingDist: params.viewingDist, observerType: 'NPWE'
        });

        const auc = mathEngine.normalCDF(dPrime / Math.SQRT2);

        return [
            { title: "d' Espectral TG-233", value: dPrime.toFixed(2), subtitle: dPrime >= 4.0 ? "Rose: Atingido" : "Incerteza" },
            { title: "Resolução f₅₀", value: `${f50.toFixed(2)} mm⁻¹`, subtitle: "Corte de 50%" },
            { title: "Área sob ROC (AUC)", value: auc.toFixed(3), subtitle: "Eficácia da tarefa" },
            { title: "Pico do Ruído (NPS)", value: "0.45 mm⁻¹", subtitle: "Rampa Jacobiana" }
        ];
    }

    getEducationalExplanation(params) {
        return `
            <p><strong>Quatro Pilares do Relatório AAPM TG-233:</strong> A qualidade de imagem não é um escalar, mas a integração das 4 funções no espaço de Fourier: $TTF(f)$ (resolução dependente de $\\Delta C$), $NPS(f)$ (textura do ruído), $E(f)$ (filtro ocular) e $W_{\\text{task}}(f)$ (espectro da lesão).</p>
            <p><strong>Risco Oncológico Hepático:</strong> Para alvos de baixo contraste ($\Delta C \\le 25\\text{ HU}$), a queda de $f_{50}$ degrada o $d'$, levando a falso-negativos em metástases hepáticas que passariam despercebidas por avaliações simplistas de SNR/CNR.</p>
        `;
    }
}
