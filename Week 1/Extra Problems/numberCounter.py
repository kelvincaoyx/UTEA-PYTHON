number = int(input("please input a 5 digit number: "))

tenThousand = number//10000

thousand = (number%10000)//1000

hundred = (number%10000)%1000//100

tenth = ((number%10000)%1000%100)//10

ones = (((number%10000)%1000%100)%10)

print("First digit is: ", tenThousand)
print("Second digit is: ", thousand)
print("Third digit is: ", hundred)
print("fourth digit is: ", tenth)
print("fifth digit is: ", ones)