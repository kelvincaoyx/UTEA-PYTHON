'''This program is used to shift elements in a lift a specified value left
or right. With a negative value meaning shifting to the left while a positive value 
meaning shifting to the right
'''

#function that will shift a list of numbers in a specified direction
def shift(list, shiftNumber):

    #copying over the list to make a new shifted list
    shiftedList = list.copy()

    #this helps the list shift left by using a while loop
    while shiftNumber < 0:
        shiftedList.append(shiftedList[0])
        shiftedList.pop(0)
        shiftNumber += 1
    
    #this helps the list shift right using a while loop
    while shiftNumber > 0:
        lastItemsIndex = len(shiftedList)-1
        shiftedList.insert(0,shiftedList[lastItemsIndex])
        shiftedList.pop(lastItemsIndex+1)
        shiftNumber -= 1

    #returning a shifted list
    return shiftedList

#declaring some variables
originalString = [1,2,3,4,5,6]
shifting = 3

#printing out the results
print("This is the original string", originalString)
print("This is the new string shifted", shifting, "units", shift(originalString,shifting))