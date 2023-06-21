# diccionario = dict(nombre= "Isma,", edad= "16")

#las listas no pueden ser claves y usamos forzenset para meter conjuntos
diccionario = {frozenset(["Nombre", "Edad"]): "jajaj"}

# creando diccionarios con fromkeys()
diccionario = dict.fromkeys(['nombre','edad','every standup'], "Nose jaja")# valor por defecto sin colocar un segundo parametro va a ser None

print(diccionario)