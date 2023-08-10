# Polimorfismo en este caso, es la capacidad de objetos de responder a un mismo metodo de manera especifica
"""
En Python que es un lenguaje de programacion dinamico
se aplica la filosofia de Duck Typing, si se escucha,
camina, y nada como un pato, probablemente lo sea.
A lo que se quiere referir es que el tipo de un 
objeto de determina no por su estructura si no por
su comportamiento.
Por eso en otros lenguajes de tipado estatico primero
se tendria que crear una clase y que subclases hereden
sus propiedades primero, ya que esta juzgandolos por
su estructura, a diferencia de Python y otros lenguajes
de tipado dinamico que no es necesario que hereden dicha
clase. EJEMPLO: ↓↓↓
"""
"""
si fuese estatico

class Animal:
    def sonido():
        pass
    y despues que Pato y Perro heredasen animal

A este se le llama polimorfismo de herencia
"""



class Pato:
    def sonido(self):
        return 'Cuac cuac'

class Perro:
    def sonido(self):
        return 'Guau guau'

def hacer_sonido(animal):
    print(animal().sonido())

# Polimorfismo ad hoc('para esto'/ 'para esta situacion'/ 'con este proposito')
hacer_sonido(Pato)

# print(Pato.sonido())
# print(Perro.sonido())
