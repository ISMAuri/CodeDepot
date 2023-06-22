cadena1 = "HOLApa"
cadena2= "pa"
cadena3= "Hola,Maquina,Como,Estas"

# dir() devuelve la lista de atributos validos y es una funcion, no un metodo    __fsfds__
# metodo = algo.metodo()
# funcion = funcion(algo,algunos o '')

mayus = cadena2.upper() #TODOO EN MAYUS

minus = cadena1.lower() #todo en minus

cap = cadena1.capitalize() #Primera letra mayuscula y si esta todo mayus lo pasa todo lo demas minus: ejem. Hola


# buscamos una cadena en otra cadena, si no hay coincidencias -1
busqueda_find = cadena1.find("HOLA" or "u")

# buscamos una cadena en otra cadena, si no hay coincidencias ValueError
busqueda_index = cadena1.index("H")


#si es numero devuelve true
numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true
alfanumerico = cadena1.isalpha()

#duevuelve el numero de coincidencias
coincidencias_count = cadena1.count(' ')

#contamos los caracteres de una cadena
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi nos devuelve True
empieza_con = cadena1.startswith("HOLA")

# verificamos si una cadena termina con otra cadena dada, si es asi nos devuelve True
termina_con = cadena1.endswith("apu")

# reemplaza un pedazo de la cadena dada por otra dada
reemplazar_cadena = cadena3.replace(","," ")
cap_cadena = reemplazar_cadena.capitalize()

# separar cadenas con la cadena que le demos
cadena_separada = cadena3.split(",")



print(cadena_separada[1])