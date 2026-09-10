/**
 * Sim3_LinearObservers.js
 * Módulo 3: Observadores de Modelo Lineares e Canais Corticais da Área Visual V1.
 * Conceitos: Observador Ideal de Hotelling (HO), NPWE, e CHO com canais D-DOG, Laguerre-Gauss e Gabor 2D.
 * Caso Clínico: AVC Isquêmico Hiperagudo (< 4.5h), Escore ASPECTS e Apagamento do Córtex Insular (ΔC = 3-5 HU).
 */

import { SimulatorBase } from '../core/SimulatorBase.js';
import { DicomSynthesizer } from '../core/DicomSynthesizer.js';

export class Sim3_LinearObservers extends SimulatorBase {
    constructor() {
        super({
            id: 'linear_observers',
            title: 'Observadores de Modelo & Canais Corticais V1 (CHO / NPWE)',
            badge: 'Módulo 3',
            clinicalScenario: 'AVC Isquêmico Hiperagudo (< 4.5h) e Escore ASPECTS',
            scenarioDesc: 'Detecção de edema citotóxico sutil (perda de 3 a 5 HU) e apagamento da fita insular em fundo anatômico cerebral altamente estruturado (1/f^β).',
            equations: [
                'd\'_{\\text{HO}} = \\sqrt{\\mathbf{s}^T \\mathbf{K}^{-1} \\mathbf{s}} \\quad (\\text{Teto Bayesiano Físico})',
                'd\'_{\\text{CHO}} = \\sqrt{\\langle \\mathbf{v}_s \\rangle^T \\mathbf{K}_v^{-1} \\langle \\mathbf{v}_s \\rangle}, \\quad \\mathbf{v} = \\mathbf{T}\\mathbf{g}',
                'C_j(f) = \\exp\\left(-\\frac{f^2}{2\\sigma_{j,1}^2}\\right) - \\exp\\left(-\\frac{f^2}{2\\sigma_{j,2}^2}\\right) \\quad (\\text{Canais D-DOG})'
            ],
            presets: {
                'avc_hiperagudo': { label: 'AVC Hiperagudo (ΔC = 4 HU - Isquemia M1)', params: { dose: 40.0, deltaC: 4.0, observerType: 'CHO', channelType: 'ddog', betaPower: 2.5 } },
                'avc_trombose_extensa': { label: 'Infarto Consolidado (ΔC = 10 HU)', params: { dose: 40.0, deltaC: 10.0, observerType: 'CHO', channelType: 'ddog', betaPower: 2.5 } },
                'fundo_homogeneo_agua': { label: 'Fantoma de Água Puro (Sem Fundo Anatômico)', params: { dose: 35.0, deltaC: 5.0, observerType: 'NPWE', channelType: 'ddog', betaPower: 0.0 } },
                'limite_hotelling': { label: 'Teto Teórico Ideal de Hotelling (HO)', params: { dose: 50.0, deltaC: 4.0, observerType: 'HO', channelType: 'ddog', betaPower: 2.5 } }
            }
        });
    }

    getParameters() {
        return {
            dose: {
                type: 'range', min: 10.0, max: 80.0, step: 2.0, default: 40.0,
                unit: 'mGy', label: 'Dose Crânio (CTDIvol)',
                description: 'Dose típica de protocolo encefálico de emergência.'
            },
            deltaC: {
                type: 'range', min: 1.0, max: 15.0, step: 0.5, default: 4.0,
                unit: 'HU', label: 'Edema Isquêmico (ΔC)',
                description: 'Diferença de atenuação causada pelo influxo de água citotóxica no parênquima cerebral.'
            },
            observerType: {
                type: 'select',
                options: [
                    { value: 'CHO', label: 'CHO (Observador de Hotelling Canalizado)' },
                    { value: 'NPWE', label: 'NPWE (Modelo Antropomórfico Clássico)' },
                    { value: 'HO', label: 'Observador Ideal de Hotelling (Teto Físico)' }
                ],
                default: 'CHO',
                label: 'Modelo de Observador',
                description: 'Define se a tomada de decisão utiliza canais corticais, integração ocular direta ou teto Bayesiano.'
            },
            channelType: {
                type: 'select',
                options: [
                    { value: 'ddog', label: 'D-DOG (5 Canais Diferença de Gaussianas)' },
                    { value: 'laguerre', label: 'Laguerre-Gauss (Ordens 0 a 3)' },
                    { value: 'gabor', label: 'Gabor 2D (Orientação Angular θ = 45°)' }
                ],
                default: 'ddog',
                label: 'Família de Canais Corticais V1',
                description: 'Mapeamento nos campos receptivos do córtex visual primário humano.'
            },
            betaPower: {
                type: 'range', min: 0.0, max: 3.5, step: 0.25, default: 2.5,
                unit: '', label: 'Ruído Anatômico Estruturado (β)',
                description: 'Expoente da lei de potência 1/f^β da textura cerebral (β=0: água pura; β=2.5: parênquima cerebral real).'
            }
        };
    }

    getDefaultWindowLevel() {
        return { window: 40, level: 40 }; // Janela estreita crítica para AVC (Stroke Window)
    }

    synthesizeSlice(width, height, params, mathEngine) {
        return DicomSynthesizer.createBrainPhantom(width, height, {
            dose: params.dose,
            ischemicDelta: params.deltaC,
            hasSignal: params.hasSignal !== undefined ? params.hasSignal : true,
            useCHO: params.observerType === 'CHO',
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

        // --- GRÁFICO 1: Perfis dos Canais Corticais V1 Selecionados ---
        this._renderCorticalChannels(ctx1, w1, h1, params.channelType, mathEngine);

        // --- GRÁFICO 2: Comparativo d' vs Dose sob Fundo Anatômico Estruturado ---
        this._renderDprimeComparison(ctx2, w2, h2, params, mathEngine);
    }

    _renderCorticalChannels(ctx, w, h, channelType, math) {
        const padX = 35, padY = 25;
        const plotW = w - 2 * padX, plotH = h - 2 * padY;

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let y = 0.2; y <= 1.0; y += 0.2) {
            ctx.moveTo(padX, (h - padY) - y * plotH);
            ctx.lineTo(w - padX, (h - padY) - y * plotH);
        }
        ctx.stroke();

        const colors = ['#00f0ff', '#10b981', '#f59e0b', '#a855f7', '#ef4444'];

        if (channelType === 'ddog') {
            // 5 Canais D-DOG
            const fMax = 1.0;
            const toScreenX = (f) => padX + (f / fMax) * plotW;
            const toScreenY = (normY) => (h - padY) - normY * plotH;

            const sigmas = [
                { s1: 0.08, s2: 0.16 },
                { s1: 0.14, s2: 0.28 },
                { s1: 0.25, s2: 0.50 },
                { s1: 0.40, s2: 0.80 },
                { s1: 0.65, s2: 1.30 }
            ];

            sigmas.forEach((sig, idx) => {
                ctx.strokeStyle = colors[idx];
                ctx.lineWidth = 2.0;
                ctx.beginPath();
                for (let f = 0; f <= fMax; f += 0.01) {
                    const val = math.dDogChannel(f, sig.s1, sig.s2);
                    const sx = toScreenX(f), sy = toScreenY(val * 1.5);
                    if (f === 0) ctx.moveTo(sx, sy);
                    else ctx.lineTo(sx, sy);
                }
                ctx.stroke();
            });

            ctx.fillStyle = '#00f0ff';
            ctx.font = '10px Inter';
            ctx.fillText('5 Canais Passa-Faixa D-DOG Corticais (0.1 a 0.85 mm⁻¹)', padX + 10, padY + 15);
            ctx.fillStyle = '#94a3b8';
            ctx.fillText('Frequência Espacial f (mm⁻¹)', padX + plotW / 2 - 55, h - 6);

        } else if (channelType === 'laguerre') {
            // Laguerre-Gauss 0 a 3
            const rMax = 10.0;
            const toScreenX = (r) => padX + (r / rMax) * plotW;
            const toScreenY = (normY) => (h - padY) - ((normY + 0.4) / 1.4) * plotH;

            [0, 1, 2, 3].forEach((order, idx) => {
                ctx.strokeStyle = colors[idx];
                ctx.lineWidth = 2.0;
                ctx.beginPath();
                for (let r = 0; r <= rMax; r += 0.1) {
                    const val = math.laguerreGauss(r, order, 4.0);
                    const sx = toScreenX(r), sy = toScreenY(val);
                    if (r === 0) ctx.moveTo(sx, sy);
                    else ctx.lineTo(sx, sy);
                }
                ctx.stroke();
            });

            ctx.fillStyle = '#10b981';
            ctx.font = '10px Inter';
            ctx.fillText('Funções Radiais Ortogonais de Laguerre-Gauss (Ordens 0 a 3)', padX + 10, padY + 15);
            ctx.fillStyle = '#94a3b8';
            ctx.fillText('Raio Espacial Radial r (mm)', padX + plotW / 2 - 50, h - 6);

        } else {
            // Gabor 2D
            const xMax = 8.0;
            const toScreenX = (x) => padX + ((x + xMax) / (2 * xMax)) * plotW;
            const toScreenY = (normY) => (h - padY) - ((normY + 1.0) / 2.0) * plotH;

            ctx.strokeStyle = '#f59e0b';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            for (let x = -xMax; x <= xMax; x += 0.1) {
                const val = Math.exp(-(x * x) / (2 * 3.5 * 3.5)) * Math.cos((2 * Math.PI * x) / 5.0);
                const sx = toScreenX(x), sy = toScreenY(val);
                if (x === -xMax) ctx.moveTo(sx, sy);
                else ctx.lineTo(sx, sy);
            }
            ctx.stroke();

            ctx.fillStyle = '#f59e0b';
            ctx.font = '10px Inter';
            ctx.fillText('Campo Receptivo Cortical Orientado de Gabor 2D (θ = 45°)', padX + 10, padY + 15);
        }
    }

    _renderDprimeComparison(ctx, w, h, params, math) {
        const padX = 35, padY = 25;
        const plotW = w - 2 * padX, plotH = h - 2 * padY;
        const doseMax = 80.0;
        const dMax = 4.5;

        const toScreenX = (dose) => padX + (dose / doseMax) * plotW;
        const toScreenY = (d) => (h - padY) - (d / dMax) * plotH;

        // Limiar de Decisão Clínica ASPECTS d' ≥ 2.0
        const sy2 = toScreenY(2.0);
        ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(padX, sy2);
        ctx.lineTo(w - padX, sy2);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#ef4444';
        ctx.font = '9px Inter';
        ctx.fillText('Limiar de Segurança Terapêutica (ASPECTS ≥ 6)', padX + 5, sy2 - 4);

        // Curva HO (Teto Ideal)
        ctx.strokeStyle = '#3b82f6';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let d = 5; d <= doseMax; d += 2) {
            const val = 0.55 * (params.deltaC / 4.0) * Math.sqrt(d);
            const sx = toScreenX(d), sy = toScreenY(val);
            if (d === 5) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Curva CHO (Descorrelaciona Fundo)
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let d = 5; d <= doseMax; d += 2) {
            const val = 0.35 * (params.deltaC / 4.0) * Math.sqrt(d) / (1.0 + params.betaPower * 0.1);
            const sx = toScreenX(d), sy = toScreenY(val);
            if (d === 5) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Curva NPWE (Falha e Subestima sob ruído 1/f^β)
        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let d = 5; d <= doseMax; d += 2) {
            const val = 0.35 * (params.deltaC / 4.0) * Math.sqrt(d) / (1.0 + params.betaPower * 0.85);
            const sx = toScreenX(d), sy = toScreenY(val);
            if (d === 5) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Ponto de Operação Atual
        let currentD = 0.35 * (params.deltaC / 4.0) * Math.sqrt(params.dose) / (1.0 + params.betaPower * 0.1);
        if (params.observerType === 'NPWE') {
            currentD = 0.35 * (params.deltaC / 4.0) * Math.sqrt(params.dose) / (1.0 + params.betaPower * 0.85);
        } else if (params.observerType === 'HO') {
            currentD = 0.55 * (params.deltaC / 4.0) * Math.sqrt(params.dose);
        }

        const opX = toScreenX(params.dose);
        const opY = toScreenY(currentD);
        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(opX, opY, 5, 0, 2 * Math.PI);
        ctx.fill();

        // Legenda
        ctx.fillStyle = '#3b82f6'; ctx.fillText('HO (Ideal)', padX + plotW - 90, padY + 15);
        ctx.fillStyle = '#10b981'; ctx.fillText('CHO D-DOG', padX + plotW - 90, padY + 28);
        ctx.fillStyle = '#ef4444'; ctx.fillText('NPWE (Colapso)', padX + plotW - 90, padY + 41);
        ctx.fillStyle = '#94a3b8'; ctx.fillText('Dose CTDIvol (mGy)', padX + plotW / 2 - 45, h - 6);
    }

    getSummaryMetrics(params, mathEngine) {
        let dPrime = 0.35 * (params.deltaC / 4.0) * Math.sqrt(params.dose) / (1.0 + params.betaPower * 0.1);
        if (params.observerType === 'NPWE') {
            dPrime = 0.35 * (params.deltaC / 4.0) * Math.sqrt(params.dose) / (1.0 + params.betaPower * 0.85);
        } else if (params.observerType === 'HO') {
            dPrime = 0.55 * (params.deltaC / 4.0) * Math.sqrt(params.dose);
        }

        const isSafeAspects = dPrime >= 2.0;

        return [
            { title: `d' (${params.observerType})`, value: dPrime.toFixed(2), subtitle: isSafeAspects ? "ASPECTS Confiável" : "Risco Falso Negativo" },
            { title: "Contraste Isquêmico", value: `${params.deltaC.toFixed(1)} HU`, subtitle: "Edema citotóxico" },
            { title: "Ruído Anatômico", value: `β = ${params.betaPower.toFixed(1)}`, subtitle: "Textura 1/f^β" },
            { title: "Validação Humana", value: params.observerType === 'CHO' ? "r > 0.92" : "r < 0.70", subtitle: "Correlação MRMC" }
        ];
    }

    getEducationalExplanation(params) {
        return `
            <p><strong>Por que o NPWE falha no Encéfalo:</strong> O modelo NPWE confunde as variações anatômicas normais do parênquima cerebral (ruído em lei de potência $1/f^\\beta$) com ruído quântico puro, subestimando severamente o $d'$.</p>
            <p><strong>Poder dos Canais Corticais (CHO):</strong> O CHO projeta a imagem nos campos receptivos da área visual V1 (D-DOG e Laguerre-Gauss), descorrelacionando a anatomia e atingindo correlação quase perfeita com radiologistas no escore ASPECTS para AVC isquêmico.</p>
        `;
    }
}
