/**
 * SimulatorBase.js
 * Classe base abstrata para todos os simuladores do TBIQ Studio.
 * Qualquer novo módulo de simulação criado por alunos ou pesquisadores deve herdar desta classe.
 */

export class SimulatorBase {
    /**
     * @param {Object} config
     * @param {string} config.id - Identificador único do simulador (ex: 'sdt_roc')
     * @param {string} config.title - Título principal exibido na interface
     * @param {string} config.badge - Etiqueta do módulo (ex: 'Módulo 1')
     * @param {string} config.clinicalScenario - Título do caso clínico real
     * @param {string} config.scenarioDesc - Descrição clínica detalhada do desafio diagnóstico
     * @param {string[]} [config.equations] - Lista de equações em formato LaTeX para renderização no KaTeX
     * @param {Object} [config.presets] - Dicionário de presets clínicos pré-configurados
     */
    constructor(config) {
        if (!config.id || !config.title) {
            throw new Error("O simulador precisa definir obrigatoriamente um 'id' e um 'title'.");
        }
        this.id = config.id;
        this.title = config.title;
        this.badge = config.badge || 'Módulo';
        this.clinicalScenario = config.clinicalScenario || 'Avaliação Tomográfica Geral';
        this.scenarioDesc = config.scenarioDesc || 'Análise metrológica da qualidade de imagem baseada em tarefa.';
        this.equations = config.equations || [];
        this.presets = config.presets || {};
    }

    /**
     * Retorna a especificação dos controles (sliders e selects) do simulador.
     * Deve retornar um objeto chave-valor onde cada chave define um parâmetro interativo.
     * @returns {Object} Definição de parâmetros
     */
    getParameters() {
        return {};
    }

    /**
     * Retorna os valores padrão iniciais de todos os parâmetros.
     * @returns {Object}
     */
    getDefaultValues() {
        const params = this.getParameters();
        const defaults = {};
        for (const [key, def] of Object.entries(params)) {
            defaults[key] = def.default !== undefined ? def.default : (def.min || 0);
        }
        return defaults;
    }

    /**
     * Sintetiza a fatia tomográfica em escala de Unidades Hounsfield (HU) em tempo real.
     * @param {number} width - Largura da matriz de imagem (ex: 256 ou 380)
     * @param {number} height - Altura da matriz de imagem
     * @param {Object} currentParams - Valores atuais dos parâmetros selecionados pelo usuário
     * @param {Object} mathEngine - Motor de funções matemáticas e físicas
     * @returns {Float32Array} Matriz 1D contínua de valores HU com tamanho (width * height)
     */
    synthesizeSlice(width, height, currentParams, mathEngine) {
        throw new Error(`O método synthesizeSlice() deve ser implementado no simulador '${this.id}'.`);
    }

    /**
     * Renderiza os dois gráficos analíticos associados a este simulador.
     * @param {HTMLCanvasElement} canvas1 - Canvas superior (ex: distribuições ou TTF/NPS)
     * @param {HTMLCanvasElement} canvas2 - Canvas inferior (ex: Curva ROC ou d' vs Dose)
     * @param {Object} currentParams - Parâmetros atuais
     * @param {Object} mathEngine - Motor matemático
     */
    renderCharts(canvas1, canvas2, currentParams, mathEngine) {
        throw new Error(`O método renderCharts() deve ser implementado no simulador '${this.id}'.`);
    }

    /**
     * Retorna métricas numéricas formatadas para exibição no HUD e no rodapé estatístico.
     * @param {Object} currentParams
     * @param {Object} mathEngine
     * @returns {Array<{title: string, value: string, subtitle: string}>}
     */
    getSummaryMetrics(currentParams, mathEngine) {
        return [];
    }

    /**
     * Retorna o texto explicativo contextualizado com os valores dos parâmetros atuais.
     * @param {Object} currentParams
     * @returns {string} Texto em HTML com destaques didáticos
     */
    getEducationalExplanation(currentParams) {
        return `<p>Ajuste os parâmetros para analisar a resposta do sistema formador de imagens.</p>`;
    }

    /**
     * Janelamento padrão sugerido para o caso clínico deste simulador.
     * @returns {{window: number, level: number}}
     */
    getDefaultWindowLevel() {
        return { window: 400, level: 40 };
    }
}
