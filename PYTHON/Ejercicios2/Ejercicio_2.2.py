# creando una funcion que nos devuelva los numeros primos entre el 0 y el argumento que le pasamos

# crear una funcion que verifique si numero es primo
def es_primo(num):
    for i in range (2, num-1):
        if num%i == 0: return False 
    return True

# creando una funcion que retorne una lista con todos los primo
def primos_hasta(num):
    primos = []
    for i in range (3,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    # devolvemos la lista
    return primos
    
# imprimo la lista pero con el bucle for
todos_primos = primos_hasta(87)
for primos in todos_primos:
    print(primos)

