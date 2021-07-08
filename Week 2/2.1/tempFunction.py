def tempConvert(celsius):
    fahreinheit = 9/5*celsius+32
    return fahreinheit

celsiusTemp = input("Please input the temperarture in Celsius that you want to convert to Fahreinheit: \n")

print(str(celsiusTemp), " is ", tempConvert(float(celsiusTemp)), " in fahreinhiet")