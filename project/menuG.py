
def mainMenu():

    print("Welcome to Rock, Paper Scissors!\n")
    print("MENU")
    print("(1) See Rules")
    print("(2) Single Player")
    print("(3) Two Player")
    print("(4) quit\n")

    premenuchoice = int(input())

    if premenuchoice == 1:
        print(" You have decided to play a one player game against the computer. \n")
        print(" 1) Paper \n")
        print(" 2) Rock \n")
        print(" 3) Scissors \n")
        print(" 4) Quit \n")
        submenuchoice = int(input("please choose the weapon from above menu:\n"))
        if submenuchoice == 1:
            print(" You have chosen Paper. ")
        elif submenuchoice == 2:
            print(" You have chosen Rock. ")
        elif submenuchoice == 3:
            print(" You have chosen Scissors. ")
        elif submenuchoice == 4:
            print(" You have chosen to quit. ")

        else:
            print(" Invalid menu choice. ")
    elif premenuchoice == 2:
        print(" You have decided to play a two player game against another human.")
        print(" 1) Paper \n")
        print(" 2) Rock \n")
        print(" 3) Scissors \n")
        print(" 4) Quit \n")
        submenuchoice = (input(" Please choose from the above weapons menu: \n"))
        if submenuchoice ==1:
            print(" You have chosen Paper. ")
        elif submenuchoice ==2:
            print(" You have chosen Rock. ")
        elif submenuchoice ==3:
            print(" You have chosen Scissors.")
        elif submenuchoice ==4:
            print(" You have chosen to quit.")

        else:
            print(" Invalid menu choice. ")
    elif premenuchoice == "3":
        print(" Quitting game. Thank you for playing, come again soon. ")
    else:
        print(" Invalid menu choice. ")

if __name__== '__main__':
   mainMenu()