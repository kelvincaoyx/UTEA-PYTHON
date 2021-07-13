'''
A calculator for a linear equation
'''

def linearEquationSolver(a,b,c):
    if a == "" or b == "" or c == "" or a == "0":
        return None
    
    x = (float(c) - float(b))/float(a)
    
    return x

def helper(a,b,c,solution):
    if solution == None:
        return "The values of your parameters are invalid"
    return "The solution of your equation " + str(a) + "x + " + str(b) + " = " + str(c) + " is x = " + str(solution)

print("This calculator solves an equation of the form ax+b=c.")

a = input("Enter the value of the parameter a: ")
b = input("Enter the value of the parameter b: ")
c = input("Enter the value of the parameter c: ")

print(helper(a,b,c,linearEquationSolver(a,b,c)))