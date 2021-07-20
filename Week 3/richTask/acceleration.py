'''Allows the user to enter two text files, one with directions and another one with magnitudes. These two files correspond to
vectors that will be added together to print the Fnetx, Fnety, acceleration of the object, and the angle of the Fnet. 
The user will also be required to input the mass of the object
'''
#importing the math library so that we can more do more advanced mathematical calculations
import math

#function that will add up all the vectors and calulate the fnet and acceleration of the object
def fnetCalc(mass, directionFile, magnitudeFile):

    #opens the files, establishes some variables and starts reading the file
    directionFileObject = open(directionFile,'r')
    magnitudeFileObject = open(magnitudeFile,'r')
    directionLine = directionFileObject.readline()
    magnitudeLine = magnitudeFileObject.readline()
    fnetx = 0
    fnety = 0
    vectorCounter = 1

    #while loops that continues running until the end of the txt file
    while directionLine != "" and magnitudeLine != "":

        #determines the xy vector components based on the line that was just read
        fx = float(magnitudeLine) * math.cos(float(directionLine)*math.pi/180)
        fy = float(magnitudeLine) * math.sin(float(directionLine)*math.pi/180)
        
        #prints out the xy vector components that were just calculated
        print("Fx" + str(vectorCounter) + " = " + str(round(fx,1)) + "N, Fy" + str(vectorCounter) + " = " + str(round(fy,1)) + "N")

        #adds to the vector counter so that we can keep track of which vector we are calculating
        vectorCounter += 1

        #adds the new vector components to the new force components
        fnetx += fx
        fnety += fy

        #reading the new line of both files
        directionLine = directionFileObject.readline()
        magnitudeLine = magnitudeFileObject.readline()
    
    #closes the files
    directionFileObject.close()
    magnitudeFileObject.close()

    #prints the calculated net force vector components and the inputted mass variable
    print("Fnetx = " + str(round(fnetx,1)) + "N, Fnety = " + str(round(fnety,1)) + "N")
    print("The object with mass m = " + str(mass) + "kg,")

    #calculating the magnitude of the combined vectors. Will be used later to calculate acceleration
    fnet = math.sqrt(fnetx**2 + fnety**2)

    #calculating the related acute angle the combined vector will have
    acuteAngle = math.atan(abs(fnety)/abs(fnetx)) * 180 / math.pi

    #using the related acute angle and the CAST rule, these if/elif blocks help determine the angle of the vector
    if fnety > 0 and fnetx > 0:
        angle = acuteAngle
    elif fnety > 0 and fnetx < 0:
        angle = 180 - acuteAngle
    elif fnety < 0 and fnetx < 0:
        angle = 180 + acuteAngle
    else:
        angle = 360 - acuteAngle
    
    #printing the results all of the calculations done in the function
    print("will experience an acceleration a = " + str(round(fnet/mass,1)) + " m/s^2    " + str(round(angle,1)) + " degrees")

#allows the user to input their desired variables into the calculator
mass = float(input("Enter the mass of the object: "))
magnitudeFile = input("Enter the file name for the magnitude data: ")
directionFile = input("Enter the file name for the direction data: ")

#uses the variables gathered from the user and inputs it into the fnet calculator
fnetCalc(mass, directionFile, magnitudeFile)

