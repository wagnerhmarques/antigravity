/**
 * SimulatorsRegistry.js
 * Registro central de simuladores do TBIQ Studio.
 * Gerencia a lista de módulos disponíveis, alternância de módulo ativo e notificação de eventos.
 */

export class SimulatorsRegistry {
    constructor() {
        this.simulators = new Map();
        this.activeSimulatorId = null;
        this.listeners = new Set();
    }

    /**
     * Registra um novo simulador no ecossistema do software.
     * @param {import('./SimulatorBase.js').SimulatorBase} simulatorInstance
     */
    register(simulatorInstance) {
        if (!simulatorInstance || !simulatorInstance.id) {
            console.error("Tentativa de registrar simulador inválido:", simulatorInstance);
            return;
        }
        this.simulators.set(simulatorInstance.id, simulatorInstance);
        
        // Se for o primeiro registrado, define como ativo
        if (!this.activeSimulatorId) {
            this.activeSimulatorId = simulatorInstance.id;
        }

        this._notifyListeners('registered', simulatorInstance);
    }

    /**
     * Retorna a lista de todos os simuladores registrados na ordem de inserção.
     * @returns {import('./SimulatorBase.js').SimulatorBase[]}
     */
    getAll() {
        return Array.from(this.simulators.values());
    }

    /**
     * Retorna um simulador específico pelo seu identificador ID.
     * @param {string} id
     * @returns {import('./SimulatorBase.js').SimulatorBase|undefined}
     */
    get(id) {
        return this.simulators.get(id);
    }

    /**
     * Retorna o simulador atualmente ativo na interface.
     * @returns {import('./SimulatorBase.js').SimulatorBase|null}
     */
    getActive() {
        if (!this.activeSimulatorId) return null;
        return this.simulators.get(this.activeSimulatorId) || null;
    }

    /**
     * Altera o simulador ativo e notifica a interface.
     * @param {string} id
     */
    setActive(id) {
        if (!this.simulators.has(id)) {
            console.warn(`Simulador com ID '${id}' não foi encontrado.`);
            return;
        }
        if (this.activeSimulatorId === id) return;

        this.activeSimulatorId = id;
        this._notifyListeners('activeChanged', this.getActive());
    }

    /**
     * Inscreve um ouvinte para alterações no registro.
     * @param {Function} callback
     */
    subscribe(callback) {
        this.listeners.add(callback);
        return () => this.listeners.delete(callback);
    }

    _notifyListeners(event, data) {
        for (const listener of this.listeners) {
            try {
                listener(event, data);
            } catch (err) {
                console.error("Erro no listener do SimulatorsRegistry:", err);
            }
        }
    }
}

// Exporta instância singleton para toda a aplicação
export const globalRegistry = new SimulatorsRegistry();
