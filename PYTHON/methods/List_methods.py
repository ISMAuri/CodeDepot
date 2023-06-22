# creamos una lista con list()
lista = list(['hola', 'dalto', 34, 2])
lista2 = list(['hola', 'dalto', 34, 2, True])
lista_numeros = [1, 42 , True, 22, 67, 0, False, 3]

# devuelve cantidad de elementos en una lista
cantidad_de_elementos = len(lista)

# agregando elementos a la lista
lista.append("JDSAFJSJD")

# agregando elemento a la lista en indice especifico
lista.insert(0, "lol")

# agregando varios elementos a la lista
lista.extend([True, 124])

# eliminando un elemento de la lista por su indice

lista.pop(-1) # -1 elimina el ultimo & so on

# elimina un elemento de la lista por su valor
lista.remove("dalto")

# elimina todos los elementos de la lista
lista2.clear()

# ordena elementos de forma ascendente
lista_numeros.sort(reverse=True)#con reverse=True ordenamos de forma descendente

#invirtiendo elementos de una lista

lista.reverse()

# verificando en que indice se un elemento encuentra en la lista
elemento_encontrado = lista.index(True)





print(elemento_encontrado)