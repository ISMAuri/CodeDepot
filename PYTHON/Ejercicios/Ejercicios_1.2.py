frase = input('Escribi una frase y te calculo cuanto tardarias si la tuvieras que decir tomando en cuenta que cada 1 segundo decis 2 palabras: ')
separar_palabras = frase.split(" ")
cantidad_palabras = len(separar_palabras)

if cantidad_palabras/2 > 60:
    print("Pero... amigo, te pedi una frase, no un testamento. Podria darte los resultados pero no quiero jssjjsjsjs.")
else:
    print(f"Dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras/2} de segundos en decirlo. ")
    print(f"dalto tardaria {round((cantidad_palabras/2) / 1.3, 1) } segundos en decirlo. ")

