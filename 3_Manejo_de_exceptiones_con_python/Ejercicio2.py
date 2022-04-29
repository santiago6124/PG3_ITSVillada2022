while True:
    try:
        num1=int(input("Ingrese numerador: "))
        num2=int(input("Ingrese denominador: "))
        div=num1/num2
        print("El resultado de la división es", div)
        ans=input("Si no desea seguir sumando ingrese [n], si quiere seguir ingrese cualquier otra letra: ")
        if ans=="n":
            break  
    except ZeroDivisionError:
        print("Es imposible dividir por 0.")
    except ValueError:
        print("Usted NO ingresó un número, por favor ingrese correctamente los números")