import pandas as pd

# usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv('archivo\\datos.csv') #, names = ['name','lastname','age'
df2 = pd.read_csv('archivo\\datos.csv') 

# obteniendo datos de la columna nombre
#nombres = print(df["nombre"])

# slicing
# cadena = '0123456789'
# print(cadena[3:])

# ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values('edad')

# ordenando de forma descendente
df_orden_descendente = df.sort_values('edad', ascending=False)

# concatenando los 2 dataframes
df_concatenado= pd.concat([df,df2])

# accediendo a las primeras dos filas con head()
primeras_filas = df.head(2)

# accediendo a las ultimas 2 filas con tail()
ultimas_filas = df.tail(2)

# accediendo a la cantidad de filas y columnas con shape
# filas_y_columnas_totales = df.shape # (x, y) x = filas __ , y = columnas |
# filas_totales = filas_y_columnas_totales[0]
# columnas_totales = filas_y_columnas_totales[1]

# oooo mejor aun
filas_totales,columnas_totales = df.shape

# obteniendo data estdistica del data frame:
df_info = df.describe()

# accediendo a un elemento especifico del df con indexloc
elemento_especifico_iloc = df.iloc[2, 1]

# accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2, 'apellido']

# accediendo a todas las filas de una columna con iloc
edades = df.iloc[:,2]

# accediendo a todas las columnas de una fila con loc (funciona con iloc tambien)
fila_2_enrealidad_3 = df.iloc[2,:]

# accediendo a filas mayores de 30 anos (si, anos porque me da pereza el Alt + Shift)
mayor_que_30 = df.loc[df['edad']>30,:] 

print(mayor_que_30)
