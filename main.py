from flask import Flask, render_template, request
from datetime import datetime
from grafico import generar_grafico_servicios

app = Flask(__name__)

generar_grafico_servicios()

@app.before_request
def log_request_info():
    ruta = request.path
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{hora}] Ruta accedida: {ruta}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/analitica')
def analitica():
    return render_template('analitica.html')

if __name__ == "__main__":
    app.run(debug=True)