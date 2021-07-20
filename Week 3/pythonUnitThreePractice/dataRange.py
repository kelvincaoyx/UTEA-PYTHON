'''Reads a bunch of data from a text file. Allows the user to input a upper and lower bound
and takes all the numbers in the text file that meets though criteria. After retreiving
those numbers, it will return the average of all the numbers in the specified range
'''

#function that allows the user to input their desired file, and the boundaries they want
def fileReader(file, low, high):
    #checks if the ranges entered are valid
    if low >= high:
        print("Your specified ranges are not valid")
        exit()
    
    #opens the file, establishes some variables and starts reading the file
    fileObject = open(file + ".txt",'r')
    line = fileObject.readline()
    sumOfNumbers = 0
    numbersAdded = 0

    #while loops that continues running until the end of the txt file
    while line != "":

        #checks if the line fits inside the specified ranges
        if float(line) >= low and float(line) <= high:

            #some operations that helsp me calculate the average of the numbers
            sumOfNumbers += float(line)
            numbersAdded += 1
            print("Data point: " + line + " added")
        
        #allows the loop to check the next line
        line = fileObject.readline()
    
    #prints out the calculated average and the results of the calculator
    print("The data in the range (",low,",",high,") have an average:", round(sumOfNumbers/numbersAdded,2))
    
    #closes the file
    fileObject.close()

#allows the user to input their file name that they want to access and the boundaries
file = input("Enter file name: ")
low = float(input("Enter the low boundary: "))
high = float(input("Enter the high boundary: "))

#starts up the function with the specified variables
fileReader(file,low,high)