class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def ladoMayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es el lado 1, con un valor de:", lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado mayor es el lado 2, con un valor de:", lado2)
        elif self.lado3 > self.lado2 and self.lado3 > self.lado1:
            print("El lado mayor es el lado 3, con un valor de:", lado3)
        else:
            print("todos los lados tienen el mismo valor")

    def equilatero(self):
        if lado1 == lado2 and lado1 == lado3:
            print("el triangulo es equilatero")
        else:
            print("el triangulo NO es equilatero")


lado1 = input("Ingrese el lado 1: ")
lado2 = input("Ingrese el lado 2: ")
lado3 = input("Ingrese el lado 3: ")

triangulo1 = Triangulo()
triangulo1.inicializar(lado1, lado2, lado3)
triangulo1.ladoMayor()
triangulo1.equilatero()
