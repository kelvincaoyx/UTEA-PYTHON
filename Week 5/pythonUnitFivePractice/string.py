'''A program that will allow you to change a specific letter in a whole sentence'''

#a function to convert a string into a list
def toList(string):
    convertedString = []
    index = 0
    while index < len(string):
        convertedString.append(string[index])
        index += 1
    return convertedString

#A function to convert a list into a string
def toString(list):
    convertedList = ""
    index = 0
    while index < len(list):
        convertedList += list[index]
        index += 1
    return convertedList

#A function that takes in a string, a character that will be replaced an a replacement character
def replace(string, character, replacementCharacter):

    #intializes some variables
    newList = toList(string)
    index = 0
    changes = 0

    #prints out the string so that the user knows what they are doing
    print(string)

    #goes through the list
    while index < len(newList):
        if newList[index] == character:
            #adding additional info
            additionalInfo = newList.copy()
            additionalInfo.pop(index)
            additionalInfo.insert(index, "(" + character + ")")
            print(toString(additionalInfo))

            #asking if the user wants to replace the character
            replace = input("Replace '" +  newList[index] + "' in position " + str(index+1) + " with '" + replacementCharacter + "' (y/n)? ")
            if replace == "y" or replace == "Y":
                newList.pop(index)
                newList.insert(index, replacementCharacter)
                changes += 1
        index += 1
        
    #printing the changes
    print("There were ", changes, " changes.")
    return toString(newList)

#activating the function
print(replace("Hella there, haw are yau", "a", "o"))