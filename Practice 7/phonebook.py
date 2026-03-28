import psycopg2
import csv
from config import db_config

def get_conn():
    return psycopg2.connect(**db_config)



def insert_from_csv(file_path):
    conn = get_conn()
    cur = conn.cursor()

    try:
        with open(file_path, 'r' , encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                    sql = """INSERT INTO phonebook 
                             (username, first_name, phone_number)
                             VALUES (%s, %s, %s)"""
                    cur.execute(sql, (row[0], row[1], row[2]))
                
        conn.commit()
        print("Successfully")
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def add_new_contact():
    user = input()
    name = input()
    phone = input()

    conn = get_conn()
    cur = conn.cursor()
    sql = """INSERT INTO phonebook
             (username, first_name, phone_number)
             VALUES (%s, %s, %s)"""
    cur.execute(sql, (user, name, phone))
    conn.commit()
    print("Append")
    cur.close()
    conn.close()

def find_contact(pattern):
        conn = get_conn()
        cur = conn.cursor()
        sql = "SELECT * FROM phonebook WHERE first_name ILIKE %s"
        cur.execute(sql, (f'%{pattern}%',))

        rows = cur.fetchall()
        print(f"\nFind '{pattern}':")
        for row in rows:
            print(row)
        cur.close()
        conn.close()


if __name__ == "__main__":
    insert_from_csv('contacts.csv')
    add_new_contact()
    name = input()
    find_contact(name)