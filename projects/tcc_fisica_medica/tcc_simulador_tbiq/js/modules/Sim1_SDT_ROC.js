/**
 * Sim1_SDT_ROC.js
 * Módulo 1: Teoria de Detecção de Sinais (SDT), Curvas ROC Paramétricas e Paradigma 2AFC.
 * Caso Clínico: Rastreamento Populacional de Câncer de Pulmão em TC de Baixa Dose (LDCT).
 */

import { SimulatorBase } from '../core/SimulatorBase.js';
import { DicomSynthesizer } from '../core/DicomSynthesizer.js';

export class Sim1_SDT_ROC extends SimulatorBase {
    constructor() {
        super({
            id: 'sdt_roc',
            title: 'Teoria de Detecção de Sinais (SDT) & Curvas ROC',
            badge: 'Módulo 1',
            clinicalScenario: 'Rastreamento de Nódulo Pulmonar em LDCT',
            scenarioDesc: 'Avaliação de nódulo subsólido em vidro fosco (-600 HU) sob parênquima pulmonar aerado (-800 HU) em protocolos de dose ultra-baixa.',
            equations: [
                'd\' = \\frac{\\langle t | H_1 \\rangle - \\langle t | H_0 \\rangle}{\\sigma_t} = \\frac{\\mu_1 - \\mu_0}{\\sigma_t}',
                'AUC = \\Phi\\left(\\frac{d\'}{\\sqrt{2}}\\right), \\quad P_C(2\\text{AFC}) = \\Phi\\left(\\frac{d\'}{\\sqrt{2}}\\right)',
                '\\text{Critério de Rose:} \\quad d\' \\ge 4.0 \\implies P_C \\ge 99.8\\%'
            ],
            presets: {
                'padrao': { label: 'Padrão (LDCT Clínico)', params: { dose: 2.5, lesionContrast: 200, threshold: 1.3, lesionRadius: 3.5 } },
                'ultra_baixa_dose': { label: 'Ultrabaixa Dose (Ruído Alto)', params: { dose: 0.8, lesionContrast: 150, threshold: 1.0, lesionRadius: 3.0 } },
                'alto_contraste': { label: 'Nódulo Sólido (Alto Contraste)', params: { dose: 3.5, lesionContrast: 400, threshold: 2.0, lesionRadius: 4.5 } },
                'certeza_rose': { label: 'Critério de Rose (d\' ≥ 4.0)', params: { dose: 8.0, lesionContrast: 350, threshold: 2.5, lesionRadius: 5.0 } }
            }
        });
    }

    getParameters() {
        return {
            dose: {
                type: 'range', min: 0.5, max: 10.0, step: 0.1, default: 2.5,
                unit: 'mGy', label: 'Dose (CTDIvol)',
                description: 'Escalona a fluência de fótons de raios X. A variância do ruído σ² ∝ 1/Dose na FBP.'
            },
            lesionContrast: {
                type: 'range', min: 50, max: 500, step: 10, default: 200,
                unit: 'HU', label: 'Contraste do Nódulo (ΔC)',
                description: 'Diferença de atenuação entre a lesão e o parênquima pulmonar sadio.'
            },
            lesionRadius: {
                type: 'range', min: 1.5, max: 8.0, step: 0.5, default: 3.5,
                unit: 'mm', label: 'Raio da Lesão (R)',
                description: 'Dimensão geométrica do nódulo.'
            },
            threshold: {
                type: 'range', min: -2.0, max: 5.0, step: 0.05, default: 1.3,
                unit: '', label: 'Limiar de Decisão do Médico (tc)',
                description: 'Postura decisória do radiologista: conservador (tc alto) vs intervencionista (tc baixo).'
            }
        };
    }

    getDefaultWindowLevel() {
        return { window: 1500, level: -600 }; // Janela típica de Pulmão
    }

    synthesizeSlice(width, height, params, mathEngine) {
        return DicomSynthesizer.createLungPhantom(width, height, {
            dose: params.dose,
            lesionContrast: params.lesionContrast,
            lesionRadius: params.lesionRadius,
            lesionType: 'ggn',
            hasSignal: params.hasSignal !== undefined ? params.hasSignal : true,
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

        // Cálculo de d' analítico escalonado pela física de SDT
        const sigma_t = 1.0;
        const mu0 = 0.0;
        const signalStrength = (params.lesionContrast / 200.0) * (params.lesionRadius / 3.5) * Math.sqrt(params.dose / 2.5);
        const mu1 = 2.2 * signalStrength;
        const dPrime = (mu1 - mu0) / sigma_t;
        const tc = params.threshold;

        // Probabilidades de Decisão
        const fpf = 1.0 - mathEngine.normalCDF((tc - mu0) / sigma_t);
        const tpf = 1.0 - mathEngine.normalCDF((tc - mu1) / sigma_t);
        const auc = mathEngine.normalCDF(dPrime / Math.SQRT2);

        // --- GRÁFICO 1: Distribuições de Probabilidade p(t|H0) e p(t|H1) ---
        this._renderDecisionDistributions(ctx1, w1, h1, mu0, mu1, sigma_t, tc, fpf, tpf, mathEngine);

        // --- GRÁFICO 2: Curva ROC Paramétrica & Ponto de Operação ---
        this._renderROCCurve(ctx2, w2, h2, dPrime, tc, fpf, tpf, auc, mathEngine);
    }

    _renderDecisionDistributions(ctx, w, h, mu0, mu1, sigma, tc, fpf, tpf, math) {
        const padX = 35, padY = 25;
        const plotW = w - 2 * padX, plotH = h - 2 * padY;

        const xMin = -3.5, xMax = Math.max(6.0, mu1 + 3.5);
        const yMax = 0.45;

        const toScreenX = (x) => padX + ((x - xMin) / (xMax - xMin)) * plotW;
        const toScreenY = (y) => (h - padY) - (y / yMax) * plotH;

        // Eixos e Grid
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let y = 0.1; y <= 0.4; y += 0.1) {
            const sy = toScreenY(y);
            ctx.moveTo(padX, sy);
            ctx.lineTo(w - padX, sy);
        }
        ctx.stroke();

        // Linha do Limiar tc
        const tcScreenX = toScreenX(tc);
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(tcScreenX, toScreenY(0));
        ctx.lineTo(tcScreenX, toScreenY(yMax));
        ctx.stroke();
        ctx.setLineDash([]);

        // Área FPF (sob H0 à direita de tc)
        ctx.fillStyle = 'rgba(0, 240, 255, 0.25)';
        ctx.beginPath();
        ctx.moveTo(tcScreenX, toScreenY(0));
        for (let x = tc; x <= xMax; x += 0.05) {
            const y = math.gaussianPDF(x, mu0, sigma);
            ctx.lineTo(toScreenX(x), toScreenY(y));
        }
        ctx.lineTo(toScreenX(xMax), toScreenY(0));
        ctx.closePath();
        ctx.fill();

        // Área TPF (sob H1 à direita de tc)
        ctx.fillStyle = 'rgba(16, 185, 129, 0.25)';
        ctx.beginPath();
        ctx.moveTo(tcScreenX, toScreenY(0));
        for (let x = tc; x <= xMax; x += 0.05) {
            const y = math.gaussianPDF(x, mu1, sigma);
            ctx.lineTo(toScreenX(x), toScreenY(y));
        }
        ctx.lineTo(toScreenX(xMax), toScreenY(0));
        ctx.closePath();
        ctx.fill();

        // Curva H0 (Ruído Puro - Azul)
        ctx.strokeStyle = '#00f0ff';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = xMin; x <= xMax; x += 0.05) {
            const y = math.gaussianPDF(x, mu0, sigma);
            const sx = toScreenX(x), sy = toScreenY(y);
            if (x === xMin) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Curva H1 (Sinal Presente - Verde)
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = xMin; x <= xMax; x += 0.05) {
            const y = math.gaussianPDF(x, mu1, sigma);
            const sx = toScreenX(x), sy = toScreenY(y);
            if (x === xMin) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Textos e Rótulos
        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px Inter';
        ctx.fillText('H0: Tecido Sadio (Ruído)', toScreenX(mu0) - 45, toScreenY(0.42));
        ctx.fillStyle = '#10b981';
        ctx.fillText('H1: Com Lesão', toScreenX(mu1) - 25, toScreenY(0.42));
        ctx.fillStyle = '#f59e0b';
        ctx.fillText(`Limiar tc = ${tc.toFixed(2)}`, tcScreenX + 4, toScreenY(0.35));
    }

    _renderROCCurve(ctx, w, h, dPrime, tc, fpf, tpf, auc, math) {
        const pad = 35;
        const plotW = w - 2 * pad, plotH = h - 2 * pad;

        const toScreenX = (x) => pad + x * plotW;
        const toScreenY = (y) => (h - pad) - y * plotH;

        // Diagonal da Sorte (AUC = 0.5)
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        ctx.lineWidth = 1;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(toScreenX(0), toScreenY(0));
        ctx.lineTo(toScreenX(1), toScreenY(1));
        ctx.stroke();
        ctx.setLineDash([]);

        // Curva ROC do d' atual
        ctx.strokeStyle = '#00f0ff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let t = -4.0; t <= 4.0; t += 0.05) {
            const f = 1.0 - math.normalCDF(t);
            const s = 1.0 - math.normalCDF(t - dPrime);
            const sx = toScreenX(f), sy = toScreenY(s);
            if (t === -4.0) ctx.moveTo(sx, sy);
            else ctx.lineTo(sx, sy);
        }
        ctx.stroke();

        // Ponto de Operação Atual (FPF, TPF)
        const opX = toScreenX(fpf);
        const opY = toScreenY(tpf);

        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(opX, opY, 5.5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // Rótulos do Gráfico ROC
        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px Inter';
        ctx.fillText('Taxa de Falso Alarme (FPF)', pad + plotW / 2 - 50, h - 8);
        ctx.save();
        ctx.translate(12, pad + plotH / 2 + 30);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Sensibilidade (TPF)', 0, 0);
        ctx.restore();

        ctx.fillStyle = '#00f0ff';
        ctx.font = '11px Fira Code';
        ctx.fillText(`AUC = ${auc.toFixed(3)} | d' = ${dPrime.toFixed(2)}`, pad + 10, pad + 20);
        ctx.fillStyle = '#f59e0b';
        ctx.fillText(`Ponto: Sensib=${(tpf*100).toFixed(1)}% | Falso-Pos=${(fpf*100).toFixed(1)}%`, pad + 10, pad + 36);
    }

    getSummaryMetrics(params, mathEngine) {
        const signalStrength = (params.lesionContrast / 200.0) * (params.lesionRadius / 3.5) * Math.sqrt(params.dose / 2.5);
        const dPrime = 2.2 * signalStrength;
        const auc = mathEngine.normalCDF(dPrime / Math.SQRT2);
        const pc = auc;
        const tc = params.threshold;
        const fpf = 1.0 - mathEngine.normalCDF(tc);
        const tpf = 1.0 - mathEngine.normalCDF(tc - dPrime);

        return [
            { title: "Índice d'", value: dPrime.toFixed(2), subtitle: dPrime >= 4.0 ? "Rose: Certeza" : "Incerteza" },
            { title: "Área sob ROC (AUC)", value: auc.toFixed(3), subtitle: "Separação total" },
            { title: "Sensibilidade (TPF)", value: `${(tpf * 100).toFixed(1)}%`, subtitle: "Detecção real" },
            { title: "Falsos Alarmes (FPF)", value: `${(fpf * 100).toFixed(1)}%`, subtitle: "Biópsias falso+" }
        ];
    }

    getEducationalExplanation(params) {
        return `
            <p><strong>Decisão sob Ruído Quântico:</strong> O Índice de Detectabilidade <em>d'</em> expressa a separação estatística entre tecido sadio (<em>H₀</em>) e patológico (<em>H₁</em>). Na FBP clássica, $d' \\propto \\sqrt{\\text{CTDI}_{\\text{vol}}}$.</p>
            <p><strong>Dilema Clínico do Limiar $t_c$:</strong> Ao deslocar $t_c$ para a direita (conservador), reduz-se o falso-positivo (${( (1.0 - mathEngine.normalCDF(params.threshold))*100 ).toFixed(1)}%), porém a sensibilidade colapsa, podendo omitir adenocarcinomas iniciais curáveis.</p>
        `;
    }
}
