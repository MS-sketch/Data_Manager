"""This module is one of the core module & if modified or deleted may result in the program crashing. This module is
responsible for the decryption of the vault (info part). It takes in the user credentials for creation of vault."""

import os
import pickle
import random
import getpass
import hashlib
import existance
import shutil
import encryptionmodule
def usec2():

    Charset = bytearray.fromhex("32594f5042334151435655584d4e52533937574530495a44344b4c4647484a3831363554").decode()
    for x in range(0, 1):
        session = ""
        for y in range(0, 20):
            session1 = random.choice(Charset)
            session = session + session1
        sessionid = session
        ECPASS = sessionid
        outFile = "Progdata.data"
        data = os.path.isfile("Progdata.data")
        data1 = str(data)
        data2 = data1.upper()

        if data2 == "TRUE":
            if os.stat("Progdata.data").st_size == 0:
                bin = format(ECPASS)
                fw = open(outFile, 'wb')
                pickle.dump(ECPASS, fw)
                fw.close()
            if os.stat("Progdata.data").st_size > 0:
                os.remove("Progdata.data")
                usec2()

        if data2 == "FALSE":
            bin = format(ECPASS)
            fw = open(outFile, 'wb')
            pickle.dump(ECPASS, fw)
            fw.close()

    file_existance = existance.exists("msp.txt")
    fe24 = existance.exists("password.txt.aes")
    fe25 = existance.exists("password.txt")

    def secure1():

        if file_existance == "TRUE":
            if os.stat("msp.txt").st_size == 0:
                os.remove("msp.txt")
                usec2()

            if os.stat("msp.txt").st_size > 0:
                print("Please enter master password to continue.")
                print("If forgotten enter the number '1' to create a new vault & deleting the old one.")
                print("If you want to exit please enter the number '2'.")
                print("For help enter '3'.")
                print("")
                impq = getpass.getpass()
                print("")
                impq2 = hashlib.sha256(impq.encode("utf-8")).hexdigest()

                def secure3():

                    if impq == "1":
                        q10 = input("You sure you want to reset? [Y/N] ")
                        print("")
                        q11 = q10.upper()

                        if q11 == "Y":
                            print("Okay, Reseting...")
                            os.remove("msp.txt")
                            if fe24 == "TRUE":
                                os.remove("password.txt.aes")
                                usec2()

                            if fe25 == "TRUE":
                                os.remove("password.txt")
                                usec2()

                            else:
                                usec2()

                        if q11 == "N":
                            print("Okay")
                            print("")
                            usec2()

                    if impq == "2":
                        print("Okay Exiting....")
                        file_existance2 = existance.exists("password.txt.aes")
                        file17 = existance.exists("password.txt")
                        if file17 == "TRUE":
                             
                            encryptionmodule.encryptFile("password.txt", "password.txt.aes", impq)
                            os.remove("password.txt")
                            exit()
                        if file_existance2 == "FALSE":
                            exit()
                        else:
                            print("ERROR 404 NOT FOUND")
                            exit()

                    if impq == "3":
                        def printtext(swefile):
                            for row in swefile:
                                print(row)

                        text = open("commands.txt", "r", encoding='utf-8')
                        printtext(text)
                        usec2()

                    else:
                        def secure4():
                            if os.stat("msp.txt").st_size == 0:
                                os.remove("msp.txt")
                                usec2()
                            elif os.stat("msp.txt").st_size > 0:
                                info4 = existance.lenghtinfile("msp.txt")
                                info2 = existance.readfile("msp.txt")

                                if info4 == 64:
                                    if info2 == impq2:
                                        import main
                                        main.question3(impq, impq2)
                                    elif info2 != impq2:
                                        print("Wrong Password!")
                                        secure1()


                        secure4()

                secure3()




            if file_existance == "FALSE":
                def secure2():
                    fe6 = existance.exists("password.txt")
                    fe3 = existance.exists("password.txt.aes")
                    if fe3 == "TRUE":
                        def again2():
                            securitywarn1 = input("Do you wish to backup the existing vault? [Y/N] ")
                            securitywarn = securitywarn1.upper()

                            if securitywarn == "Y":
                                location = input("Please enter the dir to which you want to backup vault to: ")
                                location2 = existance.direxists(location)
                                if location2 == "TRUE":
                                    shutil.copy("password.txt.aes", location)
                                    print("Copied!")
                                    print(
                                        "Please Note You Can Use The Import Function To Retrieve The Data Again If You Wish To!")
                                    os.remove("password.txt.aes")

                                    def secure9():
                                        pass_12 = getpass.getpass("Please Enter Password To Create A New Vault: ")
                                        pass_13 = getpass.getpass("Please Confirm Password: ")
                                        if pass_12 == pass_13:
                                            print(
                                                "Okay, You have to enter password again to unlock vault for security reasons.")
                                            pass_14 = hashlib.sha256(pass_12.encode("utf-8")).hexdigest()
                                            with open("msp.txt", "a") as f:
                                                print(pass_14, file=f)
                                            usec2()

                                        else:
                                            print("Passwords are not same, try again...")
                                            secure9()

                                    if location2 == "FALSE":
                                        print("No Such Directory Exists")
                                        again2()

                                    if securitywarn == "N":
                                        print("Okay! Vault will not be backed up.")
                                        usec2()

                                    secure9()

                            if securitywarn == "N":
                                print("Okay Then")
                                print("But you may recover the vault if you wish to.")
                                print("You may refer the documentation for this.")
                                print("Thank You for using this software.")
                                print("")
                                entry1 = input("So, do you wish to continue creating new? [Y/N]: ")
                                entry = entry1.upper()
                                if entry == "Y":
                                    print("Okay")
                                    print("")
                                    again2()

                                if entry == "N":
                                    entry3 = input("Please press enter to exit... ")
                                    if entry3 == "":
                                        exit()
                                    else:
                                        exit()

                        again2()

                    if fe6 == "TRUE":
                        sec20 = input("Do you wish to backup the existing vault? [Y/N]: ")
                        sec2 = sec20.upper()

                        if sec2 == "Y":
                            def section10():
                                location = input("Please enter the dir to which you want to backup vault to: ")
                                location3 = existance.direxists(location)
                                if location3 == "TRUE":
                                    print(
                                        "It appears that the vault is un-encrypted, So you have to enter a password to secure it.")
                                    pas1 = input("Want To Continue [Y/N]: ")
                                    pas = pas1.upper()
                                    if pas == "Y":
                                        pas2 = input("Please Enter Password: ")
                                         
                                        encryptionmodule.encryptFile("password.txt", "password.txt.aes", pas2)
                                        os.remove("password.txt")
                                        shutil.copy("password.txt.aes", location)
                                        print("Copied!")
                                        print(
                                            "Please Note You Can Use The Import Function To Retrieve The Data Again If You Wish To!")
                                        os.remove("password.txt.aes")

                                    if pas == "N":
                                        pas3 = input(
                                            "Your Credentials May Be At Risk! Do you want to continue? [Y/N]: ")
                                        pas4 = pas3.upper()

                                        if pas4 == "Y":
                                            print(
                                                "Okay, Your Vault Will Not Be Encrypted & Will Be Backed Up To You Preferred Directory.")
                                            shutil.copy("password.txt.aes", location)
                                            print("Completed!")

                                        if pas4 == "N":
                                            pas5 = input("Do you want to continue? [Y/N]: ")
                                            pas6 = pas5.upper()

                                            if pas6 == "N":
                                                print("")

                                            if pas6 == "Y":
                                                section10()



                                    else:
                                        print("Invalid!")
                                        print("")

                                if location3 == "FALSE":
                                    print("The Entered Directory Doesn't Exist!")
                                    print("")
                                    section10()

                            section10()

                            def secure11():
                                pass_19 = getpass.getpass("Please Enter Password To Create A New Vault: ")
                                pass_18 = getpass.getpass("Please Confirm Password: ")
                                if pass_19 == pass_18:
                                    print(
                                        "Okay, You have to enter password again to unlock vault for security reasons.")
                                    pass_17 = hashlib.sha256(pass_19.encode("utf-8")).hexdigest()
                                    with open("msp.txt", "a") as f:
                                        print(pass_17, file=f)
                                    usec2()

                                else:
                                    print("Passwords are not same, try again...")
                                    secure11()

                            secure11()

                        if sec2 == "N":
                            print("Okay!")
                            os.remove("password.txt")
                            usec2()

                    else:
                        def sec1():
                            pass_20 = getpass.getpass("Please Enter Password To Create A New Vault: ")
                            pass_21 = getpass.getpass("Please Confirm Password: ")
                            if pass_20 == pass_21:
                                print("Okay, You have to enter password again to unlock vault for security reasons.")
                                pass_22 = hashlib.sha256(pass_20.encode("utf-8")).hexdigest()
                                with open("msp.txt", "a") as f:
                                    print(pass_22, file=f)
                                fe3 = existance.exists("password.txt.aes")
                                if fe3 == "TRUE":
                                     
                                    encryptionmodule.decryptFile("password.txt.aes", "password.txt", impq)
                                    encryptionmodule.encryptFile("password.txt", "password.txt.aes", pass_20)
                                    usec2()
                                if fe3 == "FALSE":
                                    usec2()
                            if pass_20 != pass_21:
                                print("Passwords are not same, try again...")
                                sec1()

                secure2()

    secure1()

    usec2()
usec2()
