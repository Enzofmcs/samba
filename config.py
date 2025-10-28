# -*- coding: utf-8 -*-
"""
Configuração das bossas e instrumentos da bateria de samba.
Para adicionar uma nova bossa, basta adicionar uma entrada no dicionário BOSSAS.
"""

BOSSAS = {
    'bossa1': {
        'id': 'bossa1',
        'nome': 'Samba Enredo',
        'descricao': 'Bossa tradicional de samba enredo',
        'instrumentos': {
            'agogo': {
                'nome': 'Agogô',
                'arquivo': 'audio/bossa1/agogo.mp3'
            },
            'chocalho': {
                'nome': 'Chocalho',
                'arquivo': 'audio/bossa1/chocalho.mp3'
            },
            'tamborim': {
                'nome': 'Tamborim',
                'arquivo': 'audio/bossa1/tamborim.mp3'
            },
            'caixa': {
                'nome': 'Caixa',
                'arquivo': 'audio/bossa1/caixa.mp3'
            },
            'surdo1': {
                'nome': 'Surdo de Primeira',
                'arquivo': 'audio/bossa1/surdo1.mp3'
            },
            'surdo2': {
                'nome': 'Surdo de Segunda',
                'arquivo': 'audio/bossa1/surdo2.mp3'
            },
            'surdo3': {
                'nome': 'Surdo de Terceira',
                'arquivo': 'audio/bossa1/surdo3.mp3'
            },
            'repique': {
                'nome': 'Repique',
                'arquivo': 'audio/bossa1/repique.mp3'
            }
        }
    },
    'bossa2': {
        'id': 'bossa2',
        'nome': 'Samba de Quadra',
        'descricao': 'Bossa de samba de quadra',
        'instrumentos': {
            'agogo': {
                'nome': 'Agogô',
                'arquivo': 'audio/bossa2/agogo.mp3'
            },
            'chocalho': {
                'nome': 'Chocalho',
                'arquivo': 'audio/bossa2/chocalho.mp3'
            },
            'tamborim': {
                'nome': 'Tamborim',
                'arquivo': 'audio/bossa2/tamborim.mp3'
            },
            'caixa': {
                'nome': 'Caixa',
                'arquivo': 'audio/bossa2/caixa.mp3'
            },
            'surdo1': {
                'nome': 'Surdo de Primeira',
                'arquivo': 'audio/bossa2/surdo1.mp3'
            },
            'surdo2': {
                'nome': 'Surdo de Segunda',
                'arquivo': 'audio/bossa2/surdo2.mp3'
            },
            'surdo3': {
                'nome': 'Surdo de Terceira',
                'arquivo': 'audio/bossa2/surdo3.mp3'
            },
            'repique': {
                'nome': 'Repique',
                'arquivo': 'audio/bossa2/repique.mp3'
            }
        }
    }
}

# Ordem de exibição dos instrumentos
ORDEM_INSTRUMENTOS = [
    'agogo',
    'chocalho',
    'tamborim',
    'caixa',
    'surdo1',
    'surdo2',
    'surdo3',
    'repique'
]
