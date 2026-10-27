import os
import time
import psycopg2
from psycopg2 import OperationalError
from fastapi import FastAPI

app = FastAPI(title="Módulo de Ventas ERP")

DB_HOST = os.getenv('DB_HOST', 'dbprueba9')
DB_NAME = os.getenv('DB_NAME', 'ventas9')
DB_USER = os.getenv('DB_USER', 'usuario9')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'luna')
DB_PORT = os.getenv('DB_PORT', '5432')

# Inicialización de la BD
def init_db():
    conn = None
    for _ in range(10):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=DB_PORT
            )
            break
        except OperationalError:
            time.sleep(2)
    
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id SERIAL PRIMARY KEY,
                articulo VARCHAR(100) NOT NULL,
                cantidad INT NOT NULL,
                vendedor VARCHAR(100) NOT NULL
            )
        ''')
        # Insertar venta de prueba si está vacía
        cursor.execute("SELECT COUNT(*) FROM sales")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO sales (articulo, cantidad, vendedor) VALUES (%s, %s, %s)",
                ("Teclado Mecánico RGB", 3, "Alfonso Díaz Morales")
            )
        conn.commit()
        cursor.close()
        conn.close()

init_db()

@app.get("/")
def home():
    return {
        "modulo": "ERP Ventas Gateway",
        "estado": "ONLINE",
        "vendedor_principal": "Alfonso Díaz Morales"
    }

@app.get("/ventas")
def obtener_ventas():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, articulo, cantidad, vendedor FROM sales;")
        filas = cursor.fetchall()
        cursor.close()
        conn.close()

        ventas = [{"id": f[0], "articulo": f[1], "cantidad": f[2], "vendedor": f[3]} for f in filas]
        return {"total_ventas": len(ventas), "registros": ventas}
    except Exception as e:
        return {"error": str(e)}
