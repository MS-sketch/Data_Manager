def vault(impq,impq2):
    def state():
        print("Ok")

        import encryptionmodule
        import os
        import getpass
        import existance
        print("What do you want to do?")
        print("A. Add Credentials")
        print("B. Other Functions ")
        print("C. Create New Vault")
        print("D. View all stored credentials")
        data_input_1 = input("Input [A-D] ")
        data_input = data_input_1.upper()

        def vault1():
            if data_input == "A":
                file_existance1 = existance.exists("password.txt")

                if file_existance1 == "TRUE":
                    print("Please fill the following details.")
                    data_cred1 = input("Title: ")
                    data_cred2 = input("Website: ")
                    data_cred3 = input("E-Mail Address\ Username: ")
                    data_cred4 = getpass.getpass("(Hidden) Password: ")

                    with open("password.txt", "a") as f:
                        print(data_cred1, file=f)
                        print("Website: " + data_cred2, file=f)
                        print("E-Mail\ Username: " + data_cred3, file=f)
                        print("Password: " + data_cred4, file=f)

                if file_existance1 == "FALSE":
                    file_existance2 = existance.exists("password.txt.aes")

                    if file_existance2 == "TRUE":
                        encryptionmodule.decryptFile("password.txt.aes","password.txt", impq)
                        vault1()

                    if file_existance2 == "FALSE":
                        with open("password.txt", "a") as f:
                            print("Data", file=f)
                            vault1()

                def vault4():
                    vault2 = input("Do you want to enter more credentials? [Y/N] ")
                    vault3 = vault2.upper()

                    if vault3 == "Y":
                        print("Okay!")
                        vault1()

                    if vault3 == "N":
                        import main
                        print("Okay!")
                        main.question3(impq,impq2)

                    else:
                        print("Invalid Command!")
                        vault4()

                vault4()

        vault1()

        def del1():
            if data_input == "C":
                print("You sure you want to create a new vault?")
                print("Doing this will delete your old vault.")
                confirm = input("Do you want to continue?[Y/N] ")
                confirm2 = confirm.upper()

                if confirm2 == "Y":
                    print("Okay, Deleting old vault creating new....")
                    os.remove("msp.txt")
                    import authenticate
                    authenticate.usec2()

                if confirm2 == "N":
                    print("Okay, you have to enter password again to access the vault.")
                    import authenticate
                    authenticate.usec2()

                elif confirm2 != "N" or "Y":
                    print("Invalid Command!")
                    del1()

        del1()

        def xy2():
            if data_input == "D":
                xy = getpass.getpass("Password: ")
                if xy != impq:
                    print("Wrong Password!")
                    xy2()

                elif xy == impq:
                    def again2():
                        file_existance2 = existance.exists("password.txt.aes")
                        file17 = existance.exists("password.txt")

                        if file17 == "TRUE":

                            def printtext(swefile):
                                for row in swefile:
                                    print(row)

                            text = open("password.txt", "r",
                                        encoding='utf-8')
                            printtext(text)

                            state()

                        elif file17 == "FALSE":
                            if file_existance2 == "TRUE":
                                encryptionmodule.decryptFile("password.txt.aes", "password.txt",impq)
                                again2()

                            elif file_existance2 == "FALSE":
                                print("No credentials are stored.")
                                state()

                            elif os.stat("password.txt").st_size == 0:
                                print("No credentials are stored.")
                                state()

                    again2()

        xy2()

        def vault5():
            if data_input == "B":
                print("Okay, Then what do you want to do?")
                print("1. Exit")
                print("2. Restart")
                print("3. Lock")
                option = input("Input [1-3] ")

                if option == "1":
                    import exit
                    exit.exitcode(impq)

                if option == "2":
                    import main
                    print("Okay Restarting..")
                    main.question3(impq,impq2)

                if option == "3":
                    fe14 = existance.exists("password.txt.aes")
                    fe15 = existance.exists("password.txt")
                    if fe15 == "TRUE":
                        if fe14 == "TRUE":
                            os.remove("password.txt.aes")
                        encryptionmodule.encryptFile("password.txt","password.txt.aes", impq)
                        os.remove("password.txt")
                        import authenticate
                        authenticate.usec2()

                    else:
                        import authenticate
                        authenticate.usec2()


                elif option != "1" or "2" or "3":
                    print("Invalid Command!")
                    vault5()

        vault5()

    state()