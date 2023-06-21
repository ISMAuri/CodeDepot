# no se que voy a hacer pero y bueno no tengo internet, asi es la vida
import random


saldoact = random.randint(1,100)

def saldoo():
    print("tu saldo es de: ", saldoact)
    if saldoact >= 50:
        print("Estas en esa.")
    else:
        print("Dale, carga mas saldo, cicatero.")

def recarga():
    print('1. Recarga 25 lps.')  
    print("2. Recarga 50 lps.")
    print("3. Recarga 100 lps")
    # no quise seguir jaja xd xd y eso que no tengo internet jaja lo peor que estoy comentando esto cuando ya tengo internet pero y bueno la mano arriba cintura sola la media vuelta danza kuduro 
    
def lussac():
    print('Que onda los pibes.')
    print('1. consultar saldo.') 
    print("2. comprar recarga.")
    response = input("Ingrese un numero: ")
    if response == "1":
        saldoo()
    elif response == "2":
        recarga()
    else:
        print("Ingrese un numero valido porfavor.")
        return lussac()


lussac()