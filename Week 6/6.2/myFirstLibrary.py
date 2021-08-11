G = 6.67 * 10**11

def calculateGForce(m1,m2,r):
    return G*m1*m2/r**2


def scientificNotation(number, decimals):
    return("{:." + str(decimals) + "e}").format(number)