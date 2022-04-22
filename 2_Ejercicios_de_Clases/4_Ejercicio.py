class Operaciones:
    def __init__(self):
        self.numero1 = int(input("Ingrese el numero 1: "))
        self.numero2 = int(input("Ingrese el numero 2: "))
        self.Suma()
        self.Resta()
        self.Multipicacion()
        self.Divison()

    def Suma(self):
        print("la suma entre los numeros da: ", self.numero1 + self.numero2)

    def Resta(self):
        print("la resta entre los numeros da: ", self.numero1 - self.numero2)

    def Multipicacion(self):
        print("la Multiplicacion entre los numeros da: ", self.numero1 * self.numero2)

    def Divison(self):
        print("la Division entre los numeros da: ", self.numero1 / self.numero2)


operacion = Operaciones()
