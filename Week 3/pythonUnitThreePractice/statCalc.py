'''A program that allow shte user to determine the average, smallest, and 
largest value in a list that the user has entered
'''

#function that allows me to star up the calculator
def statCalc():
    #initial setup and defining the required variables
    userInput = input("Enter a number (q to quit): ")
    numberOfItems = 1
    sumOfNumbers = float(userInput)
    smallestValue = float(userInput)
    largestValue = float(userInput)

    #while loop to make sure that the calculator can go on indefinitely until the user quits
    while True:
        userInput = input("Enter a number (q to quit): ")

        #breaks the loop when use enters q
        if userInput == "q" or userInput == "Q":
            break

        #adds input to a running sum
        sumOfNumbers += float(userInput)

        #if the input is smaller than the current smallest number, the smallestValue will be replaced
        if smallestValue > float(userInput):
            smallestValue = float(userInput)

        #if the input is smaller than the current smallest number, the smallestValue will be replaced
        if largestValue < float(userInput):
            largestValue = float(userInput)

        #keeps track of how many iterations has occured
        numberOfItems += 1
        
    #prints the results of the calculator
    print("You entered", numberOfItems, "numbers.")
    print("The lowest number was", smallestValue)
    print("The highest number was", largestValue)
    print("The average was :", sumOfNumbers/numberOfItems)

statCalc()