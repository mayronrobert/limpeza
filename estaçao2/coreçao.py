import pandas as pd

df = pd.read_csv('dados.csv')

df.loc[0, 'Idade'] = 30

print(df[['Duração', 'Idade']].head())
