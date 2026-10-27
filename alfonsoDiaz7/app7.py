import time
import psycopg2
from psycopg2 import OperationalError

# Conexión con reintentos a PostgreSQL
conn = None
for _ in range(10):
    try:
        conn = psycopg2.connect(
            host='dbprueba7',
            database='basedatos7',
            user='usuario7',
            password='luna',
            port=5432
        )
        print("Conexión exitosa a la base de datos PostgreSQL")
        break
    except OperationalError as e:
        print("Esperando a la base de datos PostgreSQL...")
        time.sleep(3)

if conn:
    cursor = conn.cursor()
    
    # Crear tabla de productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            registrado_por VARCHAR(100) NOT NULL,
            producto VARCHAR(100) NOT NULL
        )
    ''')
    
    # TODO: Cambiar por vuestro nombre y apellidos
    cursor.execute(
        "INSERT INTO products (registrado_por, producto) VALUES (%s, %s)",
        ("Alfonso Díaz Morales", "Licencia ERP SAP")
    )
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla 'products' creada con éxito y datos insertados.")
else:
    print("No se pudo conectar a PostgreSQL.")

