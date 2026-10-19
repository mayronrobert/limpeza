import pandas as pd


df = pd.read_csv('dados.csv')

df['Data_Limpa'] = pd.to_datetime(df['Data'], format='mixed', errors='coerce')

df_limpo = df.dropna(subset=['Data_Limpa'])

print(df_limpo)
