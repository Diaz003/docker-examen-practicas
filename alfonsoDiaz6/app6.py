from flask import Flask, jsonify

app = Flask(__name__)

# TODO: Editar con vuestros datos
NOMBRE_ALUMNO = "Alfonso"
APELLIDOS_ALUMNO = "Diaz Morales"
ALMACEN_ASIGNADO = "Almacén Central Castillo de Luna"

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({
        "sistema": "ERP Módulo de Inventarios",
        "operador": f"{NOMBRE_ALUMNO} {APELLIDOS_ALUMNO}",
        "ubicacion": ALMACEN_ASIGNADO,
        "estado_modulo": "ACTIVO"
    })

@app.route('/stock', methods=['GET'])
def obtener_stock():
    return jsonify({
        "producto_id": "REF-8840",
        "descripcion": "Sensor Industrial Lidar",
        "unidades_disponibles": 145,
        "stock_critico": False
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
