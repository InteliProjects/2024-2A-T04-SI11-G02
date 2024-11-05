# import pandas as pd
# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import RobustScaler

# def extrair_ano_mes(df: pd.DataFrame, coluna_data: str) -> pd.DataFrame:
#     # df[coluna_data] = pd.to_datetime(df[coluna_data], format="%Y-%m-%d", errors='coerce')
#     # df['ANOMES'] = df[coluna_data].dt.strftime('%m%Y')
#     return df

# def criar_clusters(df: pd.DataFrame) -> pd.DataFrame:
#     # df = df.dropna(subset=['COD_LATITUDE', 'COD_LONGITUDE'])
#     # unique_points = df[['COD_LATITUDE', 'COD_LONGITUDE']].drop_duplicates().shape[0]
#     # n_clusters = min(4, unique_points)  # Define n_clusters com base nos pontos únicos
    
#     # kmeans = KMeans(n_clusters=n_clusters, random_state=42)
#     # df['CLUSTER'] = kmeans.fit_predict(df[['COD_LATITUDE', 'COD_LONGITUDE']])
    
#     # # Criar colunas de quadrante de acordo com o cluster atribuído
#     # for i in range(4):
#     #     df[f'QUADRANT_{i+1}'] = (df['CLUSTER'] == i).astype(int)

#     return df

# def normalizar_consumo(df: pd.DataFrame) -> pd.DataFrame:
#     # scaler = RobustScaler()
#     # df['CONS_MEDIDO'] = scaler.fit_transform(df[['CONS_MEDIDO']])
#     return df

# def criar_colunas_consumo(df: pd.DataFrame) -> pd.DataFrame:
#     # # Ordenar por 'ANOMES' para garantir a ordem correta
#     # df = df.sort_values(['MATRICULA', 'ANOMES'])
    
#     # # Filtrar os registros para remover aqueles onde 'CONS_MEDIDO' é NaN
#     # df = df[df['CONS_MEDIDO'].notna()]

#     # # Selecionar os últimos 12 registros por matrícula, independente do ano e da ordem dos meses
#     # df['RANK'] = df.groupby('MATRICULA')['ANOMES'].rank(method='first', ascending=False)

#     # # Filtrar para manter apenas as matrículas que possuem registros suficientes
#     # df = df[df['RANK'] <= 12]
#     # df = df.groupby('MATRICULA').filter(lambda x: len(x) == 12)

#     # # Criar um identificador de ordem dos últimos 12 meses
#     # df['MES'] = df.groupby('MATRICULA').cumcount() + 1

#     # # Pivotar os dados para ter 12 colunas, uma para cada mês (MES_1, MES_2, ..., MES_12)
#     # df_pivot = df.pivot_table(index='MATRICULA', columns='MES', values='CONS_MEDIDO')

#     # # Renomear as colunas para MES_1, MES_2, ..., MES_12
#     # df_pivot.columns = [f'MES_{int(col)}' for col in df_pivot.columns]

#     # # Garantir que sempre existam 12 colunas de meses, mesmo que não haja todos os meses
#     # for i in range(1, 13):
#     #     if f'MES_{i}' not in df_pivot.columns:
#     #         df_pivot[f'MES_{i}'] = 0

#     # # Reordenar as colunas MES_1 a MES_12
#     # df_pivot = df_pivot[[f'MES_{i}' for i in range(1, 13)]]
    
#     # # Resolver problema de NaN: Substituir valores ausentes por 0
#     # df_pivot = df_pivot.fillna(0)
    
#     return df

# def pre_processar_dados(df: pd.DataFrame) -> pd.DataFrame:
#     # Extrair ano e mês
#     df = extrair_ano_mes(df, 'DAT_LEITURA')
    
#     # Criar clusters
#     df = criar_clusters(df)
    
#     # Normalizar o consumo
#     df = normalizar_consumo(df)
    
#     # Criar as colunas de consumo
#     df_consumo = criar_colunas_consumo(df)
#     # Merge com os dados pivotados
#     df_final = df_consumo.merge(df_consumo, on='MATRICULA', how='inner')
    
#     # Criar colunas de categoria
#     df_final['CATEGORIA_RESIDENCIAL'] = (df_final['CATEGORIA'] == 'RESIDENCIAL').astype(float)
#     df_final['CATEGORIA_COMERCIAL'] = (df_final['CATEGORIA'] == 'COMERCIAL').astype(float)
#     df_final['CATEGORIA_PUBLICA'] = (df_final['CATEGORIA'] == 'PUBLICA').astype(float)
#     df_final['CATEGORIA_INDUSTRIAL'] = (df_final['CATEGORIA'] == 'INDUSTRIAL').astype(float)
    
#     # Garantir que df_final tenha exatamente as colunas esperadas
#     df_final = df_final[['QUADRANT_1', 'QUADRANT_2', 'QUADRANT_3', 'QUADRANT_4',
#                          'MES_1', 'MES_2', 'MES_3', 'MES_4', 'MES_5', 'MES_6',
#                          'MES_7', 'MES_8', 'MES_9', 'MES_10', 'MES_11', 'MES_12',
#                          'CATEGORIA_RESIDENCIAL', 'CATEGORIA_COMERCIAL', 'CATEGORIA_PUBLICA', 'CATEGORIA_INDUSTRIAL']]

#     # Converter todas as colunas para maiúsculas
#     df_final.columns = df_final.columns.str.upper()

#     return df_final
