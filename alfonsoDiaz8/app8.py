import os
import time
import psycopg2
from psycopg2 import OperationalError

# Cargar variables de entorno del sistema
DB_HOST = os.getenv('DB_HOST', 'dbprueba8')
DB_NAME = os.getenv('DB_NAME', 'facturacion8')
DB_USER = os.getenv('DB_USER', 'usuario8')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'luna')
DB_PORT = os.getenv('DB_PORT', '5432')

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
        print("Conexión exitosa al módulo de Facturación ERP")
        break
    except OperationalError as e:
        print(f"Esperando a PostgreSQL... ({e})")
        time.sleep(3)

if conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id SERIAL PRIMARY KEY,
            cliente VARCHAR(100) NOT NULL,
            total_eur NUMERIC(10, 2) NOT NULL,
            creado_por VARCHAR(100) NOT NULL
        )
    ''')
    
    # Insertar factura inicial
    cursor.execute(
        "INSERT INTO invoices (cliente, total_eur, creado_por) VALUES (%s, %s, %s)",
        ("Empresa Cliente S.A.", 1250.50, "Alfonso Díaz Morales")
    )
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla 'invoices' creada y factura registrada correctamente.")
else:
    print("No se pudo conectar a la base de datos.")

print("Nueva actualizacion.....")
