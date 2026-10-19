import pandas as pd

df = pd.read_csv('dados.csv')

for indice in df.index:
    if df.loc[indice, 'Idade'] > 100:
        df.loc[indice, 'Idade'] = 100

print(df[['Duração', 'Idade']].head())
