"""
Un decorador es una función que toma otra función como argumento y agrega alguna funcionalidad adicional a la función original sin modificar su código fuente. 
"""
def decorador(funcion):
    def funcion_modificada():
        print("Imprimir mensaje antes de ejecutar la funcion")
        funcion()
        print("Imprimir mensaje despues de ejecutar la funcion")
    return funcion_modificada

# def saludo():
#     print('que onda')

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print('holaa')
saludo()