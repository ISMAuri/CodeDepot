# Encapsulamiento: ocultar los detalles internos de un objeto y permitir el 
# acceso controlado a sus atributos y métodos desde el exterior.

# Encapsulamiento publico
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.edad = edad      # Atributo público

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

# persona = Persona("Juan", 30)
# print(persona.nombre)  # Acceso a un atributo público
# persona.saludar()      # Llamada a un método público

# Encapsulamiento protegido
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca    # _Atributo protegido
        self._modelo = modelo  # _Atributo protegido

    def _mostrar_informacion(self):  # _metodo protegido
        print(f"Marca: {self._marca}, Modelo: {self._modelo}")

# vehiculo = Vehiculo("Toyota", "Corolla")
# print(vehiculo._marca)  # Acceso a un atributo protegido
# vehiculo._mostrar_informacion()  # Llamada a un método protegido

# Encapsulamiento Privado
class Banco:
    def __init__(self):
        self.__saldo = 1000  # __Atributo privado

    def __mostrar_saldo(self): # metodo privado
        print(f"Saldo: {self.__saldo}")

banco = Banco()
# Acceder a un atributo privado (mediante name mangling)
print(banco._Banco__saldo)  # Acceso a un atributo privado (no recomendado)
banco._Banco__mostrar_saldo() # Acceso a metodo privado

