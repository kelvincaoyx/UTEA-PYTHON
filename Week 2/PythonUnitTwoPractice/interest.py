'''
A program to allows for the user to input their interest rate
and principle of a loan and receive the amount of simple interest 
they must pay 
'''

#A function that takes in an interest rate in percentage and a principle value and calculates simple interest.
#It will output a number in dollars with two decimal places
def simpleInterestCalculator(interestRate, principle):
    simpleInterest = (interestRate / 100) * principle
    simpleInterest = "$" + f"{simpleInterest:.2f}"
    return simpleInterest

#takes in an interest rate in percentage form
userRate = float(input("Enter the interest rate as a percentage: "))

#Takes in the principle value that the usre wants to calculate interest from
userPrinciple = float(input("Enter the principle of the loan: "))

#Prints out the simple interest calculated from this function
print("Your simple interest amount is " + simpleInterestCalculator(userRate, userPrinciple))
