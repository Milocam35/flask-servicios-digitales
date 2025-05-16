import matplotlib.pyplot as plt
import os

def generar_grafico_servicios():
    servicios = ['Asesoría de Inversiones', 'Planeación Financiera', 'Análisis de Riesgo Financiero']
    contratados = [34, 27, 19]
    colores = ['#1a237e', '#3949ab', '#90caf9']

    plt.figure(figsize=(7, 5))
    plt.bar(servicios, contratados, color=colores)
    plt.title('Servicios más contratados')
    plt.ylabel('Veces Contratado')
    plt.tight_layout()

    static_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
    os.makedirs(static_dir, exist_ok=True)
    plt.savefig(os.path.join(static_dir, 'servicios_grafico.png'))
    plt.close()