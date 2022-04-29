meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")
while True:
    try:
        ingreso=int(input("Ingrese un número de mes del 1 al 12: "))
        print(meses[ingreso-1])
        ans=input("Si no desea seguir viendo los nombres de los meses ingrese [n], si quiere seguir ingrese cualquier otra letra: ")
        if ans=="n":
            break  
    except IndexError:
        print("el número de mes va entre 1 y 12")
    except ValueError:
        print("Usted NO ingresó un número, por favor ingrese correctamente los números")