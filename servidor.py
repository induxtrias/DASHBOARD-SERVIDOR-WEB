import random
import time
import threading
from flask import Flask, jsonify, render_template

# Inicializar Flask
app = Flask(__name__)

# Variables globales para almacenar los datos
sensores_data = {}

# Función que genera datos aleatorios para los sensores
def generar_datos():
    global sensores_data
    sensores_data = {
        "Temperatura": round(random.uniform(-10, 40), 2),  # Temperatura en °C
        "Presión": round(random.uniform(900, 1100), 2),  # Presión en hPa
        "Nivel": round(random.uniform(0, 100), 2),  # Nivel (porcentaje)
        "Radiación Solar": round(random.uniform(0, 1000), 2),  # Radiación solar (W/m²)
        "Humedad": round(random.uniform(0, 100), 2),  # Humedad (%)
        "Velocidad del Viento": round(random.uniform(0, 50), 2),  # Velocidad del viento (km/h)
        "pH": round(random.uniform(0, 14), 2),  # pH del agua
        "Oxígeno Disuelto": round(random.uniform(0, 10), 2),  # Oxígeno disuelto (mg/L)
        "Radiación UV": round(random.uniform(0, 15), 2),  # Radiación UV (UVI)
        "Lluvia": round(random.uniform(0, 100), 2),  # Lluvia en mm
    }

# Función que simula el servidor generando datos cada 5 segundos
def simular_datos():
    while True:
        generar_datos()
        time.sleep(5)

# Ruta para la página de dashboard
@app.route('/')
def index():
    return render_template('dashboard.html', datos=sensores_data)

# Ruta para obtener los datos en formato JSON
@app.route('/api/datos')
def api_datos():
    return jsonify(sensores_data)

# Iniciar servidor web
if __name__ == "__main__":
    # Iniciar la simulación de datos en un hilo separado
    threading.Thread(target=simular_datos, daemon=True).start()
    
    # Iniciar Flask en el puerto 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
