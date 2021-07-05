'''
Helps the user determine the slices of pizza each guest will be receiving and the amount of
left over pizza slices
'''
#Asks the user how many slices are in a party pizza
slicesInAPizza = input("Enter the number of slices: ")

#Asks the user how many guests there are
guests = input("Enter the number of guests: ")

#Calculates the amount ot slices each guest gets
slicesPerPerson = int(slicesInAPizza) // int(guests)

#Calculates the slices of pizza left over
slicesLeft = int(slicesInAPizza) % int(guests)

print("There are " + str(slicesPerPerson) + " slices per person and " + str(slicesLeft) + " slice(s) left.")