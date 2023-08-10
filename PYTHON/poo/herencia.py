# Heredar atributos y metodos de una clase

# Superclass
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nac = nacionalidad
        
    def hablar(self):
        print('*habla*')
        
# Subclass
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


alfonso = Empleado('Alfonso', 22, 'alemán', 'Programador', 800)

print(alfonso.salario)

alfonso.hablar()