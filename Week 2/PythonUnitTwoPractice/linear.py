'''
A calculator for a linear equation
'''

#Checks if the equation can be solved/ returns the answer
def linearEquationSolver(a,b,c):
    if a == "" or b == "" or c == "" or a == "0":
        return None
    
    x = (float(c) - float(b))/float(a)
    
    return x

#Header of the calculator
print("This calculator solves an equation of the form ax+b=c.")

a = input("Enter the value of the parameter a: ")
b = input("Enter the value of the parameter b: ")
c = input("Enter the value of the parameter c: ")

#checks if the equation is solvable and can output an error message
if linearEquationSolver(a,b,c) == None:
    print("The values of your parameters are invalid")

#outputs the answer of the equation
else:
    print("The solution of your equation " + a + "x + " + b + " = " + c + " is x = " + str(linearEquationSolver(a,b,c)))