import psycopg2
import csv
import json
from connect import get_connection

def display_menu():
    print("\n" + "="*30)
    print("   PHONEBOOK MANAGER PRO")
    print("="*30)
    print("1. Search (Name/Email/Phone)")
    print("2. Filter by Group (Case-insensitive)")
    print("3. Add/Update Contact & Group (Smart)")
    print("4. Move Contact to Group")
    print("5. Paginated View & Sorting")
    print("6. Export to JSON")
    print("8. IMPORT FROM CSV (Email & Birthday)")
    print("0. EXIT")
    print("-" * 30)
    return input("Choose option: ")

# --- РАБОТА С КОНТАКТАМИ (Умное добавление) ---

def add_smart_contact():
    print("\n--- Smart Add/Update ---")
    name = input("Name: ")
    phone = input("Phone Number: ")
    p_type = input("Type (home/work/mobile): ")
    email = input("Email (optional): ")
    bday = input("Birthday (YYYY-MM-DD, optional): ")
    group_name = input("Group Name: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                # --- ВОТ ЭТОТ БЛОК НУЖНО ИЗМЕНИТЬ ---
                # 1. Умный поиск группы через ILIKE
                g_id = None
                if group_name:
                    # Ищем группу, игнорируя регистр (friend == Friend)
                    cur.execute("SELECT id FROM groups WHERE name ILIKE %s", (group_name,))
                    existing_group = cur.fetchone()
                    
                    if existing_group:
                        g_id = existing_group[0] # Если нашли похожую, берем её ID
                    else:
                        # Если не нашли — создаем новую
                        cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
                        g_id = cur.fetchone()[0]
                # ------------------------------------

                # 2. Upsert контакта
                cur.execute("""
                    INSERT INTO contacts (name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (name) DO UPDATE 
                    SET email = COALESCE(NULLIF(EXCLUDED.email, ''), contacts.email),
                        birthday = COALESCE(NULLIF(EXCLUDED.birthday, NULL), contacts.birthday),
                        group_id = COALESCE(EXCLUDED.group_id, contacts.group_id)
                    RETURNING id
                """, (name, email if email else None, bday if bday else None, g_id))
                
                c_id = cur.fetchone()[0]

                # 3. Добавляем телефон (тип должен быть home/work/mobile из-за CONSTRAINT)
                cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                            (c_id, phone, p_type))
                
                conn.commit()
                print(f"\n[✔] Done! Contact '{name}' saved.")
    except Exception as e:
        print(f"\n[!] Error: {e}")

# --- РАБОТА С ФАЙЛАМИ ---

def import_from_csv(file_name='contacts.csv'):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                with open(file_name, mode='r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        group_name = row.get('group', 'Other')
                        cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT DO NOTHING", (group_name,))
                        cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
                        g_id = cur.fetchone()[0]

                        cur.execute("""
                            INSERT INTO contacts (name, email, birthday, group_id)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (name) DO UPDATE 
                            SET email = EXCLUDED.email, 
                                birthday = EXCLUDED.birthday, 
                                group_id = EXCLUDED.group_id
                            RETURNING id
                        """, (row['name'], row['email'], row.get('birthday'), g_id))
                        c_id = cur.fetchone()[0]

                        cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                                    (c_id, row['phone'], row.get('type', 'mobile')))
                conn.commit()
        print("\n[✔] Import from CSV successful!")
    except FileNotFoundError:
        print("\n[!] File 'contacts.csv' not found!")
    except Exception as e:
        print(f"\n[!] Error: {e}")

def export_to_json():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT c.name, c.email, c.birthday, g.name as group_name, array_agg(p.phone) as phones
                    FROM contacts c 
                    LEFT JOIN groups g ON c.group_id = g.id
                    LEFT JOIN phones p ON c.id = p.contact_id
                    GROUP BY c.id, g.name
                """)
                rows = cur.fetchall()
                data = [{"name": r[0], "email": r[1], "birthday": str(r[2]), "group": r[3], "phones": r[4]} for r in rows]
                with open('contacts.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print("\n[✔] Data exported to contacts.json")
    except Exception as e:
        print(f"\n[!] Export error: {e}")

# --- ИНТЕРФЕЙС, ПОИСК И СОРТИРОВКА ---

def paginated_view():
    print("\n--- Choose sorting order ---")
    print("1. By Name (A-Z)")
    print("2. By Birthday (Oldest first)")
    print("3. By Date Added (Newest first)")
    sort_choice = input("Sort by: ")

    # Настройка сортировки
    if sort_choice == "2":
        order_by = "c.birthday ASC"
    elif sort_choice == "3":
        order_by = "c.id DESC"
    else:
        order_by = "c.name ASC"

    limit = 5
    offset = 0
    while True:
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    # ИСПРАВЛЕННЫЙ ЗАПРОС: добавляем JOIN для групп и телефонов
                    cur.execute(f"""
                        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
                        FROM contacts c
                        LEFT JOIN groups g ON c.group_id = g.id
                        LEFT JOIN phones p ON c.id = p.contact_id
                        ORDER BY {order_by} 
                        LIMIT %s OFFSET %s
                    """, (limit, offset))
                    
                    rows = cur.fetchall()
                    
                    print(f"\n--- Page {(offset//limit)+1} (Sorted: {order_by}) ---")
                    if not rows:
                        print("No contacts found.")
                    for r in rows: 
                        # r[0]-имя, r[1]-email, r[2]-bday, r[3]-группа, r[4]-телефон, r[5]-тип
                        group = r[3] if r[3] else "No Group"
                        phone = r[4] if r[4] else "No Phone"
                        p_type = r[5] if r[5] else ""
                        print(f"👤 {r[0]} | Group: {group} | Phone: {phone} ({p_type}) | B-day: {r[2]}")
                    
                    cmd = input("\n[n]ext page, [p]revious, [q]uit: ").lower()
                    if cmd == 'n': offset += limit
                    elif cmd == 'p': offset = max(0, offset - limit)
                    else: break
        except Exception as e:
            print(f"Error in pagination: {e}")
            break

def main():
    while True:
        choice = display_menu()
        if choice == "0": break
        
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    if choice == "1":
                        q = input("Search query: ")
                        # Используем надежный поиск по всем полям через SQL
                        cur.execute("""
                            SELECT c.name, c.email, p.phone, g.name
                            FROM contacts c
                            LEFT JOIN phones p ON c.id = p.contact_id
                            LEFT JOIN groups g ON c.group_id = g.id
                            WHERE c.name ILIKE %s OR c.email ILIKE %s OR p.phone ILIKE %s
                        """, (f'%{q}%', f'%{q}%', f'%{q}%'))
                        results = cur.fetchall()
                        if not results:
                            print("\n[!] No contacts found.")
                        for r in results: 
                            print(f"Found: {r[0]} | Email: {r[1]} | Phone: {r[2]} | Group: {r[3]}")
                    
                    elif choice == "2":
                        g = input("Group name: ")
                        cur.execute("""SELECT c.name, g.name FROM contacts c 
                                       JOIN groups g ON c.group_id = g.id 
                                       WHERE g.name ILIKE %s""", (g,))
                        for r in cur.fetchall(): print(f"Contact: {r[0]} | Group: {r[1]}")

                    elif choice == "3":
                        add_smart_contact()

                    elif choice == "4":
                        name, g_name = input("Name: "), input("New Group: ")
                        cur.execute("CALL move_to_group(%s, %s)", (name, g_name))
                        conn.commit()
                        print("[✔] Group updated!")

                    elif choice == "5": paginated_view()
                    elif choice == "6": export_to_json()
                    elif choice == "8": import_from_csv()
        except Exception as e:
            print(f"\n[!] Database error: {e}")

if __name__ == "__main__":
    main()