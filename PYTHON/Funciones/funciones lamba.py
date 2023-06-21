numeros = [1,2,3,4,5,6,7,8,9]

# funcion lamba
multiplicar_por_dos = lambda x : x*2
# es lo mismo/equivalente a
# def multiplicar_por_dos(x):
#     return x*2

#creando funcion comun que diga si es par o no
# def es_par(num):
#     if (num%2==0):
#         return True
# usando filter con una funcion comun
#numeros_pares = filter(es_par,numeros)

#lo mismo que antes pero con lambda
numeros_pares = filter(lambda num: num%2 == 0,numeros)

print(list(numeros_pares))

