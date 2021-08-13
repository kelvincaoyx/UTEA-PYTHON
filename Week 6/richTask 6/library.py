import random
import os

#function to help me create random digits. Less to type than random.randrange
def randomDigit(start,stop):
    return random.randrange(start,stop)

#Clears the entire screen.
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    return