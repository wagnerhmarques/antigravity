/**
 * app.js (Versão Aprimorada 2.5)
 * Orquestrador central da aplicação TBIQ Studio.
 * Gerencia a integração dos 5 simuladores do TCC, o visualizador DICOM com ROI/Split-Screen,
 * o módulo de experimentos de Iniciação Científica e a geração de Laudos Técnicos AAPM TG-233.
 */

import { globalRegistry } from './core/SimulatorsRegistry.js';
import { mathEngine } from './core/MathPhysicsEngine.js';
import { DicomViewport } from './core/DicomViewport.js';
import { Psychophysics2AFC } from './core/Psychophysics2AFC.js';
import { LabExperimentsGuide } from './core/LabExperimentsGuide.js';

// 5 Módulos Nativos do TCC
import { Sim1_SDT_ROC } from './modules/Sim1_SDT_ROC.js';
import { Sim2_Fourier_TG233 } from './modules/Sim2_Fourier_TG233.js';
import { Sim3_LinearObservers } from './modules/Sim3_LinearObservers.js';
import { Sim4_DLR_Nonlinear } from './modules/Sim4_DLR_Nonlinear.js';
import { Sim5_PCCT_Pareto } from './modules/Sim5_PCCT_Pareto.js';

class AppController {
    constructor() {
        this.viewport = null;
        this.psychophysics = null;
        this.labGuide = null;
        this.mathEngine = mathEngine;
        this.currentParams = {};
        this.activeSim = null;

        // Elementos DOM
        this.navContainer = document.getElementById('simulators-nav');
        this.moduleBadgeEl = document.getElementById('module-badge');
        this.moduleTitleEl = document.getElementById('module-title');
        this.scenarioTitleEl = document.getElementById('scenario-title');
        this.scenarioDescEl = document.getElementById('scenario-desc');
        this.controlsContainer = document.getElementById('dynamic-controls');
        this.presetSelect = document.getElementById('preset-select');
        this.equationsBox = document.getElementById('module-equations');
        this.explanationBox = document.getElementById('module-explanation');
        this.metricsGrid = document.getElementById('module-metrics-grid');
        this.metricsHudSummary = document.getElementById('metrics-hud-summary');

        // Canvases de Gráficos
        this.chartCanvas1 = document.getElementById('chart-canvas-1');
        this.chartCanvas2 = document.getElementById('chart-canvas-2');

        // HUD DICOM
        this.hudModality = document.getElementById('hud-modality');
        this.hudDose = document.getElementById('hud-dose');
        this.hudKernel = document.getElementById('hud-kernel');
        this.hudDprime = document.getElementById('hud-dprime');
        this.hudRose = document.getElementById('hud-rose');

        this.init();
    }

    init() {
        // 1. Inicializa Viewport DICOM e Módulos Centrais
        this.viewport = new DicomViewport('dicom-canvas', 'profile-canvas');
        this.psychophysics = new Psychophysics2AFC({
            onFinish: () => this.update()
        });

        // 2. Registra os 5 Simuladores do TCC
        globalRegistry.register(new Sim1_SDT_ROC());
        globalRegistry.register(new Sim2_Fourier_TG233());
        globalRegistry.register(new Sim3_LinearObservers());
        globalRegistry.register(new Sim4_DLR_Nonlinear());
        globalRegistry.register(new Sim5_PCCT_Pareto());

        // 3. Inicializa o Guia de Experimentos de Iniciação Científica
        this.labGuide = new LabExperimentsGuide(this);

        // 4. Monta a Barra Lateral de Navegação
        this.renderNavigation();

        // 5. Inscreve-se nas alterações de módulo
        globalRegistry.subscribe((event, sim) => {
            if (event === 'activeChanged') {
                this.loadSimulator(sim);
            }
        });

        // 6. Configura Todos os Eventos de Interface e Ferramentas
        this.setupToolbarEvents();
        this.setupReportGenerator();

        // 7. Carrega o primeiro módulo
        const initialSim = globalRegistry.getActive();
        if (initialSim) {
            this.loadSimulator(initialSim);
        }
    }

    renderNavigation() {
        this.navContainer.innerHTML = '';
        const sims = globalRegistry.getAll();

        sims.forEach((sim) => {
            const item = document.createElement('button');
            item.className = `sim-nav-item ${sim.id === globalRegistry.activeSimulatorId ? 'active' : ''}`;
            item.dataset.simId = sim.id;

            item.innerHTML = `
                <div class="sim-nav-header">
                    <span class="sim-num-badge">${sim.badge}</span>
                </div>
                <div class="sim-nav-name">${sim.title}</div>
                <div class="sim-nav-scenario">🏥 ${sim.clinicalScenario}</div>
            `;

            item.addEventListener('click', () => {
                globalRegistry.setActive(sim.id);
                this.updateNavActiveState();
            });

            this.navContainer.appendChild(item);
        });

        const countEl = document.getElementById('modules-count');
        if (countEl) countEl.textContent = `${sims.length} Módulos`;
    }

    updateNavActiveState() {
        const items = this.navContainer.querySelectorAll('.sim-nav-item');
        items.forEach(item => {
            item.classList.toggle('active', item.dataset.simId === globalRegistry.activeSimulatorId);
        });
    }

    loadSimulatorById(id) {
        const sim = globalRegistry.get(id);
        if (sim) {
            globalRegistry.setActive(id);
            this.updateNavActiveState();
        }
    }

    loadSimulator(sim) {
        this.activeSim = sim;
        this.currentParams = sim.getDefaultValues();

        this.moduleBadgeEl.textContent = sim.badge;
        this.moduleTitleEl.textContent = sim.title;
        this.scenarioTitleEl.textContent = `Cenário Clínico: ${sim.clinicalScenario}`;
        this.scenarioDescEl.textContent = sim.scenarioDesc;

        // Janelamento padrão sugerido
        const wl = sim.getDefaultWindowLevel();
        this.viewport.setWindowLevel(wl.window, wl.level);
        this.updateWLPresetButtons(wl.window, wl.level);

        this.renderPresets(sim);
        this.renderControls(sim);
        this.renderEquations(sim);

        this.update();
    }

    renderPresets(sim) {
        this.presetSelect.innerHTML = '<option value="custom">-- Selecione um Caso Clínico --</option>';
        if (sim.presets) {
            for (const [key, preset] of Object.entries(sim.presets)) {
                const opt = document.createElement('option');
                opt.value = key;
                opt.textContent = preset.label;
                this.presetSelect.appendChild(opt);
            }
        }

        this.presetSelect.onchange = (e) => {
            const key = e.target.value;
            if (sim.presets && sim.presets[key]) {
                const presetParams = sim.presets[key].params;
                Object.assign(this.currentParams, presetParams);
                this.updateControlValuesInUI();
                this.update();
            }
        };
    }

    renderControls(sim) {
        this.controlsContainer.innerHTML = '';
        const paramsDef = sim.getParameters();

        for (const [key, def] of Object.entries(paramsDef)) {
            const item = document.createElement('div');
            item.className = 'control-item';

            if (def.type === 'range') {
                const val = this.currentParams[key];
                item.innerHTML = `
                    <div class="control-header-row">
                        <label class="slider-label" for="slider-${key}">${def.label}</label>
                        <span id="badge-${key}" class="slider-val-badge">${val} ${def.unit || ''}</span>
                    </div>
                    <input type="range" id="slider-${key}" class="custom-range-slider"
                        min="${def.min}" max="${def.max}" step="${def.step || 1}" value="${val}">
                    <span class="control-desc">${def.description || ''}</span>
                `;

                const slider = item.querySelector(`#slider-${key}`);
                const badge = item.querySelector(`#badge-${key}`);

                slider.addEventListener('input', (e) => {
                    const numVal = parseFloat(e.target.value);
                    this.currentParams[key] = numVal;
                    badge.textContent = `${numVal} ${def.unit || ''}`;
                    this.presetSelect.value = 'custom';
                    this.update();
                });

            } else if (def.type === 'select') {
                let optionsHtml = '';
                def.options.forEach(opt => {
                    const optVal = typeof opt === 'object' ? opt.value : opt;
                    const optLabel = typeof opt === 'object' ? opt.label : opt;
                    const selected = optVal === this.currentParams[key] ? 'selected' : '';
                    optionsHtml += `<option value="${optVal}" ${selected}>${optLabel}</option>`;
                });

                item.innerHTML = `
                    <div class="control-header-row">
                        <label class="slider-label" for="select-${key}">${def.label}</label>
                    </div>
                    <select id="select-${key}" class="custom-select" style="margin-top: 4px;">
                        ${optionsHtml}
                    </select>
                    <span class="control-desc" style="margin-top: 3px;">${def.description || ''}</span>
                `;

                const select = item.querySelector(`#select-${key}`);
                select.addEventListener('change', (e) => {
                    this.currentParams[key] = e.target.value;
                    this.presetSelect.value = 'custom';
                    this.update();
                });
            }

            this.controlsContainer.appendChild(item);
        }
    }

    updateControlValuesInUI() {
        for (const [key, val] of Object.entries(this.currentParams)) {
            const slider = document.getElementById(`slider-${key}`);
            const badge = document.getElementById(`badge-${key}`);
            const select = document.getElementById(`select-${key}`);
            const def = this.activeSim.getParameters()[key];

            if (slider && badge) {
                slider.value = val;
                badge.textContent = `${val} ${def.unit || ''}`;
            }
            if (select) {
                select.value = val;
            }
        }
    }

    renderEquations(sim) {
        this.equationsBox.innerHTML = '';
        if (sim.equations && sim.equations.length > 0) {
            sim.equations.forEach(eq => {
                const eqDiv = document.createElement('div');
                eqDiv.style.marginBottom = '6px';
                if (window.katex) {
                    try {
                        window.katex.render(eq, eqDiv, { displayMode: true, throwOnError: false });
                    } catch (e) {
                        eqDiv.textContent = eq;
                    }
                } else {
                    eqDiv.textContent = eq;
                }
                this.equationsBox.appendChild(eqDiv);
            });
        }
    }

    update() {
        if (!this.activeSim) return;

        // 1. Gera Fatia Tomográfica Primária
        const sliceData = this.activeSim.synthesizeSlice(380, 380, this.currentParams, mathEngine);
        
        // Se estiver no modo Split A/B, gera uma fatia B de comparação
        if (this.viewport.isSplitMode) {
            const paramsB = { ...this.currentParams, dose: (this.currentParams.dose || 10) * 0.35, dlrLevel: 90 };
            const sliceB = this.activeSim.synthesizeSlice(380, 380, paramsB, mathEngine);
            this.viewport.sliceB = sliceB;
        }

        this.viewport.setSlice(sliceData, 380, 380);

        // 2. Renderiza Gráficos Analíticos
        this.activeSim.renderCharts(this.chartCanvas1, this.chartCanvas2, this.currentParams, mathEngine);

        // 3. Atualiza Métricas e Rodapé
        const metrics = this.activeSim.getSummaryMetrics(this.currentParams, mathEngine);
        this.renderMetrics(metrics);

        // 4. Atualiza Explicação Pedagógica
        this.explanationBox.innerHTML = this.activeSim.getEducationalExplanation(this.currentParams);

        // 5. Atualiza HUD Médico
        if (metrics.length > 0) {
            const dVal = metrics[0].value;
            this.hudDprime.textContent = dVal;
            this.metricsHudSummary.textContent = `d' = ${dVal} • Qualidade Baseada em Tarefa`;
            const numD = parseFloat(dVal);
            this.hudRose.textContent = numD >= 4.0 ? 'Certeza (Rose)' : (numD >= 2.0 ? 'Aceitável' : 'Incerteza Crítica');
            this.hudRose.style.color = numD >= 4.0 ? 'var(--accent-green)' : (numD >= 2.0 ? 'var(--accent-amber)' : 'var(--accent-red)');
        }

        if (this.currentParams.dose) {
            this.hudDose.textContent = `CTDIvol ${this.currentParams.dose} mGy`;
        }
    }

    renderMetrics(metrics) {
        this.metricsGrid.innerHTML = '';
        metrics.forEach(m => {
            const tile = document.createElement('div');
            tile.className = 'metric-tile';
            tile.innerHTML = `
                <span class="metric-tile-title">${m.title}</span>
                <span class="metric-tile-val">${m.value}</span>
                <span class="metric-tile-sub">${m.subtitle}</span>
            `;
            this.metricsGrid.appendChild(tile);
        });
    }

    setupToolbarEvents() {
        document.getElementById('btn-reset-params').addEventListener('click', () => {
            if (this.activeSim) {
                this.currentParams = this.activeSim.getDefaultValues();
                this.updateControlValuesInUI();
                this.update();
            }
        });

        // Botões W/L
        const wlBtns = document.querySelectorAll('.wl-btn');
        wlBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                wlBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const w = parseFloat(btn.dataset.w);
                const l = parseFloat(btn.dataset.l);
                this.viewport.setWindowLevel(w, l);
            });
        });

        // Colormap
        document.getElementById('colormap-select').addEventListener('change', (e) => {
            this.viewport.setColormap(e.target.value);
        });

        // Perfil de Linha
        const btnProfile = document.getElementById('btn-toggle-line-profile');
        btnProfile.addEventListener('click', () => {
            this.viewport.showLineProfile = !this.viewport.showLineProfile;
            btnProfile.classList.toggle('active', this.viewport.showLineProfile);
            this.viewport.render();
        });

        // Ferramenta de ROI (FFT 2D)
        const btnRoi = document.getElementById('btn-toggle-roi');
        const roiStatsBar = document.getElementById('roi-stats-container');
        btnRoi.addEventListener('click', () => {
            const isActive = this.viewport.toggleRoiTool();
            btnRoi.classList.toggle('active', isActive);
            roiStatsBar.classList.toggle('hidden', !isActive);
        });

        // Modo Comparador A/B Split
        const btnSplit = document.getElementById('btn-toggle-split');
        btnSplit.addEventListener('click', () => {
            const isActive = this.viewport.toggleSplitMode();
            btnSplit.classList.toggle('active', isActive);
            this.update();
        });

        // Teste 2AFC
        document.getElementById('btn-2afc-mode').addEventListener('click', () => {
            if (this.activeSim) {
                this.psychophysics.start(this.activeSim, this.currentParams);
            }
        });

        // Modal Criador
        const modal = document.getElementById('new-sim-modal');
        document.getElementById('btn-create-sim').addEventListener('click', () => {
            modal.classList.remove('hidden');
        });
        document.getElementById('btn-close-modal').addEventListener('click', () => {
            modal.classList.add('hidden');
        });
    }

    setupReportGenerator() {
        const reportModal = document.getElementById('report-modal');
        const btnOpenReport = document.getElementById('btn-export-report');
        const btnCloseReport = document.getElementById('btn-close-report-modal');
        const btnPrint = document.getElementById('btn-print-report');

        if (btnOpenReport) {
            btnOpenReport.addEventListener('click', () => {
                this.generateReportContent();
                reportModal.classList.remove('hidden');
            });
        }
        if (btnCloseReport) {
            btnCloseReport.addEventListener('click', () => {
                reportModal.classList.add('hidden');
            });
        }
        if (btnPrint) {
            btnPrint.addEventListener('click', () => {
                window.print();
            });
        }
    }

    generateReportContent() {
        const tableProto = document.getElementById('report-protocol-info');
        const tableMetrics = document.getElementById('report-metrics-table');
        const textConclusion = document.getElementById('report-conclusion');

        if (!this.activeSim) return;

        // Tabela 1: Parâmetros do Protocolo
        let protoHtml = `
            <div class="report-row"><span class="report-row-label">Módulo Ativo:</span><span class="report-row-val">${this.activeSim.title}</span></div>
            <div class="report-row"><span class="report-row-label">Cenário Clínico:</span><span class="report-row-val">${this.activeSim.clinicalScenario}</span></div>
        `;
        for (const [key, val] of Object.entries(this.currentParams)) {
            const def = this.activeSim.getParameters()[key];
            if (def) {
                protoHtml += `<div class="report-row"><span class="report-row-label">${def.label}:</span><span class="report-row-val">${val} ${def.unit || ''}</span></div>`;
            }
        }
        tableProto.innerHTML = protoHtml;

        // Tabela 2: Métricas TG-233
        const metrics = this.activeSim.getSummaryMetrics(this.currentParams, mathEngine);
        let metricsHtml = '';
        metrics.forEach(m => {
            metricsHtml += `<div class="report-row"><span class="report-row-label">${m.title}:</span><span class="report-row-val">${m.value} (${m.subtitle})</span></div>`;
        });
        tableMetrics.innerHTML = metricsHtml;

        // Parecer Físico-Metrológico
        const dVal = parseFloat(metrics[0]?.value || 0);
        const roseStatus = dVal >= 4.0 ? 'CONFORME com o Critério de Rose (d\' ≥ 4.0, Certeza Visual Diagnóstica).' : 'NÃO-CONFORME (Região de Incerteza Diagnóstica / Risco de Falso-Negativo).';

        textConclusion.innerHTML = `
            O protocolo avaliado para a tarefa de <strong>${this.activeSim.clinicalScenario}</strong> apresentou índice de detectabilidade <strong>d' = ${dVal.toFixed(2)}</strong>. O sistema classifica-se como <strong>${roseStatus}</strong>. Em conformidade com a Resolução ANVISA RDC 611/2022 e com o princípio ALARA/ICRP 103, recomenda-se a auditoria periódica contínua via observadores de modelo antropomórficos.
        `;
    }

    updateWLPresetButtons(w, l) {
        const wlBtns = document.querySelectorAll('.wl-btn');
        wlBtns.forEach(btn => {
            const bw = parseFloat(btn.dataset.w);
            const bl = parseFloat(btn.dataset.l);
            btn.classList.toggle('active', bw === w && bl === l);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.app = new AppController();
});
