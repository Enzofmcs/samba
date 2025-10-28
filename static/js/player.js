/**
 * Sistema de controle de áudio para bateria de samba
 * Gerencia play/pause/stop e ativação/desativação de instrumentos
 */

class PlayerBateria {
    constructor() {
        this.audios = {};
        this.isPlaying = false;
        this.isPaused = false;
        
        this.init();
    }
    
    init() {
        // Selecionar todos os cards de instrumentos
        const cards = document.querySelectorAll('.instrumento-card');
        
        cards.forEach(card => {
            const instrumentoId = card.dataset.instrumento;
            const audioElement = document.getElementById(`audio-${instrumentoId}`);
            
            // Armazenar referência ao áudio
            this.audios[instrumentoId] = {
                element: audioElement,
                card: card,
                ativo: true
            };
            
            // Adicionar evento de clique no card
            card.addEventListener('click', () => {
                this.toggleInstrumento(instrumentoId);
            });
        });
        
        // Configurar botões de controle
        document.getElementById('btn-play').addEventListener('click', () => {
            this.play();
        });
        
        document.getElementById('btn-pause').addEventListener('click', () => {
            this.pause();
        });
        
        document.getElementById('btn-stop').addEventListener('click', () => {
            this.stop();
        });
        
        // Sincronizar todos os áudios ao carregar
        this.sincronizarAudios();
    }
    
    /**
     * Ativa ou desativa um instrumento
     */
    toggleInstrumento(instrumentoId) {
        const audio = this.audios[instrumentoId];
        
        if (!audio) return;
        
        audio.ativo = !audio.ativo;
        
        // Atualizar visual do card
        if (audio.ativo) {
            audio.card.classList.add('ativo');
            audio.card.querySelector('.instrumento-status').textContent = 'Ativo';
            
            // Se estiver tocando, iniciar este áudio
            if (this.isPlaying) {
                audio.element.play();
            }
        } else {
            audio.card.classList.remove('ativo');
            audio.card.querySelector('.instrumento-status').textContent = 'Inativo';
            
            // Pausar o áudio
            audio.element.pause();
        }
    }
    
    /**
     * Inicia a reprodução de todos os instrumentos ativos
     */
    play() {
        if (this.isPlaying && !this.isPaused) {
            return; // Já está tocando
        }
        
        this.isPlaying = true;
        this.isPaused = false;
        
        // Sincronizar e tocar todos os áudios ativos
        Object.values(this.audios).forEach(audio => {
            if (audio.ativo) {
                audio.element.play().catch(err => {
                    console.error(`Erro ao tocar ${audio.element.id}:`, err);
                });
            }
        });
        
        this.atualizarBotoes();
    }
    
    /**
     * Pausa a reprodução de todos os instrumentos
     */
    pause() {
        if (!this.isPlaying) {
            return; // Não está tocando
        }
        
        this.isPaused = true;
        
        Object.values(this.audios).forEach(audio => {
            audio.element.pause();
        });
        
        this.atualizarBotoes();
    }
    
    /**
     * Para a reprodução e volta ao início
     */
    stop() {
        this.isPlaying = false;
        this.isPaused = false;
        
        Object.values(this.audios).forEach(audio => {
            audio.element.pause();
            audio.element.currentTime = 0;
        });
        
        this.atualizarBotoes();
    }
    
    /**
     * Sincroniza todos os áudios para começarem juntos
     */
    sincronizarAudios() {
        // Garantir que todos começam no tempo 0
        Object.values(this.audios).forEach(audio => {
            audio.element.currentTime = 0;
        });
    }
    
    /**
     * Atualiza o estado visual dos botões
     */
    atualizarBotoes() {
        const btnPlay = document.getElementById('btn-play');
        const btnPause = document.getElementById('btn-pause');
        const btnStop = document.getElementById('btn-stop');
        
        if (this.isPlaying && !this.isPaused) {
            btnPlay.disabled = true;
            btnPause.disabled = false;
            btnStop.disabled = false;
        } else if (this.isPaused) {
            btnPlay.disabled = false;
            btnPause.disabled = true;
            btnStop.disabled = false;
        } else {
            btnPlay.disabled = false;
            btnPause.disabled = true;
            btnStop.disabled = true;
        }
    }
}

// Inicializar o player quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    window.player = new PlayerBateria();
});
