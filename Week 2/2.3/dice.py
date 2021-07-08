import random

def throwDice():
    return random.randint(1,6) + random.randint(1,6)

def getPreparedStatement(choice, intOutcome, decision):
    if decision == 1:
        winLose = "win"
    if decision == 0:
        winLose = "tie"
    if decision == -1:
        winLose = "Lose"
    return "you chose " + choice + "\n" + \
        "total was " + str(intOutcome) + \
            "\nYou " + winLose + "!"


def highLowChecker(choice, intOutcome):
    if intOutcome > 7 and choice == "h":
        return 1
    if intOutcome < 7 and choice == "l":
        return 1
    if intOutcome == 7:
        return 0
    else:
        return -1

playerChoice = input("Guess if the number will be high or low: ")

randomNum = throwDice()

decision = highLowChecker(playerChoice, randomNum)

print(getPreparedStatement(playerChoice, randomNum, decision))