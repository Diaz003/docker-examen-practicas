from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Gateway IoT Industria 4.0")

# TODO: El alumno debe personalizar sus datos en estas variables
NOMBRE_ALUMNO = "Alfonso"
APELLIDOS_ALUMNO = "Diaz Morales"
LINEA_PRODUCCION = "Línea Ensamblaje IES CASTILLO DE LUNA"

@app.get("/")
def inicio():
    return {
        "sistema": "Gateway IoT Industria 4.0",
        "mensaje": "Servidor de telemetría operativo",
        "estado": "ONLINE"
    }

@app.get("/operador")
def obtener_operador():
    return {
        "operador": f"{NOMBRE_ALUMNO} {APELLIDOS_ALUMNO}",
        "linea_asignada": LINEA_PRODUCCION,
        "rol": "Técnico de Despliegue DAM"
    }

@app.get("/telemetria")
def obtener_telemetria():
    return {
        "timestamp": datetime.now().isoformat(),
        "sensores": {
            "temperatura_c": 98.6,
		    "presion_bar": 4.850, 
		    "vibracion_hz": 450.8,
		    "estado_robot": "CRITICO"
        }
    }
