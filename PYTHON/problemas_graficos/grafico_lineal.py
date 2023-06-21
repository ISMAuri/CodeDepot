import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('problemas_graficos\\pedos.csv')

# creando el grafico
sns.lineplot(x='fecha',y='pedos',data=df)

# el punto de mas pedos (casi diarrea explosiva)
plt.plot('01-09',17,'o')

# mostrando el grafico
plt.show()