# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv("/content/dataanalysis-ebac/gasolina.csv")

sns.lineplot(x=gasolina_df.columns[0],
             y=gasolina_df.columns[1],
             data=gasolina_df.head()).set(title="Gasolina: Preço(R$) x Dia")

plt.savefig("gasolina.png")