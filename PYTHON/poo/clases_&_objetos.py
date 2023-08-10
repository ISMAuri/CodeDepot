class Celular:
    def __init__(self, marca, modelo, precio):
        # Atributos o propiedades
        self.marca = marca
        self.modelo = modelo
        self.precio = '$' + precio
        self.llamando = False
        self.nombre_llamada = ''
    
    # Metodo, funcion aplicada sobre un objeto
    def llamar(self, nombre):
        if not self.llamando:
            self.llamando = True
            self.nombre_llamada = nombre
            print(f'Estas llamando a {nombre} desde un {self.modelo}')
        
        else:
            print('Ya hay una llamada en curso')
    
    def cortar(self):
        if self.llamando:
            self.llamando = False
            print(f'Cortando la llamada con {self.nombre_llamada} desde un {self.modelo}')
        
        else:
            print('No hay llamadas en curso')
            
# Aqui nosotros debemos de nombrar los atributos a la hora de instanciar una clase
s23 = Celular('Samsung','S23','698')
i13 = Celular('Apple','iphone 13','699')

print(s23.precio)
print()
i13.cortar()
i13.llamar('Rebeca')
i13.llamar('Antonio')
i13.cortar()

# class Celular():
#     #Atributos estaticos
#     marca = 'Samsung'
#     modelo = 'S23 Ultra'
#     precio = '$859'

# # Una instancia creada a partir de la clase Celular
# s23_ultra = Celular()
# #Ahora s23_ultra es un objeto
# s23_ultra.precio = '$900'

# print(s23_ultra.precio)
