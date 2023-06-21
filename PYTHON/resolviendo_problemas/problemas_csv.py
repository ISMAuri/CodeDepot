# cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv('resolviendo_problemas\\datos.csv')

# convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#print(type(df['edad']))

# reemplazar valor
df['apellido'].replace('dalto', 'maestro', inplace=True)

#eliminando filas con datos faltantes
df = df.dropna()


# eliminando filas repetidas
df = df.drop_duplicates()
print(df)

#creando un csv con el dataframe resultante
df.to_csv('resolviendo_problemas\\datos_corregidos.csv')