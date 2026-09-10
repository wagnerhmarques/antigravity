/**
 * Sim4_DLR_Nonlinear.js
 * Módulo 4: Ruptura Não-Linear sob Reconstrução por Aprendizado Profundo (DLR).
 * Conceitos: Efeito Ceroso (Plastic Look), Paradoxo do NPWE, Detrending Polinomial 2D e Observadores DLMO (Transformers).
 * Caso Clínico: Obliteração de Microfraturas Trabeculares Ósseas Submilimétricas (Escafoide / Colo Femoral).
 */

import { SimulatorBase } from '../core/SimulatorBase.js';
import { DicomSynthesizer } from '../core/DicomSynthesizer.js';

export class Sim4_DLR_Nonlinear extends SimulatorBase {
    constructor() {
        super({
            id: 'dlr_nonlinear',
            title: 'Não-Linearidade em DLR & Efeito Ceroso (Plastic Look)',
            badge: 'Módulo 4',
            clinicalScenario: 'Microfraturas Ósseas Trabeculares (150 µm)',
            scenarioDesc: 'Avaliação do paradoxo em que a IA remove o ruído aparente mas oblitera microfraturas ósseas por supressão excessiva em altas frequências (f > 0.8 mm⁻¹).',
            equations: [
                '\\text{Paradoxo NPWE:} \\quad \\sigma_{\\text{HU}} \\downarrow \\implies d\'_{\\text{NPWE}} \\uparrow\\uparrow (\\text{Falso Ganho}), \\quad r_{\\text{humano}} \\downarrow 0.68',
                '\\text{DLMO (Vision Transformers):} \\quad \\text{Attention}(\\mathbf{Q}, \\mathbf{K}_v, \\mathbf{V}) = \\text{softmax}\\left(\\frac{\\mathbf{Q}\\mathbf{K}_v^T}{\\sqrt{d_k}}\\right)\\mathbf{V} \\implies r > 0.95',
                '\\text{Detrending 2D:} \\quad \\delta I(x, y) = I(x, y) - P_2(x, y), \\quad P_2(x,y) = a_0 + a_1 x + a_2 y + a_3 x^2 + \\dots'
            ],
            presets: {
                'fbp_classico': { label: 'FBP Convencional (Ruído Gaussiano Limpo)', params: { dlrLevel: 0, doseFraction: 100, fractureGap: 180, observerModel: 'humano' } },
                'dlr_medio': { label: 'DLR Nível Médio (Equilíbrio Clínico)', params: { dlrLevel: 50, doseFraction: 50, fractureGap: 180, observerModel: 'dlmo' } },
                'dlr_ultra_agressivo': { label: 'DLR Ultra-Agressivo (Efeito Ceroso Severo)', params: { dlrLevel: 95, doseFraction: 25, fractureGap: 180, observerModel: 'npwe' } },
                'fratura_oculta': { label: 'Fratura Incompleta Sutil (120 µm)', params: { dlrLevel: 80, doseFraction: 40, fractureGap: 120, observerModel: 'dlmo' } }
            }
        });
    }

    getParameters() {
        return {
            dlrLevel: {
                type: 'range', min: 0, max: 100, step: 5, default: 0,
                unit: '%', label: 'Força da Regularização por IA (DLR)',
                description: 'Aumenta a supressão não-linear de ruído e desloca o espectro NPS para baixas frequências (efeito plástico).'
            },
            doseFraction: {
                type: 'range', min: 15, max: 100, step: 5, default: 100,
                unit: '%', label: 'Dose Relativa (%)',
                description: 'Fração da dose padrão. Softwares de IA prometem reduzir a dose em até 70%.'
            },
            fractureGap: {
                type: 'range', min: 80, max: 300, step: 10, default: 180,
                unit: 'µm', label: 'Abertura da Microfratura (Fenda)',
                description: 'Dimensão física da linha de fratura no osso esponjoso trabecular.'
            },
            observerModel: {
                type: 'select',
                options: [
                    { value: 'humano', label: 'Radiologista Especialista (Leitura 2AFC)' },
                    { value: 'dlmo', label: 'DLMO (Vision Transformers com Auto-Atenção)' },
                    { value: 'npwe', label: 'NPWE Linear (Sofre o Paradoxo do Falso Ganho)' }
                ],
                default: 'humano',
                label: 'Avaliador de Desempenho',
                description: 'Demonstra a correlação real entre observadores humanos e matemáticos.'
            }
        };
    }

    getDefaultWindowLevel() {
        return { window: 2000, level: 400 }; // Janela óssea estrita de alta densidade
    }

    synthesizeSlice(width, height, params, mathEngine) {
        return DicomSynthesizer.createTrabecularBonePhantom(width, height, {
            dlrStrength: params.dlrLevel,
            hasFracture: params.hasSignal !== undefined ? params.hasSignal : true,
            fractureGap_um: params.fractureGap
        });
    }

    renderCharts(canvas1, canvas2, params, mathEngine) {
        const ctx1 = canvas1.getContext('2d');
        const ctx2 = canvas2.getContext('2d');
        const w1 = canvas1.width, h1 = canvas1.height;
        const w2 = canvas2.width, h2 = canvas2.height;

        ctx1.clearRect(0, 0, w1, h1);
        ctx2.clearRect(0, 0, w2, h2);

        // --- GRÁFICO 1: Deslocamento Textural do NPS(f) e Coincidência com Filtro Ocular E(f) ---
        this._renderWaxyLookSpectrum(ctx1, w1, h1, params.dlrLevel, mathEngine);

        // --- GRÁFICO 2: Dispersão e Correlação (Humano vs NPWE vs DLMO) ---
        this._renderCorrelationParadox(ctx2, w2, h2, params.dlrLevel, params.observerModel, mathEngine);
    }

    _renderWaxyLookSpectrum(ctx, w, h, dlrLevel, math) {
        const padX = 35, padY = 25;
        const plotW = w - 2 * padX, plotH = h - 2 * padY;
        const fMax = 1.0;

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

        // Faixa Crítica do Olho Humano (0.05 a 0.20 mm⁻¹) hachurada
        const xEyeMin = toScreenX(0.05);
        const xEyeMax = toScreenX(0.20);
        ctx.fillStyle = 'rgba(239, 68, 68, 0.12)';
        ctx.fillRect(xEyeMin, padY, xEyeMax - xEyeMin, plotH);

        // Curva Filtro Ocular E(f)
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let f = 0; f <= fMax; f += 0.01) {
            const e = math.eyeFilterBurgess(f, 50);
            const sx = toScreenX(f), sy = toScreenY(e * 1.6);
            if (f === 0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Curva NPS FBP Clássica (Preto/Cinza)
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        for (let f = 0; f <= fMax; f += 0.01) {
            const npsVal = math.nps(f, 0.45, 350) / 350.0;
            const sx = toScreenX(f), sy = toScreenY(npsVal);
            if (f === 0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();
        ctx.setLineDash([]);

        // Curva NPS DLR Atual (Deslocada para baixa frequência proporcional a dlrLevel)
        const peakDLR = 0.45 - (dlrLevel / 100.0) * 0.27; // cai de 0.45 para 0.18 mm⁻¹
        const ampDLR = 1.0 - (dlrLevel / 100.0) * 0.45;

        ctx.strokeStyle = '#a855f7';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let f = 0; f <= fMax; f += 0.01) {
            const npsVal = math.nps(f, peakDLR, 350) / 350.0 * ampDLR;
            const sx = toScreenX(f), sy = toScreenY(npsVal);
            if (f === 0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Rótulos
        ctx.fillStyle = '#a855f7';
        ctx.font = '10px Inter';
        ctx.fillText(`NPS DLR [Pico = ${peakDLR.toFixed(2)} mm⁻¹] (Textura Cerosa)`, padX + 10, padY + 15);
        ctx.fillStyle = '#10b981';
        ctx.fillText('Filtro Ocular E(f) de Burgess', padX + 10, padY + 30);
        ctx.fillStyle = '#ef4444';
        ctx.fillText('Faixa Crítica Hiper-Conspícua', xEyeMin - 10, padY + 50);
        ctx.fillStyle = '#94a3b8';
        ctx.fillText('Frequência Espacial f (mm⁻¹)', padX + plotW / 2 - 55, h - 6);
    }

    _renderCorrelationParadox(ctx, w, h, dlrLevel, observerModel, math) {
        const pad = 35;
        const plotW = w - 2 * pad, plotH = h - 2 * pad;

        const toScreenX = (x) => pad + (x / 4.5) * plotW;
        const toScreenY = (y) => (h - pad) - (y / 4.5) * plotH;

        // Linha de Concordância Ideal (y = x)
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.lineWidth = 1;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(toScreenX(0), toScreenY(0));
        ctx.lineTo(toScreenX(4.5), toScreenY(4.5));
        ctx.stroke();
        ctx.setLineDash([]);

        // Pontos de Dispersão Simulados para Radiologistas vs Modelo
        const numPoints = 15;
        for (let i = 0; i < numPoints; i++) {
            const humanD = 0.5 + (i / numPoints) * 3.5;
            
            // NPWE dispara artificialmente sob DLR alto
            const npweError = (dlrLevel / 100.0) * (Math.random() * 1.8 + 0.8);
            const npweD = humanD + npweError;

            // DLMO permanece ancorado em y = x
            const dlmoError = (Math.random() - 0.5) * 0.25;
            const dlmoD = humanD + dlmoError;

            // Plota ponto NPWE (Vermelho/Cruzes)
            const sxN = toScreenX(humanD), syN = toScreenY(npweD);
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(sxN - 3, syN - 3); ctx.lineTo(sxN + 3, syN + 3);
            ctx.moveTo(sxN + 3, syN - 3); ctx.lineTo(sxN - 3, syN + 3);
            ctx.stroke();

            // Plota ponto DLMO (Verde/Círculos)
            const sxD = toScreenX(humanD), syD = toScreenY(dlmoD);
            ctx.fillStyle = '#10b981';
            ctx.beginPath();
            ctx.arc(sxD, syD, 3.5, 0, 2 * Math.PI);
            ctx.fill();
        }

        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px Inter';
        ctx.fillText("d' Medido em Radiologistas (2AFC)", pad + plotW / 2 - 65, h - 8);
        ctx.save();
        ctx.translate(12, pad + plotH / 2 + 45);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText("d' do Modelo Computacional", 0, 0);
        ctx.restore();

        ctx.fillStyle = '#10b981';
        ctx.fillText('• DLMO Transformers (r = 0.98)', pad + 10, pad + 18);
        ctx.fillStyle = '#ef4444';
        ctx.fillText('✕ NPWE Linear (r = 0.68 - Paradoxo)', pad + 10, pad + 32);
    }

    getSummaryMetrics(params, mathEngine) {
        const isDLRActive = params.dlrLevel > 30;
        const fracturePreserved = params.dlrLevel <= 50;
        const fakeGain = (1.0 + (params.dlrLevel / 100.0) * 1.8).toFixed(1);

        return [
            { title: "Nível de IA (DLR)", value: `${params.dlrLevel}%`, subtitle: isDLRActive ? "Textura Não-Linear" : "Linear / FBP" },
            { title: "Microfratura", value: fracturePreserved ? "Preservada" : "Obliterada (Ceroso)", subtitle: `${params.fractureGap} µm` },
            { title: "Paradoxo NPWE", value: `+${((fakeGain - 1)*100).toFixed(0)}%`, subtitle: "Superestimação irreal" },
            { title: "Correlação Humana", value: params.observerModel === 'dlmo' ? "r = 0.98" : (params.observerModel === 'npwe' ? "r = 0.68" : "Ref. Ouro"), subtitle: "Fidelidade clínica" }
        ];
    }

    getEducationalExplanation(params) {
        return `
            <p><strong>Origem Espectral do Efeito Ceroso (*Plastic Look*):</strong> A rede neural DLR reduz o ruído deslocando a densidade espectral para frequências baixas ($f < 0.2\\text{ mm}^{-1}$). Esse pico coincide exatamente com a sensibilidade máxima do olho humano ($E(f)$), tornando o ruído residual altamente desconfortável.</p>
            <p><strong>O Paradoxo Metrológico do NPWE:</strong> Como o desvio padrão escalar diminui, a fórmula clássica do $d'_{\\text{NPWE}}$ dispara artificialmente, sugerindo um ganho que não existe para o radiologista humano diante de fraturas trabeculares finas.</p>
        `;
    }
}
