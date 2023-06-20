import pandas as pd

df = pd.read_excel('../data/empresas de deputados em autos trabalhistas.xlsx')
df = df.drop(columns=['descricao_editada', 'data'])

df.to_csv('../result_data/empresas_deputados/empresas de deputados em autos trabalhistas.csv')
