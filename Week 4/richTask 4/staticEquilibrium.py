'''
This program is used to help the user practice calculating net torque
and estimating which direction the metre stick is going to tip
'''

#importing the random library to get random number generator
import random

#function to help me create random digits. Less to type than random.randrange
def randomDigit(start,stop):
    return random.randrange(start,stop)

#function that generates a list of weights that the game will be based on. 
#Just input the number of weights you want
def weightGenerator(numberOfWeightsRequired):

    #defining some variables
    thisRoundsindexes = [0,1,2,3,4,6,7,8,9,10]
    thisRoundsList = [0,0,0,0,0,"_/\_",0,0,0,0,0]
    weightsToBeAdded = []

    #gives us random numbers that will be added to the scale
    while numberOfWeightsRequired > 0:
        weightsToBeAdded.append(randomDigit(1,5))
        numberOfWeightsRequired -= 1

    #Puts the random weights generated into the list. it uses
    #another list to determine indexes because we don't want overlap
    counter = 0
    while counter < len(weightsToBeAdded):
        index = thisRoundsindexes[randomDigit(0,len(thisRoundsindexes))]
        thisRoundsindexes.remove(index)
        thisRoundsList.insert(index,weightsToBeAdded[counter])
        thisRoundsList.pop(index+1)
        counter += 1

    #returning the list for use
    return thisRoundsList

#function that takes in a list a=of weights and calculates the which way it will turn
def netForceCalc(weightList):

    #calculates the torque that causes the scale to turn in a negative direction
    negativeTorque = 0
    negativeTorqueList = weightList[:5]
    counter = 4
    runcount = 1
    while counter > 0:
        negativeTorque += negativeTorqueList[counter]*0.1*runcount
        counter -=1
        runcount += 1

    #calculates the torque that causes the scale to turn in a postitive direction
    positiveTorque = 0
    positiveTorqueList = weightList[6:]
    counter = 0
    runcount = 1
    while counter < 5:
        positiveTorque += positiveTorqueList[counter]*0.1*runcount
        counter += 1
        runcount += 1

    #returns the predicted position that the scale will turn
    if negativeTorque > positiveTorque:
        return "a"
    elif negativeTorque == positiveTorque:
        return "b"
    else:
        return "c"
    
#helper function that will start the entire program and access the other functions
def helper():

    #defining some variables that will be used throughout the function
    start = 2
    winCounter = 0
    gameCounter = 0
    continueGame = input("Would you like to continue (y/n)? ")

    #while loop to keep the game going until they don't want to play
    while continueGame.lower() == "y":
        
        #Printing the header for the scale
        print("0.0m\t0.1m\t0.2m\t0.3m\t0.4m\t0.5m\t0.6m\t0.7m\t0.8m\t0.9m\t1.0m")

        #generation of the weightlist that will be used throughout
        weightList = weightGenerator(start)

        #printing out the weightlist in a way that it lines up with the header from above
        counter = 0
        display = ""
        while True:
            if weightList[counter] == 0:
                display += "  \t"
            elif counter == 5:
                display += str(weightList[counter]) + "\t"
            else:
                display += str(weightList[counter]) + "N  \t"
            counter += 1
            if counter == 11:
                print(display)
                break
        
        #caluculating the direction that the scale will go
        answer = netForceCalc(weightList)
        
        #retreiving the user's guess
        userAnswer = input("Choose the correct answer (a,b,c):\n \
            a)spin left\t b)equilibrium\t c)spin right\t")

        #comparing the user's input with the answer. Will increase the weights
        #depending on the result of the game
        if userAnswer == answer:
            print("\nCorrect\n")
            
            #keeps track of the wins
            winCounter += 1
            start += 2
            if start > 10:
                start = 10
        else:
            print("\nIncorrect\n")
            start -= 2
            if start <=0:
                start = 1

        #keeping track of the total number of games
        gameCounter += 1

        #asks if the user wants to continue or not.
        continueGame = input("Would you like to continue (y/n)? ")

    #prints the results of the games
    print("\nYou got", winCounter, "out of", gameCounter)

#printing the header for the game
print("Welcome to the static equilbrium quiz!")

#activating the helper function
helper()



