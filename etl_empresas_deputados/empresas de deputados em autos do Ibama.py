import pandas as pd

df = pd.read_excel('../data/empresas de deputados em autos do Ibama.xlsx')
df = df.drop(columns=['cpf_mascarado', 'nome', 'cnpj_basico_x', 'TIPO_MULTA', 'PATRIMONIO_APURACAO',
                      'GRAVIDADE_INFRACAO', 'VAL_AUTO_INFRACAO', 'DAT_HORA_AUTO_INFRACAO', 'DAT_CIENCIA_AUTUACAO',
                      'INFRACAO_AREA', 'DES_OUTROS_TIPO_AREA', 'CLASSIFICACAO_AREA', 'NUM_LATITUDE_AUTO',
                      'NUM_LONGITUDE_AUTO', 'DES_LOCAL_INFRACAO', 'NOTIFICACAO_VINCULADA', 'ACAO_FISCALIZATORIA', 'TIPO_ACAO',
                      'OPERACAO', 'DENUNCIA_SISLIV', 'ORDEM_FISCALIZACAO', 'SOLICITACAO_RECURSO', 'OPERACAO_SOL_RECURSO',
                      'DAT_LANCAMENTO', 'DAT_ULT_ALTERACAO', 'ULTIMA_ATUALIZACAO_RELATORIO'], axis=1)

df["VAL_AUTO_INFRACAO"] = df['VAL_AUTO_INFRACAO'].str.replace(",", ".")
df["VAL_AUTO_INFRACAO"] = df["VAL_AUTO_INFRACAO"].astype(float)

df.rename(
    columns=({'cpf_doador': 'doador_cpf_cnpj', 'cpf_deputado': 'deputado_cpf'
              }),
    inplace=True,
)

df = df.groupby(['nome_infrator_semacentos', 'nome_urna'])['VAL_AUTO_INFRACAO'].sum().reset_index()

df.to_csv('../result_data/empresas_deputados/empresas de deputados em autos do Ibama.csv')
