# Una clase abstracta es una clase que no puede ser instanciada 
# directamente, sino que se utiliza como base para otras clases. 
from abc import ABC, abstractclassmethod 


class Persona(ABC):
    def __init__(self, nombre, edad, actividad):
        self.nombre = nombre
        self.edad = edad
        self.actividad = actividad
        
    # con esto forzamos o nos aseguramos que las las subclases implementen este metodo
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola mi nombre es {self.nombre} y tengo {self.edad} años.')

class Estudiante(Persona):
    def __init__(self, nombre, edad, actividad):
        super().__init__(nombre, edad, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy estudiando {self.actividad}.')

class Trabajador(Persona):
    def __init__(self, nombre, edad, actividad):
        super().__init__(nombre, edad, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy trabajando en el rubro de {self.actividad}.')

# ismael = Persona('Ismael', 16, 'programacion') # no se puede crear un objeto a partir de una clase abstracta
ismael = Estudiante('Ismael', 16, 'programacion')
gilberto = Trabajador('Gilberto', 26, 'administracion')

print()
ismael.presentarse()
ismael.hacer_actividad()
print()
gilberto.presentarse()
gilberto.hacer_actividad()
print()