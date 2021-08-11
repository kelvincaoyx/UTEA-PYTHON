import matplotlib.pyplot as plt

datax = list(range(10))

def getCoefficients():
    a,b,c = input("eneter a,b,c, values").split()
    return [float(a),float(b),float(c)]
datay = []

def generateYValue(coefficients, datax, datay):
    max = len(coefficients) - 1
    for x in datax:
        y = 0
        for index in range(max):
            y+= coefficients[index]*(x**(max-index))
        datay.append(y)

generateYValue(getCoefficients(),datax,datay)

print("Close the graph to end the program, or ctrl c")

plt.plot(datax,datay)
plt.show()