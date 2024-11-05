# Guia de Utilização - Predição de Fraudes

## Introdução
Este guia fornece instruções sobre como utilizar o modelo de detecção de fraudes do grupo Pega Gato.

## Passo a Passo para Utilização

1. **Upload de Dados**:
   Para a utilização do modelo, o usuário deverá fazer o upload de uma planilha CSV contendo as informações para a previsão do modelo:
   - Navegue até a aba **Upload de dados**.
   - Arraste e solte o arquivo com os dados de consumo (formato CSV) na área designada ou clique em **Browse files** para selecionar o arquivo do seu sistema.
   - **Limite de tamanho**: 200MB por arquivo.
   - Após o upload, uma mensagem de confirmação será exibida, indicando que o arquivo foi carregado com sucesso.
  ![image](https://github.com/user-attachments/assets/fecf8dad-81fe-4fdc-a132-25607402f7c8)


2. **Exemplo de Planilha de Dados (CSV)**

| EMP_CODIGO | REFERENCIA  | COD_GRUPO | COD_SETOR_COMERCIAL | NUM_QUADRA | MATRICULA | ECO_RESIDENCIAL | VOLUME_ESTIMADO | FATURADO_MEDIA | COD_LATITUDE | COD_LONGITUDE |
|------------|-------------|-----------|---------------------|------------|-----------|-----------------|-----------------|----------------|--------------|---------------|
| 2          | 2024-05-01  | 4         | 17                  | 16         | 17188010  | 0               | -1.0            | NaN            | -20.460904   | -54.634308    |
| 2          | 2024-06-01  | 4         | 87                  | 60         | 17424465  | 1               | 0.0             | NaN            | -20.520205   | -54.602621    |
| 2          | 2024-07-01  | 14        | 85                  | 314        | 17857770  | 1               | 0.0             | NaN            | -20.517992   | -54.605950    |

Este é um exemplo simplificado do formato que os dados devem ter ao serem carregados no sistema.

3. **Iniciando o Pré-processamento**:
   Para que os dados sejam adequados para a utilização no modelo, eles devem passar pelo pré-processamento.
   - Após o carregamento do arquivo, clique no botão **Iniciar pré-processamento**.
   - A aplicação processará os dados para a predição de fraudes.
![image](https://github.com/user-attachments/assets/eda8ffa2-419b-4701-9a57-0d3e5b8416b3)

4. **Visualização dos Dados Pré-processados**:
   - Após o pré-processamento, uma tabela será exibida mostrando os dados processados, incluindo as colunas relevantes para a análise.
![image](https://github.com/user-attachments/assets/3cf556d6-c469-4a88-b400-c8bd8c0fcb74)

5. **Painel de Monitoramento de Consumo**:
   - Na aba **Visualização**, você poderá acompanhar as métricas de consumo, como o volume total consumido, o número de matrículas atendidas e o valor arrecadado.
   - Também será possível visualizar gráficos e mapas com a distribuição de consumo por categoria, regiões da cidade e outras métricas.

![image](https://github.com/user-attachments/assets/8185ec89-f89c-42af-b53d-ea59515776c8)
![image](https://github.com/user-attachments/assets/5d7e7551-642c-4970-a0ed-e451cbe51235)


6. **Exploração de Ocorrências e Anomalias**:
   - A aplicação fornece gráficos de ocorrências por categoria e outros indicadores de anomalias no consumo, como medidores de difícil acesso ou imóveis desocupados.
   - Um mapeamento geoespacial também está disponível para explorar anomalias de forma visual.
![image](https://github.com/user-attachments/assets/29ea3c31-cafd-40d0-8f13-cbaf6ffdcfc4)


7. **Próximos Passos**:
   - Após a visualização dos dados, você pode navegar para a aba **Modelo de previsão** para visualizar as previsões de fraudes.

## IMPORTANTE
- Certifique-se de que os dados estejam formatados corretamente para evitar erros durante o upload e pré-processamento.
- Utilize arquivos de consumo referentes aos últimos 6 meses para obter melhores resultados.
