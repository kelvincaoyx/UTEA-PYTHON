'''
this program is used to check if postal codes are valid and sees where 
the postal codes come from
'''
#importing functions
from postal import formatCode
from postal import getProvince
from postal import isValid

'''
formatted = formatCode("m 5P1j 4")
print(formatted)

province = getProvince("M5P 1J4")
print(province)

province = getProvince("D5P 1J4")
print(province)

print(isValid("M5R 1J4"))
print(isValid("   m  5 P 1 j    4"))
print(isValid("M5P1J"))
print(isValid("m5p114"))
'''
#helper function to help check if postal codes are valid
def helper(code):
    if isValid(formatCode(code)) == False:
        print("'" + code + "' is improper code")
        return
    print("'" + code + "' properly formatted is " + formatCode(code))
    print("it belongs to " + getProvince(formatCode(code)))

#test cases
helper(" ")
helper("")
helper("M5M q1j")
helper("M4M1L4")
helper("1K2 L4M")
helper("m5M 1p2")
helper("t2t    4   f2")
helper("D2E 1l4")