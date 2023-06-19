import pandas as pd

df = pd.read_excel('../data/doacoes_indiretas_vindas_pessoas_com_autos_de_infracao_ibama_2018.xlsx')
df = df.drop(columns=['origem_do_dinheiro_no_tse', 'data', 'nome_deputado'])

df["valor"] = df['valor'].str.replace(",", ".")
df["valor"] = df["valor"].astype(float)

df.rename(
    columns=({'cpf_doador': 'doador_cpf_cnpj', 'cpf_deputado': 'deputado_cpf'
              }),
    inplace=True,
)

df = df.groupby(['deputado_cpf', 'doador_cpf_cnpj', 'nome_doador', 'doacoes_tipo', 'nome_urna'])['valor'].sum().reset_index()

df.to_csv('../result_data/doacoes_indiretas/doacoes_diretas_vindas_pessoas_com_autos_de_mte_2018.csv')
