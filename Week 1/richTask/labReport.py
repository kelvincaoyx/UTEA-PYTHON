'''
Reads measurements from a file and then calculates its
average, standard deviation, and t-score
'''

#quick function to save some typing. Does the calculation of differences squared
def difCalc(measurement):
    calculation = (measurement - average)**2
    return calculation

#open measurements.txt file
fileObject = open("measurements.txt", "r")

#reads each line in the measurements.txt file and assigns it a variable
firstMeasurement = float(fileObject.readline())
secondMeasurement = float(fileObject.readline())
thirdMeasurement = float(fileObject.readline())
fourthMeasurement = float(fileObject.readline())
fifthMeasurement = float(fileObject.readline())
expectedValue = float(fileObject.readline())

#closing the measurements.txt file
fileObject.close()

#Calculates the average of all the measurements
average = (firstMeasurement + secondMeasurement + thirdMeasurement + fourthMeasurement + fifthMeasurement)/5

#printing the header
print("information:\nLab results:")

#printing the average of all the measurements with it rounded to 2 decimals
print("average = " + str(round(average,2)))

#calculating the standard deviation of the measurements
sigma = ((difCalc(firstMeasurement) + difCalc(secondMeasurement) + difCalc(thirdMeasurement) + difCalc(fourthMeasurement) + difCalc(fifthMeasurement))/5)**0.5

#printing the standard deviation with it rounded to 2 decimals
print("sigma = " + str(round(sigma,2)))

'''
Calculating the t-score. I originally just used the unrounded values to calculate the 
tscores, but I think you guys used the rounded answers in your example, so that's what
I did. The formula on the slides squared and then square root the top? So I assume 
you just want the absolute value?
'''
tScore = abs(round(average,2) - expectedValue)/round(sigma,2)

#printing the rounded value of the tscore
print("t-score = " + str(round(tScore,2)))

#Create a file object that will create/open a file called conclusions.txt and start writing in it
conclusionObject = open('conclusions.txt','w')

#write the string inside the bracket into the beginning of the file
conclusionObject.write("Lab results:" +
    "\naverage = " + str(round(average,2)) + 
    "\nsigma = " + str(round(sigma,2)) +
    "\nt-score = " + str(round(tScore,2))
)

#close the file
conclusionObject.close()

#print end message to confirm that the conclusion file has been created
print("has been successfully saved in the file conclusions.txt")