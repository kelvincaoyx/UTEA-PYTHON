#asking the use for the temperature in degree celsius

userInputTempInCelsius = input("Please enter a temperature in Celsius:")

convertedTemp = 9/5* float(userInputTempInCelsius) + 32

print(userInputTempInCelsius + " is " + str(convertedTemp) + " in fahrenheit")