import psycopg2
from config import db_config

def create_tables():
    commands = (
        """CREATE TABLE IF NOT EXISTS phonebook (
                contact_id SERIAL PRIMARY KEY ,
                username VARCHAR(50) NOT NULL,
                first_name VARCHAR(50), 
                phone_number VARCHAR(20) NOT NULL
        )
        """,
    )
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        print("Table is create")
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    create_tables()