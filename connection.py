import psycopg2

# Conectar a la base de datos
def get_connection():
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="Kenny_Zhu158",
        database="aves"
    )

# Consulta de datos
def fetch_data(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data