import pandas as pd

df = pd.read_csv('dados.csv')

df['Data_Limpa'] = pd.to_datetime(df['Data'], format='mixed', errors='coerce')

quantidade_nat = df['Data_Limpa'].isna().sum()

print(df)
print(f"\nQuantidade de NaT encontrados: {quantidade_nat}")
