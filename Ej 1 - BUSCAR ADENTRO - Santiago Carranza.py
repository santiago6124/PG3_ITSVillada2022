ListaDeNumeros = ["8", "12" , "9" , "45"]

def funcion(ListaDeNumeros):
    print(ListaDeNumeros)

    NumeroDelUsuario = input("Ingresá un número: ")

    index = ListaDeNumeros.index(NumeroDelUsuario)
    print("La posición del número buscado es: ", index)


funcion(ListaDeNumeros)
