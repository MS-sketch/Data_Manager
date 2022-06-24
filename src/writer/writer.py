def write(id, setting_name, value, OnOff1):
    def write2():
        import sqlite3
        import dataencryptor
        import existance

        f1 = existance.exists("universal.key")
        if f1 == "FALSE":
            dataencryptor.keychk()
            write2()

        else:
            conn = sqlite3.connect("data.dvb")
            cursor = conn.cursor()


            cursor.execute("CREATE TABLE IF NOT EXISTS SETTINGS (ID, SETTING_NAME, SETTING_OnOff, Setting_Value)")

            identity = dataencryptor.Encrypt(id)
            setname = dataencryptor.Encrypt(setting_name)
            setval = dataencryptor.Encrypt(value)
            onoff = dataencryptor.Encrypt(str(OnOff1))
            cursor.execute("insert into SETTINGS (ID, SETTING_NAME, SETTING_OnOff, Setting_Value) values (?, ?, ?, ?)",
                           (identity, setname, setval, onoff))

            conn.commit()

            cursor.execute("SELECT * FROM SETTINGS")

            print(str(cursor.lastrowid) + " Last Row")

            rows = cursor.fetchall()
            for row in rows:
                cell2 = ""
                for cell in row:
                    cell2 = cell2 + " " + dataencryptor.Decrypt(cell)
                print(cell2)
            for row1 in rows:
                for cell1 in row1:
                    print(cell1)

            conn.close()
    write2()