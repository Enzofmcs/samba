# 🥁 Site de Ensaio de Bateria de Samba

Site desenvolvido para ajudar ritmistas de bateria de escola de samba a ensaiarem em casa, permitindo controlar individualmente cada instrumento de uma bossa.

## ✨ Características

- **Interface bonita** com tema azul e amarelo pastel
- **Controle individual** de 8 instrumentos diferentes
- **Múltiplas bossas** disponíveis
- **Sincronização perfeita** de todos os áudios
- **Fácil expansão** para adicionar novas bossas

## 🎵 Instrumentos Disponíveis

1. Agogô
2. Chocalho
3. Tamborim
4. Caixa
5. Surdo de Primeira
6. Surdo de Segunda
7. Surdo de Terceira
8. Repique

## 🚀 Como Executar

### Requisitos

- Python 3.11 ou superior
- Flask (instalado automaticamente)

### Instalação

```bash
cd bateria-samba
pip3 install flask
```

### Executar o Servidor

```bash
python3 app.py
```

O site estará disponível em: **http://localhost:5000**

## 📁 Estrutura do Projeto

```
bateria-samba/
├── app.py                 # Aplicação Flask (backend)
├── config.py              # Configuração das bossas
├── static/
│   ├── css/
│   │   └── style.css      # Estilos (tema azul/amarelo pastel)
│   ├── js/
│   │   └── player.js      # Controle de áudio JavaScript
│   └── audio/
│       ├── bossa1/        # Arquivos MP3 da Bossa 1
│       └── bossa2/        # Arquivos MP3 da Bossa 2
└── templates/
    ├── index.html         # Página principal
    └── player.html        # Página do player
```

## 🎨 Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Áudio**: HTML5 Audio API

## ➕ Como Adicionar uma Nova Bossa

Adicionar uma nova bossa é muito simples:

### 1. Criar pasta com os áudios

```bash
mkdir static/audio/bossa3
```

### 2. Adicionar os 8 arquivos MP3

Coloque os seguintes arquivos na pasta criada:
- `agogo.mp3`
- `chocalho.mp3`
- `tamborim.mp3`
- `caixa.mp3`
- `surdo1.mp3`
- `surdo2.mp3`
- `surdo3.mp3`
- `repique.mp3`

### 3. Editar o arquivo `config.py`

Adicione uma nova entrada no dicionário `BOSSAS`:

```python
'bossa3': {
    'id': 'bossa3',
    'nome': 'Nome da Nova Bossa',
    'descricao': 'Descrição da nova bossa',
    'instrumentos': {
        'agogo': {
            'nome': 'Agogô',
            'arquivo': 'audio/bossa3/agogo.mp3'
        },
        'chocalho': {
            'nome': 'Chocalho',
            'arquivo': 'audio/bossa3/chocalho.mp3'
        },
        'tamborim': {
            'nome': 'Tamborim',
            'arquivo': 'audio/bossa3/tamborim.mp3'
        },
        'caixa': {
            'nome': 'Caixa',
            'arquivo': 'audio/bossa3/caixa.mp3'
        },
        'surdo1': {
            'nome': 'Surdo de Primeira',
            'arquivo': 'audio/bossa3/surdo1.mp3'
        },
        'surdo2': {
            'nome': 'Surdo de Segunda',
            'arquivo': 'audio/bossa3/surdo2.mp3'
        },
        'surdo3': {
            'nome': 'Surdo de Terceira',
            'arquivo': 'audio/bossa3/surdo3.mp3'
        },
        'repique': {
            'nome': 'Repique',
            'arquivo': 'audio/bossa3/repique.mp3'
        }
    }
}
```

### 4. Reiniciar o servidor

```bash
# Pressione Ctrl+C para parar o servidor
python3 app.py
```

Pronto! A nova bossa aparecerá automaticamente na página principal.

## 🎯 Como Usar o Site

### Página Principal

1. Acesse o site
2. Escolha uma bossa clicando no card correspondente

### Página do Player

1. Todos os instrumentos começam **ativos** (destacados)
2. **Clique em um instrumento** para ativá-lo ou desativá-lo
3. Use os botões de controle:
   - **▶ Play**: Inicia a reprodução de todos os instrumentos ativos
   - **⏸ Pause**: Pausa a reprodução
   - **⏹ Stop**: Para e volta ao início
4. Clique em **"← Voltar para lista de bossas"** para escolher outra bossa

## 📝 Notas Importantes

### Arquivos MP3 de Exemplo

Os arquivos MP3 incluídos são **silenciosos** (apenas para demonstração). Você deve substituí-los pelos áudios reais dos instrumentos da sua bateria.

### Sincronização de Áudio

O sistema usa a API de áudio HTML5 para garantir que todos os instrumentos toquem sincronizados. Os áudios devem ter:
- **Mesma duração**
- **Mesmo BPM** (batidas por minuto)
- **Mesmo ponto de início**

### Formato dos Arquivos

- Use arquivos **MP3** para melhor compatibilidade
- Recomenda-se **loop perfeito** (sem silêncio no início/fim)
- Taxa de bits recomendada: **128-192 kbps**

## 🎨 Personalização de Cores

Para alterar as cores do tema, edite o arquivo `static/css/style.css`:

```css
:root {
    /* Cores azul pastel */
    --azul-claro: #A8D8EA;
    --azul-medio: #6CB4E8;
    --azul-escuro: #4A90E2;
    
    /* Cores amarelo pastel */
    --amarelo-claro: #FFF9C4;
    --amarelo-medio: #FFE082;
    --amarelo-escuro: #FFD54F;
}
```

## 🐛 Solução de Problemas

### Os áudios não tocam

- Verifique se os arquivos MP3 estão na pasta correta
- Confirme que os nomes dos arquivos estão corretos (minúsculas)
- Abra o console do navegador (F12) para ver erros

### Áudios dessincronizados

- Certifique-se de que todos os MP3s têm a mesma duração
- Use software de edição de áudio para alinhar os arquivos

### Site não carrega

- Verifique se o Flask está instalado: `pip3 install flask`
- Confirme que a porta 5000 não está em uso
- Execute `python3 app.py` e verifique mensagens de erro

## 📄 Licença

Este projeto foi desenvolvido para uso educacional e comunitário em escolas de samba.

## 🤝 Contribuições

Para melhorias ou sugestões, edite diretamente os arquivos do projeto.

---

**Desenvolvido com ❤️ para os ritmistas de bateria de samba**
