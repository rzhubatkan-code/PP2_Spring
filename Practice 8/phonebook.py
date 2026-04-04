import psycopg2
from connect import get_connection

def display_menu():
    print("\n phonebook")
    print("1. Find contact (SEARCH)")
    print("2. Append contact (UPSERT)")
    print("3. (FOR, WHILE)")
    print("4. Show all contacts (PAGINATION)")
    print("5. Delete contact")
    print("0. EXIT")
    return input("Choose function:")

def main():
    while True:
        user_choice = display_menu()
        if user_choice == "0":
            print("Error")
            break
        connection = None
        cursor = None
      
        try:
            connection = get_connection()
            cursor = connection.cursor()
            if user_choice == "1":
                pattern = input("Pattern")
                cursor.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
                rows = cur.fetchall()
                for row in rows:
                    print(f"name: {row[0]}, phone: {row[1]}")
            elif user_choice == "2":
                name = input("name")
                phone = input("phone")
                cursor.execute("CALL upsert_contact(%s, 5s)", (name , phone))
                conn.commit()
                print("done")
            elif user_choice == '3':
                names = ['Adil' , 'Arman' , 'Aya']
                phones = ['87071111223', '87087895667', '123']
                cursor.execute("CALL insert_members(%s, %s)", (names , phones))
                conn.commit()
                print("done")
            elif user_choice =='4':
                limit = int(input("length"))
                offset= int(input("step"))
                cursor.execute("SELECT * FROM get_contacts_paged(%s, %s)", (limit, offset))
                rows = cur.fetchall()
                for row in rows: print(f"Name {row[0]}, Phone {row[1]}")

            elif user_choice == '5':
                search = input("name or phone")
                cursor.execute("CALL delete_contact(%s)", (search,))
                conn.commit()
                print("Delete")

            elif user_choice == '0':
                break
        except Exception as e:
            print(f"Error {e}")
            if connection:
                connection.rollback()
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
          

if __name__ == "__main__":
    main()