'''this program is used to demonstate the probability of dice throws and their sums'''

#importing functions
from statistics import simulateDice
from statistics import generateData
from statistics import createGraph


'''
print(simulateDice(6,2))

data = [0,0,0,0,0,0,0,0,0,0,0]
generateData(6,2,1000,data)
print(data)

dataX = [1,2,3,4,5,6,7,8,9,10,11,12]
dataY = [0,0,1,0,0,1,3,4,0,0,1,0]
title = "Dice outcome"
xlabel = "Outcomes"
ylabel = "frequencies"

createGraph(dataX, dataY, title, xlabel, ylabel)
'''

#helper function to start the trials
def helper():
    #retreiving inputs
    dice = int(input("How many dice to throw? "))
    faces = int(input("How many faces will the dice like to have? "))
    trials = int(input("How many trials whould you like to have?"))
    
    #creating empty data list
    data = []
    i = 0
    while i < faces*dice:
        data.append(0)
        i += 1

    #generating data
    dataY = generateData(faces, dice, trials, data)
    
    #generating an x value list
    dataX = []
    i = 1
    while i <= faces*dice:
        dataX.append(i)
        i += 1

    #creating graph
    createGraph(dataX, dataY, "probability distribution", "possible outcome", "frequency")

#activating the helper function
helper()