from myFirstLibrary import G
from myFirstLibrary import scientificNotation
from myFirstLibrary import calculateGForce

print("G = " + str(scientificNotation(G,2)) + " N*m^2.kg^2")

print("g = " + str(round(calculateGForce(5.99*10**24,1,6.4*10**6),1)) + " m/s^2")