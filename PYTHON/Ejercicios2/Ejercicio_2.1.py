# falto el profe y los pibes van a armar a clase

# pedir el nombre y edad de los companeros que vinieron hoy a clase
def obtener_companeros(cantidad_compas):
    companeros = []
    for i in range(cantidad_compas):
       nombre = input('Ingrese el nombre del companero: ')
       edad = int(input('Ingrese la edad del companero: '))
       companero = (nombre,edad)
       companeros.append(companero)
    companeros.sort(key=lambda x:x[1])
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    return asistente, profesor
 
asistente, profesor = obtener_companeros(5)

print(f'El profesor es {profesor} y su asistente es {asistente}')
     
