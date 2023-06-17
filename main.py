import pandas as pd

df = pd.read_excel(r'./data/cadastro_de_empregadores.xlsx', sheet_name='cadastro_de_empregadores')
df.to_csv(r'./data/cadastro_de_empregadores.xlsx', index=None, header=True)

print(df.head())
