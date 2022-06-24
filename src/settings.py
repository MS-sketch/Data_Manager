"""In Development To Be Tested."""

def settings(impq, impq2):
    def set1():
        print("")
        print("What Do You Want To Do?")
        print("1. Return To Main")
        print("2. Modify Items")
        print("3. Exit")
        settings1 = input("Input [1-5]: ")

        if settings1 == "1":
            import main
            main.question3(impq, impq2)

        if settings1 == "2":
            def var1():
                print("Which Settings Are To Be Modified? ")
                print("")
                print("1. Vault Timeout")
                print("2. Backup Vault")
                print("3. Decline EULA")
                print("4. Back")
                print("5. Reset All To Default")
                p2 = input("Input [1-5]: ")
                if p2 == "1":
                    print("Please Select Time")
                    print("1. 30 Minutes")
                    print("2. 1 Hour")
                    print("3. 2 Hours")
                    print("4. 24 Hours")
                    print("5. Never (Not Recommended)")
                    print("6. Custom")

                elif p2 == "2":

                elif p2 == "3":

                elif p2 == "4":

                else:

            var1()

        if settings1 == "3":
            import exit
            exit.exitcode(impq)

        if settings1 == "2":
            print("What Do You Want To Modify?")


        else:
            print("Invalid!")
            set1()
    set1()