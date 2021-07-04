#Create a fiel object that has the file test.txt open or created
#in writing mode
fileObject = open('Week 1/1.2/text.txt','w')


#write the string inside the bracket into the beginning of the file
fileObject.write('this line will be saved to the test.txt file')

#close the file
fileObject.close()



#Open the same file for reading
fileObject = open('Week 1/1.2/text.txt','r')

'''
Print in the console the contents of the file and its Name
using properties and the built-in functions of the file object
get the text from the file using the read() built-in function
and store it in the fileText variable
'''

fileText = fileObject.read()

#get the file name form the txt file and store it in the fileName Variable
fileName = fileObject.name

#display the information in the console
print('the file ' + fileName + ', has the following content \n' + fileText)