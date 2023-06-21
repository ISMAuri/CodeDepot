import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('problemas_graficos\\cofla.csv')

# creando el grafico
sns.barplot(x='Fuente',y='Ingresos',data=df)

# sumando el total de los ingresos que obtiene el cofla( un capo )
total_ingresos = df['Ingresos'].sum()

# mostrando el total de ingresos que obtiene cofla ( un capo )
print(f' el total de ingresos de el cofla es de {total_ingresos} dolares (todo un capo).')

# mostrando el grafico ( de los ingresos de el coflas ( un capo (muy capo) ))
plt.show()

