# Creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'Cometiste el siguiente error: {err}') 
        
# Lanzar excepcion a proposito
# raise ZeroDivisionError('Que boludo que sos, maestro, como vas a dividir por zerooo pero anda dormii.')

#lanzando mi propia excepcion
# raise MiExcepcion('texto ejemplo que pereza')

# manejando mi propia excepcion
try:
    raise MiExcepcion('texto ejemplo que pereza')
except:
    print('maneje el error')    
