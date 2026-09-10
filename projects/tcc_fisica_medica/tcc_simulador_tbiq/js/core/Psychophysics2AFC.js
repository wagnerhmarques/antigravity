/**
 * Psychophysics2AFC.js
 * Módulo de Experimento Psicofísico de Escolha Forçada entre Duas Alternativas (2AFC).
 * Permite ao aluno atuar como observador humano, comparando sua taxa de acerto real e d' observado
 * com o d' teórico do modelo computacional.
 */

import { mathEngine } from './MathPhysicsEngine.js';

export class Psychophysics2AFC {
    constructor({ onFinish } = {}) {
        this.overlay = document.getElementById('challenge-overlay');
        this.canvasLeft = document.getElementById('canvas-2afc-left');
        this.canvasRight = document.getElementById('canvas-2afc-right');
        this.boxLeft = document.getElementById('choice-left');
        this.boxRight = document.getElementById('choice-right');
        
        this.ctxLeft = this.canvasLeft ? this.canvasLeft.getContext('2d') : null;
        this.ctxRight = this.canvasRight ? this.canvasRight.getContext('2d') : null;

        this.trialCounterEl = document.getElementById('challenge-trial-counter');
        this.scoreCorrectEl = document.getElementById('score-correct');
        this.scoreTotalEl = document.getElementById('score-total');
        this.scorePctEl = document.getElementById('score-pct');
        this.scoreDprimeEl = document.getElementById('score-dprime');
        this.btnExit = document.getElementById('btn-exit-2afc');

        this.currentSimulator = null;
        this.currentParams = null;
        this.onFinish = onFinish;

        this.totalTrials = 10;
        this.currentTrial = 0;
        this.correctCount = 0;
        this.signalLocation = 'left'; // 'left' ou 'right'

        this._setupEvents();
    }

    _setupEvents() {
        if (this.boxLeft) {
            this.boxLeft.addEventListener('click', () => this.handleChoice('left'));
        }
        if (this.boxRight) {
            this.boxRight.addEventListener('click', () => this.handleChoice('right'));
        }
        if (this.btnExit) {
            this.btnExit.addEventListener('click', () => this.stop());
        }
    }

    start(simulator, params) {
        this.currentSimulator = simulator;
        this.currentParams = { ...params };
        this.currentTrial = 0;
        this.correctCount = 0;
        this.overlay.classList.remove('hidden');
        this.nextTrial();
    }

    stop() {
        this.overlay.classList.add('hidden');
        if (this.onFinish) this.onFinish();
    }

    nextTrial() {
        if (this.currentTrial >= this.totalTrials) {
            this.showFinalSummary();
            return;
        }

        this.currentTrial++;
        this.trialCounterEl.textContent = `Tentativa ${this.currentTrial} de ${this.totalTrials}`;
        
        // Sorteia aleatoriamente se o sinal (H1) estará à esquerda ou à direita
        this.signalLocation = Math.random() < 0.5 ? 'left' : 'right';

        // Gera as duas imagens 180x180
        const patchW = 180;
        const patchH = 180;

        const paramsH0 = { ...this.currentParams, hasSignal: false };
        const paramsH1 = { ...this.currentParams, hasSignal: true };

        const sliceLeft = this.signalLocation === 'left' 
            ? this.currentSimulator.synthesizeSlice(patchW, patchH, paramsH1, mathEngine)
            : this.currentSimulator.synthesizeSlice(patchW, patchH, paramsH0, mathEngine);

        const sliceRight = this.signalLocation === 'right'
            ? this.currentSimulator.synthesizeSlice(patchW, patchH, paramsH1, mathEngine)
            : this.currentSimulator.synthesizeSlice(patchW, patchH, paramsH0, mathEngine);

        const wl = this.currentSimulator.getDefaultWindowLevel();
        this._drawSliceToCanvas(this.ctxLeft, sliceLeft, patchW, patchH, wl.window, wl.level);
        this._drawSliceToCanvas(this.ctxRight, sliceRight, patchW, patchH, wl.window, wl.level);

        this.boxLeft.style.borderColor = 'var(--border-subtle)';
        this.boxRight.style.borderColor = 'var(--border-subtle)';
    }

    handleChoice(chosenSide) {
        const isCorrect = chosenSide === this.signalLocation;
        if (isCorrect) {
            this.correctCount++;
        }

        // Feedback visual instantâneo
        const targetBox = chosenSide === 'left' ? this.boxLeft : this.boxRight;
        targetBox.style.borderColor = isCorrect ? 'var(--accent-green)' : 'var(--accent-red)';

        // Atualiza estatísticas parciais
        this.scoreCorrectEl.textContent = this.correctCount;
        this.scoreTotalEl.textContent = this.currentTrial;
        const pct = (this.correctCount / this.currentTrial) * 100;
        this.scorePctEl.textContent = `${pct.toFixed(0)}%`;

        // Cálculo do d' empírico do observador humano via probit invertido
        const clampedPc = Math.min(0.99, Math.max(0.51, this.correctCount / this.currentTrial));
        const observedDprime = Math.SQRT2 * mathEngine.probit(clampedPc);
        this.scoreDprimeEl.textContent = observedDprime.toFixed(2);

        setTimeout(() => {
            this.nextTrial();
        }, 500);
    }

    showFinalSummary() {
        const pct = ((this.correctCount / this.totalTrials) * 100).toFixed(0);
        const clampedPc = Math.min(0.99, Math.max(0.51, this.correctCount / this.totalTrials));
        const observedDprime = (Math.SQRT2 * mathEngine.probit(clampedPc)).toFixed(2);

        alert(`🎉 Teste Psicofísico 2AFC Concluído!\n\n` +
              `• Acertos: ${this.correctCount} de ${this.totalTrials} (${pct}%)\n` +
              `• Seu d' Observado: ${observedDprime}\n` +
              `• Critério de Rose (d' ≥ 4.0): ${observedDprime >= 4.0 ? 'Atingido (Certeza Visual)' : 'Região de Incerteza Diagnóstica'}`);
        this.stop();
    }

    _drawSliceToCanvas(ctx, slice, w, h, winW, winL) {
        if (!ctx || !slice) return;
        const imgData = ctx.createImageData(w, h);
        const data = imgData.data;

        const minHU = winL - winW / 2.0;
        const maxHU = winL + winW / 2.0;

        for (let i = 0; i < slice.length; i++) {
            let norm = (slice[i] - minHU) / (maxHU - minHU);
            if (norm < 0) norm = 0;
            if (norm > 1) norm = 1;

            const val = Math.round(norm * 255);
            const pIdx = i * 4;
            data[pIdx] = val;
            data[pIdx + 1] = val;
            data[pIdx + 2] = val;
            data[pIdx + 3] = 255;
        }

        ctx.putImageData(imgData, 0, 0);
    }
}
