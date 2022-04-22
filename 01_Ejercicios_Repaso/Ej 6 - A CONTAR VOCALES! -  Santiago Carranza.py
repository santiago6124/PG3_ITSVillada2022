from itertools import count

Frase = input("Ingrese una frase: ")


def cuentavocales(string):
    numeroVocales = 0
    for char in string:
        if char in "aeiouAEIOU":
            numeroVocales = numeroVocales + 1
    return print("La frase cuenta con: ", numeroVocales, " Vocales")


cuentavocales(Frase)
