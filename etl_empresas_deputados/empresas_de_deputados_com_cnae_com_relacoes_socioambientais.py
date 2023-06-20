import pandas as pd

df = pd.read_excel('../data/empresas_de_deputados_em _autos_do_Ibama.xlsx')
df = df.drop(columns=['nome', 'cpf_mascarado', 'cnpj_basico_x', 'cnpj_cpf_socio', 'nome_fantasia',
                      'cnae_fiscal_secundaria', 'descricao_editada'])


df.to_csv('../result_data/empresas_deputados/empresas_de_deputados_em _autos_do_Ibama.csv')
