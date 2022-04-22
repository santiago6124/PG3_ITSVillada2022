class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def imprimir(self):
        print("El nombre es: ", self.nombre)
        print("La edad es: ", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese el sueldo del empleado: "))

    def imprmir(self):
        super().imprimir()
        print("El sueldo del empleado es: ", self.sueldo)

    def pagaImpuestos(self):
        if self.sueldo > 3000:
            print("El empleado deberá pagar impuestos")
        else:
            print("el empleado NO deberá pagar impuestos")


persona1 = Persona()
persona1.imprimir()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
empleado1 = Empleado()
empleado1.imprimir()
empleado1.pagaImpuestos()
