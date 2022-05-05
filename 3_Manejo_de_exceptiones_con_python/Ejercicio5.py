while True:
    try:
        ingreso = input("ingrese un texto: ")
        datos = open('texto.txt', 'a')

        if ingreso.isnumeric():
            datos.write(int(ingreso))
        else:
            datos.write(ingreso)
        ans=input("Si no desea seguir viendo los nombres de los meses ingrese [n], si quiere seguir ingrese cualquier otra letra: ")
        if ans=="n":
            break  

    except TypeError:
        print("Ingrese un texto sin números")