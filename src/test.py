"""import entry_manager as sql
import sqlite3
import config_manager
#sql.create_blank_table()
#sql.insert_in_default(4 ,"why", "www.lambda.com", "1", "whu&POken", "johnwu", "This top a random message.PLS")
#sql.update_create_entry(4 ,"yydgfydgfd", "www.whyme.com", "0", "whu&POken", "johnwu", "This top a random message.PLS")

#sql.delete_entry_from_default(1)

""""""index = sql.fetch_all_from_index_entry()

for x in range(len(index)):
    y = index[x]
    print(y[0])""""""

"""#sql.create_special_table()
"""sql.insert_special_folder_index("Mainakh")"""
"""config_manager.create_default_config()"""



import entry_manager as en

print(len(en.fetch_from_folder_index()))


