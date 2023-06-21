# Creando funcion que suma numeros
def sumar_dos(): # o tambien
    while True:
     a = input('Numero 1: ')
     b = input('Numero 2: ')
     try:
      resultado = int(a) + int(b)
     except Exception as e: # podemos especificar el error, en este caso seria ValueError (creo creo creo en miii, uuuuuu(ajaj(no denuevo)))
        print('No introduzcas caracteres que no sean numeros enteros porfavor.')
        print(f'ERROR: {type(e).__name__}') # {e} da una 'explicacion de a que se debe el error'
        #return sumar_dos() # 'esto no iria'
     else:
      break
     finally: # 'finally:' se ejecuta siempre
        print('Manejo de excepcion finalizado.')
    
    return resultado
   
    
    
print(sumar_dos())