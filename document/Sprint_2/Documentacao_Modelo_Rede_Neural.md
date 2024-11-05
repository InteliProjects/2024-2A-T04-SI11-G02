# Documentação Modelo de Rede Neural

```python
!pip install imblearn
```

**Descrição:** Este comando instala o pacote **imbalanced-learn** (`imblearn`), que é uma biblioteca Python especializada no tratamento de conjuntos de dados desbalanceados.

```python
!pip install tensorflow-addons
```

**Descrição:** Este comando instala o pacote **TensorFlow Addons** (`tensorflow-addons`), que é uma coleção de componentes adicionais para o TensorFlow, a popular biblioteca de aprendizado de máquina desenvolvida pelo Google.

```python
import pandas as pd
import tensorflow as tf
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import RMSprop
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ReduceLROnPlateau
import tensorflow_addons as tfa
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

tf.random.set_seed(42)
```

Descrição:

1. **`import pandas as pd`**
    - **Pandas**: Biblioteca para manipulação e análise de dados, especialmente com estruturas como DataFrames.
    - **Uso**: Carregamento, transformação e análise de dados tabulares.
2. **`import tensorflow as tf`**
    - **TensorFlow**: Framework de aprendizado profundo amplamente utilizado para construir e treinar redes neurais.
    - **Uso**: Construção e execução de modelos de deep learning.
3. **`import plotly.express as px`**
    - **Plotly Express**: Biblioteca para criar gráficos interativos.
    - **Uso**: Visualizações de dados interativas, como gráficos de dispersão, linhas e barras.
4. **`import matplotlib.pyplot as plt`**
    - **Matplotlib**: Biblioteca padrão para criação de gráficos estáticos.
    - **Uso**: Visualizações de dados mais simples e básicas.
5. **`from sklearn.cluster import KMeans`**
    - **KMeans**: Algoritmo de agrupamento não supervisionado para particionar os dados em clusters.
    - **Uso**: Agrupamento de dados em subconjuntos similares, útil em análise exploratória.
6. **`from sklearn.preprocessing import StandardScaler, LabelEncoder`**
    - **StandardScaler**: Normaliza dados, padronizando recursos para que tenham média 0 e desvio padrão 1.
    - **LabelEncoder**: Converte rótulos categóricos em valores numéricos.
    - **Uso**: Pré-processamento de dados, normalizando e codificando variáveis categóricas.
7. **`from sklearn.model_selection import train_test_split, cross_val_score`**
    - **train_test_split**: Divide os dados em conjuntos de treino e teste.
    - **cross_val_score**: Realiza validação cruzada para avaliar a performance de um modelo.
    - **Uso**: Avaliação do desempenho de modelos e divisão dos dados.
8. **`from sklearn.linear_model import LogisticRegression`**
    - **LogisticRegression**: Modelo de regressão logística para tarefas de classificação binária.
    - **Uso**: Criação de modelos preditivos simples, com interpretação direta dos coeficientes.
9. **`from sklearn.ensemble import RandomForestClassifier`**
    - **RandomForestClassifier**: Algoritmo de aprendizado de máquina que usa múltiplas árvores de decisão para a classificação.
    - **Uso**: Classificação de alta performance e menor tendência ao overfitting.
10. **`from sklearn.metrics import classification_report, confusion_matrix`**
    - **classification_report**: Gera uma tabela com as principais métricas de classificação (precisão, recall, f1-score).
    - **confusion_matrix**: Gera a matriz de confusão para avaliar a performance do modelo.
    - **Uso**: Avaliação de modelos de classificação.
11. **`from tensorflow.keras.models import Sequential`**
    - **Sequential**: Tipo de modelo em que as camadas são empilhadas linearmente.
    - **Uso**: Construção de redes neurais camada a camada.
12. **`from tensorflow.keras.layers import Dense, Dropout, Input`**
    - **Dense**: Camada densa totalmente conectada.
    - **Dropout**: Camada para evitar overfitting, desativando aleatoriamente neurônios durante o treinamento.
    - **Input**: Definir a entrada da rede.
    - **Uso**: Construção da arquitetura da rede neural.
13. **`from tensorflow.keras.optimizers import Adam, RMSprop`**
    - **Adam** e **RMSprop**: Otimizadores usados para ajustar os pesos da rede durante o treinamento.
    - **Uso**: Ajuste de pesos para minimizar a função de perda.
14. **`from imblearn.over_sampling import SMOTE`**
    - **SMOTE**: Técnica de oversampling para lidar com conjuntos de dados desbalanceados.
    - **Uso**: Geração de exemplos sintéticos da classe minoritária para equilibrar as classes.
15. **`from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau`**
    - **EarlyStopping**: Para o treinamento quando a performance não melhora após um certo número de épocas.
    - **ReduceLROnPlateau**: Reduz a taxa de aprendizado quando a performance estagna.
    - **Uso**: Controle do treinamento para evitar overfitting e melhorar a eficiência.
16. **`import tensorflow_addons as tfa`**
    - **TensorFlow Addons**: Pacote que contém funções e camadas adicionais para modelos TensorFlow.
    - **Uso**: Funcionalidades avançadas e adicionais para redes neurais.
17. **`from sklearn.model_selection import train_test_split`**
    - Mesma função já descrita anteriormente.

```python
!gdown 1iZDFEefN0J2wao1QRIAuT-ukp0coX0Rp
!gdown 1_lY6ydxyDA9-HNrYleq4UrL-JKcKLM7c
!gdown 1C1ZHPeYF71NVVOkZD6cW5SmzV9Uui4QK
!gdown 1Lbayox3-fo92nLSvk1MPbai5ek0Noqi3
```

**Descrição:** 
Cada comando `!gdown` faz o download do arquivo associado ao ID fornecido e o salva no diretório de trabalho atual do ambiente onde o código está sendo executado

```python
df = pd.read_csv('/content/DADOS_PROCESSADOS (1).csv', delimiter=','
df
```

**Descrição:** 

- **Carrega** o conteúdo do arquivo CSV chamado `DADOS_PROCESSADOS (1).csv` em um DataFrame `df`.
- **Exibe** o DataFrame `df` para que o usuário possa visualizar os dados.

```python
df_ext = pd.read_csv('/content/DADOS_PROCESSADOS_COMPLETOS.csv', delimiter=',')
df_ext
```

**Descrição:**

- **Carrega** o conteúdo do arquivo `DADOS_PROCESSADOS_COMPLETOS.csv` em um DataFrame chamado `df_ext`.
- **Exibe** o DataFrame `df_ext` para que o usuário possa visualizar os dados.

```python
df.columns
df_ext.columns
```

Descrição:

- Retornas as colunas dos respectivos DataFrames

```python
df_ext = df_ext.drop(columns=['MATRICULA', 'CONS_MEDIDO', 'ANOMES', 'COD_LATITUDE', 'COD_LONGITUDE', 'CLUSTER'])
```

**Descrição**:

- Exclui as colunas especificadas

```python
X = df.drop(columns=['FRAUDADOR'])
y = df['FRAUDADOR']
X

X_ext = df_ext.drop(columns=['FRAUDADOR'])
y_ext = df_ext['FRAUDADOR']
X_ext
```

**Descrição:**

- Aqui, dividimos a coluna target das outras colunas utilizadas como features do modelo.

```python
# Analisando o desequilíbrio das classes
y.value_counts().plot(kind='bar')
plt.title('Distribuição das Classes')
plt.show()

# Aplicando SMOTE para balanceamento
smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(X, y)

# Verificando a nova distribuição das classes
y_balanced.value_counts().plot(kind='bar')
plt.title('Distribuição das Classes Após SMOTE')
plt.show()
```

Descrição:

- **`y.value_counts()`**: Conta a quantidade de ocorrências de cada classe no vetor `y`, que é a variável alvo (ou rótulo) no problema de classificação.
- **`plot(kind='bar')`**: Cria um gráfico de barras para visualizar a distribuição das classes.
- **`plt.title('Distribuição das Classes')`**: Define o título do gráfico.
- **`plt.show()`**: Exibe o gráfico
- **`smote = SMOTE(random_state=42)`**: Cria uma instância da classe `SMOTE` com uma semente aleatória definida por `random_state=42` para garantir a reprodutibilidade dos resultados.
- **`X_balanced, y_balanced = smote.fit_resample(X, y)`**: Aplica o SMOTE ao conjunto de dados. `fit_resample` gera novos exemplos da classe minoritária para equilibrar as classes:
    - **`X_balanced`**: As características (`features`) do conjunto de dados após o balanceamento.
    - **`y_balanced`**: A variável alvo (`labels`) após o balanceamento
- **`y_balanced.value_counts()`**: Conta a quantidade de ocorrências de cada classe no vetor `y_balanced`, que é a variável alvo após o balanceamento.
- **`plot(kind='bar')`**: Cria um gráfico de barras para visualizar a nova distribuição das classes.
- **`plt.title('Distribuição das Classes Após SMOTE')`**: Define o título do gráfico.
- **`plt.show()`**: Exibe o gráfico.

![classe_fraudador.png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/classe_fraudador.png)

![classe_pos_smote.png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/classe_pos_smote.png)

A partir do gráfico é possível entender que há uma distribuição de classes sobre fraudador sendo definidas como 0 e 1.

1. **Gráfico Antes do SMOT**:
    - Esse gráfico mostra um **desequilíbrio de classes** significativo, onde uma classe  ("0" ou "1") tem muito mais exemplos do que a outra.

1. **Gráfico Depois do SMOTE:**
    - Mostra a distribuição das classes após o uso do SMOTE. Ambas as barras (representando as diferentes classes) estão equilibradas, ou seja, têm aproximadamente a mesma altura.
    - **Interpretação**: Isso indica que o SMOTE foi bem-sucedido em gerar exemplos sintéticos para a classe minoritária, equilibrando as classes no conjunto de dados.
    - **Importância**: Com as classes balanceadas, o modelo de aprendizado de máquina treinado neste conjunto de dados terá uma chance maior de aprender a prever ambas as classes de maneira eficaz, sem tendenciosidade para a classe majoritária.

### Implicações para o Negócio

- **Redução de Tendências**: O gráfico pós-SMOTE indica que o modelo agora será menos tendencioso, pois terá uma quantidade igual de exemplos para aprender sobre ambas as classes.
- **Melhoria no Desempenho do Modelo**: Em termos práticos, isso significa que o modelo de classificação deve melhorar na identificação de casos importantes (como fraudes ou churn), que anteriormente poderiam ter sido negligenciados devido ao desequilíbrio.

Portanto, após a aplicação do SMOTE, as classes estão balanceadas, o que é crucial para garantir que o modelo de aprendizado de máquina seja justo e eficaz na previsão das diferentes classes. Isso, por sua vez, aumenta a confiabilidade do modelo em aplicações críticas para o negócio.

Sendo assim, inicia-se a divisão dos dados em treino, teste e validação.

Essas linhas de código dividem o conjunto de dados balanceado em conjuntos de **treinamento**, **validação**, e **teste**. 

### 1. **Divisão em Treinamento e Teste**

```python
X_train_full, X_test, y_train_full, y_test = train_test_split(X_balanced, y_balanced, test_size=0.3, random_state=42)

```

- **Objetivo**: Dividir o conjunto de dados balanceado em dois conjuntos:
    - **Treinamento Completo (`X_train_full`, `y_train_full`)**: 70% dos dados, que serão usados para treinar o modelo.
    - **Teste (`X_test`, `y_test`)**: 30% dos dados, que serão usados para avaliar o desempenho do modelo final.
- **Parâmetros**:
    - **`test_size=0.3`**: Especifica que 30% dos dados serão reservados para o conjunto de teste.
    - **`random_state=42`**: Garante que a divisão seja reprodutível, ou seja, sempre que o código for executado com essa semente, os dados serão divididos da mesma forma.

### 2. **Divisão em Treinamento e Validação**

```python
X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.3, random_state=42)

```

- **Objetivo**: Dividir o conjunto de treinamento completo (`X_train_full`, `y_train_full`) em dois conjuntos:
    - **Treinamento (`X_train`, `y_train`)**: 70% dos dados de treinamento, que serão efetivamente usados para ajustar o modelo.
    - **Validação (`X_val`, `y_val`)**: 30% dos dados de treinamento, que serão usados para ajustar hiperparâmetros e prevenir overfitting.
- **Parâmetros**:
    - **`test_size=0.3`**: Indica que 30% dos dados de treinamento completo serão usados para validação.
    - **`random_state=42`**: Novamente, garante a reprodutibilidade da divisão.

### Resumo

- **Primeira divisão**: Separa os dados em **treinamento completo (70%)** e **teste (30%)**.
- **Segunda divisão**: Separa o conjunto de treinamento completo em **treinamento (70% do total)** e **validação (30% do total)**.

Esse processo cria três conjuntos: **treinamento** (para treinar o modelo), **validação** (para ajustar o modelo), e **teste** (para avaliar o desempenho final).

```python
# Primeiro, divisão dos dados em treino (70%) e teste (30%)
X_train_full_ext, X_test_ext, y_train_full_ext, y_test_ext = train_test_split(X_balanced_ext, y_balanced_ext, test_size=0.3, random_state=42)

# Agora, dividimos o conjunto de treino em treino (70% do total) e validação (30% do total)
X_train_ext, X_val_ext, y_train_ext, y_val_ext = train_test_split(X_train_full_ext, y_train_full_ext, test_size=0.3, random_state=42)
```

Esse código divide o conjunto de dados balanceado `X_balanced_ext` e `y_balanced_ext` em três partes: primeiro, ele separa 70% dos dados para treino (`X_train_full_ext`, `y_train_full_ext`) e 30% para teste (`X_test_ext`, `y_test_ext`). Em seguida, divide novamente o conjunto de treino em 70% para treinamento final (`X_train_ext`, `y_train_ext`) e 30% para validação (`X_val_ext`, `y_val_ext`). Isso cria conjuntos separados para treinar, validar e testar o modelo de forma organizada e controlada.

```python
model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compilando o modelo
model.compile(loss='binary_crossentropy', optimizer='RMSprop', metrics=['accuracy'])

# Resumo da arquitetura do modelov
model.summary()
```

Acima há um modelo de rede neural usando a API `Sequential` do Keras. 

1. **Definição do Modelo**:
    - **Camadas Densas (`Dense`)**:
        - A rede é composta por 6 camadas densas (fully connected):
            - **Primeira camada**: 128 neurônios, função de ativação `ReLU`, e `input_dim=X_train.shape[1]`, que define a quantidade de entradas com base no número de características (`features`) no conjunto de dados de treino.
            - As camadas subsequentes têm 64, 32, 16, 8 neurônios, todas com função de ativação `ReLU`.
            - **Última camada**: 1 neurônio com ativação `sigmoid`, adequada para problemas de classificação binária.
2. **Compilação do Modelo**:
    - **Função de perda**: `binary_crossentropy`, usada para classificação binária.
    - **Otimizador**: `RMSprop`, que ajusta os pesos da rede para minimizar a perda.
    - **Métrica**: `accuracy`, que mede a precisão das previsões do modelo.
3. **Resumo do Modelo**:
    - **`model.summary()`**: Exibe um resumo da arquitetura do modelo, incluindo o número de camadas, o número de parâmetros em cada camada, e o total de parâmetros.

Logo, o código define uma rede neural densa com 5 camadas ocultas e 1 camada de saída, compilada para um problema de classificação binária, e exibe um resumo da arquitetura do modelo.

```python
model_ext = Sequential()
model.add(Dense(128, input_dim=X_train_ext.shape[1], activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compilando o modelo
model.compile(loss='binary_crossentropy', optimizer='RMSprop', metrics=['accuracy'])

# Resumo da arquitetura do modelov
model.summary()
```

A diferença entre os dois modelos `model` e `model_ext` está nos seguintes pontos principais:

1. **Entrada de Dados (`input_dim`)**:
    - **`model`:** Usa `input_dim=X_train.shape[1]`, onde `X_train` representa os dados de treinamento do modelo.
    - **`model_ext`:** Usa `input_dim=X_train_ext.shape[1]`, onde `X_train_ext` representa uma versão estendida ou diferente dos dados de treinamento.
    

A diferença sugere que `X_train` e `X_train_ext` podem ter diferentes números de características (colunas) ou podem representar conjuntos de dados distintos.

**Otimização**:

- **`model`:** Usa o otimizador `RMSprop`.
- **`model_ext`:** Usa o otimizador `Adam`.

`RMSprop` e `Adam` são algoritmos de otimização diferentes. O `Adam` é uma combinação de `RMSprop` e `Momentum`, e geralmente é mais robusto e eficaz em muitos cenários de treinamento de redes neurais. Ele adapta a taxa de aprendizado para cada parâmetro, o que pode resultar em um treinamento mais eficiente.

Essas são as diferenças principais, sendo que a estrutura das camadas e a função de ativação final (`sigmoid`) são as mesmas em ambos os modelos, assim como a função de perda (`binary_crossentropy`) e a métrica de avaliação (`accuracy`).

# Compilação do Modelo

```python
optimizer = RMSprop(learning_rate=0.001)

model.compile(loss='binary_crossentropy',
              optimizer='RMSprop',
              metrics=[
                  'accuracy',
                  tfa.metrics.F1Score(num_classes=1, threshold=0.5),
                  tf.keras.metrics.Precision(),
                  tf.keras.metrics.Recall()
              ])
```

Na configuração do modelo de inteligência artificial que visa  fazer previsões,  usamos um "professor" (um otimizador chamado RMSprop) que ajuda a ajustar os erros do modelo. Além disso, estamos avaliando o desempenho do modelo usando várias formas de verificar se ele está acertando: verificamos quantas vezes ele acerta (acurácia), quão bem ele detecta casos positivos (precisão), como ele consegue identificar corretamente os casos positivos (recall), e uma combinação dessas medidas chamada F1-Score. Essas métricas ajudam a garantir que o modelo esteja não apenas fazendo previsões, mas que essas previsões sejam precisas e confiáveis.

```python
optimizer = Adam(learning_rate=0.0001)

model_ext.compile(loss='binary_crossentropy',
              optimizer='Adam',
              metrics=[
                  'accuracy',
                  tfa.metrics.F1Score(num_classes=1, threshold=0.5),
                  tf.keras.metrics.Precision(),
                  tf.keras.metrics.Recall()
              ])
```

Aqui, estamos configurando outro modelo de inteligência artificial, mas com um "professor" diferente, chamado Adam, que também ajuda o modelo a melhorar a cada tentativa. A principal diferença é que este "professor" tem uma abordagem um pouco diferente para corrigir os erros do modelo e está ensinando de forma mais lenta, com uma taxa de aprendizado menor (0,0001). As mesmas verificações de desempenho (acurácia, F1-Score, precisão e recall) estão sendo usadas para garantir que o modelo faça previsões precisas e confiáveis, mas com um método de aprendizado ligeiramente diferente do modelo anterior.

# Treinamento do Modelo

No treinamento do modelo envolveram-se algumas etapas e estratégias adicionais para garantir que ele aprenda de forma eficiente e seja avaliado corretamente:

1. **Parada Antecipada (Early Stopping):**
    - Foi definido um critério para parar o treinamento mais cedo se o modelo parar de melhorar. Especificamente, se a perda no conjunto de validação (`val_loss`) não melhorar por 5 épocas consecutivas, o treinamento será interrompido para evitar que o modelo continue ajustando e potencialmente acabe piorando. Além disso, o modelo restaurará os pesos da melhor versão encontrada durante o treinamento.
2. **Treinamento do Modelo:**
    - O modelo é treinado usando os dados de entrada (`X_train`) e os rótulos de saída (`y_train`) por até 100 épocas, mas pode parar mais cedo devido ao Early Stopping.
    - O treinamento é feito em lotes de 64 exemplos de cada vez, o que ajuda o modelo a aprender em pequenos passos.
    - Durante o treinamento, o modelo é avaliado continuamente com dados de validação (`X_test` e `y_test`) para verificar se está realmente aprendendo a generalizar para dados que não viu antes.
3. **Classificação Ponderada (Comentada):**
    - Há uma linha de código comentada que sugere uma técnica chamada `class_weight`, que seria usada para dar mais peso à classe positiva (classe 1). Isso é útil quando as classes estão desbalanceadas, mas nesse caso, essa linha está desativada.
4. **Avaliação do Modelo:**
    - Após o treinamento, o modelo é avaliado nos dados de teste (`X_test` e `y_test`) para medir seu desempenho final.
    - Os resultados incluem a perda (quão errado o modelo está), a acurácia (quantas vezes o modelo acerta), o F1-Score (uma média que leva em conta a precisão e o recall), a precisão (quantas previsões positivas estão corretas) e o recall (quantos dos verdadeiros positivos o modelo encontrou).

Esses passos ajudam a garantir que o modelo não apenas aprenda, mas que ele pare no momento certo e seja avaliado de maneira abrangente para garantir que suas previsões sejam de alta qualidade.

![image.png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/treinamento_modelo1.png)

A imagem acima evidencia o processo de treinamento de um modelo de machine learning em várias épocas, detalhando o desempenho do modelo em cada uma delas. Vamos analisar os elementos principais:

1. **Épocas**: O treinamento é dividido em épocas (de 1 a 100). A cada época, o modelo ajusta seus parâmetros com base nos dados de treinamento e é avaliado com dados de validação.
2. **Perda (`loss`)**: Essa métrica indica o quão bem o modelo está performando. Quanto menor a perda, melhor o modelo está se saindo. Ela é calculada tanto nos dados de treinamento quanto nos de validação (indicado como `val_loss`).
3. **Acurácia (`accuracy`)**: Reflete a porcentagem de previsões corretas feitas pelo modelo. O modelo está sendo avaliado tanto em termos de acurácia nos dados de treinamento quanto nos de validação (indicado como `val_accuracy`).
4. **F1-Score (`f1_score`)**: É uma métrica que combina precisão e recall para fornecer uma visão balanceada da performance do modelo, especialmente em conjuntos de dados desbalanceados. Um valor mais alto indica um melhor equilíbrio entre precisão e recall.
5. **Precisão (`precision`)**: Mede a porcentagem de previsões positivas que realmente são positivas. A precisão do modelo melhora ao longo das épocas.
6. **Recall (`recall`)**: Mede a capacidade do modelo de identificar corretamente todas as instâncias positivas. Esta métrica também é avaliada e tende a melhorar conforme o modelo treina.
7. **Validação**: As métricas com o prefixo `val_` (como `val_loss` e `val_accuracy`) indicam o desempenho do modelo nos dados de validação, que não são usados diretamente no treinamento. Isso dá uma ideia de quão bem o modelo pode generalizar para novos dados.

### Interpretação Geral:

- **Melhoria ao longo das épocas**: O modelo está aprendendo, conforme indicado pela diminuição da perda (`loss`) e melhoria das métricas (`accuracy`, `f1_score`, `precision`, `recall`).
- **Estabilidade**: As métricas de validação (como `val_loss` e `val_accuracy`) são importantes para observar. Se elas começam a piorar enquanto as métricas de treinamento melhoram, isso pode ser um sinal de overfitting, onde o modelo se ajusta demais aos dados de treinamento e perde a capacidade de generalizar.
- **Parada Antecipada**: Como o `EarlyStopping` foi configurado, o treinamento pararia mais cedo se `val_loss` não melhorasse por 5 épocas consecutivas, o que ajuda a evitar o overfitting.

No final da 10ª época, os resultados são: `Loss: 0.5330`, `Accuracy: 0.7174`, `F1-Score: 0.6419`, `Precision: 0.8732`, `Recall: 0.5076`. Esses números indicam que o modelo tem uma boa precisão, mas ainda pode melhorar em termos de recall (capacidade de identificar corretamente todos os positivos).

```python
# Avaliar o modelo no conjunto de teste
results = model.evaluate(X_test, y_test)
test_loss, test_accuracy, test_f1_score, test_precision, test_recall = results
print(f'Conjunto de Teste - Loss: {test_loss}, Accuracy: {test_accuracy}, F1-Score: {test_f1_score}, Precision: {test_precision}, Recall: {test_recall}')

# Avaliar o modelo no conjunto de validação
results_val = model.evaluate(X_val, y_val)
val_loss, val_accuracy, val_f1_score, val_precision, val_recall = results_val
print(f'Conjunto de Validação - Loss: {val_loss}, Accuracy: {val_accuracy}, F1-Score: {val_f1_score}, Precision: {val_precision}, Recall: {val_recall}')
```

Esse código está avaliando o desempenho do modelo em dois conjuntos de dados diferentes: o conjunto de teste e o conjunto de validação.

1. **Avaliação no Conjunto de Teste:**
    - O modelo é avaliado usando os dados de teste (`X_test` e `y_test`), que são separados do treinamento e validação.
    - As métricas de perda, acurácia, F1-Score, precisão e recall são calculadas e armazenadas em variáveis.
    - Os resultados são impressos para mostrar o desempenho do modelo em dados que ele nunca viu durante o treinamento.
2. **Avaliação no Conjunto de Validação:**
    - De forma similar, o modelo é avaliado no conjunto de validação (`X_val` e `y_val`).
    - As mesmas métricas (perda, acurácia, F1-Score, precisão e recall) são calculadas e exibidas.

Essas avaliações ajudam a entender como o modelo performa em dados que não foram usados diretamente no treinamento e fornecem insights sobre sua capacidade de generalização.

3596/3596 [==============================] - 5s 1ms/step - loss: 0.5330 - accuracy: 0.7174 - f1_score: 0.6420 - precision_12: 0.8732 - recall_12: 0.5076
Conjunto de Teste - Loss: 0.5330330729484558, Accuracy: 0.7173614501953125, F1-Score: [0.6419582], Precision: 0.8731765747070312, Recall: 0.5075564980506897
2517/2517 [==============================] - 3s 1ms/step - loss: 0.5344 - accuracy: 0.7136 - f1_score: 0.6393 - precision_12: 0.8734 - recall_12: 0.5042
Conjunto de Validação - Loss: 0.5343939065933228, Accuracy: 0.7135619521141052, F1-Score: [0.6393032], Precision: 0.8734458684921265, Recall: 0.5041554570198059

Os resultados fornecem uma avaliação do desempenho do modelo tanto no conjunto de teste quanto no conjunto de validação:

1. **Conjunto de Teste:**
    - **Loss (Perda):** 0.5330 - Indica o quão bem o modelo está performando nos dados de teste. Um valor mais baixo é geralmente melhor.
    - **Accuracy (Acurácia):** 0.7174 - O modelo acertou aproximadamente 71,74% das previsões nos dados de teste.
    - **F1-Score:** 0.6420 - Mostra um equilíbrio entre precisão e recall. Um valor mais próximo de 1 indica melhor desempenho.
    - **Precision (Precisão):** 0.8732 - Cerca de 87,32% das previsões positivas do modelo estavam corretas.
    - **Recall:** 0.5076 - O modelo conseguiu identificar corretamente 50,76% das instâncias que eram realmente positivas.
2. **Conjunto de Validação:**
    - **Loss (Perda):** 0.5344 - Similar ao conjunto de teste, indicando um desempenho próximo nos dados de validação.
    - **Accuracy (Acurácia):** 0.7136 - O modelo acertou cerca de 71,36% das previsões nos dados de validação.
    - **F1-Score:** 0.6393 - Similar ao conjunto de teste, indicando um desempenho consistente.
    - **Precision (Precisão):** 0.8734 - Muito próxima da precisão no conjunto de teste.
    - **Recall:** 0.5042 - Um pouco menor que no conjunto de teste, mas ainda consistente.

Esses resultados indicam que o modelo tem um desempenho estável entre os conjuntos de teste e validação, com boas métricas de precisão, embora o recall (a capacidade de identificar todas as instâncias positivas) ainda possa ser melhorado.

# Visualização

Abaixo nota-se um gráfico de linha com as épocas ao longo do tempo

![newplot (2).png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot_(2).png)

Este gráfico mostra a evolução da perda (loss) durante o treinamento de um modelo de machine learning ao longo das épocas (epochs), tanto para o conjunto de treinamento (linha azul) quanto para o conjunto de validação (linha vermelha).

### Observações sobre o gráfico:

1. **Perda no Conjunto de Treinamento (Training Loss):**
    - A perda no conjunto de treinamento (linha azul) está diminuindo de forma consistente, o que é um bom sinal, indicando que o modelo está aprendendo e melhorando sua capacidade de prever os dados de treinamento.
2. **Perda no Conjunto de Validação (Validation Loss):**
    - A perda no conjunto de validação (linha vermelha) inicialmente diminui, o que é esperado, mas depois começa a oscilar, com um pico significativo na 4ª época. Essa oscilação pode indicar que o modelo está começando a se ajustar demais aos dados de treinamento (overfitting), especialmente se a perda de validação começa a aumentar ou variar muito em relação à perda de treinamento.
    - No final, a perda de validação diminui um pouco, mas ainda há uma diferença considerável em relação à perda no treinamento.

### Análise:

- **Overfitting:** A oscilação e a divergência entre a perda de treinamento e a perda de validação indicam um possível overfitting. O modelo parece estar se ajustando demais aos dados de treinamento, o que pode comprometer sua capacidade de generalizar para novos dados.
- **Pico na Perda de Validação:** O pico na 4ª época pode sugerir que, nessa fase do treinamento, o modelo fez um ajuste inadequado ou encontrou dificuldades em generalizar para os dados de validação.
- **Sugestões:** Para mitigar o overfitting, você pode considerar:
    - Aumentar a quantidade de dados de treinamento.
    - Aplicar regularização (L1, L2).
    - Ajustar a arquitetura do modelo (por exemplo, adicionando dropout).
    - Usar técnicas de data augmentation se estiver trabalhando com dados de imagem.

Em resumo, o gráfico mostra um padrão típico de treinamento onde o modelo pode estar começando a superajustar os dados de treinamento em detrimento de sua capacidade de generalização.

![newplot (3).png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot_(3).png)

Já o gráfico acima mostra sobre a acurácia durante o treinamento do modelo.

Isso é sobre o modelo 1. 

# Visualização Gráfica do Modelo 2

![newplot (6).png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot_(6).png)

![newplot (7).png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot_(7).png)

# Matriz de Confusão

## Modelo 1

![newplot (8).png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot_(8).png)

## Modelo 2

![newplot (9).png](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot_(9).png)

# Conclusão

**Escolha dos Modelos:**

- **Modelo 1:** Utilizou três variáveis principais (consumo, localização e categoria) com o objetivo de testar a capacidade de identificação de fraudes com um modelo mais simples e de baixa complexidade computacional.
- **Modelo 2:** Incorporou um conjunto mais amplo de variáveis para capturar padrões mais complexos e melhorar a performance na detecção de fraudes.

**Análise de Resultados:**

- **Modelo 1:** Acurácia de 71%, F1-Score de 0,65, alta precisão (82%), mas baixo recall (54%). Isso indica que o modelo detecta bem as fraudes quando identificadas, mas deixa muitas fraudes passarem despercebidas.
- **Modelo 2:** Acurácia de 80%, F1-Score de 0,75, precisão de 82% e recall melhorado de 69%. Este modelo é mais eficaz na detecção de fraudes, reduzindo a quantidade de falsos negativos.

**Viabilidade para o Negócio:**

- O **Modelo 2** é mais adequado para o negócio da Aegea, pois oferece maior capacidade de detecção de fraudes, crucial para reduzir riscos financeiros e aumentar a confiabilidade.

**Possíveis Preocupações:**

- **Modelo 2**: Maior complexidade, podendo aumentar os requisitos computacionais e o risco de overfitting, além de dificultar a interpretação dos resultados e a explicação das decisões do modelo.

Em resumo, o Modelo 2 oferece melhor desempenho e é mais viável para o negócio, mas requer atenção em termos de complexidade e operabilidade.
