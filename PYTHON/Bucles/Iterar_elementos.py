#
lista_animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [10,453,52,64]

#recorriendo la lista animales
for animal in lista_animales: 
    print("ahora la variable animal es igual a", animal)
 
for numero in numeros:
    print(numero * 10)

for animal,numero in zip(lista_animales,numeros):
    print("al siguiente animal:", animal,",", "le corresponde el numero.", numero)

# # si le pasas un parametro recorre de 0 a {parametro}, 
for num in range(len(numeros)): #<== forma no optima de recorrer una lista con su indice
    print(numeros[num])  #  NO FUNCIONA EN CONJUNTOS
    
# forma correcta
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(num) 

# for/else
for numero in numeros:
    print(numero)     
else:
    print('el bucle termino')
    
# FUNCIONA EXACTAMENTE IGUAL CON LISTAS QUE CON TUPLAS y conjuntos