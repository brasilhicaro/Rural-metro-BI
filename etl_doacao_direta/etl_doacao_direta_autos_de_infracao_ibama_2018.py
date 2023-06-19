import pandas as pd

df = pd.read_excel('../data/doacoes_diretas_vindas_pessoas_com_autos_de_infracao_ibama_2018.xlsx')
df = df.drop(columns=['entidade_id_mascarada', 'origem_do_dinheiro_no_tse', 'data', 'nome_deputado'])
df["valor"] = df['valor'].str.replace(",", ".")

df["valor"] = df["valor"].astype(float)

df = df.groupby(['cpf_deputado', 'cpf_doador', 'nome_doador','doacoes_tipo', 'nome_urna'])['valor'].sum().reset_index()

df.rename(
    columns=({'cpf_doador': 'doador_cpf_cnpj', 'cpf_deputado': 'deputado_cpf'
              }),
    inplace=True,
)

df.to_csv('../result_data/doacoes_diretas/resultados_doacao_direta_infracao_ibama_2018.csv')

