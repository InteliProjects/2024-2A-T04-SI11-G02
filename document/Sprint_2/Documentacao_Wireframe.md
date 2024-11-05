# Documentação Wireframe

# Seção 1 - Upload de Dados

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(5).png" alt="Logo da empresa" width="900"/>
</p>

Nessa primeira seção do wireframe, a interface possui os seguintes elementos principais:

1. **Título**:
    - "Aplicação de Modelo de Deep Learning para Detecção Avançada de Fraudes"
    - É um título destacado, centralizado no topo da interface.
2. **Descrição**:
    - Há um bloco de texto logo abaixo do título que parece ser um placeholder (Lorem ipsum) que deve ser substituído pela descrição real do modelo e sua construção.
3. **Seção de Upload de Dados**:
    - Abaixo da descrição, há uma área dedicada ao upload de dados.
    - Inclui um ícone de nuvem com uma seta apontando para cima, indicando o envio de dados.
    - Ao lado do ícone, há o texto "Upload de Dados".
    - À direita, há um botão rotulado como "Buscar arquivos", que provavelmente abrirá uma janela para o usuário selecionar os arquivos a serem carregados.
4. **Layout**:
    - O layout em si, possui uma estrutura simples e clara.
    - O uso do espaço é eficaz, mantendo o foco na função principal da tela, que é o upload de dados para o modelo.

É uma versão preliminar de uma página de interface que será usada em uma aplicação de machine learning focada na detecção de fraudes, oferecendo uma área para o upload de dados, o que sugere que a aplicação permitirá aos usuários enviar seus próprios dados para análise.

### 1.1 Funcionalidades

### **Upload de Dados**

A principal funcionalidade dessa interface parece ser o upload de dados. Os usuários podem carregar arquivos de dados que serão utilizados pelo modelo de Deep Learning para realizar a detecção de fraudes.

Há um botão de "Buscar arquivos" que permite ao usuário selecionar arquivos de seu dispositivo local. Pode suportar múltiplos formatos de arquivo, como CSV, Excel, JSON, entre outros. Além disso, haverá uma etapa de validação para garantir que os dados carregados estejam no formato correto e contenham as informações necessárias para a análise.

Após o upload, o sistema fornecerá um feedback, como uma barra de progresso ou uma mensagem de confirmação, para indicar que o upload foi bem-sucedido ou se houve algum erro.

**O uso do privacy by design nessa seção se dá pelo fato de:**

- Implementar validações rigorosas para garantir que apenas arquivos com formatos e estruturas apropriados sejam aceitos.
- Antes do lançamento, realizar uma análise de risco para identificar possíveis vulnerabilidades e tomar medidas corretivas para mitigá-las.
- Sempre que possível, os dados devem ser anonimizados ou minimizados para limitar a coleta de informações pessoais.
- A interface deve garantir que o upload de dados seja feito de forma segura. Isso inclui o uso de criptografia para proteger dados durante a transmissão e o armazenamento seguro desses dados
- Fornecer feedback claro e imediato ao usuário sobre o status do upload, incluindo mensagens de erro se o arquivo não for aceito

**e portanto a conclusão é:**

A implementação dos princípios de Privacy by Design na seção de upload de dados assegura que a privacidade e a segurança dos dados dos usuários são priorizadas e protegidas. A interface foi projetada para oferecer uma experiência de usuário segura e transparente, alinhada com as melhores práticas de proteção de dados.

# Seção 2 - Pré-Processamento de Dados

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(3).png" alt="Logo da empresa" width="900"/>
</p>

### **1. Cabeçalho**

- **Título:**
    - "Pré-Processamento de Dados" — Este é o título principal da página, destacando a fase do pipeline de dados que está sendo abordada.
- **Descrição:**
    - Abaixo do título, há um bloco de texto placeholder ("Lorem ipsum...") que será substituído por uma descrição real. Este espaço é destinado a explicar o propósito e as etapas envolvidas no pré-processamento de dados.

### 2.1 Seção de Tratamento de Nulos

- **Título de Seção:**
    - "Tratamento de Nulos" — Indica que essa área da interface está relacionada ao tratamento de valores nulos dentro do conjunto de dados.
- **Ícone de Expansão/Colapso:**
    - Um ícone de seta para cima ao lado do título de seção indica que essa seção pode ser expandida ou minimizada, permitindo que o usuário oculte ou exiba os detalhes dessa etapa específica.

### **3. Tabela de Dados**

- **Título da Tabela:**
    - "Tabela Com Primeira Etapa de Limpeza (tratamento de nulos)" — Indica que a tabela exibe os dados após a primeira etapa de limpeza, que se refere ao tratamento de valores nulos.
- **Descrição de Colunas:**

Abaixo do título, há uma descrição que lista as colunas incluídas na tabela. As colunas que requerem anonimização estão identificadas com a palavra "anonimizar". As colunas listadas são:

- EMP_CODIGO (anonimizar)
- REFERENCIA
- COD_GRUPO
- COD_SETOR_COMERCIAL
- NUM_QUADRA (anonimizar)
- COD_ROTA_LEITURA
- MATRICULA (anonimizar)
- ECO_RESIDENCIAL
- ECO_COMERCIAL
- ECO_INDUSTRIAL
- LTR_ATUAL
- DAT_LEITURA
- CONS_MEDIDO
- TIPO_LIGACAO
- CATEGORIA
- COD_LATITUDE (anonimizar)
- COD_LONGITUDE (anonimizar)
- **Área de Scroll:**
    - A tabela possui barras de rolagem à direita e abaixo, indicando que os dados podem ser extensos e requerem rolagem para visualização completa.

### **4. Botão para Anonimizar/Desanonimizar Dados**

- **Ícone de Olho:**
    - Ao lado da tabela, há um ícone de olho com um texto que indica a funcionalidade de "anonimizar/desanonimizar" dados sensíveis. Essa funcionalidade permite ao usuário aplicar ou remover anonimização das colunas indicadas.
- **Descrição da Funcionalidade:**
    - "Botão para anonimizar/desanonimizar dados sensíveis da tabela (destacados na lista de colunas por 'anonimizar')" — Explica que essa ferramenta permite ao usuário controlar a anonimização de colunas específicas destacadas na tabela.

**5. Descrição do Processo**

- **Caixa de Texto:**
    - Abaixo da tabela, há uma pequena caixa de texto com uma descrição placeholder ("Lorem ipsum..."). Este espaço é provavelmente destinado a fornecer uma breve explicação sobre essa etapa específica do pré-processamento de dados, descrevendo o output esperado e outros detalhes relevantes.

Nesse caso acima, aparece-se a tabela quando a flag de expandir seção é acionada.

Já na demonstração do wireframe abaixo, é possível visualizar a funcionalidade da flag sem a expansão, que mostra apenas o título do que aquela seção da tela representa. Logo, clicando na função de expandir, é possível ter a visualização dos processos referentes àquela seção.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(7).png" alt="Logo da empresa" width="900"/>
</p>

### 2.2 Seção de Filtro de Estabelecimentos

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(2).png" alt="Logo da empresa" width="900"/>
</p>


**Título de Seção:**

- "Filtro de Estabelecimentos" — Este título indica que a seção está relacionada ao filtro de dados por estabelecimentos específicos.

**Ícone de Expansão/Colapso:**

- Um ícone de seta para cima ao lado do título sugere que essa seção pode ser expandida ou minimizada, permitindo que o usuário oculte ou exiba os detalhes dessa etapa específica.

**Tabela de Dados (Segunda Etapa de Limpeza):**

- **Título da Tabela:**
    - "Tabela Com Segunda Etapa de Limpeza (Filtro de Estabelecimentos)" — Indica que a tabela exibe os dados após a segunda etapa de limpeza, focada no filtro de estabelecimentos.
- **Descrição de Colunas:**
    - A tabela apresenta as mesmas colunas listadas na primeira etapa de limpeza, com várias delas marcadas para anonimização:
        - EMP_CODIGO (anonimizar)
        - REFERENCIA
        - COD_GRUPO
        - COD_SETOR_COMERCIAL
        - NUM_QUADRA (anonimizar)
        - COD_ROTA_LEITURA
        - MATRICULA (anonimizar)
        - ECO_RESIDENCIAL
        - ECO_COMERCIAL
        - ECO_INDUSTRIAL
        - LTR_ATUAL
        - DAT_LEITURA
        - CONS_MEDIDO
        - TIPO_LIGACAO
        - CATEGORIA
        - COD_LATITUDE (anonimizar)
        - COD_LONGITUDE (anonimizar)
- **Área de Scroll:**
    - A tabela possui barras de rolagem à direita e abaixo, permitindo a navegação completa dos dados apresentados.

**Botão para Anonimizar/Desanonimizar Dados:**

- **Ícone de Olho:**
    - Ao lado da tabela, há um ícone de olho indicando a funcionalidade de anonimização/desanonimização de dados sensíveis. As colunas marcadas para anonimização podem ser ajustadas por meio desse botão.

**Descrição da Funcionalidade:**

- Um breve texto placeholder ("Lorem ipsum...") ao lado da tabela oferece espaço para uma descrição detalhada sobre o processo de filtro de estabelecimentos, explicando o que é feito nessa etapa e os resultados esperados.

### 2.3 Seção de Exclusão de Dados Repetidos

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(1).png" alt="Logo da empresa" width="900"/>
</p>

**Título de Seção:**

- "Exclusão de Dados Repetidos" — Esta seção aborda a remoção de dados duplicados ou repetidos no conjunto de dados.

**Ícone de Expansão/Colapso:**

- Um ícone de seta para cima ao lado do título sugere que essa seção também pode ser expandida ou minimizada.

**Tabela de Dados (Terceira Etapa de Limpeza):**

- **Título da Tabela:**
    - "Tabela Com Terceira Etapa de Limpeza (Exclusão de Dados Repetidos)" — Esta tabela exibe os dados após a terceira etapa de limpeza, focada na exclusão de dados repetidos.
- **Descrição de Colunas:**
    - As colunas apresentadas na tabela são idênticas às das etapas anteriores, com as mesmas marcações para anonimização.
- **Área de Scroll:**
    - A tabela inclui barras de rolagem, permitindo a visualização completa dos dados.

**Botão para Anonimizar/Desanonimizar Dados:**

- **Ícone de Olho:**
    - Assim como na seção anterior, há um ícone de olho para permitir a anonimização/desanonimização das colunas destacadas.

**Descrição da Funcionalidade:**

- Uma caixa de texto ao lado da tabela, com um placeholder ("Lorem ipsum..."), oferece um espaço para descrever o processo de exclusão de dados repetidos, os critérios utilizados, e os benefícios dessa etapa.

### 2.1.1 Funcionalidades

**Expandir/Minimizar Seções:**

- Os ícones de seta permitem ao usuário expandir ou minimizar seções da interface para gerenciar o espaço de trabalho de forma eficiente.

**Tratamento de Nulos:**

- Esta funcionalidade é responsável por identificar e tratar valores nulos no conjunto de dados, o que pode incluir a substituição por valores padrão, remoção de linhas/colunas ou outras técnicas de imputação.

**Anonimização/Desanonimização de Dados:**

- Essa funcionalidade permite ao usuário aplicar anonimização em colunas que contêm dados sensíveis, protegendo a privacidade dos indivíduos ou entidades mencionados nos dados.

**Navegação e Visualização de Dados:**

- A tabela com barras de rolagem sugere que os dados podem ser navegados e visualizados diretamente na interface, com a possibilidade de interagir com eles através de ferramentas como a anonimização.

**Descrição Contextual:**

- A caixa de texto e as descrições proporcionam ao usuário um entendimento claro de cada etapa do processo, aumentando a transparência e facilitando o uso da interface.

**O uso do privacy by design nessa seção se dá pelo fato de:**

- **Prevenção de Perda de Dados**: Implementar estratégias robustas para tratamento de valores nulos, como substituição por valores padrão ou técnicas de imputação.
- **Prevenção de Dados Irrelevantes**: Garantir que o filtro de estabelecimentos remova dados irrelevantes ou desnecessários, prevenindo a sobrecarga de dados que pode levar a problemas de privacidade.
- **Controle por Padrão**: As colunas identificadas para anonimização são protegidas por padrão. O usuário deve explicitamente optar por desanonimizar os dados, garantindo que a privacidade seja mantida sem necessidade de ações adicionais.
- **Interface Interativa**: A tabela com barras de rolagem permite uma navegação eficiente e a visualização completa dos dados, assegurando que os usuários possam interagir com os dados de forma controlada e transparente.
- **Caixas de Texto Descritivas**: As caixas de texto com placeholders são usadas para fornecer explicações detalhadas sobre cada etapa do pré-processamento, aumentando a transparência e permitindo que os usuários compreendam claramente o que está acontecendo com seus dados.

Logo, conclui-se que:

A Seção de Pré-Processamento de Dados foi projetada com os princípios de Privacy by Design em mente, assegurando que a privacidade e a segurança dos dados sejam prioritárias em cada etapa do processo. A interface foi cuidadosamente elaborada para fornecer controle e transparência, garantindo que os dados sejam manipulados de forma segura e eficiente.

# Seção 3 - Tela de Resultados de Desempenho do Modelo

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(6).png" alt="Logo da empresa" width="900"/>
</p>

A tela apresentada está relacionada à avaliação do desempenho de um modelo, contendo seções para a visualização de correlações entre variáveis e as métricas utilizadas para avaliar o modelo. Abaixo segue a descrição detalhada de cada elemento, etapa e funcionalidade presente na interface.

### **1. Título Principal**

- **"Resultados de Desempenho do Modelo"**
    - O título principal da tela indica que a interface é focada na análise dos resultados e no desempenho do modelo aplicado.

### **2. Descrição Geral**

- **Descrição Contextual (Placeholder):**
    - Abaixo do título, há um texto descritivo, que é um placeholder ("Lorem ipsum..."), indicando onde a explicação geral sobre a estruturação dos resultados do desempenho do modelo deve ser inserida. Essa descrição fornecerá contexto ao usuário sobre o que ele está visualizando e a importância dessa etapa.

### **3. Tabela de Correlação**

- **Título de Seção:**
    - "Tabela de Correlação" — Essa seção é dedicada à análise de correlação entre as variáveis.
- **Ícone de Expansão/Colapso:**
    - Um ícone de seta para cima ao lado do título sugere que essa seção pode ser expandida ou minimizada, permitindo que o usuário exiba ou oculte os detalhes da análise de correlação.
- **Descrição das Variáveis:**
    - **Colunas Para Serem Correlacionadas:**
        - "Colunas e Linhas Apresentadas na tabela (16) X (16)" — Essa parte indica que 16 variáveis foram consideradas para a análise de correlação.
    - **Lista de Variáveis:**
        - As variáveis incluídas na tabela de correlação são:
            - EMP_CODIGO
            - REFERENCIA
            - COD_GRUPO
            - COD_SETOR_COMERCIAL
            - NUM_QUADRA
            - COD_ROTA_LEITURA
            - MATRICULA
            - ECO_RESIDENCIAL
            - ECO_COMERCIAL
            - ECO_INDUSTRIAL
            - LTR_ATUAL
            - DAT_LEITURA
            - CONS_MEDIDO
            - TIPO_LIGACAO
            - CATEGORIA
            - COD_LATITUDE
            - COD_LONGITUDE
- **Botão para Visualização de Gráfico de Correlação:**
    - **Ícone de Olho com Interrogação:**
        - Ao lado da tabela, há um ícone com um olho e um ponto de interrogação, indicando que ao clicar, o usuário poderá obter mais detalhes sobre o gráfico de correlação e suas interpretações.
    - **Descrição do Gráfico (Placeholder):**
        - Um texto descritivo (placeholder "Lorem ipsum...") acompanha o botão de gráfico, onde serão inseridas informações sobre o tipo de gráfico gerado e os insights que ele pode proporcionar.

### **4. Métricas Avaliativas do Modelo**

- **Título de Seção:**
    - "Métricas Avaliativas do Modelo" — Essa seção é dedicada à apresentação e escolha das métricas para avaliação do modelo.
- **Ícone de Expansão/Colapso:**
    - Similar à seção anterior, há um ícone de seta para cima que permite expandir ou minimizar esta seção, proporcionando controle sobre a visualização das métricas.
- **Descrição das Métricas:**
    - **Métricas a Serem Utilizadas:**
        - "Accuracy, Precision, Recall, F1-Score, ROC-AUC, Log Loss, Balanced Accuracy, G-Mean" — Estas são as métricas listadas que serão utilizadas para avaliar o desempenho do modelo. Cada uma dessas métricas oferece uma perspectiva diferente sobre a performance do modelo, incluindo acurácia, equilíbrio entre precisão e sensibilidade, e desempenho em classes desbalanceadas.
- **Botão para Descrição das Métricas:**
    - **Ícone de Interrogação:**
        - Abaixo da lista de métricas, há um ícone de interrogação que sugere a presença de uma funcionalidade que fornece uma explicação detalhada de cada métrica.
    - **Descrição das Métricas (Placeholder):**
        - Um texto placeholder ("Lorem ipsum...") acompanha o ícone de interrogação, onde serão inseridas explicações detalhadas sobre cada métrica e como elas contribuem para a avaliação geral do modelo.

### **Documentação de Funcionalidades**

1. **Expandir/Minimizar Seções:**
    - Ambas as seções ("Tabela de Correlação" e "Métricas Avaliativas do Modelo") possuem ícones de seta para cima que permitem ao usuário expandir ou minimizar as seções para facilitar a navegação na tela.
2. **Tabela de Correlação:**
    - Essa seção mostra a análise de correlação entre 16 variáveis. As correlações podem ajudar a entender as relações entre diferentes variáveis no conjunto de dados, o que é crucial para a interpretação dos resultados do modelo.
3. **Métricas Avaliativas do Modelo:**
    - Essa seção apresenta as métricas que serão utilizadas para avaliar o desempenho do modelo. A presença de múltiplas métricas permite uma análise abrangente do desempenho, abordando diferentes aspectos, como precisão, recall, e desempenho em classes desbalanceadas.
4. **Botões de Informações Adicionais:**
    - Os ícones de interrogação e o olho com interrogação sugerem que há funcionalidades interativas para fornecer mais informações sobre o gráfico de correlação e as métricas utilizadas, permitindo que o usuário entenda melhor as ferramentas e análises que está utilizando.
5. **Descrição Contextual:**
    - Os textos placeholders indicam áreas onde serão inseridas descrições detalhadas e específicas para guiar o usuário através do processo de análise de desempenho, explicando o propósito e os resultados esperados de cada etapa.

Essa interface facilita a visualização e análise do desempenho do modelo, permitindo ao usuário explorar correlações entre variáveis e avaliar o modelo usando várias métricas, com suporte de informações detalhadas sobre cada elemento.

O privacy by design é implementado nessa seção por conta de:

- **Anonimização Padrão**: Durante a visualização da tabela de correlação, deve-se garantir que variáveis sensíveis sejam automaticamente anonimizadas ou substituídas por identificadores genéricos, a menos que o usuário opte explicitamente por visualizá-las em seu formato original, garantindo que a privacidade seja a configuração padrão.
- **Interação com Dados Sensíveis**: A interface deve permitir que o usuário interaja com as análises de desempenho e correlações de forma segura, incorporando mecanismos que ocultem ou minimizem a exposição de dados sensíveis
- **Transparência nas Métricas**: As descrições das métricas e os botões de informações adicionais devem fornecer detalhes claros sobre o que cada métrica avalia e como isso impacta a privacidade e segurança dos dados.
- **Confidencialidade das Análises**: Durante a análise de correlação e avaliação de métricas, os dados devem ser mantidos seguros. A interface deve garantir que todas as operações, incluindo a visualização de gráficos e métricas, sejam realizadas em um ambiente seguro, com medidas como criptografia para proteger dados sensíveis.

Logo, conclui-se que:

A Tela de Resultados de Desempenho do Modelo foi projetada com base nos princípios de Privacy by Design, garantindo que a privacidade dos dados seja protegida durante todo o processo de análise e visualização. A interface oferece uma experiência segura e transparente, permitindo que os usuários avaliem o desempenho do modelo sem comprometer a privacidade e a segurança dos dados.

# Seção 4 - Resultados Finais para Detecção de Fraudes

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(8).png" alt="Logo da empresa" width="900"/>
</p>

### **1. Título Principal:**

- **Texto:** "Resultados Finais para Detecção de Fraudes"**Anonimização Padrão**: Durante a visualização da tabela de correlação, deve-se garantir que variáveis sensíveis sejam automaticamente anonimizadas ou substituídas por identificadores genéricos, a menos que o usuário opte explicitamente por visualizá-las em seu formato original, garantindo que a privacidade seja a configuração padrão.
- **Descrição:** Indica que a página mostra os resultados finais de uma análise de detecção de fraudes.

### **2. Subtítulo:**

- **Texto:** "Principais Suspeitos de Fraude"
- **Descrição:** Introduz a seção que mostra os principais suspeitos de fraude identificados.

### **3. Seta de Expansão/Recolhimento:**

- **Descrição:** Uma seta apontando para cima, que provavelmente serve para expandir ou recolher a seção dos "Principais Suspeitos de Fraude".

### **4. Tabela Principal:**

- **Título:** "Tabela Com os Principais Suspeitos de Fraude"
- **Descrição:** Uma tabela que lista as principais colunas relacionadas à suspeita de fraude.
- **Colunas Listadas:**
    1. PROBABILIDADE_DE_FRAUDE
    2. EMP_CODIGO (anonomizar)
    3. REFERENCIA
    4. COD_GRUPO
    5. COD_SETOR_COMERCIAL
    6. NUM_QUADRA (anonimizar)
    7. COD_ROTA_LEITURA
    8. MATRICULA (anonimizar)
    9. ECO_RESIDENCIAL
    10. ECO_COMERCIAL
    11. ECO_INDUSTRIAL
    12. LTR_ATUAL
    13. DAT_LEITURA
    14. CONS_MEDIDO
    15. TIPO_LIGACAO
    16. CATEGORIA
    17. COD_LATITUDE (anonimizar)
    18. COD_LONGITUDE (anonimizar)
- **Função:** Exibe dados sobre os principais suspeitos de fraude, onde algumas colunas estão identificadas para anonimização.

### **5. Botão "Olho":**

- **Descrição:** Um ícone de olho, que possivelmente permite visualizar detalhes adicionais ou alternar a visualização de dados sensíveis.

### **6. Seção de Ajuda ou Informações:**

- **Título:** "Sobre esse output"
- **Descrição:** Um quadro que provavelmente oferece informações sobre os dados apresentados ou uma explicação do output da tabela.
- **Texto:** Contém texto de exemplo ("Lorem ipsum..."), indicando que este pode ser um espaço para descrever como os dados foram gerados ou interpretados.

### **7. Rodapé:**

- **Descrição:** Um rodapé simples sem muito conteúdo visível, mas que poderia ser usado para navegação ou informações adicionais em uma interface completa.

### **Funcionalidades Potenciais:**

- **Expansão/Recolhimento:** A seta pode permitir ao usuário expandir ou recolher a tabela de suspeitos.
- **Visualização Detalhada:** O ícone do olho pode ser um botão para visualizar informações adicionais ou alternar entre dados anonimizados e não anonimizados.
- **Ajuda/Informações:** A seção "Sobre esse output" pode ser clicável ou expansível para fornecer mais detalhes ou contexto.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(4).png" alt="Logo da empresa" width="900"/>
</p>

### **1. Seção: Distribuição de Fraudadores e Não Fraudadores**

- **Título:** "Distribuição de Fraudadores e Não Fraudadores"
- **Descrição:** Esta seção parece focar em exibir a distribuição de entidades identificadas como fraudadoras e não fraudadoras.
- **Seta de Expansão/Recolhimento:**
    - **Descrição:** Uma seta apontando para cima, permitindo que o usuário expanda ou recolha a seção.
- **Gráfico de Barras:**
    - **Título:** "Gráfico de Fraudadores e Não F."
    - **Descrição:** Um gráfico de barras simples mostrando a comparação entre fraudadores e não fraudadores.
    - **Função:** Este gráfico visualiza o número ou proporção de fraudadores em comparação aos não fraudadores.
- **Seção de Ajuda/Informações do Gráfico:**
    - **Título:** "Sobre o gráfico"
    - **Descrição:** Um ícone de interrogação que parece abrir uma seção de ajuda ou informação sobre o gráfico.
    - **Texto:** Contém texto de exemplo ("Lorem ipsum..."), indicando que é um espaço reservado para explicações sobre como o gráfico foi gerado e como interpretá-lo.

### **2. Seção: Número de Fraudadores Ao Longo do Período**

- **Título:** "Número de Fraudadores Ao Longo do Período"
- **Descrição:** Esta seção foca na análise do número de fraudadores ao longo de um determinado período.
- **Seta de Expansão/Recolhimento:**
    - **Descrição:** Uma seta apontando para cima, permitindo que o usuário expanda ou recolha a seção.
- **Gráfico de Série Temporal:**
    - **Descrição:** Um gráfico de linha que mostra a variação no número de fraudadores ao longo de um período de tempo.
    - **Texto:** "Gráfico de série de tempo para avaliar número e tendência de fraudes no período da base carregada."
    - **Função:** Este gráfico serve para analisar a tendência de fraudes ao longo do tempo, observando picos e quedas na atividade fraudulenta.
- **Seção de Ajuda/Informações do Gráfico:**
    - **Título:** "Sobre o gráfico"
    - **Descrição:** Um ícone de interrogação, semelhante ao da seção anterior, provavelmente oferecendo informações ou explicações sobre o gráfico de série temporal.
    - **Texto:** Contém texto de exemplo ("Lorem ipsum..."), similar ao anterior, reservado para explicações sobre a criação e interpretação do gráfico.

### **Funcionalidades Potenciais:**

- **Expansão/Recolhimento das Seções:** As setas permitem expandir ou recolher cada seção, dando ao usuário controle sobre o que visualizar.
- **Visualização e Análise Gráfica:** Os gráficos fornecem uma representação visual das análises, permitindo a interpretação rápida dos dados.
- **Ajuda e Explicações:** As seções de "Sobre o gráfico" parecem ser projetadas para fornecer aos usuários informações adicionais ou explicações sobre a interpretação dos gráficos.

Essa seção contém princípios de privacy by design pois:

- A Tabela Principal que lista os principais suspeitos de fraude inclui colunas que contêm informações sensíveis, como EMP_CODIGO, NUM_QUADRA, MATRICULA, COD_LATITUDE e COD_LONGITUDE. Essas colunas devem ser automaticamente anonimizadas ou substituídas por identificadores genéricos para evitar a exposição de informações pessoais identificáveis (PII). Essa precaução proativa minimiza os riscos de privacidade desde o início.
- A configuração padrão da tabela deve garantir que todas as informações sensíveis sejam exibidas de forma anonimizada.
- **Controles Visuais de Exposição**: O ícone de "Olho" na tabela principal permite alternar entre a visualização de dados anonimizados e não anonimizados. Esse design oferece ao usuário um controle intuitivo sobre a exposição de informações sensíveis, integrando a privacidade diretamente na funcionalidade de visualização de dados.
- **Explicações Claras e Seguras**: A seção "Sobre esse output" oferece uma oportunidade para explicar como os resultados foram gerados e como interpretar os dados.

# Seção 5 - Reporte do Modelo

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/tela1%20(9).png" alt="Logo da empresa" width="900"/>
</p>

A tela enviada parece ser uma seção de uma interface de usuário voltada para a ação de "reportar" um modelo de detecção de fraudes e a lista associada de possíveis fraudes detectadas. Vou documentar os elementos e funcionalidades:

### **1. Seção Principal: Reportar Modelo e Lista de Possíveis Fraudes Detectadas**

- **Texto:** "Reportar Modelo e Lista de Possíveis Fraudes Detectadas"
- **Descrição:** Esta seção permite que o usuário reporte um modelo específico e a lista de fraudes detectadas.
- **Botão "Reportar":**
    - **Descrição:** Um botão com um ícone de aviso (triângulo com exclamação) seguido pela palavra "Reportar".
    - **Função:** O botão é projetado para acionar a ação de reportar o modelo e as fraudes detectadas. Provavelmente, ao clicar, o sistema envia o modelo e os dados associados para uma análise posterior ou notificação.

### **2. Seção de Ajuda/Informações: Efeitos de Reportar**

- **Título:** "Efeitos de Reportar"
- **Descrição:** Esta seção parece fornecer informações sobre as consequências ou o impacto de reportar o modelo e a lista de fraudes.
- **Texto:** "Descrição breve sobre os efeitos de reportar o modelo e lista. Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
- **Ícones:**
    - **Interrogação:** Indicando que esta seção oferece informações ou ajuda.
    - **Aviso:** Um ícone de triângulo com um ponto de exclamação, sugerindo que a informação pode ser importante ou que há um alerta relacionado ao reporte.

### **Funcionalidades Potenciais:**

- **Ação de Reportar:** O botão "Reportar" é a principal funcionalidade, permitindo que o usuário envie o modelo e a lista de fraudes para revisão ou processamento.
- **Informações e Alertas:** A seção "Efeitos de Reportar" é projetada para informar o usuário sobre o que esperar ao realizar a ação de reportar, possivelmente abordando o impacto ou as etapas subsequentes.

PRIVACY BY DESIGN 

Aqui está uma tabela com os princípios do *Privacy by Design*:

| **Princípio** | **Descrição** |
| --- | --- |
| **Proativo e não reativo; preventivo e não corretivo** | A privacidade deve ser projetada de forma a prevenir problemas antes que eles ocorram, adotando uma abordagem preventiva e não corretiva. |
| **Privacidade como configuração padrão** | A proteção de dados pessoais deve ser automática, sendo a configuração padrão nos sistemas, sem exigir ação do usuário. |
| **Privacidade embutida no design** | A privacidade deve ser uma parte integral do design e da arquitetura dos sistemas desde o início. |
| **Funcionalidade completa – sem compensações** | A privacidade e a funcionalidade devem coexistir, sem a necessidade de sacrificar uma em detrimento da outra. |
| **Segurança de ponta a ponta – proteção ao longo do ciclo de vida** | A proteção de dados deve ser garantida durante todo o ciclo de vida dos dados, desde a coleta até a destruição. |
| **Visibilidade e transparência – manutenção da transparência** | As operações relacionadas aos dados pessoais devem ser transparentes, assegurando que todos os processos sejam claros para as partes interessadas. |
| **Respeito pela privacidade do usuário – centrado no usuário** | O design deve priorizar os interesses e a privacidade do usuário, oferecendo garantias fortes e opções de proteção de dados. |

A implementação dos princípios de Privacy by Design na seção de upload de dados assegura que a privacidade e a segurança dos dados dos usuários são priorizadas e protegidas. A interface foi projetada para oferecer uma experiência de usuário segura e transparente, alinhada com as melhores práticas de proteção de dados.
