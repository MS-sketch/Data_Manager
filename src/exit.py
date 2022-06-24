"""This module is used for exiting the application. It basically encrypts the file containing sensitive info of a
user to prevent un-authorised access. Note: This is also an essential component. Modifying this may result in
full failure of application."""

import os
import existance
import encryptionmodule
def exitcode(impq):
    print(impq)
    file17 = existance.exists("password.txt")
    print(file17)

    if file17 == "TRUE":
        print(impq)
        encryptionmodule.encryptFile("password.txt", "password.txt.aes", impq)
        os.remove("password.txt")
        print("EXITING")
        exit()
    if file17 == "FALSE":
        print("EXITING")
        exit()