# Los metodos Dunder permiten que las clases definan comportamientos especiales para ciertas operaciones o funcionalidades estándar del lenguaje.
# Double underscore

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'(nombre = {self.nombre}, edad = {self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro):
        return Persona(self.nombre + otro.nombre, self.edad + otro.edad)

davi = Persona('David', 18)
isma = Persona('Ismael', 16)
print(isma + davi)
# repre = repr(isma)
# res = eval(repre)
# print(repre)
# print(res)

