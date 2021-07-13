'''
Allows the user to input variables to solve a linear quadratic system
'''

#Function to more easily check the value of a variable and will output an error if the variable is invalid
def inputChecker(letter):
    value = input("Enter the value of parameter " + letter + ": ")
    if value == "":
        print("The values of your parameter are invalid!")
        exit()
    return float(value)

#easy way for the program to find the y value after finding valid x values
def yValueSolver(m,d,x):
    return m*x + d

#prints out the header for the user
print("This calculator solves a linear quadratic system.\
    \ny=ax^2+bx+c\
    \ny=mx+d")

#allows the user to input a
a = input("Enter the value of parameter a: ")

#checks if a is valid and then gives an error if it isn't
if a == "0" or a == "":
    print("The values of your parameter are invalid!")
    exit()

#allows the user to input values
b = inputChecker("b")
c = inputChecker("c")
m = inputChecker("m")
d = inputChecker("d")

#Creating new variables so I can use the Quadratic formula with these numbers
letterA = float(a)
letterB = b - m
letterC = c - d

#Creating the discriminant variable to make it clear what I am doing and because I use this variable often
discriminant = letterB**2 - 4 * letterA * letterC

#When the discriminant is below 0, there are no solutions for the system and the program replies as such
if discriminant < 0:
    print("There is no solution for this linear quadratic system")
    exit()

#when the discriminate is 0, there is only one answer. This if loop helps the program find that single point
if discriminant == 0:
    solutionX = -letterB/2*letterA
    solutionY = yValueSolver(m,d,solutionX)
    print("The solution of your linear quadratic system is: \
        \n(x , y) = (" + str(solutionX) + " , " + str(solutionY) + ")")

#in other words, whenever the discriminant is positive, there are two answers to the system and this loop finds it
else:
    solutionX1 = (-letterB + discriminant**0.5)/2/letterA
    solutionY1 = yValueSolver(m,d,solutionX1)

    solutionX2 = (-letterB - discriminant**0.5)/2/letterA
    solutionY2 = yValueSolver(m,d,solutionX2)

    print("The solution of your linear quadratic system are:" + \
        "\n(x1 , y1) = (" + str(solutionX1) + " , " + str(solutionY1) + ")" +  \
        "\n(x2 , y2) = (" + str(solutionX2) + " , " + str(solutionY2) + ")")
    