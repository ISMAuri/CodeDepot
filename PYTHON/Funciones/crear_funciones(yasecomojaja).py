# creando una funcion simple
# def saludar():
#     print('Hola Ismael')

# #ejecutando    
# saludar()

#creando una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'amiga'
    elif (sexo == 'hombre'):
        adjetivo = 'amigo'
    else:
        adjetivo = 'compañere'
        
        
    print(f"Hola {nombre}, como estas {adjetivo}?")
    
saludar('Ismael', 'hombre')

#crear una funcion que nos retorne valores

def crear_contasena_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num  = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena,num

# desempaquetando
passw,num_utilizado = crear_contasena_random(21)

print(f'tu nueva contrasena es {passw} y el numero utilizado fue {num_utilizado}')

