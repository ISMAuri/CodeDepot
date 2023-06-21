import re

texto = '''Hola maestro. esta es la cadena 1. como va eso pa? definitiva
Esta es la linea 12332214323 de texto.  abbbb   abb abababababababab
Y esta es la final (linea 3) definitiva'''

# Haciendo una busqueda simple     re.search una sola          re.flags=IGNORECASE
# resultado = re.findall('esta',texto)

#\d  --  busca digitos numeros del 0 al 9
# resultado = re.findall(r'\d', texto)

#\D  --  busca TODO MENOS digitos numeros del 0 al 9
# resultado = re.findall(r'\D', texto)

#\w  --  busca caracteres alfanumericos [ a-z, A-Z, 0-9, _ ]
# resultado = re.findall(r'\w', texto)

#\W  --  busca TODO MENOS caracteres alfanumericos [ a-z, A-Z, 0-9, _ ]
# resultado = re.findall(r'\W', texto)

#\s  --  busca espacios en blanco --> espacios, tabs, newlines
# resultado = re.findall(r'\s', texto)

#\S  --  busca TODO MENOS espacios en blanco --> espacios, tabs, newlines
#resultado = re.findall(r'\S', texto)

#\n -> busca saltos en linea
#resultado = re.findall(r'\n',texto)

#. -> busca TODO MENOS saltos en linea
#resultado = re.findall(r'.',texto) 

#\ -> cancelar caracteres especiales, cancelando la funcion del punto, y buscando puntos
#resultado = re.findall(r'\.',texto)

# armando una cadena que busque un numero, al que le siga un punto y un espacio
#resultado = re.findall(r'\d\.\s', texto) 

#^ -> busca el comienzo del texto ( buscando Hola al principio del texto)
# re.M para multilinea
#resultado = re.findall(r'^Hola', texto, flags=re.M)   

#$ -> busca final de una texto (definitiva al final del texto)
# # re.M para multilinea
#resultado = re.findall(r'definitiva$', texto, flags=re.M)   

#{n} -> busca n cantidad de veces el valor de la izquierda (tres numeros juntos esta vez)
#resultado = re.findall(r'\d{3}\s', texto)

#{n,} -> almenos n, como maximo m
# resultado = re.findall(r'\d{2,4}', texto)

#devuelve ab segun la cantidad de veces que encuentre lo especificado, con [] se aplica a cada uno ( devuelve aa, ab, ba, bb)
resultado = re.findall(r'(ab){2,3}', texto)

#| -> busca una cosa o/y la otra
resultado = re.findall(r'\d{2,4}|Hola', texto)


print(resultado)