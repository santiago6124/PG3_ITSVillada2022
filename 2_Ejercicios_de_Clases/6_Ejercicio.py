class Familia:
    def __init__(self):
        self.nombrep = input("Ingrese el nombre del padre: ")
        self.nombrem = input("Ingrese el nombre de la madre: ")
        self.lista = input(
            "Ingrese el nombre de los hijos separados por un espacio: "
        ).split()

    def __str__(self):
        string = self.nombrep + "," + self.nombrem
        for i in self.lista:
            string = string + "," + i
        return string


familia1 = Familia()


print(familia1)
