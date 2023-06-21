# creando una funcion que cree una serie fibonacci entre el 0 y el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = []
    for i in range(num):
        if b <= num:
            fibonacci_lista.append(b)
            a,b = b,a+b  
    return fibonacci_lista
                    
resultado = fibonacci(34)
print(resultado)