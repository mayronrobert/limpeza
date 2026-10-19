import pandas as pd

df = pd.read_csv('dados.csv')

for indice in df.index:
    if df.loc[indice, 'Idade'] > 100:
        df = df.drop(indice)

print(df[['Duração', 'Idade']].head())
