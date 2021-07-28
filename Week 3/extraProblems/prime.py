def primeCheck(number):
    primeFileObject = open("prime.txt",'w')
    numberFileObject = open("number.txt",'w')
    divisibleNumberCheck = 2
    while divisibleNumberCheck < number:
        if number % divisibleNumberCheck == 0:
            print(number, "is not a prime number")
            primeFileObject.write(False)
            numberFileObject.write(number)
            return
        divisibleNumberCheck += 1
    print(number, "is a prime number")
    primeFileObject.write(True)
    numberFileObject.write(number)
        
def inputHelper():
    userInput = input("Enter a number: ")
    while userInput != "exit":
        primeCheck(float(userInput))
        userInput = input("Enter a number: ")

inputHelper()