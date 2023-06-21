# abriendo el archivo con with open
with open('archivo\\abogadojaja.txt', encoding="utf-8") as archivo:
    #leemos el archivo 
    contenido = archivo.read()
    
    #mostramos contenido del archivo
    print(contenido)
    
# no es necesario cerralo al usarlo con with open