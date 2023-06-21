# encontrando el numero mayor de una lista, tupla o conjunto
numeros = [1,23,4,3,43,53,2,1,53,53,543,5,34,5,30]

numeros_mas_alto = max(numeros)
print(numeros_mas_alto)

# encontrando el numero menor de una lista, tupla o conjunto
numeros_mas_bajo = min(numeros)
print(numeros_mas_bajo)

#redondeando a 6 decimales
numero_float = 3.424234234213
print(round(numero_float, 6))

# retorna False -> 0,vacio, Flase, None / True -> !0, True, cadena, datos no vacios
resultado_booleano = bool(12)
print(resultado_booleano)

# retorna True si todos los valores son verdades de lo contario False
resultado_all = all([16,'true',[12,243],True])
print(resultado_all)

# suma todos los valores de un iterable

suma_total = sum(numeros)
print(suma_total)