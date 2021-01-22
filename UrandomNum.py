#Computer guesses the number you chose/inputted

from random import randrange as ran

print("~~~~~~~~~~~~~ Computer guesses your number ~~~~~~~~~~~~~")
while True:
    while True:
        try:
            compRandomNum = int(input("Enter the number you want the computer to guess (the computer wont cheat): "))
        except:
            print("Please try again, an error occured:")
        else:
            break

    print("The computer will start and it has 8 guesses to guess the choosen number: ")

    global cMin
    cMin = 0

    global cMax
    cMax = 101

    for x in range(8):
        cRandomNum = ran(cMin, cMax)

        winOrAgain = None
        if cRandomNum == compRandomNum:
            print("\nThe computer won, the computer got the correct answer of " + str(cRandomNum))
            winOrAgain =  True
        elif cRandomNum < compRandomNum:
            print("Higher, the computer got " + str(cRandomNum))
            cMin = cRandomNum + 1
            winOrAgain = False
        else:
            print("Lower, the computer got " + str(cRandomNum))
            cMax = cRandomNum + 1
            winOrAgain = False

        if winOrAgain == True:
            break
        else:
            pass
    else:
        print("\nCongratulations, you won..")

    print("The game has finished...\n")
    while True:
        global yesNo
        yesNo = input("Do you want to play again (y/n): ")
        if yesNo == "y" or yesNo == "Y" or yesNo == "n" or yesNo == "N":
            break
        else:
            print("Try again, an error occured.\n")

    if yesNo == "y" or yesNo == "Y":
        print("\nNew game reloading...\n")
    else:
        print("Thanks for playing\n")
        break
    
print("Done")
