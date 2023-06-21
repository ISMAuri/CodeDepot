dict = {
     'nombre': 'ismael',
     'apellido': 'Castro',
     'anos': 16
     }

# recorriendo dict con items para obtener el valor
for datos in dict.items():
   key = datos[0]
   value = datos[1]
   print('la clave es', key, 'y el valor es:', value)