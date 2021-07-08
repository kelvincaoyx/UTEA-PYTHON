def evenChecker(number):
    return isinstance(number,float) \
        or isinstance(number,int) \
        and number%2 == 0

print(evenChecker(8))
print(evenChecker(3))
print(evenChecker(-0.24))