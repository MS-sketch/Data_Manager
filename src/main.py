"""This is the home module. A core module too. Just asks the user what function to perform."""
import exit
import vault
import passgen
import help
#import settings
def question3(impq, impq2):
    def q6():
        print(impq, impq2)
        print("What do you want to open?")
        print("1. Password Generator")
        print("2. Vault")
        print("3. Exit")
        print("4. Settings")
        print("5. Help")
        question2 = input("[1-5]: ")

        if question2 == "1":
            passgen.question10(impq, impq2)

        if question2 == "2":
            vault.vault(impq, impq2)

        if question2 == "3":
            exit.exitcode(impq)

        if question2 == "4":
            settings.settings(impq, impq2)

        if question2 == "5":
            help.help20(impq, impq2)

        else:
            print("Invalid!")
            q6()
    q6()