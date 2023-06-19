import pandas as pd
file1 = './result_data/doacoes_diretas/doacoes_diretas_vindas_pessoas_com_autos_de_mte_2018.csv'
file2 = './result_data/doacoes_diretas/doacoes_vindas_pessoas_com_autos_icmbio_2018.csv'
file3 = './result_data/doacoes_diretas/doacoes_vindas_pessoas_com_embargos_ibama_2018.csv'
file4 = './result_data/doacoes_diretas/resultados_doacao_direta_infracao_ibama_2018.csv'
df = pd.concat(map(pd.read_csv, [file1, file2, file3, file4]), ignore_index=True)
df.reset_index(drop=True, inplace=True)
df.to_csv('./result_data/etlFinalDireta/etl_final_direta.csv')
