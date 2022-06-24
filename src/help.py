import time


def help20(impq, impq2):
    def help2():
        import hashlib
        import os
        import shutil
        import encryptionmodule
        import main
        import existance
        help1 = input("1. About  2. Commands  3. Credits  4. Return To Main  5. Other [1-5] ")
        if help1 == "1":
            print("Password Manager Version 1.2.9 Canary Release")
            print("Year Released: 2022")
            help2()

        elif help1 == "2":
            print("Opening documentation...")

            def printtext(swefile):
                for row in swefile:
                    print(row)

            text = open("commands.txt", "r", encoding='utf-8')
            printtext(text)

            help2()

        elif help1 == "3":
            print("By MS-sketch")
            print("Programming Language: Python")
            print("IDE: Jet Brains PyCharm Community Edition")
            help2()

        elif help1 == "4":
            print("Returning.....")
            main.question3(impq, impq2)

        elif help1 == "5":
            def set11():
                print("Please Enter What To Do. ")
                print("1. Change Password")
                print("2. Main")
                print("3. License")
                print("4. Changelog")
                print("5. Import Old Vault")
                set = input("Input [1-5] ")

                if set == "1":
                    set1 = input("Do you want to change the password? [Y/N]")
                    set2 = set1.upper()

                    def set15():

                        if set2 == "Y":
                            set3 = input("Please enter old password: ")
                            set4 = hashlib.sha256(
                                set3.encode("utf-8")).hexdigest()

                            if set3 == impq:
                                def set10():
                                    if set4 == impq2:
                                        set5 = input("Please enter new password: ")
                                        set6 = input("Please enter password again: ")
                                        if set5 == set6:
                                            set7 = hashlib.sha256(set5.encode("utf-8")).hexdigest()
                                            os.remove("msp.txt")
                                            with open("msp.txt","a") as f:
                                                print(set7, file=f)
                                            f1 = existance.exists("password.txt")
                                            f2 = existance.exists("password.txt.aes")
                                            if f2 == "TRUE":
                                                if f1 == "FALSE":
                                                    encryptionmodule.decryptFile("password.txt.aes", "password.txt", impq)
                                                    os.remove("password.txt.aes")
                                                    encryptionmodule.encryptFile("password.txt", "password.txt.aes", set6)
                                                    os.remove("password.txt")

                                                if f1 == "TRUE":
                                                    os.remove("password.txt.aes")
                                                    encryptionmodule.encryptFile("password.txt", "password.txt.aes",set6)
                                                    os.remove("password.txt")

                                            print("Password Reset Complete!")
                                            import authenticate
                                            authenticate.usec2()

                                    else:
                                        print("The Passwords don't match!")
                                        set10()

                                set10()

                            elif set3 != impq:
                                print("Wrong Password")
                                set12 = input("Do you want to continue? [Y/N] ")
                                set14 = set12.upper()

                                if set14 == "Y":
                                    print("Okay")
                                    set15()

                                elif set14 == "N":
                                    print("Okay")
                                    help2()

                    set15()

                if set == "2":
                    help2()

                if set == "3":
                    def printtext(swefile):
                        for row in swefile:
                            time.sleep(0.05)
                            print(row)

                    text = open("EULA.txt", "r", encoding='utf-8')
                    printtext(text)
                    set11()

                if set == "4":
                    def printtext(swefile):
                        for row in swefile:
                            time.sleep(0.05)
                            print(row)

                    text = open("Changelog.txt", "r", encoding='utf-8')
                    printtext(text)
                    set11()

                if set == "5":
                    # NEEDS WORK BETA
                    print("Warning! This will replace your own vault.")

                    def imp1():
                        ver1 = input("Do You Want To Continue? [Y/N]: ")
                        ver = ver1.upper()
                        if ver == "Y":
                            print("Okay")

                            def pas17():
                                pas11 = input("Please enter the directory to be searched: ")
                                pas14 = os.path.isdir(pas11)
                                pas15 = str(pas14)
                                pas16 = pas15.upper()

                                if pas16 == "FALSE":
                                    print("'" + pas11 + "'" + " Doesn't Exists!")
                                    pas17()

                                if pas16 == "TRUE":
                                    pas18 = pas11 + "/" + "password.txt"
                                    pas19 = pas11 + "/" + "password.txt.aes"
                                    pas22 = existance.exists(pas18)
                                    pas25 = existance.exists(pas18)

                                    if pas22 or pas25 == "TRUE":
                                        print("Vault Detected!")
                                        q26 = os.path.isfile("password.txt")
                                        q27 = str(q26)
                                        q28 = q27.upper()

                                        q29 = os.path.isfile("password.txt.aes")
                                        q30 = str(q29)
                                        q31 = q30.upper()

                                        if q28 or q31 == "TRUE":
                                            def qa1():
                                                q20 = input("Would you like to backup your current vault? [Y/N]: ")
                                                q21 = q20.upper()

                                                if q21 == "Y":
                                                    def abc1():
                                                        q22 = input("Please Enter The Directory: ")
                                                        q25 = existance.direxists(q22)

                                                        if q25 == "TRUE":
                                                            shutil.move(
                                                                "password.txt.aes",
                                                                q22)
                                                            q32 = os.getcwd()

                                                            if q28 == "TRUE":
                                                                shutil.copy(pas18,q32)

                                                            if q31 == "TRUE":
                                                                shutil.copy(pas19,q32)

                                                            print("Note: The Master Password Will Change As Per The Entered Master Password.")
                                                            def correct50():
                                                                qa2 = input("Please Enter Vault Password: ")
                                                                try:
                                                                    encryptionmodule.decryptFile("password.txt.aes",
                                                                                                 "password.txt", qa2)

                                                                except ValueError:
                                                                    print("The Password Entered Is Wrong!")
                                                                    def crr5():
                                                                        q30 = input("Want TO Try Again?")
                                                                        if (q30.upper()) == "Y":
                                                                            correct50()

                                                                        if (q30.upper()) == "N":
                                                                            main.question3(impq, impq2)

                                                                        else:
                                                                            print("")
                                                                            print("Invalid")
                                                                            crr5()
                                                                    crr5()
                                                            correct50()


                                                        if q25 == "FALSE":
                                                            print("Invalid Directory!")
                                                            abc1()

                                                    abc1()

                                                if q21 == "N":
                                                    print("Okay")
                                                    print("Note: The Master Password Will Change As Per The Entered Master Password.")
                                                    qa2 = input("Please Enter Vault Password: ")
                                                    encryptionmodule.decryptFile("password.txt.aes","password.txt",qa2)



                                                else:
                                                    qa1()

                                            qa1()

                                        else:
                                            print("Processing Your Action")
                                            q32 = os.getcwd()
                                            if q28 == "TRUE":
                                                shutil.copy(
                                                    pas18,
                                                    q32)

                                            if q31 == "TRUE":
                                                shutil.copy(
                                                    pas19,
                                                    q32)





                                    else:
                                        def chk():
                                            print("Please Enter File Name (Without Dir).")
                                            print("To Exit Press Enter")
                                            pas12 = input("Input: ")
                                            print("Please Enter Dir")
                                            pass14 = input("Input: ")
                                            pas16 = str(pass14) + "/" + str(pas12)

                                            pas18 = existance.exists(pas16)
                                            if pas18 == "FALSE":
                                                print("Invalid!")

                                            if pas18 == "TRUE":
                                                chk2 = os.getcwd
                                                chk3 = str(chk2)

                                                shutil.copy(pas16, chk3)



                                        chk()



                            pas17()

                        elif ver == "N":
                            print("Okay..")
                            print("")
                            set11()

                        else:
                            print("Invalid!")
                            imp1()

                    imp1()

                else:
                    print("Invalid!")
                    set11()

            set11()



        else:
            print("Invalid Command!")
            help2()

    help2()