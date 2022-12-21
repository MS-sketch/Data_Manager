def enter(id_int,settingname_str,settingconfig_str,settingvalue_int):
    import sqlite3
    import dataencryptor
    import existance


    conn = sqlite3.connect("dmvalut.dmdb")
    crsr = conn.cursor()

    settings_table =  """ CREATE TABLE IF NOT EXISTS SETTINGS (
            ID INT(100),
            SETTING_NAME CHAR(100),
            SETTING_CONFIG CHAR(100),
            SETTING_VALUE CHAR(100)
        ); """

    settings_write = """INSERT INTO SETTINGS (id_int, settingname_str, settingconfig_str, settingvalue_int) 
    VALUES (?,?,?,?)"""

    #sql_command = """CREATE TABLE ROUTINE(data1,data2,data3,data4,data5)
        #INSERT INTO ROUTINE(data1,data2,data3,data4,data5)
        #VALUES (?,?,?,?,?);"""

    id_int = dataencryptor.Encrypt(id_int)
    settingname_str = dataencryptor.Encrypt(settingname_str)
    settingconfig_str = dataencryptor.Encrypt(settingconfig_str)
    settingvalue_int = dataencryptor.Encrypt(settingvalue_int)

    tup = (id_int, settingname_str, settingconfig_str, settingvalue_int)
    crsr.execute(settings_table,tup)
    crsr.execute(settings_write)
    conn.commit()
    conn.close()
