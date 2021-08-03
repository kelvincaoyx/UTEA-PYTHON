"""Accepts a list of objects of the same type and will return true if there are no duplicates"""
#importing random library so that we can use it
import random

#function that tests if there are any duplicate objects inside a list 
def isSet(list):
    index = 0
    
    while index < len(list):
        testIndex = index + 1
        while testIndex < len(list):
            if list[index] == list[testIndex]:
                return False
            testIndex += 1
        index += 1
    return True

#function that randomly generates a list of numbers
def generateRandomSet(items, low, high):
    set = []
    for index in range(items):
        set.append(random.randint(low,high))
    return set

#function that helps me automatically print out if the list is a set or not
def helper(set):
    if isSet(set) == True:
        print(set, "is a set\n")
    else:
        print(set, "is not a set\n")

#printing out some example uses of the function
print("1) Testing isSet() function\n")
helper([1,2,3,4,5,5])

print("2) Testing isSet() function\n")
helper([1,2,3,4,5,6])

print("3) Testing isSet() with generateRandomSet() function:\n")
print("testSet2 = generateRandomSet(5, 1, 10)\n")
helper(generateRandomSet(5, 1, 10))
