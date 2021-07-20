'''This function is suppoed to emulate a traffic light system'''

#this function helps the program decide what to do after receving an input from the user
def currentLight(choice):
    if choice == "b" or choice == "B":
        print("Green")
    elif choice == "y" or choice == "Y":
        print("Red")
    elif choice == "r" or choice == "R":
        print("Blue")
    elif choice == "g" or choice == "G":
        print("Yellow")
    elif choice == "q" or choice == "Q":
        print("Good bye!")
    else:
        print("Invalid Colour")

#allows the user to make a choice of colours or exit
choice = input("Enter a colour choice (q to quit)\
    \n(B or b, G or g, Y or y, R or r) ")

#runs the function
currentLight(choice)