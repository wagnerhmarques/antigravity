/**
 * DicomViewport.js (Versão Aprimorada 2.5)
 * Visualizador Interativo de TC com suporte a:
 * - Window/Level dinâmico com mouse drag;
 * - Ferramenta de ROI Interativa para cálculo de FFT 2D e NPS empírico em tempo real;
 * - Modo Comparativo A/B Split-Screen (Divisor Deslizante);
 * - Scanner de Perfil de Linha Seccional (HU vs mm);
 * - HUD Médico e Colormaps.
 */

import { mathEngine } from './MathPhysicsEngine.js';

export class DicomViewport {
    constructor(canvasId, profileCanvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        
        this.profileCanvas = document.getElementById(profileCanvasId);
        this.profileCtx = this.profileCanvas ? this.profileCanvas.getContext('2d') : null;

        this.currentSlice = null;
        this.sliceB = null; // Para modo comparativo A/B
        this.width = 380;
        this.height = 380;

        // Parâmetros de Exibição
        this.windowWidth = 1500;
        this.windowLevel = -600;
        this.colormap = 'gray';

        this.showHud = true;
        this.showLineProfile = true;
        this.showRoiTool = false;
        this.isSplitMode = false;
        this.splitPosition = 0.5; // 0.0 a 1.0 (divisor vertical)

        // ROI Interativa (64x64 pixels padrão)
        this.roi = { x: 158, y: 158, size: 64, isDragging: false };
        this.empiricalNPS = null;

        this.mousePos = { x: 0, y: 0, hu: 0, isHovering: false };
        this.isDraggingWL = false;
        this.isDraggingSplit = false;
        this.dragStart = { x: 0, y: 0, w: 1500, l: -600 };

        this._setupEvents();
    }

    _setupEvents() {
        this.canvas.addEventListener('mousemove', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            const scaleX = this.width / rect.width;
            const scaleY = this.height / rect.height;
            const x = Math.floor((e.clientX - rect.left) * scaleX);
            const y = Math.floor((e.clientY - rect.top) * scaleY);

            this.mousePos.x = Math.max(0, Math.min(this.width - 1, x));
            this.mousePos.y = Math.max(0, Math.min(this.height - 1, y));
            this.mousePos.isHovering = true;

            // Cursor HU Value
            if (this.currentSlice) {
                this.mousePos.hu = this.currentSlice[this.mousePos.y * this.width + this.mousePos.x];
                const cursorEl = document.getElementById('hud-cursor-val');
                if (cursorEl) cursorEl.textContent = `${Math.round(this.mousePos.hu)} HU`;
            }

            if (this.roi.isDragging) {
                this.roi.x = Math.max(0, Math.min(this.width - this.roi.size, x - this.roi.size / 2));
                this.roi.y = Math.max(0, Math.min(this.height - this.roi.size, y - this.roi.size / 2));
                this._updateRoiMetrics();
                this.render();
            } else if (this.isDraggingSplit) {
                this.splitPosition = Math.max(0.05, Math.min(0.95, (e.clientX - rect.left) / rect.width));
                this.render();
            } else if (this.isDraggingWL) {
                const deltaX = (e.clientX - this.dragStart.x) * 4.0;
                const deltaY = (e.clientY - this.dragStart.y) * 4.0;
                this.windowWidth = Math.max(1, Math.round(this.dragStart.w + deltaX));
                this.windowLevel = Math.round(this.dragStart.l - deltaY);
                this.updateHudValues();
                this.render();
            } else {
                this.render();
            }
        });

        this.canvas.addEventListener('mouseleave', () => {
            this.mousePos.isHovering = false;
            this.isDraggingWL = false;
            this.roi.isDragging = false;
            this.isDraggingSplit = false;
            const cursorEl = document.getElementById('hud-cursor-val');
            if (cursorEl) cursorEl.textContent = `-- HU`;
            this.render();
        });

        this.canvas.addEventListener('mousedown', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            const x = (e.clientX - rect.left) * (this.width / rect.width);
            const y = (e.clientY - rect.top) * (this.height / rect.height);

            // Verifica se clicou dentro da ROI
            if (this.showRoiTool && x >= this.roi.x && x <= this.roi.x + this.roi.size &&
                y >= this.roi.y && y <= this.roi.y + this.roi.size) {
                this.roi.isDragging = true;
                return;
            }

            // Verifica se clicou próximo ao divisor split A/B
            if (this.isSplitMode) {
                const splitX = this.splitPosition * this.width;
                if (Math.abs(x - splitX) < 10) {
                    this.isDraggingSplit = true;
                    return;
                }
            }

            if (e.button === 0) {
                this.isDraggingWL = true;
                this.dragStart = {
                    x: e.clientX,
                    y: e.clientY,
                    w: this.windowWidth,
                    l: this.windowLevel
                };
            }
        });

        window.addEventListener('mouseup', () => {
            this.isDraggingWL = false;
            this.roi.isDragging = false;
            this.isDraggingSplit = false;
        });
    }

    toggleRoiTool() {
        this.showRoiTool = !this.showRoiTool;
        if (this.showRoiTool) {
            this._updateRoiMetrics();
        }
        this.render();
        return this.showRoiTool;
    }

    toggleSplitMode(sliceB = null) {
        this.isSplitMode = !this.isSplitMode;
        this.sliceB = sliceB;
        this.render();
        return this.isSplitMode;
    }

    setSlice(sliceData, width = 380, height = 380) {
        this.currentSlice = sliceData;
        this.width = width;
        this.height = height;
        this.canvas.width = width;
        this.canvas.height = height;
        if (this.showRoiTool) this._updateRoiMetrics();
        this.render();
    }

    setWindowLevel(w, l) {
        this.windowWidth = w;
        this.windowLevel = l;
        this.updateHudValues();
        this.render();
    }

    setColormap(cmap) {
        this.colormap = cmap;
        this.render();
    }

    updateHudValues() {
        const wEl = document.getElementById('hud-window');
        const lEl = document.getElementById('hud-level');
        if (wEl) wEl.textContent = `${Math.round(this.windowWidth)} HU`;
        if (lEl) lEl.textContent = `${Math.round(this.windowLevel)} HU`;
    }

    _updateRoiMetrics() {
        if (!this.currentSlice) return;

        const roiData = new Float32Array(this.roi.size * this.roi.size);
        let sum = 0, sumSq = 0;
        let min = Infinity, max = -Infinity;

        for (let ry = 0; ry < this.roi.size; ry++) {
            for (let rx = 0; rx < this.roi.size; rx++) {
                const srcIdx = (this.roi.y + ry) * this.width + (this.roi.x + rx);
                const val = this.currentSlice[srcIdx];
                roiData[ry * this.roi.size + rx] = val;

                sum += val;
                sumSq += val * val;
                if (val < min) min = val;
                if (val > max) max = val;
            }
        }

        const count = this.roi.size * this.roi.size;
        const mean = sum / count;
        const variance = (sumSq / count) - (mean * mean);
        const std = Math.sqrt(Math.max(0, variance));

        // Calcula NPS empírico via FFT 2D da ROI
        this.empiricalNPS = mathEngine.computeEmpiricalNPS(roiData, this.roi.size, 0.5);

        // Atualiza elementos de ROI no HUD se existirem
        const roiInfoEl = document.getElementById('roi-stats-info');
        if (roiInfoEl) {
            roiInfoEl.innerHTML = `Média: <strong>${mean.toFixed(1)} HU</strong> | σ: <strong>${std.toFixed(1)} HU</strong> | Min: ${min.toFixed(0)} | Max: ${max.toFixed(0)}`;
        }
    }

    _huToRGB(hu) {
        const minHU = this.windowLevel - this.windowWidth / 2.0;
        const maxHU = this.windowLevel + this.windowWidth / 2.0;

        let norm = (hu - minHU) / (maxHU - minHU);
        if (norm < 0.0) norm = 0.0;
        if (norm > 1.0) norm = 1.0;

        if (this.colormap === 'inverted') {
            const v = Math.round((1.0 - norm) * 255);
            return [v, v, v];
        }
        if (this.colormap === 'bone') {
            return [Math.round(norm * 255), Math.round(Math.pow(norm, 1.2) * 240), Math.round(Math.pow(norm, 1.8) * 210)];
        }
        if (this.colormap === 'rainbow') {
            const h = (1.0 - norm) * 240;
            return this._hslToRgb(h / 360, 1.0, 0.5);
        }
        if (this.colormap === 'hot') {
            const r = Math.min(255, Math.round(norm * 3 * 255));
            const g = Math.min(255, Math.max(0, Math.round((norm - 0.33) * 3 * 255)));
            const b = Math.min(255, Math.max(0, Math.round((norm - 0.66) * 3 * 255)));
            return [r, g, b];
        }

        const val = Math.round(norm * 255);
        return [val, val, val];
    }

    _hslToRgb(h, s, l) {
        let r, g, b;
        if (s === 0) {
            r = g = b = l;
        } else {
            const hue2rgb = (p, q, t) => {
                if (t < 0) t += 1;
                if (t > 1) t -= 1;
                if (t < 1/6) return p + (q - p) * 6 * t;
                if (t < 1/2) return q;
                if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
                return p;
            };
            const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
            const p = 2 * l - q;
            r = hue2rgb(p, q, h + 1/3);
            g = hue2rgb(p, q, h);
            b = hue2rgb(p, q, h - 1/3);
        }
        return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
    }

    render() {
        if (!this.currentSlice) return;

        const imgData = this.ctx.createImageData(this.width, this.height);
        const data = imgData.data;
        const splitX = Math.floor(this.splitPosition * this.width);

        for (let y = 0; y < this.height; y++) {
            for (let x = 0; x < this.width; x++) {
                const idx = y * this.width + x;
                let hu = this.currentSlice[idx];

                // No modo split A/B, usa sliceB à direita do divisor
                if (this.isSplitMode && this.sliceB && x >= splitX) {
                    hu = this.sliceB[idx];
                }

                const [r, g, b] = this._huToRGB(hu);
                const pIdx = idx * 4;
                data[pIdx]     = r;
                data[pIdx + 1] = g;
                data[pIdx + 2] = b;
                data[pIdx + 3] = 255;
            }
        }

        this.ctx.putImageData(imgData, 0, 0);

        // Renderiza linha divisória do modo Split A/B
        if (this.isSplitMode) {
            this.ctx.strokeStyle = '#00f0ff';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.moveTo(splitX, 0);
            this.ctx.lineTo(splitX, this.height);
            this.ctx.stroke();

            // Marcadores de lado
            this.ctx.fillStyle = '#00f0ff';
            this.ctx.font = '10px Fira Code';
            this.ctx.fillText('PROTOCOLO A', 10, 20);
            this.ctx.fillText('PROTOCOLO B', splitX + 10, 20);
        }

        // Renderiza Ferramenta de ROI se ativa
        if (this.showRoiTool) {
            this.ctx.strokeStyle = '#10b981';
            this.ctx.lineWidth = 1.5;
            this.ctx.strokeRect(this.roi.x, this.roi.y, this.roi.size, this.roi.size);
            this.ctx.fillStyle = 'rgba(16, 185, 129, 0.15)';
            this.ctx.fillRect(this.roi.x, this.roi.y, this.roi.size, this.roi.size);

            this.ctx.fillStyle = '#10b981';
            this.ctx.font = '9px Fira Code';
            this.ctx.fillText(`ROI ${this.roi.size}x${this.roi.size} (FFT2D)`, this.roi.x + 4, this.roi.y - 4);
        }

        // Linha do Perfil Seccional
        if (this.showLineProfile) {
            const centerY = this.height / 2;
            this.ctx.strokeStyle = 'rgba(255, 184, 0, 0.65)';
            this.ctx.lineWidth = 1;
            this.ctx.setLineDash([4, 4]);
            this.ctx.beginPath();
            this.ctx.moveTo(0, centerY);
            this.ctx.lineTo(this.width, centerY);
            this.ctx.stroke();
            this.ctx.setLineDash([]);

            this._renderProfileGraph(centerY);
        }

        // Cursor Crosshair
        if (this.mousePos.isHovering) {
            this.ctx.strokeStyle = 'rgba(0, 240, 255, 0.7)';
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            this.ctx.arc(this.mousePos.x, this.mousePos.y, 6, 0, 2 * Math.PI);
            this.ctx.stroke();
        }
    }

    _renderProfileGraph(lineY) {
        if (!this.profileCtx || !this.currentSlice) return;

        const pCanvas = this.profileCanvas;
        const pCtx = this.profileCtx;
        const w = pCanvas.width;
        const h = pCanvas.height;

        pCtx.clearRect(0, 0, w, h);

        pCtx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
        pCtx.lineWidth = 1;
        pCtx.beginPath();
        for (let y = 15; y < h; y += 20) {
            pCtx.moveTo(0, y);
            pCtx.lineTo(w, y);
        }
        pCtx.stroke();

        const profile = [];
        let minHU = Infinity;
        let maxHU = -Infinity;

        for (let x = 0; x < this.width; x++) {
            const hu = this.currentSlice[lineY * this.width + x];
            profile.push(hu);
            if (hu < minHU) minHU = hu;
            if (hu > maxHU) maxHU = hu;
        }

        const range = Math.max(50, maxHU - minHU);
        const marginY = 10;
        const plotH = h - 2 * marginY;

        pCtx.strokeStyle = '#ffb800';
        pCtx.lineWidth = 1.5;
        pCtx.beginPath();

        for (let x = 0; x < w; x++) {
            const sliceX = Math.floor((x / w) * this.width);
            const val = profile[sliceX];
            const normY = (val - minHU) / range;
            const plotY = (h - marginY) - normY * plotH;

            if (x === 0) pCtx.moveTo(x, plotY);
            else pCtx.lineTo(x, plotY);
        }
        pCtx.stroke();

        pCtx.fillStyle = '#94a3b8';
        pCtx.font = '9px Fira Code';
        pCtx.fillText(`Max: ${Math.round(maxHU)} HU`, 6, 12);
        pCtx.fillText(`Min: ${Math.round(minHU)} HU`, 6, h - 3);

        const contrastEl = document.getElementById('profile-contrast-val');
        if (contrastEl) {
            contrastEl.textContent = `Variação Δ = ${Math.round(maxHU - minHU)} HU`;
        }
    }
}
