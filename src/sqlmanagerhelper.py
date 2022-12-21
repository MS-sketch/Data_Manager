import sqlite3


def type(type):
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS type(
        id INTEGER PRIMARY KEY,
        method TEXT NOT NULL)
        """)

    info = str(dynamic_table_fetch("type", "method", "usr_settings.db"))
    if info == "[]":
        password = type
        cursor.execute("INSERT INTO type (method) VALUES(?)", [password])
        conn.commit()

    else:
        password = type
        cursor.execute("UPDATE type SET method = ? WHERE id = 1 ", [password])
        conn.commit()


"""""def prompt_username(con):
    cur = con.cursor()
    while True:
        username = input("Enter User Name : ")
        cur.execute("SELECT COUNT(*) FROM pg_catalog.pg_roles WHERE rolname = %s", [username])
        n, = cur.fetchone()
        if n == 0:
            return username
        print("User already exists.")


def userCreation(username, password):
    con = psycopg2.connect(
        user=username,
        host='localhost',
        password=password,
        database='main_settings'
    )

    username = prompt_username(con)
    password = input(f"Enter Password for {username} : ")
    query = sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1}").format(
        sql.Identifier(username),
        sql.Literal(password),
    )
    cur = con.cursor()
    cur.execute(query.as_string(con))
    cur.execute("COMMIT")
"""""

def masterpasswordsave(password_hash):
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS masterpassword(
        id INTEGER PRIMARY KEY,
        hash TEXT NOT NULL)
        """)

    cursor.execute("INSERT INTO masterpassword (hash) VALUES(?)", [password_hash])
    conn.commit()


def getmasterpassword(masterpasswordtobechecked):
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND hash = ?", [masterpasswordtobechecked])
    return cursor.fetchall()


def dynamic_table_fetch(table_name, what_to_select, database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT " + str(what_to_select) + " FROM " + str(table_name) + " WHERE id = 1")
    return cursor.fetchall()


def dynamic_table_create(database_name, table_name, feild_name, field_prop):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS " + str(table_name) + "(id INTEGER PRIMARY KEY, " + str(feild_name) + " " +
        str(field_prop) + ")")
    conn.commit()


def dynamic_insert(database_name, table_name, info_to_be_insert, feild_to_be_data_value):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO  " + str(table_name) + " (" + str(feild_to_be_data_value) + ") VALUES(?)",
                   [info_to_be_insert])
    conn.commit()


def admin_create(admin_name_hash, password_hash):
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS admin_account(
            id INTEGER PRIMARY KEY,
            admin_name_hash TEXT NOT NULL,
            hash TEXT NOT NULL)
            """)

    cursor.execute("INSERT INTO admin_account (admin_name_hash, hash) VALUES(?,?)",
                   [(admin_name_hash), (password_hash)])
    conn.commit()


def table_check():
    conn = sqlite3.connect("usr_settings.db")
    cursor = conn.cursor()

    try:
        try:
            cursor.execute("SELECT * FROM masterpassword")
            return "single_user"

        except:
            cursor.execute("")
            return "multiple_user"

    except:
        return "nothing"
