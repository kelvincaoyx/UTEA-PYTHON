def round10(num):
    rightmostDigit = num%10
    if rightmostDigit < 5:
        roundedNum = num//10*10
    elif rightmostDigit >= 5:
        roundedNum = num//10*10 + 10
    return roundedNum

def roundSum(a,b,c):
    return round10(a) + round10(b) + round10(c)

print(roundSum(4,4,6))