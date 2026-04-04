import psycopg2
from config import db_config

def get_connection():
    return psycopg2.connect(**db_config)

def create_tables():
    conn=None
    try:
        conn = get_connection()
        cur = conn.cursor()
        conn.commit()
        print("Table is Create")
    except Exception as e:
        print(e)
    finally:
        if conn: conn.close()