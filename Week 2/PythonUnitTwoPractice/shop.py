'''
Helps the user calculate the tax that they should charge the customer
'''

def tax():
    location = input("Are you shopping from Ontario? Enter Y or N: ")
    
    if location == "n" or location == "N":
        taxRate = input("Enter the tax of your state or province as a percentage: ")

    if location == "y" or location == "Y":
        taxRate = "13"

    price = float(input("Enter the price of the item: "))
    age = int(input("Enter your age: "))
    member = input("Are you a member of this store? Enter Y or N: ")

    if (age < 18 or age >= 65) and (member == "y" or member == "Y"):
        price = price * 0.85

    return str(round((price * float("1." + taxRate)),2))


print("The total cost with tax for your order is " + tax())
        