def question10(impq, impq2):
    import random
    import encryptionmodule
    import main
    def question1():
        chars = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY1234567890!@#$%^&*()_-=+:;/][}{\|?/.,`~"
        q1 = input("Do you want to store your site & generated password in database? [Y/N] or Main (A) ")
        q2 = q1.upper()

        if q2 == "Y":
            def correct():

                while 1:
                    try:
                        pass_len = int(input("What length would you like the password to be? "))
                    except ValueError:
                        print("The input should be an integer.")
                        correct()
                    pass_count = int(pass_len)


                    pass_purpose = input("Please enter site name: ")
                    pass_email = input("Please provide the E- Mail address. ")


                    for x in range(0, pass_count):
                        password = ""
                        for x in range(0, pass_len):
                            pass_char = random.choice(chars)
                            password = password + pass_char
                        print("Here is your password: ", password)
                        import existance

                        file_exists3 = existance.exists("password.txt")
                        file_exists23 = existance.exists("password.txt.aes")

                        if file_exists3 == "TRUE":
                            with open("password.txt", "a") as f:
                                print("Site Credentials:", file=f)
                                print(pass_purpose, file=f)
                                print("E- Mail Address: " + pass_email,
                                      file=f)
                                print("Password: " + password, file=f)
                                print("", file=f)
                                print("", file=f)
                            break

                        if file_exists3 == "FALSE":
                            if file_exists23 == "TRUE":
                                encryptionmodule.decryptFile(
                                    "password.txt.aes",
                                    "password.txt", impq)

                                with open("password.txt", "a") as f:
                                    print("Site Credentials:", file=f)
                                    print(pass_purpose, file=f)
                                    print("E- Mail Address: " + pass_email,
                                          file=f)
                                    print("Password: " + password,
                                          file=f)
                                    print("", file=f)
                                    print("", file=f)
                                break

                            if file_exists23 == "FALSE":
                                with open("password.txt", "a") as f:
                                    print("Site Credentials:", file=f)
                                    print(pass_purpose, file=f)
                                    print(
                                        "E- Mail Address: " + pass_email,
                                        file=f)
                                    print("Password: " + password,
                                          file=f)
                                    print("", file=f)
                                    print("", file=f)
                                break

                    def question6():
                        question4 = input("Do you want to generate more passwords? [Y/N] ")
                        question5 = question4.upper()

                        if question5 == "Y":
                            question1()

                        if question5 == "N":
                            main.question3(impq,impq2)

                        else:
                            print("Invalid Command!")
                            question6()

                    question6()

            correct()
        elif q2 == "N":
            def corr():
                while 1:
                    try:
                        pass_len = int(input("What length would you like the password to be? "))
                    except ValueError:
                        print("The input should be an integer.")
                        corr()

                    try:
                        pass_count = int(input("How many passwords would you like to generate? "))
                    except ValueError:
                        print("The input should be an integer.")
                        corr()

                    for x in range(0, pass_count):
                        password = ""
                        for x in range(0, pass_len):
                            pass_char = random.choice(chars)
                            password = password + pass_char
                        print("Here is your password: ", password)

                        with open("password.txt", "a") as f:

                            print("Password:", file=f)

                            print(password, file=f)

                            print("", file=f)

                            print("", file=f)

                    def question13():
                        question40 = input(
                            "Do you want to generate more passwords? [Y/N] ")
                        question50 = question40.upper()

                        if question50 == "Y":
                            question1()

                        if question50 == "N":
                            main.question3(impq, impq2)

                        else:
                            print("Invalid Command!")
                            question13()

                    question13()
            corr()

        elif q2 == "MAIN" or "A":
            print("")
            main.question3(impq, impq2)

    question1()