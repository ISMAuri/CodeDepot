class Animal:
    def comer(self):
        print('*come*')

class Ave(Animal):
    def volar(self):
        print('*vuela*')

class Mamifero(Animal):
    def amamantar(self):
        print('*lo amamanta*')

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.volar()
murcielago.amamantar()
murcielago.comer()
print(Murcielago.mro())














class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f'Mi nombre es {self.nombre} y tengo {self.edad} años.')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def grado_estudiante(self):
            print(f'Soy {self.nombre} del grado {self.grado}.')

daniel = Estudiante('Daniel', 16, 10)

# daniel.datos()
# daniel.grado_estudiante()