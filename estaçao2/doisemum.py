import pandas as pd

df = pd.read_csv('dados.csv')

df['Data_Limpa'] = pd.to_datetime(df['Data'], format='mixed', errors='coerce')
df = df.dropna(subset=['Data_Limpa'])

for indice in df.index:
    if df.loc[indice, 'Idade'] > 100:
        df = df.drop(indice)

print(df[['Data_Limpa', 'Idade', 'Calorias']].head())
