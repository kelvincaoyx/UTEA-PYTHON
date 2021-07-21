'''This function is suppoed to emulate a traffic light system'''

#this function helps the program decide what to do after receving a colour from the user
def currentLight(colour):
    if colour == "b" or colour == "B":
        print("\nGreen\n")
    elif colour == "y" or colour == "Y":
        print("\nRed\n")
    elif colour == "r" or colour == "R":
        print("\nBlue\n")
    elif colour == "g" or colour == "G":
        print("\nYellow\n")
    else:
        print("\nInvalid Colour\n")

def inputHelper():
    #allows the user to make a choice of colours or exit
    choice = input("Enter a colour choice (q to quit)\
        \n(B or b, G or g, Y or y, R or r) ")
    while choice != "q" and choice != "Q":
        currentLight(choice)
        choice = input("Enter a colour choice (q to quit)\
        \n(B or b, G or g, Y or y, R or r) ")
    print("\nGood bye!\n")

#runs the function
inputHelper()