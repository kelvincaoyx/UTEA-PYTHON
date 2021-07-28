def is_in(list,number):
    index = 0
    items = len(list)
    while index != items:
        if list[index] == number:
            return True
        index += 1
    return False
print(is_in([4,3,10,29,2,5],5))