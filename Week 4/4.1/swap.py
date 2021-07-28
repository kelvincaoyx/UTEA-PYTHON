def swap(list):
    swappingList = []
    if len(list)% 2 == 0:
        middle = len(list)//2
        swappingList = list[middle:] + list[:middle]
    else:
        middle = len(list)//2
        swappingList = list[middle+1:] 
        swappingList.append(list[middle]) 
        swappingList += list[:middle]
    return swappingList
list1 = [4,3,10,20,2]
print(swap(list1))