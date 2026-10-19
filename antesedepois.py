import pandas as pd

df = pd.read_csv('dados.csv')

print("--- Tipos de dados ANTES da conversão ---")
print(df.dtypes)

df['Data_Limpa'] = pd.to_datetime(df['Data'], format='mixed', errors='coerce')

print("\n--- Tipos de dados DEPOIS da conversão ---")
print(df.dtypes)
