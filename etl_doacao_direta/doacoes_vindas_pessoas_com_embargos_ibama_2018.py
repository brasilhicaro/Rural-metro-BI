import pandas as pd

df = pd.read_excel('../data/doacoes_vindas_pessoas_com_embargos_ibama_2018.xlsx')
df = df.drop(columns=['origem_do_dinheiro_no_tse', 'data', 'nome'])
df["valor"] = df['valor'].str.replace(",", ".")
df["valor"] = df["valor"].astype(float)

df = df.groupby(['cpf_deputado', 'doador_cpf', 'doador_nome', 'doacoes_tipo', 'nome_urna'])['valor'].sum().reset_index()

df.to_csv('../result_data/doacoes_vindas_pessoas_com_embargos_ibama_2018.csv')
