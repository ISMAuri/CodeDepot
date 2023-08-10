# Los "getters" y "setters" son métodos públicos utilizados para acceder y 
# modificar atributos privados de una clase de manera controlada. 

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_name(self, n):
        self.__name = n

    def set_age(self, n):
        self.__age = n

persona = Person('Gabriel', 23)

print(persona.get_name())
print(persona.get_age())

persona.set_name('Pepe')
persona.set_age(22)

print(persona.get_name())
print(persona.get_age())