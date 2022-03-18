lst1 = []

def funcion(lst1):
    lst1 = [int(item) for item in input("Ingrese una lista de numeros: ").split()]

    lst1.sort(reverse = True)

    print(lst1)

funcion(lst1)