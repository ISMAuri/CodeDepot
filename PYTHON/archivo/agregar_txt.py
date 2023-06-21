# con 'a' (osea append) agregamos texto sin sobreescribir
with open('archivo\\abogadojaja.txt','a',encoding = 'Utf-8') as archivo:
    # sobreescribiendo el archivo
    #archivo.write('Jjsfjsdjjdja te la recontra teclee')
    
    
    # agregando dos lineas con write lines
    archivo.writelines(['- Hola maestro como andas\n','- Shut up and dance\n'])
    
    # agregando otras dos lineas con write lines 
    archivo.writelines(['- El que vio el video de programacion en Python de Dalto fijo entiende esta secuen\n','- Seguro que si ajasjas\n'])
    
    # usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f'Linea {i+1} agregado.\n')