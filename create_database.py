import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "empresa"
DB_USER = "curro"
DB_PASSWORD = "1"
DB_HOST = "localhost"

def create_db():
    try:
        
        connection = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"✅ Base de datos '{DB_NAME}' creada.")
        else:
            print(f"ℹ️ La base de datos '{DB_NAME}' ya existe.")

        cursor.close()
        connection.close()

    except Exception as e:
        print("❌ Error al crear la base de datos:", e)

if __name__ == "__main__":
    create_db()
