class Nada:
    pass
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Empleado:
    def __init__(self, identificacion, salario):
        self.id = identificacion
        self.salario = salario
    
    def miid(self):
        return f'mi numero de identificacion es {self.id}'

class Programador(Persona, Empleado):
    def __init__(self, nombre, apellido, edad, identificacion, salario, puesto, empresa):
        super().__init__(nombre, apellido, edad)
        Empleado.__init__(self, identificacion, salario)
        self.puesto = puesto
        self.empresa = empresa
    
    def presentarse(self):
        return f'Mi nombre es {self.nombre} y ' + super().miid()

camila = Programador('Camila','Garces', 25, 1050243542927, 1200, 'Desarrolladora backend', 'IBM')

print(camila.presentarse())
print()
print(issubclass(Programador, Persona))
print()
print(isinstance(camila, Empleado))
