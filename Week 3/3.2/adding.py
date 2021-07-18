def add(number):
    total = ""
    totalNumber = 0
    counter = 0
    while counter <= number:
        if counter == 0:
            total = str(counter)
        else:
            total = total + " + " + str(counter)
            totalNumber = totalNumber + counter
        counter += 1
    return total + " = " + str(totalNumber)
print(add(6))