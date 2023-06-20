import pandas as pd

df = pd.read_excel('../data/empresas_de_deputados_em _autos_do_Ibama.xlsx')
df = df.drop(columns=['nome', 'cpf_mascarado', 'cnpj_basico_x', 'cnpj_cpf_socio', 'nome_fantasia',
                      "TIPO_MULTA",'PATRIMONIO_APURACAO','cnae_fiscal_secundaria', 'descricao_editada',
                      'DAT_HORA_AUTO_INFRACAO','FORMA_ENTREGA','DAT_CIENCIA_AUTUACAO' , 'GRAVIDADE_INFRACAO',
                      'descricao_editada', 'INFRACAO_AREA', 'DES_OUTROS_TIPO_AREA', 'DES_OUTROS_TIPO_AREA',
                      'CLASSIFICACAO_AREA', 'NUM_LATITUDE_AUTO', 'NUM_LONGITUDE_AUTO', 'NOTIFICACAO_VINCULADA',
                      'ACAO_FISCALIZATORIA', 'TIPO_ACAO','OPERACAO', 'DENUNCIA_SISLIV', 'ORDEM_FISCALIZACAO', 'SOLICITACAO_RECURSO',
                      'OPERACAO_SOL_RECURSO', 'DAT_LANCAMENTO', 'DAT_ULT_ALTERACAO', 'ULTIMA_ATUALIZACAO_RELATORIO'])


df.to_csv('../result_data/empresas_deputados/empresas_de_deputados_em _autos_do_Ibama.csv')
