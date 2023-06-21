# EJEMPLO SACADO DE CHATGPT BASTANTE SENCILLO

class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
    def ladrar(self):
        print("¡Guau! ¡Guau!")
    
    def comer(self, comida):
        print(f"{self.nombre} está comiendo {comida}.")

# Crear objetos de la clase Perro
perro1 = Perro("Fido", 3, "Labrador")
perro2 = Perro("Rex", 5, "Bulldog")

# Acceder a los atributos y llamar a los métodos de los objetos
print(perro1.nombre)  # Output: Fido
print(perro2.edad)    # Output: 5

perro1.ladrar()       # Output: ¡Guau! ¡Guau!
perro2.comer("carne") # Output: Rex está comiendo carne.
