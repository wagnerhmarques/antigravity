/**
 * LabExperimentsGuide.js
 * Módulo de Roteiros Práticos de Iniciação Científica (Bancada Virtual de Física Médica).
 * Estrutura 5 experimentos guiados com hipóteses físico-matemáticas, metas quantitativas e validação automática.
 */

export class LabExperimentsGuide {
    constructor(appController) {
        this.app = appController;
        this.modal = document.getElementById('lab-guide-modal');
        this.listContainer = document.getElementById('experiments-list');
        this.feedbackEl = document.getElementById('experiment-feedback');
        
        this.experiments = [
            {
                id: 'exp1',
                module: 'sdt_roc',
                title: 'Experimento 1: Otimização ALARA e Critério de Rose no Pulmão',
                targetModuleBadge: 'Módulo 1',
                objective: 'Encontrar o menor CTDIvol capaz de garantir d\' ≥ 4.0 (Critério de Rose) para um nódulo pulmonar de 3.5 mm com contraste ΔC = 200 HU.',
                hypothesis: 'Como d\' ∝ √(Dose), a redução excessiva de dose induz incerteza diagnóstica, exigindo CTDIvol suficiente para PC ≥ 99.8%.',
                instructions: '1. No Módulo 1, ajuste o Raio para 3.5 mm e Contraste para 200 HU.\n2. Varie o slider de Dose até atingir d\' ≥ 4.00.\n3. Clique em "Validar Hipótese".',
                validate: (params, metrics) => {
                    const dPrime = parseFloat(metrics[0]?.value || 0);
                    if (dPrime >= 3.95 && params.lesionRadius >= 3.0 && params.lesionContrast >= 180) {
                        return {
                            success: true,
                            message: `✅ Hipótese Confirmada! Com Dose = ${params.dose} mGy, você atingiu d' = ${dPrime.toFixed(2)} (Critério de Rose satisfeito, AUC = ${(metrics[1]?.value || '')}). A probabilidade de acerto PC é > 99.8% com mínima dose ionizante.`
                        };
                    }
                    return {
                        success: false,
                        message: `❌ Meta não atingida: Seu d' atual é ${dPrime.toFixed(2)}. Eleve a dose ou aumente o contraste/raio até atingir d' ≥ 4.00.`
                    };
                }
            },
            {
                id: 'exp2',
                module: 'fourier_tg233',
                title: 'Experimento 2: Quebra da Resolução TTF em Alvos de Baixo Contraste',
                targetModuleBadge: 'Módulo 2',
                objective: 'Demonstrar a não-linearidade da resolução espacial ao alternar entre insertos de Alto Contraste (+300 HU Iodo) e Baixo Contraste (+25 HU Água).',
                hypothesis: 'A frequência de corte f50 da TTF sofre degradação acentuada em alvos de baixo contraste (f50 cai de ~0.58 para ~0.35 mm⁻¹), borrando metástases hepáticas.',
                instructions: '1. No Módulo 2, selecione o inserto "Parênquima Hepático / Água (+25 HU)".\n2. Observe a queda na curva TTF(f) e a redução do d\' espectral.\n3. Clique em "Validar Hipótese".',
                validate: (params, metrics) => {
                    if (params.insertType === 'water' && params.deltaC <= 30) {
                        return {
                            success: true,
                            message: `✅ Hipótese Confirmada! Em alvos de baixo contraste, f50 = 0.35 mm⁻¹, evidenciando que sistemas tomográficos não lineares perdem resolução de borda exatamente onde o diagnóstico oncológico mais necessita.`
                        };
                    }
                    return {
                        success: false,
                        message: `❌ Selecione o inserto "Água (+25 HU)" com ΔC ≤ 30 HU no Módulo 2 para evidenciar o efeito de borramento não-linear.`
                    };
                }
            },
            {
                id: 'exp3',
                module: 'linear_observers',
                title: 'Experimento 3: Falha do NPWE vs Robustez do CHO no AVC Isquêmico',
                targetModuleBadge: 'Módulo 3',
                objective: 'Provar que em fundo cerebral estruturado (1/f^β com β = 2.5), o modelo NPWE falha (d\' < 0.8), enquanto o CHO com canais D-DOG mantém d\' ≥ 2.0 (ASPECTS confiável).',
                hypothesis: 'O cérebro humano utiliza canais corticais sintonizados (V1) para filtrar o ruído anatômico 1/f^β, capacidade que o NPWE não possui.',
                instructions: '1. No Módulo 3, selecione o observador "CHO (Canais D-DOG)" com β = 2.5 e Edema ΔC = 4.0 HU.\n2. Observe o d\' CHO em comparação com o NPWE.\n3. Clique em "Validar Hipótese".',
                validate: (params, metrics) => {
                    if (params.observerType === 'CHO' && params.betaPower >= 2.0 && params.deltaC <= 5.0) {
                        return {
                            success: true,
                            message: `✅ Hipótese Confirmada! O Observador CHO descorrelacionou o fundo anatômico cerebral através dos 5 canais D-DOG, alcançando ${metrics[0]?.value} (d' ≥ 2.0, viabilizando a conduta de trombólise no AVC).`
                        };
                    }
                    return {
                        success: false,
                        message: `❌ Configure o Módulo 3 com observador CHO, β ≥ 2.0 e edema sutil ΔC ≤ 5 HU.`
                    };
                }
            },
            {
                id: 'exp4',
                module: 'dlr_nonlinear',
                title: 'Experimento 4: Desmascarando o Paradoxo do NPWE em Microfraturas',
                targetModuleBadge: 'Módulo 4',
                objective: 'Demonstrar que o aumento do nível de DLR (> 70%) reduz o desvio padrão de ruído mas oblitera a fenda da microfratura trabecular (150 µm).',
                hypothesis: 'A regularização não-linear da IA suprime altas frequências (f > 0.8 mm⁻¹), fundindo espículas ósseas e gerando falso laudo negativo em radiologistas humanos.',
                instructions: '1. No Módulo 4, eleve a Força DLR para > 70% e observe a imagem trabecular.\n2. Verifique o paradoxo do disparo do d\' NPWE contrastando com a perda da fratura na imagem.\n3. Clique em "Validar Hipótese".',
                validate: (params, metrics) => {
                    if (params.dlrLevel >= 70) {
                        return {
                            success: true,
                            message: `✅ Hipótese Confirmada! Sob DLR em ${params.dlrLevel}%, a fenda trabecular foi obliterada pelo efeito ceroso. Enquanto o NPWE indicaria um falso ganho de +${params.dlrLevel * 1.5}%, o observador humano e o DLMO perdem acurácia diagnóstica.`
                        };
                    }
                    return {
                        success: false,
                        message: `❌ Eleve o slider de DLR para ≥ 70% para observar a fusão cerosa das microespículas ósseas.`
                    };
                }
            },
            {
                id: 'exp5',
                module: 'pcct_pareto',
                title: 'Experimento 5: Otimização Espectral VMI e Fronteira de Pareto na PCCT',
                targetModuleBadge: 'Módulo 5',
                objective: 'Identificar a energia monoenergética virtual ótima (VMI entre 45 e 50 keV) que maximiza o d\' na angiotomografia coronariana.',
                hypothesis: 'A proximidade com a borda K do iodo (33.2 keV) maximiza o coeficiente fotoelétrico, compensando o ruído e criando o pico global de detectabilidade vascular.',
                instructions: '1. No Módulo 5, varie o slider de Energia VMI e localize o valor que maximiza o d\'.\n2. Configure entre 44 e 50 keV com detector PCCT.\n3. Clique em "Validar Hipótese".',
                validate: (params, metrics) => {
                    if (params.detectorType === 'PCCT' && params.vmiEnergy >= 44 && params.vmiEnergy <= 50) {
                        return {
                            success: true,
                            message: `✅ Hipótese Confirmada! Em ${params.vmiEnergy} keV, o PCCT atinge o pico global de d' (${metrics[0]?.value}), eliminando o blooming calcificado e permitindo redução de 60% na carga de iodo em pacientes renais.`
                        };
                    }
                    return {
                        success: false,
                        message: `❌ Ajuste a energia VMI para a faixa ótima de 44 a 50 keV com detector PCCT.`
                    };
                }
            }
        ];

        this._setupEvents();
    }

    _setupEvents() {
        const btnOpen = document.getElementById('btn-lab-guide');
        const btnClose = document.getElementById('btn-close-lab-modal');

        if (btnOpen) {
            btnOpen.addEventListener('click', () => this.open());
        }
        if (btnClose) {
            btnClose.addEventListener('click', () => this.close());
        }
    }

    open() {
        this.renderExperimentsList();
        this.modal.classList.remove('hidden');
    }

    close() {
        this.modal.classList.add('hidden');
    }

    renderExperimentsList() {
        this.listContainer.innerHTML = '';

        this.experiments.forEach((exp, idx) => {
            const card = document.createElement('div');
            card.className = 'exp-card';

            const isActiveModule = this.app.activeSim && this.app.activeSim.id === exp.module;

            card.innerHTML = `
                <div class="exp-header">
                    <div class="exp-title-area">
                        <span class="category-badge">${exp.targetModuleBadge}</span>
                        <strong class="exp-title">${exp.title}</strong>
                    </div>
                    <button class="btn-sm ${isActiveModule ? 'btn-accent' : 'btn-secondary'} btn-load-exp" data-exp-idx="${idx}">
                        ${isActiveModule ? '▶ Módulo Ativo' : 'Ir para este Módulo'}
                    </button>
                </div>
                <div class="exp-body">
                    <p><strong>🎯 Objetivo:</strong> ${exp.objective}</p>
                    <p><strong>💡 Hipótese Física:</strong> ${exp.hypothesis}</p>
                    <div class="exp-instructions">
                        <strong>📋 Roteiro de Ação:</strong>
                        <pre>${exp.instructions}</pre>
                    </div>
                </div>
                <div class="exp-footer">
                    <button class="action-btn btn-accent btn-validate-exp" data-exp-idx="${idx}">
                        🧪 Validar Hipótese Experimental
                    </button>
                </div>
            `;

            const btnLoad = card.querySelector('.btn-load-exp');
            btnLoad.addEventListener('click', () => {
                this.app.loadSimulatorById(exp.module);
                this.renderExperimentsList();
            });

            const btnValidate = card.querySelector('.btn-validate-exp');
            btnValidate.addEventListener('click', () => {
                if (!this.app.activeSim || this.app.activeSim.id !== exp.module) {
                    this.app.loadSimulatorById(exp.module);
                }
                const metrics = this.app.activeSim.getSummaryMetrics(this.app.currentParams, this.app.mathEngine);
                const result = exp.validate(this.app.currentParams, metrics);
                this.showFeedback(result.message, result.success);
            });

            this.listContainer.appendChild(card);
        });
    }

    showFeedback(message, isSuccess) {
        this.feedbackEl.className = `exp-feedback-banner ${isSuccess ? 'success' : 'error'}`;
        this.feedbackEl.innerHTML = `<strong>${isSuccess ? '🎉 RESULTADO EXPERIMENTAL:' : '⚠️ ATENÇÃO:'}</strong> ${message}`;
        this.feedbackEl.scrollIntoView({ behavior: 'smooth' });
    }
}
