'''This program is used to accept an email address and mask all of its vowels
all vowels before the @ will be replaced with a * and everything afterwards will
be replaced with a #
'''

#function that replaced all the vowels in the email with the designated symbols
def maskEmail(email):
    if emailChecker(email) == False:
        return "Invalid email format"
    #determining where the @ is in the string
    index = 0
    while email[index] != "@":
        index += 1

    #replaces all the vowels with stars (only applies to the characters before the @)
    replaceWithStar = email[:index]
    starIndex = 0
    while starIndex < len(replaceWithStar):
        if replaceWithStar[starIndex].lower() in ["a","e","i","o","u"]:
            firstPart = replaceWithStar[:starIndex]
            secondPart = replaceWithStar[starIndex+1:]
            replaceWithStar = firstPart + "*" + secondPart
        starIndex += 1

    #replaces all the vowels with  # (only applies to the characters after the @)
    replaceWithA = email[index+1:]
    AIndex = 0
    while AIndex < len(replaceWithA):
        if replaceWithA[AIndex].lower() in ["a","e","i","o","u"]:
            firstPart = replaceWithA[:AIndex]
            secondPart = replaceWithA[AIndex+1:]
            replaceWithA = firstPart + "#" + secondPart
        AIndex += 1
    return replaceWithStar + "@" + replaceWithA

#function to check if the domain entered is valid
def emailChecker(email):

    #determining where the @ is in the string and if there is one at all
    indexA = 0
    while email[indexA] != "@":
        indexA += 1
        if indexA >= len(email):
            return False

    #seperating the domain from the email so that the program goes through less work
    domain = email[indexA:]

    #Checks if there is an invalid character after the @
    indexP = 0
    if domain[1] in [".",""," "]:
        return False

    #Checks if there is a period at all in the domain. if not, there will be an error
    indexP = 1
    while True:
        if domain[indexP] == ".":
            break
        indexP += 1
        if indexP == len(domain)-1:
            return False

    #checks if there is a valid character behind the period
    indexP = 0
    while indexP < len(domain):
        if domain[indexP] == "." and domain[indexP+1] in ["", " "]:
            return False
        indexP += 1
    
    return True

email1 = "some.NameAha@notValidDomain"
email2 = "some.NameAha@notValidDomain."
email3 = "some.NameAha@notValidDomain.c"
email4 = "some.NameAhanotValidDomain@.c"
email5 = "some.NameAha@c.c"

#printing out all headers and stuff
print("3) Testing maskEmail() function\n\n")
print("email: ", email1)
print(maskEmail(email1))
print("email: ", email2)
print(maskEmail(email2))
print("email: ", email3)
print(maskEmail(email3))
print("email: ", email4)
print(maskEmail(email4))
print("email: ", email5)
print(maskEmail(email5))

