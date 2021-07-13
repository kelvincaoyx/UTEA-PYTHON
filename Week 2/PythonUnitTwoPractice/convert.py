'''A program to take in either fahrenheit or celsius and converts it 
into the other unit
'''
#accepts fahreheit temperatures and converts it to celsius
def fToCTemp(fahrenheitTemp):
    convertedTemp = round(((float(fahrenheitTemp) - 32) * 5 / 9),2)
    return convertedTemp

#accepts celsius temperatures and converts it to fahrenheit
def cToFTemp(celsiusTemp):
    convertedTemp = round(((float(celsiusTemp) * 9 / 5) + 32),2)
    return convertedTemp

#Helps decide which function to use to convert the temps
def helper(temp, unit):
    if unit == "C":
        return str(temp) + "C = " + str(cToFTemp(temp)) + "F"

    elif unit == "F":
        return str(temp) + "F = " + str(fToCTemp(temp)) + "C"

    else:
        return "incorrect units"
#Takes in the temperature without any units
temperature = input("Enter the temperatre: ")

#Takes in the unit of the temperature
unit = input("Enter the unit (C for Celsius and F for Fahrenheit): ")

print(helper(temperature,unit))
