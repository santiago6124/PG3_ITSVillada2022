NumeroUsuario = int(input("Ingrese un número: "))


def isStep(n):
    a = map(int, str(n)[1:])
    b = map(int, str(n)[:-1])
    return all(abs(a_digit - b_digit) == 1 for a_digit, b_digit in zip(a, b))


if isStep(NumeroUsuario) == True:
    print("El numero", NumeroUsuario, " SI es step")
else:
    print("El numero", NumeroUsuario, " NO es step")
