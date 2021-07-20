'''A program to allow the user to input a wavelength in nanometers
and then have a program output the corresponding colour in the
visible spectrum
'''
#import the library to change the colour of the text
from colorama import init, Fore, Back
init()

#function that accepts a wavelength number and then outputs the corresponding colour
def getColor(number):
    if number < 380:
        return "unknown"
    elif number < 450:
        return "Violet"
    elif number < 495:
        return "Blue"
    elif number < 570:
        return "Green"
    elif number < 590:
        return "Yellow"
    elif number < 620:
        return "Orange"
    elif number < 750:
        return "Red"
    else:
        return "unknown"

#helps me make the last colour of the output the corresponding color to make it easier for the user to understand the output
def colorHelper(colour):
    if colour == "unknown":
        print("The colour for the light with lambda = ", waveLength, "nm is", Back.WHITE, getColor(waveLength))
    elif colour == "Violet":
        print("The colour for the light with lambda = ", waveLength, "nm is", Fore.MAGENTA, getColor(waveLength))
    elif colour == "Blue":
        print("The colour for the light with lambda = ", waveLength, "nm is", Fore.BLUE, getColor(waveLength))
    elif colour == "Green":
        print("The colour for the light with lambda = ", waveLength, "nm is", Fore.GREEN, getColor(waveLength))
    elif colour == "Yellow":
        print("The colour for the light with lambda = ", waveLength, "nm is", Fore.YELLOW, getColor(waveLength))
    elif colour == "Orange":
        print("The colour for the light with lambda = ", waveLength, "nm is", Back.YELLOW, getColor(waveLength))
    elif colour == "Red":
        print("The colour for the light with lambda = ", waveLength, "nm is", Fore.RED, getColor(waveLength))

#allows the user to enter the wavelength they want to calculate colour with
waveLength = float(input("Enter the wave length: "))

#activated the helper to allows for the answer to be printed
colorHelper(getColor(waveLength))