"""
Abstraccion se refiere a la simplificación y representación de objetos 
del mundo real en un modelo de programación más abstracto y manejable.
Es el proceso de enfocarse en los aspectos esenciales y relevantes de un
objeto, mientras se ocultan los detalles complejos que no son necesarios 
para un propósito particular.
"""
class Automovil():
    def __init__(self):
        self.estado = True
    
    def encender(self):
        self.estado = True
        if self.estado == False: 
            print('Encendiste el auto')

    def conducir(self):
        if self.estado == False:
            self.encender() 
        print('Estas conduciendo el auto')

mi_auto = Automovil()

mi_auto.conducir()