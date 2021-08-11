import random
import matplotlib.pyplot as plt

#simulating a dice throw of a specified number of dice and faces
def simulateDice(faces, dice):
    totalNumber = 0
    x = 0
    while x < dice:
        totalNumber += random.randint(1,faces)
        x += 1
    return totalNumber

#generating data based on trials, faces, and dice that are rolled
def generateData(faces, dice, trials, data):
    x = 0
    testData = []
    while x < trials:
        testData.append(simulateDice(faces, dice))
        x += 1

    i = 1
    while i <= faces*dice:
        data[i-1] = testData.count(i)
        i += 1
    return data

#creating a graph
def createGraph(dataX, datay, title, horlabel, verlabel):
    plt.bar(dataX, datay)
    plt.title(title)
    plt.xlabel(horlabel)
    plt.ylabel(verlabel)
    plt.show()
    return
