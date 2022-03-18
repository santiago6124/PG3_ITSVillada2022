Year = int(input("Ingrese un año: "))
def Añobisiesto(Year):

    if (( Year%400 == 0) or (( Year%4 == 0 ) and ( Year%100 != 0))):
        print(Year, " SI es un año bisiesto")
    else:
        print(Year, " NO es un año bisiesto")

Añobisiesto(Year)
