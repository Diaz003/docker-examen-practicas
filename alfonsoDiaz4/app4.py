import time
import mysql.connector
from mysql.connector import Error

# Configuración de la conexión a la base de datos
while True:
    try:
        conn = mysql.connector.connect(
            host='dbprueba4',  # nombre del servicio en docker-compose
            user='usuario4',
            password='luna',
            database='basedatos4'
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
            break
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        print("Reintentando en 5 segundos...")
        time.sleep(5)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Crear la tabla 'employees' si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
)
''')

# Insertar datos en la tabla
cursor.execute('INSERT INTO employees (name) VALUES (%s)', ('Alfonso Diaz',))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Tabla 'employees' creada con éxito y datos insertados.")

