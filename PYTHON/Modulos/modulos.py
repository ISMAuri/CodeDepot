# from saludar import saludo as sal # si quisiera mas del mismo solo agrego coma (,) 
from saludar import * #(todo) mala practica porque hace que el programa se sobrecargue, sea muy pesado
saludo = saludo('Ismael')
print(saludo)

#para ver propiedades y metodos del namespace
# print(dir(namespace))

# accedemos al nombre de este modulo
# print(__main__)

# accedemos al nombre de otro modulo
# print(namespace.__main__) 