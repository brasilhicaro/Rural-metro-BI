import pandas as pd

df = pd.read_excel('../data/doacoes_vindas_pessoas_com_embargos_ibama_2018.xlsx')
df = df.drop(columns=['origem_do_dinheiro_no_tse', 'data', 'nome'])
df["valor"] = df['valor'].str.replace(",", ".")
df["valor"] = df["valor"].astype(float)

df = df.groupby(['cpf_deputado', 'doador_cpf', 'doador_nome', 'doacoes_tipo', 'nome_urna'])['valor'].sum().reset_index()
df.rename(
    columns=({'doador_cpf': 'doador_cpf_cnpj', 'doador_nome': 'nome_doador', 'cpf_deputado': 'deputado_cpf'
              }),
    inplace=True,
)
df.to_csv('../result_data/doacoes_diretas/doacoes_vindas_pessoas_com_embargos_ibama_2018.csv')
