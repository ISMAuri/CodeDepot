# creando las listas
frutas = ['banana','manzana','pera','naranja', 'computadora']
cadena = "Hola Castro"
numeros = [2,5,8,10]
for fruta in frutas:
    if fruta == 'pera':
        continue # no imprime pera y se sigue ejecutando
    
    print(f"me voy a comer una {fruta}")
    

for fruta in frutas:
    if fruta == 'pera':
        break # no imprime pera y se deja de ejecutar
    
    print(f"me voy a comer una {fruta}")
#else:       con else se dejaria de ejecutar    
print('bucle terminado')

for letra in cadena:
    print(letra)
    

# for en una sola linea de codigo (duplicamos los numeros)
numeros_dup = [x*2 for x in numeros]
print(numeros_dup)



# en muchas lineas
# numeros_dup = list()

# for numero in numeros:
#     numeros_dup.append(numero*2)
    
# print(numeros_dup)


    