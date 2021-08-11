#reformats a valid code
def formatCode(code):
    code = code.replace(" ", "").upper()
    return code[:3] + " " + code[3:]

#checks what province the code is from
def getProvince(postalCode):
    if postalCode[0] == "A":
        return "NL"
    elif postalCode[0] == "B":
        return "NS"
    elif postalCode[0] == "C":
        return "PE"
    elif postalCode[0] == "E":
        return "NB"
    elif postalCode[0] in ["G", "H", "J"]:
        return "QC"
    elif postalCode[0] in ["K", "L", "M", "N", "P"]:
        return "ON"
    elif postalCode[0] == "R":
        return "MB"
    elif postalCode[0] == "S":
        return "SK"
    elif postalCode[0] == "T":
        return "AB"
    elif postalCode[0] == "V":
        return "BC"
    elif postalCode[0] == "X":
        return "NU/NT"
    elif postalCode[0] == "Y":
        return "YT"
    else:
        return "None"

#checks if the code is valic
def isValid(code):
    code = code.replace(" ", "")
    if len(code) != 6:
        return False
    if code[0].isalpha() == False or code[2].isalpha() == False or code[4].isalpha() == False:
        return False
    if code[1].isdigit() == False or code[3].isdigit() == False or code[5].isdigit() == False:
        return False
    return True