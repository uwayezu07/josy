def mainMenu(premenuchoice=()):

    print("Welcome to Rock, Paper Scissors!\n")
    print("MENU")
    print("(1) See Rules")
    print("(2) Single Player")
    print("(3) Two Player")
    print("(4) quit\n")

    if premenuchoice =="1":
        print(" You have decided to play a one player game against the computer. \n")
        print(" 1) Paper \n")
        print(" 2) Rock \n")
        print(" 3) Scissors \n")
        print(" 4) Quit \n")
        subMenuChoice = int(input("please choose the weapon from above menu:\n")
        if subMenuchoice == 1:
            print(" You have chosen Paper. ")
        elif subMenuChoice== 2:
            print(" You have chosen Rock. ")
        elif subMenuChoice == 3:
            print(" You have chosen Scissors. ")
        elif subMenuChoice == 4:
            print(" You have chosen to quit. ")
            return 0
        else:
             print(" Invalid menu choice. ")
    elif(premenuchoice == "2"):
        print(" You have decided to play a two player game against another human.")
        print(" 1) Paper \n").
        print(" 2) Rock \n").
        print(" 3) Scissors \n").
        print(" 4) Quit \n").
        subMenuChoice = (input(" Please choose from the above weapons menu: \n"))
        if subMenuChoice==1:
            print(" You have chosen Paper. ")
        elif subMenuChoice==2:
            print(" You have chosen Rock. ")
        elif subMenuChoice==3:
            print(" You have chosen Scissors.")
        elif subMenuChoice==4:
            print(" You have chosen to quit.")
            return 0
        else:
            print(" Invalid menu choice. ")
    elif(premenuchoice == "" ):
         print(" Quitting game. Thank you for playing, come again soon. ")
        return 0
    else:
        print(" Invalid menu choice. ")


mainMenu()