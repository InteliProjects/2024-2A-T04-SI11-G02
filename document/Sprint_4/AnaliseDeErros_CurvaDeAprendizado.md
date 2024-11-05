# Análise de Erros e Curva de Aprendizado nos Modelos LSTM e GRU

## Introdução
Este documento tem como objetivo explorar os tipos e causas dos erros cometidos pelos modelos **LSTM** e **GRU** durante o treinamento e validação. A análise foi baseada nos gráficos de perda (Loss), acurácia, matrizes de confusão, relatórios de classificação, curvas ROC, curvas de Precisão-Recall e gráficos de precisão e recall em diferentes limiares, a fim de identificar padrões e comportamentos dos modelos ao longo das épocas.

Também contém gráficos e explicações da curva de aprendizado.

---

## Modelo LSTM

### Curva de Aprendizado do LSTM

![image](https://github.com/user-attachments/assets/bd61325d-b409-4db1-bedc-ce3b7214e5fe)

As curvas de aprendizado do modelo **LSTM** mostram um padrão de overfitting nas últimas épocas. Enquanto a acurácia de treinamento continua a aumentar, a acurácia de validação se estabiliza e começa a oscilar, indicando que o modelo está começando a memorizar o conjunto de treinamento, em vez de aprender generalizações úteis para dados nunca vistos.

### Perda (Loss) e Acurácia durante o treinamento

![image](https://github.com/user-attachments/assets/a0db4ef5-bfde-43d9-84b7-92383bac4f92)

- **Acurácia**:
    - A acurácia do conjunto de validação cresce até certo ponto, mas existe uma oscilação visível, indicando que o modelo está começando a superajustar os dados de treinamento. Esse comportamento é característico de overfitting e pode ser um ponto de atenção no modelo.

- **Perda (Loss)**:
    - A perda de validação diminui, mas também começa a apresentar variações ao longo das últimas épocas, o que é um sinal de que o modelo está começando a se ajustar excessivamente ao conjunto de treinamento. Isso pode prejudicar o desempenho em dados nunca vistos.
    - A perda no conjunto de validação não diminui tão drasticamente quanto no treinamento, o que sugere que o modelo pode estar memorizando o conjunto de treinamento.

### Relatório de Classificação

![image](https://github.com/user-attachments/assets/4cf5ebea-b767-43df-a4fc-835539a12907)

- Para a classe negativa (0.0), a precisão é alta (0.77), mas o recall é baixo (0.06), indicando que o modelo tende a classificar poucos exemplos da classe negativa corretamente.
- Para a classe positiva (1.0), o recall é alto (0.98), mas a precisão é relativamente baixa (0.51), o que sugere que o modelo classifica muitos exemplos como positivos, resultando em muitos falsos positivos.
- O f1-score geral para ambas as classes é desequilibrado, com um valor muito baixo para a classe negativa (0.11), o que confirma que o modelo tem dificuldade em classificar corretamente a classe negativa.

### Curva ROC

![image](https://github.com/user-attachments/assets/23f82851-2b0b-4043-9983-f4f4e8e08b9c)

- A curva ROC do modelo mostra uma performance moderada, com um valor de AUC = 0.61.
- Isso indica que o modelo tem uma capacidade limitada de discriminar entre as classes positivas e negativas, com uma tendência a errar mais em relação à classe negativa (falsos positivos altos).

### Curva de Precisão-Recall

![image](https://github.com/user-attachments/assets/52d24c50-6835-46b0-ba70-2c1ba3cbe970)

- A **Curva de Precisão-Recall** mostra uma performance com uma **AP = 0.59**, o que indica que o modelo não consegue manter uma precisão alta quando o recall aumenta.
- A precisão cai drasticamente quando o recall aumenta, sugerindo que o modelo está tentando identificar muitos exemplos como positivos, mas ao custo de cometer muitos erros (falsos positivos). Isso é uma indicação de que o modelo pode não estar equilibrando bem a precisão e recall.

### Precisão e Recall em Diferentes Limiares

![image](https://github.com/user-attachments/assets/5a72eef2-d95e-45b0-a03d-91bb6a91a55c)

- O gráfico mostra que o recall é alto em limiares baixos, mas diminui significativamente à medida que o limiar aumenta, enquanto a precisão se mantém baixa nos limiares mais baixos e só começa a aumentar em limiares mais altos.
- Isso indica que, ao aumentar o limiar de decisão, o modelo tende a ser mais conservador, priorizando a precisão sobre o recall.

---

## Modelo GRU

### Curva de Aprendizado

![image](https://github.com/user-attachments/assets/321b5f59-84dd-4789-a81c-aeb13bc5c7ef)

As curvas mostram que a precisão e a perda do treinamento e validação evoluem de forma consistente, com aumento da precisão e redução da perda até a 25ª época. As perdas de treinamento e validação permanecem próximas, indicando bom ajuste e generalização sem sinais evidentes de overfitting.

### Perda (Loss) e Acurácia durante o treinamento

![image](https://github.com/user-attachments/assets/42019e97-07bf-4b74-ad8a-aa6221abc5a4)

- **Acurácia**:
    - O modelo GRU mostra um aumento consistente na acurácia tanto para o conjunto de treinamento quanto para o de validação ao longo das épocas. Isso indica que o modelo está aprendendo de forma eficaz e ajustando seus pesos com base nos dados fornecidos.
    - Embora a acurácia pareça excelente, é importante destacar que o modelo pode não generalizar bem quando confrontado com novos dados, visto que parece estar aprendendo muito bem os dados fornecidos, mas pode não capturar adequadamente a variação dos dados do mundo real.

- **Perda (Loss)**:
    - A perda de treinamento diminui de forma constante ao longo das épocas, o que indica que o modelo está conseguindo minimizar o erro e se ajustando corretamente aos dados.
    - A perda de validação segue um padrão semelhante ao da perda de treinamento, o que é um bom sinal de que o modelo está generalizando bem e não está ajustando excessivamente os dados de treinamento.
    - No entanto, nas últimas épocas, nota-se uma leve oscilação na perda de validação, o que pode indicar que o modelo começa a encontrar dificuldades para continuar a melhorar o desempenho nos dados de validação.

### Relatório de Classificação

- O modelo GRU atinge uma acurácia quase perfeita tanto para o conjunto de treinamento quanto para o de validação. **Isso pode ser um sinal de overfitting**, uma vez que uma acurácia tão alta, especialmente em validação, é rara e suspeita de excesso de ajuste aos dados.
