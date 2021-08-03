'''This program is used to create a pyramid made out of the desired symbol and height'''

#this function is used to create the list of triangles and then print it
def createTriangularNumber(termNumber, symbol):
    #Establishing the variables required. 
    triangleNumber = 1
    triangleList = []

    #loops until there are as many triangles as desired
    while triangleNumber <= termNumber:
        #creating local variables for each round of triangle making
        triangleForThisRound = ""
        numberOfSymbolsThisRound = 1

        #this loops actually creates the triangle
        while numberOfSymbolsThisRound <= triangleNumber:
            thisRoundAddition = "   "*(triangleNumber-numberOfSymbolsThisRound) + (symbol + "     ")*numberOfSymbolsThisRound + "\n"
            triangleForThisRound += thisRoundAddition
            numberOfSymbolsThisRound += 1

        #adds an additional triangle to the entire list
        triangleNumber += 1
        triangleList.append(triangleForThisRound)
    
    #loop to print out all the triangles
    index = 0
    while index < len(triangleList):
        print(triangleList[index])
        index += 1

#activating the program
createTriangularNumber(4, "*")