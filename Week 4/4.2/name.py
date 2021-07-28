def nameSlicer(name):
    index = 0
    while name[index] != " ":
        index += 1
    firstName = name[:index].lower()
    lastName = name[index+1:].lower()
    firstName = firstName[0].upper() + firstName[1:]
    print(firstName)
    print(lastName)

nameSlicer("Kelvin Cao")