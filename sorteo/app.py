from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sorteo', methods=['POST'])
def sorteo():
    data = request.get_json()  # Obtiene los datos como JSON
    participantes = data.get('participantes')
    lista_participantes = [p.strip() for p in participantes.split(',')]
    ganador = random.choice(lista_participantes)
    return jsonify({'ganador': ganador})  # Devuelve JSON con el ganador

if __name__ == '__main__':
    app.run(debug=True)