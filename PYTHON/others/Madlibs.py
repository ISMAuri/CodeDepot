# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ______.

# organizacion = "FreeCodeCamp"

# print("Aprende a programar con " + organizacion)

# print("Aprende a programar con {}" .format(organizacion))

# print(f"Aprende a programar con {organizacion}") # f-string

# Mad Libs
 

adj = input("Enter an adjective")
verb1 = input("Enter a verb")
verb2 = input("Enter a verb(yes,another verb)")
pluralnoun = input("Enter a plura noun")
madlibs = f"Programming is so {adj}! It always excites me because i love {verb1} problems. Learn how to {verb2} with FreeCodeCamp and reach your {pluralnoun}."

print(madlibs)
