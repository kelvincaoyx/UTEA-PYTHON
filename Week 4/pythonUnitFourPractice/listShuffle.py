"""A function that accepts two list with equal lengtha and then combining
alternating elements from both lists
"""

#function that accepts the two list and then returns a new one with them combined
def shuffle(list1, list2):

    #checks if the lengths of both lists are the same
    if len(list1) != len(list2):
        print("The lengths of both lists are not the same")
        exit()
    items = len(list1)
    index = 0
    combineList = []
    while index < items:
        combineList.append(list1[index])
        combineList.append(list2[index])
        index+=1
    return combineList

#declaring the lists we are going to use
list1 = [1,3,5,7]
list2 = [2,4,6,8]

#printing the lists we are using and the use of the shuffle function
print("2) Testing suffle() function")
print("first list:", list1)
print("second list", list2)
print("combined list:",shuffle(list1, list2))