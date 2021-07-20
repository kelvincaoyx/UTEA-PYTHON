'''A program that reads data from two different files. One file corresponds to the word while the
other one corresponds to the word's frequency. This program will accept a cutoff frequency and 
print all the words that make the cutoff
'''

#funtion that accepts two text files and a cutoff and uses these variables to output words above a specified frequency
def fileReader(wordFile, frequencyFile, cutoff):
    
    #opens the files, establishes some variables and starts reading the file
    wordFileObject = open(wordFile + ".txt",'r')
    frequencyFileObject = open(frequencyFile + ".txt",'r')
    wordLine = wordFileObject.readline()
    frequencyLine = frequencyFileObject.readline()
    numberOfWords = 0

    #while loops that continues running until the end of the txt file
    while wordLine != "" and frequencyLine != "":

        #checks if the frequency fits inside the specified ranges
        if float(frequencyLine) >= cutoff:
            
            #prints out the word and its actual frequency
            print("Word = ", wordLine.strip("\n"))
            print("Freq = ", frequencyLine)

            #keeps track fo the number of words that make the cutoff
            numberOfWords += 1
            
        #allows the loop to check the next line
        wordLine = wordFileObject.readline()
        frequencyLine = frequencyFileObject.readline()
    
    #prints out the calculated total number of words that made the cutoff 
    print("\n\nThere were", numberOfWords, "with freq >=", cutoff)
    
    #closes the files
    wordFileObject.close()
    frequencyFileObject.close()

#allows the user to input the cutoff frequency they want
cutoff = float(input("Enter cutoff frequency: "))

#starts up the function with the specified variables
fileReader("words","frequency",cutoff)