'''
This program is used to allow a user to open a file
'''
#allows the user to input the name that they want to name the new file
fileName = input("Enter the file name: ")

#add the ".txt" so that the user's file name works
fileNameWithExtension = fileName + ".txt"

#Create a file object that the user will be accessing
fileObject = open(fileNameWithExtension,'r')

#read the string from inside the file specified by the user
textInFile = fileObject.read()

#close the file
fileObject.close()

print("The content \"" + textInFile +"\",\nhas been successfully retrieved in the file " + fileNameWithExtension)