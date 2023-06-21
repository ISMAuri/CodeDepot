# lista con nombres y otra apellidos
nombres = ['Ismael','Dalto','Matias','Camila','Elmo']
apellidos = ['Castillo','Lucas','Dororo','Lucas','Reno']

# ingresar esta info en un .txt de forma optima
with open('resolviendo_problemas\\nombres_y_apellidos.txt','w') as info:
    info.writelines('Los datos son:\n\n')
    [info.writelines(f'Nombre: {n}\nApellido: {a}\n----------\n') for n,a in zip(nombres,apellidos)]
    
v = 'hola'
