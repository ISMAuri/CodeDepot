import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('problemas_graficos\\bigotes.csv')

# creando el grafico
sns.boxplot(x='categoria',y='valor',data=df)

plt.show()

