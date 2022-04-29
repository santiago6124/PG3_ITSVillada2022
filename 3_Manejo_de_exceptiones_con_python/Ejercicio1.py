while True:
    try:
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese un segundo número: "))
        sum=num1+num2
        print("La suma es: ", sum)
        ans=input("Desea seguir sumando?[y/n]: ")
        if ans=="n":
            break  
    except ValueError:
       print("Usted NO ingresó un número, por favor ingrese correctamente los números")
       