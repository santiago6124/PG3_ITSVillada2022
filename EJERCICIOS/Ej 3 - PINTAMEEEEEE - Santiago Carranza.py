def pintar():
    for i in range(0, alto):
        print(char * ancho)


def pintar_triangulo(alto, char):
    for i in range(alto):
        print(" " * (alto - i - 1) + (char + " ") * (i + 1))


def pintar_triangulo_invertido(alto, char):
    for i in range(alto):
        print(" " * (i + 1) + (char + " ") * (alto - i))


opcion = int(
    input(
        "Si quiere dibujar un cuadrado ingrese 1, si quiere dibujar un triangulo ingrese 2 e ingrese 3 si quiere pintar un triangulo invertido: "
    )
)

if opcion == 1:
    char = input("Ingrese el caracter que quiera que sea usado para formar la figura: ")
    ancho = int(input("Ingresá el ancho de la figura: "))
    alto = int(input("Ingresá el alto de la figura: "))
    pintar()

elif opcion == 2:
    char = input("Ingrese el caracter que quiera que sea usado para formar la figura: ")
    alto = int(input("Ingresá el alto de la figura: "))
    pintar_triangulo(alto, char)

elif opcion == 3:
    char = input("Ingrese el caracter que quiera que sea usado para formar la figura: ")
    alto = int(input("Ingresá el alto de la figura: "))
    pintar_triangulo_invertido(alto, char)

else:
    print("Ingrese una opcion valida")
