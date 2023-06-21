# forma no optima
# def suma(lista):
    # numero_sumados = 0
    # for numero in lista:
    #     numero_sumados = numero_sumados + numero
    # return numero_sumados
#print(suma([12,34,34,2,2]))

# forma optima
def suma_total(numeros):
    return sum([*numeros])

resultado1 = suma_total([23,423,24,21,4,2,3])
    
#utilizando el como parametro a args(*args)
def suma(nombre, *numeros):
    return f'Hola {nombre}, la suma de tus numeros es "{sum(numeros)}"'
    
resultado = suma('Ismael', 23,423,24,21,4,2,3)
print(resultado1)