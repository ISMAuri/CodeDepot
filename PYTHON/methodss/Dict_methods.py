diccionario = { 
"nombre" : "Ismael",
'edad' : 16,
'altura': '122'
}
diccionario2 = { 
"nombre" : "Eduardo",
'edad' : 17,
'altura': '143'
}

# devuelve las claves (tambien nos sirve para iterar las claves)
claves = diccionario.keys()

# devuelve el valor de la clave(si no se encuentra con [] devuelve KeyError y con get() devuelve el valor None)
valor = diccionario["nombre"]
valor = diccionario.get("nombre")

# eliminar todo el diccionario
diccionario2.clear() 

#eliminar uno o mas elementos del diccionario y se puede guardar el valor en una variable
guardar_elemento_removido = diccionario.pop("altura")

# obtener un elemento dict_items iterable
diccionario_iterable = diccionario.items()


print(diccionario_iterable)