import psycopg2
try:    
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="Kenny_Zhu158",
        database="aves"
    )
    print("Conexion exitosa")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aves")
except Exception as e:
    print(f"Ocurrio un error: {e}")