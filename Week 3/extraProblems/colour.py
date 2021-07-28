colour = input("Enter a colour (blue/red) : ")

if colour == "blue":
    typeOfBlue = input("Is it a light blue? (y/n) : ")
    if typeOfBlue == "y":
        print("Sky Blue")
    else:
        print("Navy blue")
elif colour == "red":
    typeOfRed = input("is it a light red? (y/n) : ")
    if typeOfRed == "y":
        print("Pink")
    else:
        print("Maroon")
else:
    print("That's not a colour!")