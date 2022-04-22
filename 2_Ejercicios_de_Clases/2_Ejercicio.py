class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def print(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def status(self):
        if self.nota>=7:
            print(nombre, " está aprobado")
        else:
            print(nombre, " está desaprobando")

persona1 = Alumno()
nombre = input("Ingrese el nombre de la persona 1 ")
nota = int(input("Ingrese la nota de la persona 1 "))
persona1.inicializar(nombre, nota)
persona1.print()
persona1.status()

persona2 = Alumno()
nombre = input("Ingrese el nombre de la persona 2 ")
nota = int(input("Ingrese la nota de la persona 2 "))
persona2.inicializar(nombre, nota)
persona2.print()
persona2.status()