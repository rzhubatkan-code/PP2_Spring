import psycopg2
from config import db_config

def get_connection():
    return psycopg2.connect(**db_config)

def create_tables():
    conn = None
    try:
        conn = get_connection()
        print("Connection successful")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()