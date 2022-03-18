char = input("Ingrese el caracter que quiera que sea usado para formar la figura: ")
ancho = int(input("Ingresá el ancho de la figura: "))
alto = int(input("Ingresá el alto de la figura: "))
def pintar():
    for i in range(0,alto):
        print(char * ancho)

pintar()