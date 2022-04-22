class Persona:

    def inicializar(self,nombre):
        self.nombre=nombre

    def print(self):
        print("Nombre",self.nombre)


persona1=Persona()
nombre=input("Ingrese el nombre de la persona 1 ")
persona1.inicializar(nombre)
persona1.print()

persona2=Persona()
nombre=input("Ingrese el nombre de la persona 2 ")
persona2.inicializar(nombre)
persona2.print()