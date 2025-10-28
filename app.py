# -*- coding: utf-8 -*-
"""
Aplicação Flask para o site de ensaio de bateria de samba.
"""

from flask import Flask, render_template, jsonify
from config import BOSSAS, ORDEM_INSTRUMENTOS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    """Página principal com a lista de bossas disponíveis."""
    return render_template('index.html', bossas=BOSSAS.values())


@app.route('/player/<bossa_id>')
def player(bossa_id):
    """Página do player para uma bossa específica."""
    if bossa_id not in BOSSAS:
        return "Bossa não encontrada", 404
    
    bossa = BOSSAS[bossa_id]
    return render_template(
        'player.html',
        bossa=bossa,
        ordem_instrumentos=ORDEM_INSTRUMENTOS
    )


@app.route('/api/bossas')
def api_bossas():
    """API JSON com todas as bossas disponíveis."""
    return jsonify(list(BOSSAS.values()))


@app.route('/api/bossa/<bossa_id>')
def api_bossa(bossa_id):
    """API JSON com informações de uma bossa específica."""
    if bossa_id not in BOSSAS:
        return jsonify({'erro': 'Bossa não encontrada'}), 404
    
    return jsonify(BOSSAS[bossa_id])


if __name__ == '__main__':
    print("=" * 60)
    print("🥁 Site de Ensaio de Bateria de Samba")
    print("=" * 60)
    print(f"Bossas disponíveis: {len(BOSSAS)}")
    for bossa_id, bossa in BOSSAS.items():
        print(f"  - {bossa['nome']} ({bossa_id})")
    print("=" * 60)
    print("Servidor rodando em: http://127.0.0.1:5000")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
