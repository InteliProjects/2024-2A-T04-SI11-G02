# Relatório de Avaliação e Visualização das Métricas

## Introdução
Aqui está a documentação da avaliação e comparação entre dois modelos de rede neural para detecção de fraudes na rede de saneamento da Aegea, utilizando arquiteturas **Long Short-Term Memory (LSTM)** e **Gated Recurrent Unit (GRU)**. O foco principal desta documentação é analisar as métricas de desempenho obtidas por ambos os modelos, avaliando seu comportamento durante o treinamento e no conjunto de teste. A avaliação detalhada, juntamente com características da arquitetura, permitiu determinar o modelo mais adequado para a escalabilidade do projeto.

## Arquitetura dos Modelos

### 1. Modelo LSTM
A arquitetura LSTM (Long Short-Term Memory) é uma variação das redes neurais recorrentes (RNNs) projetada para lidar com dependências de longo prazo em sequências de dados. Ela utiliza células de memória e três portas (entrada, esquecimento e saída) que controlam o fluxo de informações, permitindo a retenção seletiva de dados relevantes. Isso torna o modelo eficaz em tarefas de séries temporais, como processamento de linguagem natural e previsão de dados sequenciais.

### 2. Modelo GRU
A rede neural GRU (Gated Recurrent Unit) simplifica as LSTMs, usando duas portas: atualização, que controla a memória mantida, e reset, que ajusta a incorporação de novas informações. Além disso, sua arquitetura em formato piramidal garante menos neurônios ao longo das camadas. Com menos parâmetros, as GRUs são mais rápidas para treinar, mantendo desempenho eficiente em tarefas de sequências, como tradução automática e processamento de linguagem natural.

## Avaliação e Métricas de Desempenho
As métricas de desempenho utilizadas para avaliar ambos os modelos foram selecionadas com base na natureza do problema e sua importância no contexto do projeto.

### Métricas Utilizadas

- **Acurácia:** Mede a fração de previsões corretas em relação ao total. É uma métrica importante para problemas de classificação.
- **Perda (Loss):** Calcula a diferença entre as previsões do modelo e os valores reais utilizando a função de custo. Valores menores indicam previsões mais precisas.
- **F1-Score:** Fornece uma média harmônica entre precisão e recall, sendo especialmente útil em problemas de classificação com classes desbalanceadas.
- **Precisão e Recall:** São métricas específicas para avaliar a qualidade das previsões em termos de falsos positivos e falsos negativos.
- **Tempo de Treinamento:** Mede o tempo total gasto para treinar o modelo, sendo relevante para avaliar a eficiência computacional.

## Resultados de Desempenho dos Modelos
A seguir estão os resultados individuais de cada modelo, seguidos de uma comparação detalhada.

### Desempenho do Modelo LSTM
O modelo LSTM foi avaliado utilizando os conjuntos de validação e teste, e os resultados das principais métricas foram registrados:

| Métrica           | Teste        |
|-------------------|--------------|
| **Acurácia**      |57,7%      |
| **Perda (Loss)**  | 67,3%      |
| **F1-Score**      | 39,3%      |
| **Precisão**      | 63,2%      |
| **Recall**        |52,1%      |
| **Tempo de Treinamento** | 90s por época |

### Desempenho do Modelo GRU
Resultados obtidos com o modelo GRU nos mesmos conjuntos de dados:

| Métrica         |   Teste        |
|-------------------|--------------|
| **Acurácia**       | 98%    |
| **Perda (Loss)**   | 4%     |
| **F1-Score**       |  98%    |
| **Precisão**      | 98%     |
| **Recall**         | 98%     |
| **Tempo de Treinamento** |35s por época  |

## Comparação entre LSTM e GRU

### Acurácia
- **LSTM**: O modelo LSTM apresentou uma acurácia de 57,7% no conjunto de validação, mostrando que ele foi capaz de capturar as dependências temporais presentes nos dados. Entretanto, a curva de aprendizado apresentou sinais de saturação após 20 épocas.
![Captura de tela 2024-09-28 132758](https://github.com/user-attachments/assets/968ca79c-e839-4101-af58-a03d510eb50d)


- **GRU**: O modelo GRU, embora mais simples, alcançou uma acurácia de 98%, superior ao LSTM, mesmo menor complexidade computacional. Isso porque foram adicionadas novas variáveis como estações do ano e o aumento de quadrantes de localização de quatro para oito. Além disso, não acreditamos que houve overfitting no conjuto de validação, porém este considerou apenas uma pequena amostra dos dados após o balanceamento.
![Captura de tela 2024-09-28 132510](https://github.com/user-attachments/assets/d4a56f09-8ac9-4505-99e9-d496224b7b21)
![Captura de tela 2024-09-28 132636](https://github.com/user-attachments/assets/cd022dbd-f736-4d55-bff6-2c42816eba98)
![Captura de tela 2024-09-29 040117](https://github.com/user-attachments/assets/cb01fca5-396e-4e9d-87b9-1bd1de457c14)





**Conclusão sobre acurácia**: O GRU se destaca pelo ótimo desempenho da métrica.

### Perda (Loss)
- **LSTM**: A perda no modelo LSTM no conjunto de validação foi de 67,3%, indicando uma boa capacidade de ajuste ao problema, mas também sugerindo que o modelo pode estar começando a sobreajustar após 20 épocas.
![Captura de tela 2024-09-28 133052](https://github.com/user-attachments/assets/12fa63b8-d252-47ac-a053-dab403d62739)

- **GRU**: O modelo GRU, com uma perda de no conjunto de validação de 4%, apresentou resultados similares ao LSTM, mas com um padrão de generalização mais estável, mesmo após épocas.
![Captura de tela 2024-09-29 040104](https://github.com/user-attachments/assets/1c85b6ad-a90c-4702-b429-ba379b2ccaa4)


**Conclusão sobre a perda**: O modelo GRU apresentou-se de forma mais vantajosa em termos de Loss devido ao seu padrão de generalização mais estável.

### F1-Score, Precisão e Recall
- **LSTM**: O F1-Score de 39,3% no LSTM foi levemente inferior ao do GRU, indicando que o modelo não conseguiu equilibrar bem entre precisão e recall. A precisão e o recall foram de 63,2% e 52,1%.
![Captura de tela 2024-09-29 040619](https://github.com/user-attachments/assets/9becd510-3ce6-40ee-aaac-d9abe69780a2)


- **GRU**: O GRU, com um F1-Score de , se mostrou robusto, com precisão e recall de 97% e 95%, respectivamente.

![Captura de tela 2024-09-29 040727](https://github.com/user-attachments/assets/faff2331-d7c3-459d-81e0-b0b02220e07d)


**Conclusão sobre F1-Score**: O GRU se destacou em função de mostra uma métrica mais robusta.

### Tempo de Treinamento
- **LSTM**: O tempo total de treinamento do modelo LSTM foi de 44 minutos, refletindo sua maior complexidade devido à arquitetura.
- **GRU**: O modelo GRU completou o treinamento em 18 minutos, significativamente mais rápido, o que o torna uma escolha eficiente para aplicações onde o tempo de execução é crítico.

**Conclusão sobre tempo de treinamento**: O GRU superou o LSTM em eficiência computacional, sendo mais rápido de treinar, o que deve ser um fator determinante dependendo da infraestrutura disponível.

## Conclusão
A comparação detalhada entre LSTM e GRU mostra que ambos os modelos têm pontos fortes dependendo das características específicas do problema. Embora o **LSTM** se destaque em longas sequências temporais, o **GRU** se mostrou mais eficiente em termos de tempo de treinamento e manteve um desempenho 
 mais competitivo nas métricas e deve ser o melhor modelo para o projeto.
