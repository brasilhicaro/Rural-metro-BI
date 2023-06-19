import pandas as pd

df = pd.read_excel('../data/doacoes_indiretas_vindas_pessoas_com_embargos_ibama_2018.xlsx')
df = df.drop(columns=['origem_do_dinheiro_no_tse', 'data', 'nome'])

df["valor"] = df['valor'].str.replace(",", ".")
df["valor"] = df["valor"].astype(float)

df.rename(
    columns=({'cpf_cnpj_doador': 'doador_cpf_cnpj', 'cpf_deputado': 'deputado_cpf', 'doador' : 'nome_doador'
              }),
    inplace=True,
)

df = df.groupby(['deputado_cpf', 'doador_cpf_cnpj', 'nome_doador', 'doacoes_tipo', 'nome_urna'])['valor'].sum().reset_index()

df.to_csv('../result_data/doacoes_indiretas/doacoes_indiretas_vindas_pessoas_com_embargos_ibama_2018.csv')
