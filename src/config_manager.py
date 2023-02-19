import configparser

def create_default_config():
    config_file = configparser.ConfigParser()

    config_file.add_section("Limits")

    config_file.set("Limits", "folder_name_limit", "30")
    config_file.set("Limits", "save_recently_copied_passwords", "YES")
    config_file.set("Limits", "number_of_passwords_to_save", "8")

    with open(r"config.ini", 'w') as config_file_obj:
        config_file.write(config_file_obj)
        config_file_obj.flush()
        config_file_obj.close()



"""        
config_file = configparser.ConfigParser()
f = config_file.read("config.ini")
content = config_file.get('Limits', 'folder_name_limit')

print("Content of the config file are:")
print(content)"""