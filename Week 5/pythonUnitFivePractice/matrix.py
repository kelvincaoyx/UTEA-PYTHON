'''This program is used to switch the rows with columns in a matrix'''

#this function accepts a matrix and then flips the rows and columns

def matrixFlipper(matrix):

    #initializing the required variables
    row, rows = 0, len(matrix)
    flippedMatrix =[]

    #creating a list of lists
    for i in range(len(matrix[row])):
        flippedMatrix.append([])

    #iterating through every row and column and flipping them
    while row < rows:
        col, cols = 0, len(matrix[row])
        while col < cols:
            flippedMatrix[col].append(matrix[row][col])
            col += 1
        row += 1
    return flippedMatrix

#function that creates a nice visual for the user to see the matrix
def matrixPrinter(matrix):
    row, rows = 0, len(matrix)
    printingList=""
    while row < rows:
        col, cols = 0, len(matrix[row])
        while col < cols:
            printingList += str(matrix[row][col]) + " "
            col += 1
        printingList += "\n"
        row += 1
    return printingList

#takes in a matrix and then prints out the original matrix and then the transformed one
def helper(matrix):
    print(matrixPrinter(matrix))
    print(matrixPrinter(matrixFlipper(matrix)))

#Creating sample matrix to test out the function
matrix1 = [[2,3,4],[1,5,8]]
matrix2 = [[2,3,4],]

#Activating the matrix functions

helper(matrix1)
helper(matrix2)


