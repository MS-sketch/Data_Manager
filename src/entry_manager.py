import sqlite3
import dataencryptor
import dataencryptor as crypt

def create_blank_table():
    dataencryptor.keychk()

    conn = sqlite3.connect("vault_data.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS default_dir(
        "id" INT PRIMARY KEY,
        "title" TEXT NOT NULL,
        "website_name" TEXT NOT NULL,
        "is_default" BOOL NOT NULL,
        "user_name" TEXT NOT NULL,
        "password" TEXT NOT NULL,
        "notes" TEXT NOT NULL
        )
        
        """)

    conn.commit()

def insert_in_default(id, title, website, is_default, user_name, password, notes):
    conn = sqlite3.connect("vault_data.db")
    cursor = conn.cursor()

    notes_val = ""

    if notes == "":
        notes_val = "NUL"

    else:
        notes_val = crypt.Encrypt(notes)

    title_encrypt = crypt.Encrypt(title)
    website_encrypt = crypt.Encrypt(str(website))
    user_name_encrypt = crypt.Encrypt(str(user_name))
    password_encrypt = crypt.Encrypt(str(password))

    cursor.execute("INSERT INTO default_dir VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (id, title_encrypt, website_encrypt, is_default, user_name_encrypt, password_encrypt, notes_val))

    conn.commit()

def fetch_from_default(id):
    conn = sqlite3.connect("vault_data.db")
    cursor = conn.cursor()

    #Website
    cursor.execute("SELECT website_name FROM default_dir WHERE id = ?", (id,))
    decrypt_website = crypt.Decrypt(cursor.fetchone()[0])

    #User
    cursor.execute("SELECT user_name FROM default_dir WHERE id = ?", (id,))
    decrypt_usr = crypt.Decrypt(cursor.fetchone()[0])

    #Password
    cursor.execute("SELECT password FROM default_dir WHERE id = ?", (id,))
    decrypt_pass = crypt.Decrypt(cursor.fetchone()[0])

    #Chk
    cursor.execute("SELECT is_default FROM default_dir WHERE id = ?", (id,))
    is_default = cursor.fetchone()[0]

    #Title
    cursor.execute("SELECT title FROM default_dir WHERE id = ?", (id,))
    title_decrypt = crypt.Decrypt(cursor.fetchone()[0])

    #Notes
    cursor.execute("SELECT notes FROM default_dir WHERE id = ?", (id,))
    value_of_note = cursor.fetchone()[0]

    note_val = ""

    if value_of_note == "NUL":
        note_val = ""

    else:
        note_val = crypt.Decrypt(value_of_note)

    return [id, title_decrypt, decrypt_website, is_default, decrypt_usr, decrypt_pass, note_val]

def update_create_entry(id, title, website, is_default, user_name, password, notes):
    conn = sqlite3.connect("vault_data.db")
    cursor = conn.cursor()

    title_encrypt = crypt.Encrypt(title)
    website_encrypt = crypt.Encrypt(str(website))
    user_name_encrypt = crypt.Encrypt(str(user_name))
    password_encrypt = crypt.Encrypt(str(password))

    notes_encrypt = ""
    if notes == "NUL":
        notes_encrypt = ""

    else:
        notes_encrypt = crypt.Encrypt(str(notes))


    try:
        cursor.execute("""
        
        UPDATE default_dir

        SET title = ?, website_name = ?, is_default = ?, user_name = ?, password = ?, notes = ?

        WHERE id = ?
        
        """, 
        (title_encrypt, website_encrypt, is_default, user_name_encrypt, password_encrypt, notes_encrypt, id))
        conn.commit()

    except:
        return 1

def delete_entry_from_default(id):
    conn = sqlite3.connect("vault_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    
    DELETE FROM default_dir
    
    WHERE id = ?
    
    """, (id,))

    conn.commit()

def index_entry():
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS index_for_default(
    index_number INT PRIMARY KEY
    )
    """)

    conn.commit()

def fetch_all_from_index_entry():
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT index_number FROM index_for_default
    """)

    return cursor.fetchall()

def insert_into_index(id):
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO index_for_default VALUES (?)
    """, (id,))

    conn.commit()

def delete_from_index(id):
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM index_for_default
    
    WHERE index_number = ?
    """, (id,))

    conn.commit()

