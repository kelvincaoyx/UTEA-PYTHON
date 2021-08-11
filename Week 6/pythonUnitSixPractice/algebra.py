import math

#generates a specific row from pascals triangle and fills the row with it
def generateRow(number, row):
    startingIndex = 0
    while startingIndex < number:
        row[startingIndex] = int((math.factorial(number))/math.factorial(number-startingIndex)/math.factorial(startingIndex))
        startingIndex += 1
    return row

#creates an empty triangle so that the numbers can be filled in
def createEmptyTriangle(rows):
    rowList = []
    x = 1
    while x < rows+1:
        rowForThisRound = []
        i = 0
        while i < x:
            rowForThisRound.append(1)
            i += 1
        rowList.append(rowForThisRound)
        x += 1
    return rowList

#printing out the 2d triangle list
def printTriangle(triangle):
    x = 0 
    while x < len(triangle):
        print(triangle[x])
        x += 1
    return

#generating pascals' triangle
def generateTriangle(rows, triangle):
    i = 0
    while i < rows:
        generateRow(i,triangle[i])
        i += 1
    return triangle






