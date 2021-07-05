#A function that allows the user to determine the standard deviation of inputed numbers

#Getting the inputs from the user
firstMeasurement = float(input("Enter first measurement: "))
secondMeasurement = float(input("Enter second measurement: "))
thirdMeasurement = float(input("Enter third measurement: "))

#Calculating the mean of the 3 measurements
mean = (firstMeasurement + secondMeasurement + thirdMeasurement)/3

#Calculating the standard deviation of the 3 measurements
standardDeviation = (((firstMeasurement - mean)**2 + (secondMeasurement - mean)**2 + (thirdMeasurement - mean)**2)/3)**0.5

#Rounding the standard deviation to 2 decimal places
stDev = round(standardDeviation, 2)

print("The standard deviation for the measurements (" + str(firstMeasurement) + ", " + str(secondMeasurement) + ", " + str(thirdMeasurement) + ") is " + str(stDev) + ".")