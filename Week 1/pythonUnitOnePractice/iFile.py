'''
This program is used to allow a user to create a file and write stuff in the file
'''
#allows the user to input the name that they want to name the new file
fileName = input("Enter the file name: ")

#allows the user to input a line of text to put into the file
textInFile = input("Enter a one line text: ")

#add the ".txt" so that the user's file name works
fileNameWithExtension = fileName + ".txt"

#Create a file object that the user will be accessing
fileObject = open(fileNameWithExtension,'w')

#write the string from the user into the beginning of the file
fileObject.write(textInFile)

#close the file
fileObject.close()

print("The content \"" + textInFile +"\",\nhas been successfully saved in the file " + fileNameWithExtension)