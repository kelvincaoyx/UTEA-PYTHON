import random



def guess():
    numberToGuess = random.randint(1,8)
    print("Your number to guess is ", numberToGuess)
    splitAt5 = input("Is your number greater than or equal to 5?")
    if splitAt5 == "y" or splitAt5 == "Y":
        splitAt7 = input("Is your number greater than or equal 7?")
        if splitAt7 == "y" or splitAt7 == "Y":
            splitAt7in = input("Is your number greater than 7?")
            if splitAt7in == "y" or splitAt7in == "Y":
                print("number is 8")
            else:
                print("number is 7")
        else:
            splitAt5in = input("Is your number greater than 5?")
            if splitAt5in == "y" or splitAt5in == "Y":
                print("number is 6")
            else:
                print("number is 4")
    else:
        splitAt3 = input("Is your number greater than or equal 3?")
        if splitAt3 == "y" or splitAt3 == "Y":
            splitAt3in = input("Is your number greater than 3?")
            if splitAt3in == "y" or splitAt3in == "Y":
                print("number is 4")
            else:
                print("number is 3")
        else:
            splitAt1 = input("Is your number greater than 1?")
            if splitAt1 == "y" or splitAt1 == "Y":
                print("number is 2")
            else:
                print("number is 1")
guess()