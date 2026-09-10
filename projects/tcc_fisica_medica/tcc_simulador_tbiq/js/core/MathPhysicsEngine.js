/**
 * MathPhysicsEngine.js
 * Motor matemático e físico do TBIQ Studio.
 * Implementa as formulações analíticas fundamentais de óptica de Fourier, Teoria de Decisão (SDT),
 * observadores de modelo antropomórficos, filtros corticais, FFT 2D empírica e otimização de Pareto.
 */

export class MathPhysicsEngine {
    constructor() {
        this.TWO_PI = 2 * Math.PI;
    }

    /**
     * Função Densidade de Probabilidade Gaussiana Univariada
     */
    gaussianPDF(x, mean = 0, std = 1) {
        if (std <= 0) return 0;
        const diff = x - mean;
        return (1 / (std * Math.sqrt(this.TWO_PI))) * Math.exp(-0.5 * (diff * diff) / (std * std));
    }

    /**
     * Função de Erro Gaussiana (erf) aproximada
     */
    erf(x) {
        const a1 = 0.254829592;
        const a2 = -0.284496736;
        const a3 = 1.421413741;
        const a4 = -1.453152027;
        const a5 = 1.061405429;
        const p = 0.3275911;

        const sign = x >= 0 ? 1 : -1;
        const absX = Math.abs(x);
        const t = 1.0 / (1.0 + p * absX);
        const y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-absX * absX);
        return sign * y;
    }

    /**
     * Função de Distribuição Cumulativa Normal Padrão Φ(z)
     */
    normalCDF(z) {
        return 0.5 * (1.0 + this.erf(z / Math.SQRT2));
    }

    /**
     * Inversa da Função de Distribuição Cumulativa Normal Padrão Φ⁻¹(p) (Probit)
     */
    probit(p) {
        if (p <= 0) return -8.0;
        if (p >= 1) return 8.0;

        const a = [-3.969683028665376e+01,  2.209460984245205e+02, -2.759285104469687e+02,  1.383577518672690e+02, -3.066479806614716e+01,  2.506628277459239e+00];
        const b = [-5.447609879822406e+01,  1.615858368580409e+02, -1.556989798598866e+02,  6.680131188771972e+01, -1.328068155288572e+01];
        const c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00, -2.549732539343734e+00,  4.374664141464968e+00,  2.938163982698783e+00];
        const d = [ 7.784695709041462e-03,  3.224671290700398e-01,  2.445134137142996e+00,  3.754408661907416e+00];

        const q = p - 0.5;
        let r;
        if (Math.abs(q) <= 0.42) {
            r = q * q;
            return q * (((((a[0]*r + a[1])*r + a[2])*r + a[3])*r + a[4])*r + a[5]) /
                       (((((b[0]*r + b[1])*r + b[2])*r + b[3])*r + b[4])*r + 1.0);
        } else {
            r = p < 0.5 ? p : 1.0 - p;
            r = Math.log(-Math.log(r));
            let x = c[0] + r*(c[1] + r*(c[2] + r*(c[3] + r*(c[4] + r*c[5]))));
            let y = 1.0 + r*(d[0] + r*(d[1] + r*(d[2] + r*d[3])));
            let val = x / y;
            return p < 0.5 ? -val : val;
        }
    }

    /**
     * Função de Bessel de Primeira Espécie e Ordem 1: J₁(x)
     */
    besselJ1(x) {
        const ax = Math.abs(x);
        if (ax < 3.75) {
            const y = (x / 3.75) * (x / 3.75);
            return x * (0.5 + y * (-0.56249985 + y * (0.21093573 + y * (-0.03954289 + y * (0.00443319 - y * 0.00031761)))));
        } else {
            const y = 3.75 / ax;
            const f0 = 0.79788456 + y * (-0.00000077 + y * (-0.00552740 + y * (0.00009512 + y * (0.00137237 - y * 0.00072805))));
            const theta0 = ax - 2.35619449 + y * (0.044177 + y * (-0.00000003 + y * (-0.0007613 + y * (0.00000007 + y * 0.0000057))));
            const res = (1.0 / Math.sqrt(ax)) * f0 * Math.cos(theta0);
            return x < 0 ? -res : res;
        }
    }

    /**
     * Função de Transferência da Tarefa TTF(f; ΔC)
     */
    ttf(f, f50 = 0.45, alpha = 3.0) {
        if (f <= 0) return 1.0;
        const ratio = f / f50;
        return 1.0 / (1.0 + Math.pow(ratio, alpha));
    }

    /**
     * Espectro de Potência do Ruído NPS(f) para Tomografia
     */
    nps(f, fpeak = 0.45, amplitude = 350, shapePower = 2.5) {
        if (f <= 0) return 0.001;
        const normalizedF = f / fpeak;
        return amplitude * normalizedF * Math.exp(-0.5 * Math.pow(normalizedF, shapePower));
    }

    /**
     * Filtro Ocular Humano de Burgess E(f)
     */
    eyeFilterBurgess(f_mm, viewingDistance_cm = 50) {
        const viewingDistance_mm = viewingDistance_cm * 10;
        const mmToCpd = (viewingDistance_mm * Math.PI) / 180;
        const f_cpd = f_mm * mmToCpd;

        const f0 = 0.8;
        const n = 1.3;
        const m = 1.1;
        const c = 2.2;

        if (f_cpd <= 0) return 0.0;
        const ratio = f_cpd / f0;
        return Math.pow(ratio, n) * Math.exp(-c * Math.pow(ratio, m));
    }

    /**
     * Espectro da Tarefa Diagnóstica Wtask(f)
     */
    taskSpectrumSphere(f, radius_mm = 3.0, deltaC_HU = 35) {
        if (f <= 0.0001) {
            return Math.abs(deltaC_HU) * Math.PI * radius_mm * radius_mm;
        }
        const arg = this.TWO_PI * f * radius_mm;
        const j1 = this.besselJ1(arg);
        return Math.abs(deltaC_HU * this.TWO_PI * radius_mm * radius_mm * (j1 / arg));
    }

    /**
     * Canal Cortical D-DOG
     */
    dDogChannel(f, sigma1, sigma2) {
        const g1 = Math.exp(-(f * f) / (2 * sigma1 * sigma1));
        const g2 = Math.exp(-(f * f) / (2 * sigma2 * sigma2));
        return Math.max(0, g1 - g2);
    }

    /**
     * Polinômio de Laguerre-Gauss
     */
    laguerreGauss(r, n = 0, a = 4.0) {
        const x = (2 * Math.PI * r * r) / (a * a);
        let Ln = 1;
        if (n === 1) Ln = 1 - x;
        else if (n === 2) Ln = 1 - 2*x + 0.5*x*x;
        else if (n === 3) Ln = 1 - 3*x + 1.5*x*x - (x*x*x)/6.0;

        return Ln * Math.exp(-(Math.PI * r * r) / (a * a));
    }

    /**
     * Integração Espectral Contínua do Índice de Detectabilidade (d') segundo AAPM TG-233
     */
    integrateDPrime({
        f50 = 0.45,
        alpha = 3.0,
        fpeak = 0.45,
        npsAmp = 350,
        lesionRadius = 3.0,
        deltaC = 35,
        viewingDist = 50,
        observerType = 'NPWE',
        internalNoise = 0.05
    }) {
        const fMax = 2.0;
        const numSteps = 200;
        const df = fMax / numSteps;

        let numIntegral = 0;
        let denIntegral = 0;

        for (let i = 1; i <= numSteps; i++) {
            const f = i * df;
            const ttfVal = this.ttf(f, f50, alpha);
            const wVal = this.taskSpectrumSphere(f, lesionRadius, deltaC);
            const eVal = this.eyeFilterBurgess(f, viewingDist);
            const npsVal = Math.max(0.01, this.nps(f, fpeak, npsAmp));

            const ttfSq = ttfVal * ttfVal;
            const wSq = wVal * wVal;
            const eSq = eVal * eVal;
            const eQuad = eSq * eSq;

            if (observerType === 'HO') {
                numIntegral += ((ttfSq * wSq) / npsVal) * f * df;
            } else {
                numIntegral += ttfSq * wSq * eSq * f * df;
                denIntegral += ttfSq * wSq * eQuad * npsVal * f * df;
            }
        }

        if (observerType === 'HO') {
            return Math.sqrt(Math.max(0, this.TWO_PI * numIntegral));
        } else {
            const num = this.TWO_PI * numIntegral;
            const den = Math.sqrt(this.TWO_PI * denIntegral + internalNoise);
            return den > 0 ? num / den : 0;
        }
    }

    /**
     * Extração de NPS Empírico 2D com Detrending Polinomial a partir de uma Matriz de Pixels
     * @param {Float32Array} roiPixels - Array com pixels da ROI (N x N)
     * @param {number} size - Dimensão N (ex: 64)
     * @param {number} pixelSizeMm - Tamanho do pixel em mm (ex: 0.5 mm)
     * @returns {{radialFreqs: number[], radialNps: number[]}}
     */
    computeEmpiricalNPS(roiPixels, size = 64, pixelSizeMm = 0.5) {
        // 1. Detrending Subtraindo Plano Médio
        let sum = 0;
        for (let i = 0; i < roiPixels.length; i++) sum += roiPixels[i];
        const mean = sum / roiPixels.length;

        const detrended = new Float32Array(size * size);
        for (let i = 0; i < roiPixels.length; i++) {
            detrended[i] = roiPixels[i] - mean;
        }

        // 2. Janela de Hanning 2D
        const hanning2D = new Float32Array(size * size);
        for (let y = 0; y < size; y++) {
            const wy = 0.5 * (1.0 - Math.cos((this.TWO_PI * y) / (size - 1)));
            for (let x = 0; x < size; x++) {
                const wx = 0.5 * (1.0 - Math.cos((this.TWO_PI * x) / (size - 1)));
                hanning2D[y * size + x] = wx * wy;
            }
        }

        // 3. Transformada Discreta de Fourier 2D Simplificada e Rápida para Amostragem Radial
        const halfSize = Math.floor(size / 2);
        const df = 1.0 / (size * pixelSizeMm);
        const radialBins = new Float32Array(halfSize);
        const binCounts = new Float32Array(halfSize);

        for (let u = 0; u < halfSize; u++) {
            for (let v = 0; v < halfSize; v++) {
                const radiusBin = Math.min(halfSize - 1, Math.round(Math.sqrt(u * u + v * v)));
                
                // Magnitude espectral estimada
                let realSum = 0, imagSum = 0;
                // Amostragem esparsa rápida
                for (let y = 0; y < size; y += 2) {
                    for (let x = 0; x < size; x += 2) {
                        const val = detrended[y * size + x] * hanning2D[y * size + x];
                        const angle = this.TWO_PI * ((u * x) / size + (v * y) / size);
                        realSum += val * Math.cos(angle);
                        imagSum -= val * Math.sin(angle);
                    }
                }
                const power = (realSum * realSum + imagSum * imagSum) * (pixelSizeMm * pixelSizeMm) / (size * size);
                radialBins[radiusBin] += power;
                binCounts[radiusBin] += 1;
            }
        }

        const radialFreqs = [];
        const radialNps = [];
        for (let i = 1; i < halfSize; i++) {
            radialFreqs.push(i * df);
            radialNps.push(binCounts[i] > 0 ? radialBins[i] / binCounts[i] : 0);
        }

        return { radialFreqs, radialNps };
    }

    /**
     * Projeção Tridimensional Isométrica de Ponto 3D (Dose, Tempo, -d')
     */
    project3D(x, y, z, rotX = 25, rotY = 45, scale = 1.0, cx = 200, cy = 120) {
        const radX = (rotX * Math.PI) / 180;
        const radY = (rotY * Math.PI) / 180;

        // Rotação em Y
        const x1 = x * Math.cos(radY) + z * Math.sin(radY);
        const y1 = y;
        const z1 = -x * Math.sin(radY) + z * Math.cos(radY);

        // Rotação em X
        const x2 = x1;
        const y2 = y1 * Math.cos(radX) - z1 * Math.sin(radX);
        const z2 = y1 * Math.sin(radX) + z1 * Math.cos(radX);

        return {
            screenX: cx + x2 * scale,
            screenY: cy - y2 * scale,
            depth: z2
        };
    }
}

export const mathEngine = new MathPhysicsEngine();
