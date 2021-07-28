'''This program is supposed to emulate the copy() function built into python'''

#function to emulate the copy function in python
def copy(list):
    copyList = list[:]
    return copyList

#defining the list
some_data = [1,2,3,4,"w"]

#printing header and the original list
print("1) Test copy() function")
print("The original data:")
print(some_data)

#using the copy function that was newly created
copy_data = copy(some_data)
copy_data.append("New data will not be in the original data")
print("The copied modified data:")
print(copy_data)

#checking if the data was actually copied and a new list was created
print("some_data == copy_data is " + str(copy_data == some_data))