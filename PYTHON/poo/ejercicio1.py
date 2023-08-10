class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f'El estudiante {self.nombre} del grado {self.grado} esta estudiando.')
        
nombre = input('Digame su nombre: ')
edad = input('Digame su edad: ')
grado = input('Digame su grado: ')

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado {estudiante.grado} \n      
      """)

estudiar = input("Quieres estudiar? ")
if (estudiar.lower() == 'si' or estudiar.lower() == 'claro'):
    estudiante.estudiar()
