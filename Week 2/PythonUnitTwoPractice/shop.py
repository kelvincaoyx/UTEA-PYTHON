'''
Helps the user calculate the price that they should charge the customer
'''

def tax():
    #Checks if the user is from ontario or not
    location = input("Are you shopping from Ontario? Enter Y or N: ")
    
    #Makes the user input a tax rate if they are not from ontario
    if location == "n" or location == "N":
        taxRate = input("Enter the tax of your state or province as a percentage: ")

    #Gives the user the default rate of 13 percent if they are from ontario
    if location == "y" or location == "Y":
        taxRate = "13"

    #Gets some information from the user to help us calculate the final price
    price = float(input("Enter the price of the item: "))
    age = int(input("Enter your age: "))
    member = input("Are you a member of this store? Enter Y or N: ")

    #Gives the customer a discount if they fulfill all the proper conditions
    if (age < 18 or age >= 65) and (member == "y" or member == "Y"):
        price = price * 0.85

    return str(round((price * float("1." + taxRate)),2))

#prints out the final price that the user will need to pay
print("The total cost with tax for your order is " + tax())
        