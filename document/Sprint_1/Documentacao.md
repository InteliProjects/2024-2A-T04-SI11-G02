# Projeto Parceiro Empresa AEGEA - Modelo Preditivo

# Sumário

1. Introdução	

   1.1 Definição do Problema	

   1.2 Solução Proposta	

2. Persona

3. Antipersona

4. Jornada do Usuário

   4.1 Fases da Jornada

6. Canva Proposta de Valor

   5.1 Perfil do Cliente	

   5.2 Proposta de Valor	

6. Matriz de Risco	

7. Pré-processamento e Tratamento dos Dados	

   7.1 Introdução aos Dados	

   7.2 Limpeza dos dados	

   7.3 Tratamento dos dados

8. Análise Exploratória	

   8.1 Introdução aos Dados	

   8.2 Entendimento dos Dados

   8.3 Visualização dos dados

      8.3.1 Gráficos	

      8.3.1 Premissas	

   8.4 Conclusão

# 1. Introdução

Este documento apresenta uma análise dos desafios enfrentados pela empresa Aegea, as soluções propostas para esses desafios e o plano de ação delineado para alcançar os objetivos estabelecidos.

A fraude no consumo de água é um desafio crítico para empresas de saneamento básico, incluindo a Aegea Saneamento e Participações S.A., líder do setor privado no Brasil. Este problema afeta diretamente o faturamento, a arrecadação e a qualidade do serviço prestado, comprometendo a eficiência e a integridade da distribuição de água. A Aegea busca continuamente soluções inovadoras para mitigar esse desafio, melhorando suas operações e garantindo um serviço confiável à população.

O projeto desse módulo em si visa o desenvolvimento de um modelo de Machine Learning que permitirá à Aegea detectar e prevenir fraudes no consumo de água de forma mais assertiva e explicativa. Este documento apresenta a definição do problema, a solução proposta, e os benefícios esperados para a empresa.

## 1.1 Definição do Problema

As fraudes no consumo de água ocorrem quando consumidores manipulam os hidrômetros, realizam ligações clandestinas ou adotam outras práticas que reduzem ou eliminam os valores cobrados pelo consumo real.

Essas práticas fraudulentas não apenas resultam em perdas econômicas para a Aegea, mas também causam danos significativos à infraestrutura de distribuição, como danos a tubulação, resultando em vazamentos e perda de água, além de alterar a pressão na rede de distribuição; intermitência no abastecimento de água à população, comprometendo a continuidade do serviço; redução de receita devido à diminuição dos valores faturados; e aumento do risco de contaminação, pois métodos fraudulentos que não seguem padrões de segurança podem introduzir contaminantes na rede de abastecimento.

A Aegea já aplica diversas estratégias para combater esse problema, como a verificação de padrões de consumo e a atuação de agentes de campo especializados. No entanto, a identificação de fraudes ainda apresenta desafios que exigem soluções tecnológicas mais avançadas e assertivas, uma vez que o processo atual ocorre de forma manual.

## 1.2 Solução Proposta

O projeto propõe o desenvolvimento de um modelo preditivo de Machine Learning capaz de identificar e prever fraudes no consumo de água, utilizando dados históricos de consumo e incorporando variáveis exógenas, como indicadores macroeconômicos, climáticos e geográficos.

A solução proposta buscará melhorar a assertividade na detecção de fraudes, identificando padrões suspeitos com alta precisão e mínima incerteza, além de auxiliar na priorização de ações. Outro objetivo importante é garantir a explicabilidade dos resultados, ou seja, além de prever fraudes, o modelo deve fornecer insights sobre as variáveis e padrões que influenciam as fraudes, permitindo uma melhor compreensão do problema e suporte à tomada de decisões estratégicas.

Adicionalmente, a aplicação dos resultados do modelo deverá impactar diretamente as operações da empresa, aumentando a eficácia das equipes de campo e direcionando suas ações de maneira mais eficiente e assertiva.


# 2. Persona

A persona é uma ferramenta essencial na análise de negócios, usada para criar um perfil detalhado do cliente ideal. Este perfil representa as características, necessidades e comportamentos do público-alvo, permitindo que as estratégias de marketing, desenvolvimento de produtos e atendimento ao cliente sejam alinhadas para maximizar o valor entregue. A construção da persona ajuda a empresa a focar em suas ações de maneira mais eficaz, direcionando esforços para atrair e reter clientes que realmente se beneficiam dos produtos ou serviços oferecidos.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Persona1.jpg" alt="Logo da empresa" width="500"/>
</p>

Figura 1: Persona

Fonte: Autores

# 3. Antipersona

A antipersona é uma ferramenta complementar à persona, utilizada para identificar perfis de clientes que não agregam valor ao negócio. Este perfil descreve características e comportamentos de clientes que não são ideais, seja por não se alinharem com a proposta de valor da empresa ou por gerarem custos desproporcionais aos benefícios. A criação da antipersona permite à empresa evitar desperdício de recursos em estratégias que não são produtivas, melhorando a eficiência operacional e focando em públicos que realmente contribuem para o sucesso do negócio.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Antipersona1.jpg" alt="Logo da empresa" width="500"/>
</p>
Figura 2: Antipersona

Fonte: Autores

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Antipersona2.jpg" alt="Logo da empresa" width="500"/>
</p>
Figura 3: Antipersona

Fonte: Autores

# 4. Jornada do Usuário

A jornada do usuário é uma representação visual ou narrativa do caminho que um usuário percorre ao interagir com um produto, serviço ou sistema, a qual mapeia cada etapa da experiência do usuário, desde o primeiro contato até a conclusão da tarefa ou objetivo desejado. Esse processo inclui as ações que o usuário realiza, os pensamentos e emoções que ele experimenta, além dos pontos de contato com a marca ou produto.

Ao criar uma jornada do usuário, o objetivo é entender profundamente as necessidades, motivações e desafios enfrentados pelo usuário em cada fase da interação, o que permite que as equipes de design, desenvolvimento e negócios possam identificar pontos de melhoria, antecipar problemas e criar soluções que realmente atendam às expectativas dos usuários.

A jornada do usuário é uma ferramenta utilizada para alinhar as estratégias de design centrado no usuário, uma vez que ela coloca o foco nas experiências e percepções reais dos usuários, promovendo uma abordagem mais empática e eficiente no desenvolvimento de produtos e serviços.

![Jornada](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Jornada_do_Usuario.jpg)

Figura 4: Jornada do Usuário
Fonte: Autores

### **Persona: João Martins**

**Cenário**:

João Martins é um funcionário da Aegea, uma empresa de saneamento, e trabalha diretamente com a detecção de fraudes no consumo de água. Ele busca uma solução eficaz para identificar irregularidades e possíveis fraudes antes que elas ocorram, melhorando a eficiência e a justiça nas cobranças de água.

**Expectativas de João**:

1. Obter uma visão clara e abrangente das áreas com possíveis fraudes, evitando preconceitos ou vieses.
2. Ter acesso a dados confiáveis e seguros, que não possam ser manipulados ou interpretados incorretamente.


## 4.1 Fases da Jornada

### **Fase 1: Suspeita de Fraudes em uma Região**

1. **Identificação de Irregularidades**:
    
    João percebe uma discrepância nas cobranças de água em uma determinada região, o que levanta suspeitas.
    
2. **Investigação Inicial**:
    
    Ele investiga as possíveis causas dessa irregularidade, analisando os dados disponíveis e verificando outras fontes.
    
3. **Hipótese de Fraude**:
    
    Incapaz de encontrar uma explicação direta, João começa a suspeitar que a irregularidade possa estar relacionada a uma fraude.
    

**Citação de João**:

*"Há algumas injustiças na cobrança de água! Estou com uma falta de clareza sobre o consumo de água."*

### **Fase 2: Pesquisa e Planejamento**

1. **Busca por Soluções**:
    
    João pesquisa e explora diferentes ferramentas e metodologias que possam ajudá-lo a melhorar o processo de detecção de fraudes.
    
2. **Análise de Dados**:
    
    Ele revisa planilhas históricas, consulta especialistas e examina padrões de consumo de água para identificar possíveis anomalias.
    
3. **Desafios na Compreensão**:
    
    João enfrenta dificuldades para entender os comportamentos suspeitos e manter a infraestrutura de dados adequada para essas análises.
    

**Citação de João**:

*"Que perda de tempo! Vou utilizar um sistema mais eficiente."*

### **Fase 3: Uso da Aplicação (Modelo de Machine Learning)**

1. **Análise de Dados com a Aplicação**:
    
    João acessa uma aplicação específica que utiliza machine learning para rodar análises detalhadas dos dados de consumo de água.
    
2. **Ajustes e Testes**:
    
    Ele ajusta os parâmetros do modelo e testa novas variáveis que possam influenciar a detecção de fraudes, buscando sempre refinar os resultados.
    

**Citação de João**:

*"Tudo pronto, agora consigo fazer a análise."*

### **Fase 4: Análise e Interpretações**

1. **Interpretação das Previsões**:
    
    João utiliza a aplicação para entender as causas por trás das previsões de fraude, buscando explicações claras que possam ser compartilhadas com sua equipe.
    
2. **Geração de Insights**:
    
    Ele procura insights que possam ser úteis para gestores e equipes de campo, facilitando a tomada de decisões informadas.
    
3. **Obtenção de Evidências**:
    
    Com base nas análises, João identifica evidências que indicam uma possível fraude em uma localidade específica, relacionada a uma matrícula específica.
    

**Citação de João**:

*"Agora sim eu consigo embasar minhas hipóteses, vou encaminhar para o time responsável!"*

### **Fase 5: Comunicação e Chamado para Ação**

1. **Compartilhamento de Resultados**:
    
    João apresenta suas descobertas para outras equipes da Aegea, incluindo TI, análise de dados e fiscalização.
    
2. **Alinhamento e Feedback**:
    
    Ele trabalha para alinhar o entendimento dos resultados entre todas as partes envolvidas, garantindo que todos estejam na mesma página.
    
3. **Ação Preventiva**:
    
    Com base nas evidências coletadas, João ajuda a coordenar as ações preventivas para mitigar a ocorrência de fraudes futuras.
    

**Citação de João**:

*"Meu trabalho aqui foi feito, vou procurar outras fraudes!"*

### **Oportunidades Identificadas com a solução**

- **Automatização de Análises**: facilitação na detecção de comportamentos fraudulentos através de processos automatizados.
- **Identificação de Regiões Suspeitas**: melhor precisão na identificação de áreas de risco a partir do modelo.
- **Dashboard Personalizado**: dashboards adaptados para suportar decisões mais informadas e eficazes.
- **Colaboração entre Equipes**: facilitação na colaboração e no compartilhamento de informações entre diferentes equipes.
- **Maior Embasamento com Dados**: base de dados sólida e confiável para suportar as decisões e ações das equipes.


# 5. Canva Proposta de Valor

O Canvas de Proposta de Valor é uma ferramenta que ajuda as empresas a delinear claramente como seus produtos e serviços criam valor para os clientes. Ele é parte fundamental do modelo de negócios, focado em identificar e alinhar os benefícios que a empresa oferece (proposta de valor) com as necessidades e desejos dos clientes (perfil do cliente).

O canvas é dividido em duas partes principais:

- **Proposta de Valor**: Onde a empresa define os produtos e serviços que entrega, os ganhos que proporciona ao cliente e como alivia suas dores.
- **Perfil do Cliente**: Que descreve as tarefas que o cliente precisa realizar, os ganhos que ele busca e as dores que enfrenta.

![Canva](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Canva_Proposta_de_Valor.jpg)
Figura 5: Canva Proposta de Valor

Fonte: Autores

## 5.1 Perfil do Cliente

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Perfil_do_Cliente.jpg" alt="Logo da empresa" width="500"/>
</p>
Figura 6: Canva Proposta de Valor - Perfil do Cliente

Fonte: Autores

### **Tarefas do Cliente**

- **Monitorar consumo de água**:
    - O cliente precisa constantemente monitorar o consumo de água para garantir que esteja dentro dos padrões esperados e para identificar qualquer anomalia que possa indicar fraude.
- **Detectar e corrigir fraudes de forma manual**:
    - Antes da implementação de sistemas automatizados, a detecção e correção de fraudes eram feitas manualmente, o que é um processo trabalhoso e menos eficiente.
- **Implementar melhorias contínuas na detecção de fraudes**:
    - O cliente busca constantemente melhorar os métodos de detecção de fraudes para garantir que a rede de distribuição opere de forma eficiente e segura.
- **Garantir qualidade e continuidade do abastecimento**:
    - Um dos principais objetivos do cliente é garantir que a água fornecida seja de alta qualidade e que o abastecimento seja contínuo, sem interrupções devido a fraudes ou problemas na rede.

### **Dores**

- **Perda de receita por fraudes**:
    - As fraudes no consumo de água resultam em perda significativa de receita, afetando diretamente a lucratividade da empresa.
- **Dificuldade na detecção precisa de fraudes**:
    - A detecção manual de fraudes é complexa e suscetível a erros, resultando em dificuldades para identificar todas as ocorrências de fraude com precisão.
- **Danos à infraestrutura por ligações clandestinas e perdas de água**:
    - As fraudes também causam danos à infraestrutura, como vazamentos e contaminação, além de resultarem em perdas de água que comprometem o fornecimento.
- **Intermitência no abastecimento de água à população**:
    - Fraudes e problemas na rede de distribuição podem causar interrupções no abastecimento, afetando a confiança dos consumidores na empresa.
- **Risco de contaminação e na qualidade da água devido às fraudes**:
    - As ligações clandestinas e outros tipos de fraude podem levar à contaminação da rede de água, comprometendo a qualidade da água distribuída.

### **Ganhos**

- **Melhoria na qualidade do abastecimento**:
    - A redução de fraudes e a detecção proativa de problemas contribuem para um abastecimento de água mais confiável e de alta qualidade.
- **Aumento da precisão na detecção de fraudes**:
    - Com sistemas automatizados e modelos avançados de Machine Learning, a precisão na identificação de fraudes aumenta, reduzindo a quantidade de falsos positivos e negativos.
- **Capacidade de antecipar e mitigar riscos de fraudes**:
    - O uso de modelos preditivos permite que a empresa se antecipe a possíveis fraudes, mitigando riscos antes que causem impactos significativos.
- **Dados precisos para análise de consumo**:
    - A disponibilidade de dados precisos facilita a análise detalhada do consumo, permitindo uma melhor gestão dos recursos e a identificação de padrões de consumo anômalos.
- **Conformidade com regulamentações**:
    - A detecção eficiente de fraudes garante que a empresa opere em conformidade com regulamentações, evitando penalidades e assegurando o cumprimento das normas.
- **Infraestrutura preservada**:
    - A detecção e correção rápida de fraudes ajudam a preservar a infraestrutura da rede de distribuição de água, evitando danos que poderiam resultar em interrupções ou contaminações.
- **Redução de custos operacionais**:
    - A automação e precisão na detecção de fraudes contribuem para a redução dos custos operacionais, eliminando a necessidade de inspeções manuais frequentes e reduzindo as perdas associadas a fraudes.

## 5.2 Proposta de Valor

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Proposta_de_Valor.jpg" alt="Logo da empresa" width="500"/>
</p>
Figura 7: Canva Proposta de Valor - Proposta de Valor

Fonte: Autores

**Proposta de Valor**

- **Sistema de detecção de fraudes com Deep Learning:**
- Utilização de técnicas avançadas de deep learning para identificar padrões de fraude no consumo de água. Esse sistema automatizado permite detectar anomalias no consumo que indicam possíveis fraudes, reduzindo a necessidade de inspeções manuais e melhorando a precisão na detecção.
- **Análise e visualizações precisas e detalhadas de consumo e fraudes**:
- Ferramentas que permitem analisar detalhadamente os padrões de consumo de água, oferecendo visualizações claras e precisas que ajudam a identificar inconsistências e padrões suspeitos de fraude.
- **Automação da detecção de fraudes com alta precisão**:
    - A automação do processo de detecção permite maior precisão e consistência na identificação de fraudes, minimizando erros humanos e garantindo que padrões suspeitos sejam identificados em tempo hábil.
- **Modelo de ML identifica padrões suspeitos de fraudes**:
    - Um modelo de Machine Learning treinado para reconhecer padrões de comportamento que são indicativos de fraude, permitindo a detecção proativa e a tomada de ações preventivas.
- **Relatórios detalhados para melhor embasamento de decisões**:
    - Geração de relatórios que consolidam as análises de fraudes e padrões de consumo, proporcionando informações valiosas para a tomada de decisões estratégicas e operacionais.

### **Alívio das Dores**

- **Monitoramento contínuo que evita vazamentos e interrupções**:
    - A capacidade de monitorar o consumo de água continuamente permite identificar e corrigir problemas antes que se tornem críticos, evitando vazamentos e interrupções no fornecimento.
- **Predição de fraudes para minimização de danos**:
    - Com a predição de fraudes, é possível agir de forma preventiva, minimizando os danos financeiros e operacionais que uma fraude poderia causar.
- **Ações preventivas minimizam o risco de contaminação na rede de distribuição**:
    - A detecção proativa de fraudes e a correção de anomalias ajudam a evitar a contaminação da rede de distribuição, garantindo a qualidade da água fornecida.
- **Relatórios detalhados para melhor embasamento de decisões**:
    - Os relatórios detalhados fornecem informações essenciais para a tomada de decisões estratégicas, ajudando as equipes a planejar ações corretivas e preventivas de maneira mais eficaz.
- **Automatização da detecção de fraudes com alta precisão**:
    - A automação reduz o erro humano e garante que fraudes sejam identificadas com maior precisão, minimizando as perdas e evitando danos maiores à infraestrutura e à receita da empresa.

### **Criadores de Ganho**

- **Automatização reduz inspeções manuais e custos**:
    - A implementação do sistema de detecção automatizado reduz a necessidade de inspeções manuais, o que, por sua vez, diminui os custos operacionais associados a essas atividades.
- **Tomada de decisão mais informada e estratégica**:
    - Com dados precisos e detalhados, as equipes podem tomar decisões mais bem informadas e alinhadas com a estratégia da empresa, melhorando a eficácia das ações contra fraudes.
- **Ferramentas de visualização de dados**:
    - Oferecem uma visão clara e compreensível dos dados, permitindo que as equipes de análise e operação identifiquem rapidamente padrões anômalos e tomem decisões baseadas em dados.
- **Melhor entendimento dos fatores que influenciam fraudes**:
    - Com a análise detalhada, é possível identificar e compreender melhor os fatores que contribuem para as fraudes, permitindo que medidas preventivas sejam tomadas de forma mais eficaz.
- **Melhoria na coordenação entre equipes técnicas e de campo**:
    - Através de relatórios e análises detalhadas, as equipes técnicas e de campo podem alinhar suas atividades, garantindo que as ações sejam coordenadas e eficazes na mitigação de fraudes.

# 6. Matriz de Risco

É uma das principais ferramentas na análise de negócios, utilizada para o gerenciamento de riscos operacionais existentes na empresa. A figura ilustra a construção da matriz de risco para o projeto.

## 6.1 Matriz de Risco - Projeto

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Matriz_de_Risco_Projeto.jpg" alt="" width="1500"/>
</p>
Figura 8: Distribuição dos riscos e oportunidades na matriz - projeto

Fonte: Autores

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Riscos_Projeto.jpg" alt="" width="750"/>
</p>
Figura 9: Distribuição dos riscos na matriz - projeto

Fonte: Autores

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Oportunidades_Projeto.jpg" alt="" width="750"/>
</p>
Figura 10: Distribuição das oportunidades na matriz - projeto

Fonte: Autores

## 6.2 Matriz de Risco - Grupo

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Matriz_de_Risco_Grupo.jpg" alt="" width="1500"/>
</p>
Figura 11: Distribuição dos riscos e oportunidades na matriz - grupo

Fonte: Autores

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Riscos_Grupojpg.jpg" alt="" width="750"/>
</p>
Figura 12: Distribuição dos riscos na matriz - grupo

Fonte: Autores

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/Oportunidades_Grupo.jpg" alt="" width="750"/>
</p>
Figura 13: Distribuição das oportunidades na matriz - grupo

Fonte: Autores

## 6.3 Plano de Ação

Apresenta-se abaixo a descrição dos riscos e oportunidades identificados para o projeto:

| Risco 01 | Incapacidade de identificar padrões de fraude corretamente |
| --- | --- |
| Descrição | Este risco refere-se à possibilidade do modelo de Machine Learning (ML) não conseguir identificar corretamente padrões de consumo fraudulentos, resultando em falhas na detecção de fraudes ou em falsos positivos, o que pode ocorrer devido a uma variedade de fatores, como a escolha inadequada de variáveis, técnicas de modelagem ineficiente, ou um treinamento insuficiente do modelo devido à baixa qualidade dos dados. |
| Probabilidade | 30% |
| Impacto | Muito alto |
| Justificativa | Este risco é considerado muito alto porque a principal finalidade do projeto é precisamente identificar fraudes no consumo de água. Se o modelo não conseguir cumprir essa função com precisão, toda a eficácia do projeto fica comprometida. A incapacidade de detectar fraudes corretamente pode levar a grandes perdas financeiras para a Aegea, além de comprometer a confiança dos stakeholders e dos clientes na solução proposta. Além disso, falsos positivos podem resultar em ações injustas contra consumidores que não estão cometendo fraudes, o que pode gerar repercussões legais e prejudicar a reputação da empresa. |
| Plano de Ação | Como equipe de projeto responsável pelo desenvolvimento do modelo de previsão de fraudes no consumo de água para a Aegea, devemos focar inicialmente em realizar uma análise minuciosa das variáveis disponíveis, identificando aquelas que são mais relevantes para a detecção de fraudes. Em seguida, é essencial treinar o modelo utilizando dados rotulados de alta qualidade, garantindo que ele aprenda padrões de comportamento tanto normais quanto fraudulentos. Implementaremos uma validação cruzada rigorosa e testes do modelo em diferentes cenários. Além disso, adotaremos um ciclo iterativo de aprimoramento, revisando continuamente o desempenho do modelo e incorporando feedback de testes e dos stakeholders. Monitoraremos o modelo em tempo real para ajustes rápidos e criaremos cenários simulados de fraudes para avaliar e melhorar a aplicabilidade do modelo antes de sua implementação final. |
| Responsável | Larissa e Izabella |

| Risco 02 | Falta de testes e validações adequadas dos modelos |
| --- | --- |
| Descrição | Este risco envolve a possibilidade de que os modelos de Machine Learning (ML) desenvolvidos não passem por um processo adequado de testes e validações, o que pode resultar em falhas significativas na sua precisão e confiabilidade. Sem validações rigorosas, o modelo pode apresentar erros, como overfitting ou underfitting, e não generalizar bem para novos dados, comprometendo a sua capacidade de identificar fraudes de maneira consistente. |
| Probabilidade | 30% |
| Impacto | Muito alto |
| Justificativa | Este risco é considerado muito alto porque testes e validações adequadas são fundamentais para garantir que o modelo funcione corretamente em ambientes de produção. A ausência de testes robustos pode levar à implementação de um modelo que não detecta fraudes de forma eficaz, resultando em grandes perdas financeiras, além de colocar em risco a reputação da Aegea. Além disso, falhas no modelo podem gerar custos adicionais com retrabalho e correções, aumentando o tempo e os recursos necessários para alcançar os objetivos do projeto. |
| Plano de Ação | Como equipe de projeto, devemos assegurar que todos os modelos de Machine Learning desenvolvidos passem por um rigoroso processo de testes e validações, o que inclui a aplicação de validação cruzada em múltiplos subconjuntos de dados, além de testar o modelo em diferentes cenários e conjuntos de dados externos para avaliar sua capacidade de generalização. Devemos também implementar um ciclo contínuo de revisão e ajustes com base nos resultados dos testes, garantindo que o modelo seja refinado e otimizado. Além disso, é importante documentar detalhadamente todos os processos de teste e validação para garantir a rastreabilidade e facilitar futuras melhorias. |
| Responsável | Lucas e João |

| Risco 03 | Alterações no escopo do projeto durante o desenvolvimento |
| --- | --- |
| Descrição | A possibilidade de receber informações extras que sejam necessárias  no desenvolvimento do projeto próximo à entrega ao cliente do que foi produzido na sprint, implica que a equipe pode não ter tempo suficiente para analisar, compreender e integrar adequadamente essas informações no produto final, o que pode resultar em atrasos, erros ou entregas incompletas. |
| Probabilidade | 30% |
| Impacto | Moderado |
| Justificativa | É importante ter acesso às informações para o desenvolvimento com tempo suficiente para uma análise completa e uma integração adequada. Além disso, o escopo já foi estabelecido no tapi e toda a organização de tarefas e priorização realizada pelo grupo foi com base no que foi solicitado e abordado no workshop com o parceiro. Receber a informação de que precisa-se ter mais elementos no projeto e funcionalidades pode comprometer a qualidade do trabalho realizado pela equipe, afetando a satisfação do cliente e potencialmente prejudicando o projeto. |
| Plano de Ação | Será estabelecido um processo de comunicação claro e regular com os stakeholders para enfatizar a importância de fornecer informações dentro dos prazos estabelecidos. Durante o planejamento de cada sprint, a equipe definirá claramente os pré-requisitos de informação e dados necessários, garantindo que todas as partes envolvidas estejam cientes e comprometidas com esses requisitos desde o início. |
| Responsável | Eric e Gabriel |

| Risco 04 | Problemas de desempenho no modelo de Machine Learning |
| --- | --- |
| Descrição | Este risco refere-se à possibilidade de que o modelo de Machine Learning (ML) desenvolvido apresente problemas de desempenho, como tempos de processamento excessivamente longos, consumo elevado de recursos computacionais, ou baixa escalabilidade. Esses problemas podem comprometer a eficiência do modelo em ambientes de produção, dificultando sua integração com sistemas operacionais existentes e afetando negativamente a experiência dos usuários finais. |
| Probabilidade | 50% |
| Impacto | Alto |
| Justificativa | Este risco é considerado alto porque problemas de desempenho podem limitar a aplicabilidade do modelo na detecção de fraudes em tempo real, o que é importante para a Aegea, dado o volume de dados e a necessidade de respostas rápidas. Se o modelo não for eficiente, ele pode se tornar inviável para uso em larga escala, exigindo recursos adicionais para correções e otimizações, além de potencialmente atrasar o cronograma do projeto. Isso não apenas aumentaria os custos operacionais, mas também comprometeria a confiança dos stakeholders no valor do projeto. |
| Plano de Ação | Para mitigar este risco, nossa equipe de projeto deve focar na otimização contínua do desempenho do modelo durante o desenvolvimento. Isso inclui selecionar algoritmos de ML que sejam eficientes em termos de recursos e garantir que o modelo seja escalável. Implementaremos técnicas de otimização de código e uso eficiente de recursos computacionais, como ajustes de hiperparâmetros. Além disso, devemos monitorar o desempenho do modelo durante os testes, com planos de contingência para ajustes rápidos se necessário. |
| Responsável | Larissa e Izabella |

| Risco 05 | Ausência não prevista de um membro do grupo |
| --- | --- |
| Descrição | A possibilidade de uma ausência não prevista de um membro do grupo pode ocorrer devido a razões como doença, emergência familiar ou qualquer outra eventualidade que impeça o membro de participar das atividades do projeto. |
| Probabilidade | 10% |
| Impacto | Moderado |
| Justificativa | Uma ausência não prevista pode impactar negativamente o cronograma do projeto, resultando em atrasos nas entregas e possíveis sobrecargas para os outros membros da equipe, especialmente considerando que já estamos operando com uma equipe reduzida em comparação com o padrão da turma. |
| Plano de Ação | Estabeleceremos uma rotacionalidade de papéis ao longo das sprints para todos os membros da equipe, o que garantirá que, em caso de ausência de um membro, outros possam assumir suas responsabilidades temporariamente, mantendo o fluxo de trabalho e evitando atrasos nas entregas. Além disso, criaremos e manteremos uma documentação detalhada dos processos-chave, procedimentos e informações críticas do projeto. |
| Responsável | Lucas e João |

| Risco 06 | Pouca experiência em Machine Learning na equipe |
| --- | --- |
| Descrição | Este risco refere-se à possibilidade de que a equipe envolvida no desenvolvimento do modelo tenha pouca experiência prática com técnicas de Machine Learning (ML), o que pode levar a escolhas inadequadas de algoritmos, dificuldades na preparação dos dados, erros na interpretação dos resultados, e uma curva de aprendizado mais longa, comprometendo a qualidade e a eficácia do modelo. |
| Probabilidade | 30% |
| Impacto | Alto |
| Justificativa | O sucesso do projeto depende diretamente da aplicação correta de técnicas de ML. A falta de experiência pode resultar em um modelo que não atinge os objetivos propostos, com erros que poderiam ser evitados por uma equipe mais experiente. Além disso, pode haver necessidade de retrabalho, prolongando o cronograma do projeto e aumentando os custos. |
| Plano de Ação | Promover trocas de conhecimento dentro da equipe, em que os membros com mais experiência possam compartilhar suas habilidades com os demais. Além disso, é essencial definir marcos de revisão periódica para avaliar o progresso técnico e ajustar o plano de ação conforme necessário, garantindo que a equipe adquira a competência necessária para superar os desafios do projeto. |
| Responsável | Eric e Gabriel |

| Risco 07 | Ausência de dados para executar os objetivos desejados pelo cliente |
| --- | --- |
| Descrição | A possibilidade de ausência de dados necessários para executar os objetivos desejados pelo cliente, pode ocorrer devido a fatores, como falta de acesso aos dados, dados incompletos ou inadequados para as necessidades do projeto. |
| Probabilidade | 30% |
| Impacto | Alto |
| Justificativa | A ausência de dados essenciais pode comprometer diretamente a capacidade da equipe de atender às expectativas do cliente e alcançar os objetivos estabelecidos para o projeto. Sem os dados corretos, a tomada de decisão pode ser prejudicada e as soluções propostas podem não atender às necessidades reais do cliente. |
| Plano de Ação | Avaliaremos a disponibilidade atual de dados e identificaremos lacunas ou áreas onde os dados podem estar ausentes ou incompletos. Isso nos permitirá concentrar nossos esforços na aquisição dos dados necessários para preencher essas lacunas. |
| Responsável | Larissa e Izabella |

| Risco 08 | Dificuldades na interpretação e visualização dos dados |
| --- | --- |
| Descrição | Este risco refere-se à possibilidade de que a equipe enfrente dificuldades na interpretação correta dos dados brutos e na criação de visualizações claras e significativas. A má interpretação ou visualização inadequada dos dados pode levar a análises imprecisas, decisões erradas e uma compreensão limitada dos padrões e insights que o modelo de Machine Learning (ML) deve identificar. |
| Probabilidade | 10% |
| Impacto | Alto |
| Justificativa | Erros na interpretação dos dados podem comprometer a fase de treinamento do modelo, levando a resultados imprecisos e a uma incapacidade de detectar fraudes com precisão. Visualizações inadequadas também dificultam a comunicação dos resultados e insights para os stakeholders, tornando mais difícil justificar decisões ou ajustes no modelo. Isso pode resultar em retrabalho, aumento de custos e perda de confiança no projeto. |
| Plano de Ação | Para mitigar este risco, nossa equipe utilizará ferramentas avançadas de visualização de dados, como d3.js, ou Python com bibliotecas como Matplotlib e Seaborn, que facilitem a criação de gráficos claros e intuitivos. Além disso, realizaremos revisões regulares das análises de dados e visualizações em equipe, garantindo que as interpretações sejam precisas e alinhadas com os objetivos do projeto. Trazer os insights para as apresentações com stakeholder para coleta de feedbacks e para validação das abordagens e conclusões também é uma ação estratégica, garantindo a qualidade e a relevância das interpretações. |
| Responsável | Lucas e João |

| Risco 09 | Problemas de comunicação entre os membros da equipe |
| --- | --- |
| Descrição | Este risco refere-se à possibilidade de que falhas na comunicação entre os membros da equipe de projeto resultem em mal-entendidos, informações perdidas ou incompletas, e desalinhamento das atividades. A comunicação ineficaz pode levar a atrasos, duplicação de esforços, falhas na coordenação das tarefas e, em última instância, comprometer a qualidade e os prazos do projeto. |
| Probabilidade | 10% |
| Impacto | Moderado |
| Justificativa | Problemas de comunicação podem causar confusões, impedir a resolução rápida de problemas, e dificultar a tomada de decisões, o que pode impactar negativamente o andamento do projeto e sua entrega dentro do prazo. Além disso, a falta de comunicação pode gerar conflitos internos e desmotivação entre os membros da equipe. |
| Plano de Ação | Implementar estratégias de comunicação e resolução de conflitos, como reuniões regulares (Dailys e Retrospective) para discussão aberta de questões sobre o desempenho e atividade de cada membro da equipe, além disso, mediação pelo orientador em casos de conflito. |
| Responsável | Eric e Gabriel |

| Risco 10 | Problemas na gestão do backlog e priorização de tarefas |
| --- | --- |
| Descrição | Este risco envolve a possibilidade de que a equipe enfrente dificuldades na gestão eficiente do backlog e na priorização adequada das tarefas, o que pode resultar em atrasos, tarefas importantes não sendo atendidas no tempo certo, e um desalinhamento em relação aos objetivos do projeto. Mesmo com o uso de ferramentas como o Monday e a realização de reuniões diárias (dailys), a má gestão do backlog pode levar a uma alocação ineficiente de recursos e comprometer o andamento do projeto. |
| Probabilidade | 30% |
| Impacto | Moderado |
| Justificativa | A priorização correta das tarefas é importante para garantir que os elementos mais críticos do projeto sejam abordados primeiro, mantendo o projeto dentro do cronograma e dentro do escopo planejado. Problemas na gestão do backlog podem causar sobrecarga de trabalho, confusão sobre as responsabilidades, e potencialmente levar ao fracasso na entrega de funcionalidades essenciais. A falta de priorização pode também resultar em retrabalho e desmotivação da equipe, impactando negativamente a qualidade do produto final. |
| Plano de Ação | Para mitigar este risco, nossa equipe deve reforçar as práticas de gestão do backlog utilizando o Monday de forma mais estratégica, estabelecendo critérios claros para a priorização de tarefas, como impacto no projeto, urgência e dependências. Durante as reuniões diárias (dailys), é importante revisar e ajustar as prioridades conforme necessário, garantindo que todos os membros da equipe estejam alinhados com os objetivos do projeto. Além disso, devemos designar um membro da equipe como responsável pela gestão do backlog, assegurando que as tarefas sejam organizadas e priorizadas corretamente (PO). A realização de retrospectivas regulares também pode ajudar a identificar e corrigir problemas de gestão de backlog antes que eles afetem o progresso do projeto. |
| Responsável | Larissa e Izabella |

| Risco 11 | Dificuldade em encontrar e integrar novas fontes de dados |
| --- | --- |
| Descrição | A equipe pode encontrar dificuldades em localizar e integrar novas fontes de dados que possam ser relevantes para melhorar a detecção de fraudes no consumo de água. A falta de dados adicionais ou a dificuldade em integrar fontes externas podem limitar a capacidade do modelo de Machine Learning (ML) de identificar padrões complexos e anômalos, afetando a precisão e a eficácia do projeto. |
| Probabilidade | 70% |
| Impacto | Alto |
| Justificativa | A integração de dados é fundamental para criar um modelo robusto e abrangente. Dados adicionais podem fornecer insights valiosos e melhorar a precisão da detecção de fraudes. A dificuldade em encontrar e integrar essas fontes pode resultar em um modelo menos preciso e menos eficaz, comprometendo a equipe a identificar fraudes de forma eficiente para a Aegea. Além disso, pode levar a atrasos no projeto e aumento dos custos associados à coleta e integração de dados. |
| Plano de Ação | Para mitigar este risco, nossa equipe deve iniciar com uma pesquisa abrangente para identificar potenciais fontes de dados que possam ser relevantes para o projeto, como dados públicos e registros de instituições parceiras. A equipe deve implementar processos claros para a coleta, validação e integração de novos dados, garantindo que eles sejam compatíveis com os dados existentes e a estrutura do modelo. Além disso, é importante manter uma documentação detalhada dos processos de integração para facilitar a manutenção e futuras atualizações. |
| Responsável | Lucas e João |

| Risco 12 | Falta de entendimento e detalhamento nas bases de dados disponibilizadas |
| --- | --- |
| Descrição | Dificuldades em compreender e detalhar adequadamente as bases de dados fornecidas para o projeto. A falta de entendimento sobre a estrutura, o conteúdo e as características dos dados pode levar a uma análise inadequada, escolha incorreta de variáveis, e dificuldades na integração e uso eficiente desses dados no desenvolvimento do modelo de Machine Learning (ML). |
| Probabilidade | 50% |
| Impacto | Moderado |
| Justificativa | Este risco é considerado moderado porque, embora o entendimento inadequado das bases de dados possa impactar a qualidade da análise e do modelo, ele é mitigável através de processos de análise e documentação adequados por parte do cliente. Com um esforço consciente para revisar e compreender as bases de dados e utilizar ferramentas e técnicas apropriadas, é possível superar essas dificuldades e minimizar o impacto. No entanto, é importante tratar esse risco com atenção para evitar problemas subsequentes que podem afetar a precisão e a eficácia do modelo. |
| Plano de Ação | Para mitigar este risco, a equipe deve começar com uma análise detalhada das bases de dados disponibilizadas, documentando suas estruturas, atributos e características. Realizar reuniões com os responsáveis pelos dados e stakeholders para esclarecer dúvidas e obter informações adicionais é fundamental. Além disso, faremos uma exploração de dados (EDA - Exploratory Data Analysis) para entender melhor o conteúdo e identificar possíveis problemas. Utilizaremos ferramentas de visualização e análise de dados para ajudar na compreensão das bases e vamos construir uma documentação detalhada e um glossário de termos pode ajudar a garantir que todos os membros da equipe tenham um entendimento claro e uniforme das bases de dados, facilitando a integração e uso eficaz dos dados no projeto. |
| Responsável | Eric e Gabriel |

| Risco 13 | Interpretação errônea dos resultados |
| --- | --- |
| Descrição | Este risco refere-se à possibilidade de que a equipe interprete incorretamente os resultados obtidos do modelo de Machine Learning (ML), o que pode levar a conclusões erradas sobre padrões de fraude e decisões inadequadas. A interpretação errônea pode resultar de uma compreensão inadequada dos dados, falhas na validação dos resultados, ou análise incorreta dos outputs do modelo. |
| Probabilidade | 50% |
| Impacto | Alto |
| Justificativa | A interpretação errônea dos resultados pode ser corrigida através de revisões e validações por múltiplos membros da equipe juntamente com o cliente, e é importante ter procedimentos estabelecidos para verificar a precisão das conclusões antes de tomar decisões com base nos resultados do modelo. |
| Plano de Ação | Para mitigar este risco, a equipe deve adotar uma abordagem de validação cruzada dos resultados, envolvendo revisões e discussões com diferentes membros da equipe e professores da área de Machine Learning. Implementar práticas de verificação e validação dos resultados obtidos, como análise de erro e comparação com benchmarks conhecidos para garantir a precisão. Além disso, realizar reuniões regulares para discutir e revisar os resultados com toda a equipe garantirá que quaisquer erros de interpretação sejam identificados e corrigidos rapidamente. |
| Responsável | Larissa e Izabella |

| Risco 14 | Falta de alinhamento com os objetivos de negócios da Aegea |
| --- | --- |
| Descrição | Possibilidade de que o desenvolvimento do modelo de Machine Learning (ML) e as suas funcionalidades não estejam completamente alinhados com os objetivos estratégicos e as necessidades de negócios da Aegea. A falta de alinhamento pode resultar em um modelo que, embora tecnicamente avançado, não atende efetivamente às necessidades reais da empresa ou não contribui para os objetivos de crescimento e eficiência estabelecidos. |
| Probabilidade | 10% |
| Impacto | Alto |
| Justificativa | Se o modelo não estiver alinhado com esses objetivos, pode resultar em investimentos que não agregam valor real à empresa, desperdício de recursos e tempo, e falta de suporte dos stakeholders. Além disso, um modelo desalinhado pode levar a decisões que não têm impacto positivo nas operações da empresa, prejudicando a eficácia do projeto e sua aceitação dentro da organização. |
| Plano de Ação | A equipe deve iniciar o projeto com uma compreensão clara dos objetivos de negócios da Aegea, envolvendo stakeholders chave para garantir que as metas do modelo estejam alinhadas com as necessidades da empresa. Realizar reuniões regulares com stakeholders para revisar o progresso do projeto e garantir que o modelo continue a atender às expectativas e objetivos da Aegea é essencial. Documentar e mapear claramente como cada funcionalidade do modelo contribui para os objetivos de negócios pode ajudar a manter o foco. Além disso, realizar análises de impacto e validação de requisitos durante o desenvolvimento ajudará a assegurar que o modelo permaneça alinhado com as metas estratégicas da empresa. |
| Responsável | Lucas e João |

| Risco 15 | Falta de alinhamento entre os dados históricos e os modelos desenvolvidos |
| --- | --- |
| Descrição | Isso pode ocorrer se os dados históricos não refletirem com precisão as condições atuais ou não forem representativos dos padrões de consumo e fraude que o modelo precisa identificar. |
| Probabilidade | 10% |
| Impacto | Muito alto |
| Justificativa | A eficácia do modelo depende da qualidade e relevância dos dados históricos utilizados. Se os dados históricos não estiverem alinhados com os padrões e condições atuais, o modelo pode não generalizar bem para novas situações, resultando em baixa precisão e capacidade de detecção de fraudes, o que pode comprometer a utilidade do modelo, levar a decisões baseadas em informações incorretas e impactar negativamente a capacidade da Aegea de identificar e prevenir fraudes de maneira satisfatória. |
| Plano de Ação | A equipe deve começar com uma revisão detalhada dos dados históricos para garantir que eles sejam representativos das condições atuais e dos padrões de consumo e fraude. Realizar um processo de atualização e validação contínua dos dados históricos é essencial para refletir mudanças e tendências recentes. A equipe deve também realizar testes para verificar como o modelo se comporta com dados históricos. Além disso, documentar e revisar regularmente a adequação dos dados históricos e ajustar o modelo conforme necessário também contribui para manter a precisão e relevância do modelo. |
| Responsável | Eric e Gabriel |

| Risco 16 | Aderência do modelo às necessidades do parceiro |
| --- | --- |
| Descrição |  |
| Probabilidade | 50% |
| Impacto | Muito alto |
| Justificativa | O risco de que os números de probabilidade de fraudes gerados pelo modelo não sejam considerados relevantes pelo parceiro pode ser justificado pela possibilidade de que, embora tecnicamente precisos, esses resultados não correspondam às expectativas ou necessidades práticas do parceiro. Por exemplo, o parceiro pode buscar uma solução que não apenas indique a probabilidade de fraude, mas que também forneça insights acionáveis ou facilite a tomada de decisões em tempo real, o que pode não estar totalmente contemplado pelo modelo. |
| Plano de Ação | Como plano de ação, realizaremos alinhamentos contínuos com o parceiro durante o desenvolvimento do modelo, garantindo que as expectativas sejam claramente compreendidas e incorporadas ao projeto. Inclui workshops, revisões periódicas dos resultados preliminares e a implementação de feedback para ajustar o modelo às necessidades do parceiro. Além disso, criaremos uma interface ou relatório que traduza as probabilidades em recomendações práticas, aumentando a utilidade e relevância dos resultados para o parceiro. |
| Responsável | Eric e Gabriel |

| Oportunidade 01 | Acesso a Aegea com maior frequência |
| --- | --- |
| Probabilidade | 70% |
| Impacto | Muito alto |
| Descrição | Potencial de aumentar a interação e o envolvimento direto com a equipe da Aegea durante o desenvolvimento do projeto. Um acesso mais frequente à Aegea permite uma boa comunicação, um melhor alinhamento das expectativas e a possibilidade de feedback contínuo e imediato, que facilita a adaptação rápida às necessidades do parceiro, melhora a compreensão dos requisitos de negócios e técnicos, e garante que o modelo de Machine Learning esteja sempre alinhado com os objetivos estratégicos da empresa. |

| Oportunidade 02 | Melhorar a organização de gerenciamento de projetos |
| --- | --- |
| Probabilidade | 90% |
| Impacto | Muito alto |
| Descrição | A equipe pode aprimorar os processos de gerenciamento de projetos, incluindo o cronograma e a alocação de tarefas. Ao adotar ferramentas de gestão mais complexas e estabelecer uma comunicação clara sobre responsabilidades e prazos. |

| Oportunidade 03 | Melhor compreensão do comportamento do consumidor |
| --- | --- |
| Probabilidade | 90% |
| Impacto | Alto |
| Descrição | Capacidade de utilizar os dados coletados para analisar e compreender melhor os padrões de consumo dos clientes. Ao identificar comportamentos típicos e atípicos, a Aegea pode segmentar seus clientes de forma mais decisiva, personalizar seus serviços e melhorar a satisfação do cliente. Isso também pode ajudar a prever demandas e ajustar a oferta de água de acordo com as necessidades reais dos consumidores. |

| Oportunidade 04 | Desenvolvimento de novas competências e habilidades para a equipe |
| --- | --- |
| Probabilidade | 90% |
| Impacto | Muito alto |
| Descrição | O desenvolvimento deste projeto oferece à equipe a oportunidade de adquirir e aprimorar habilidades em áreas críticas como Machine Learning, análise de dados, e gestão de projetos tecnológicos. Essas competências fortalecem a capacidade de inovação e execução de projetos. |

| Oportunidade 05 | Melhorias do modelo na precisão da detecção de fraudes |
| --- | --- |
| Probabilidade | 70% |
| Impacto | Muito alto |
| Descrição | Esta oportunidade destaca a possibilidade de aprimorar os processos de detecção de fraudes, tornando-os mais precisos e menos propensos a erros. Com um modelo preditivo eficiente, a Aegea pode reduzir a incidência de falsos positivos e negativos, garantindo que os recursos sejam direcionados adequadamente para a investigação e correção de casos de fraude. |

| Oportunidade 06 | Aquisição de novas fontes de dados |
| --- | --- |
| Probabilidade | 70% |
| Impacto | Alto |
| Descrição | A busca por novas fontes de dados pode revelar informações valiosas que melhoram a capacidade do modelo de detectar fraudes e identificar padrões de consumo não convencionais, aumentando a precisão do sistema. |

| Oportunidade 07 | Otimização do desempenho do modelo |
| --- | --- |
| Probabilidade | 70% |
| Impacto | Alto |
| Descrição | Problemas de desempenho podem ser uma chance para que nossa equipe explore novas técnicas de otimização e arquitetura de modelos, resultando em um sistema mais eficiente e capaz de lidar com grandes volumes de dados. |

| Oportunidade 08 | Oportunidade de inovação tecnológica |
| --- | --- |
| Probabilidade | 50% |
| Impacto | Alto |
| Descrição | O desenvolvimento deste projeto traz para a Aegea uma aplicação de tecnologias avançadas como Machine Learning e Inteligência Artificial no setor de saneamento, o que aumenta a eficiência e a eficácia dos seus processos internos, e também posiciona a empresa como líder em inovação tecnológica, podendo abrir novas oportunidades de mercado e parcerias estratégicas. |

| Oportunidade 09 | Aprimoramento das ferramentas de visualização e análise |
| --- | --- |
| Probabilidade | 50% |
| Impacto | Muito alto |
| Descrição | Dificuldades na interpretação e visualização dos dados incentivam a adoção de ferramentas e práticas avançadas de visualização, que facilitam a compreensão e comunicação dos resultados para o parceiro. |

| Oportunidade 10 | Profunda compreensão das bases de dados |
| --- | --- |
| Probabilidade | 50% |
| Impacto | Muito alto |
| Descrição | Investir tempo na análise detalhada das bases de dados existentes pode resultar em insights mais profundos sobre os comportamentos dos consumidores e fatores que influenciam fraudes, permitindo uma modelagem mais robusta. |

| Oportunidade 11 | Exploração de novas abordagens para suprir a ausência de dados |
| --- | --- |
| Probabilidade | 50% |
| Impacto | Alto |
| Descrição | A ausência de dados específicos nos incentivará a desenvolver novas metodologias para coletar ou simular dados, abrindo caminho para abordagens inovadoras na modelagem de fraudes para a entrega do modelo ao parceiro. |

| Oportunidade 12 | Oportunidade de inovação tecnológica |
| --- | --- |
| Probabilidade | 50% |
| Impacto | Alto |
| Descrição | A inovação tecnológica representa uma oportunidade de explorar e implementar novas tecnologias e metodologias no desenvolvimento do modelo de Machine Learning para detecção de fraudes. Ao incorporar técnicas avançadas, como redes neurais profundas, aprendizado de máquina não supervisionado e análise preditiva, a equipe pode não apenas melhorar a precisão e eficiência do modelo, mas também posicionar a Aegea como líder em inovação no setor de saneamento. Essa abordagem inovadora pode abrir portas para o desenvolvimento de soluções pioneiras, diferenciando a empresa no mercado e oferecendo novas oportunidades de negócio. |

# 7. Análise Exploratória

O código pode ser acessado em:

https://github.com/Inteli-College/2024-2A-T04-SI11-G02/tree/main/src/Sprint_1/An%C3%A1lise%20explorat%C3%B3ria

## 7.1 Introdução aos Dados

A análise exploratória de dados (EDA, do inglês Exploratory Data Analysis) é uma etapa fundamental em qualquer projeto de ciência de dados. Trata-se de um processo inicial de investigação dos dados que visa compreender suas principais características, detectar padrões, identificar outliers e verificar possíveis relações entre as variáveis. A EDA envolve o uso de técnicas estatísticas descritivas e visualizações gráficas que auxiliam na interpretação dos dados de forma intuitiva. Esta documentação apresenta os principais resultados e insights obtidos durante a análise exploratória, fornecendo uma base sólida para as próximas etapas do projeto, como modelagem e tomada de decisões.	

**1.Setup**

A configuração de setup é o processo de preparar e organizar o ambiente para uso. Envolvendo a instalação de bibliotecas e configuração de outros ajustes necessários. O objetivo é criar um ambiente funcional para executar tarefas específicas.

**1.2 Instalação das bibliotecas**

Primeiro, instala-se as bibliotecas que serão utilizadas no processo de limpeza e pré-processamento dos dados.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image66.png" alt="" width="750"/>
</p>

**1.3 Leitura do CSV**

Foram disponibilizadas duas bases de dados, uma cuja informação principal é o consumo dos clientes (BASE_CONSUMO) e outra com o apontamento de quais clientes já tiveram fraudes identificadas (BASE_FRAUDES). Para importá-las, basta utilizar a função read do pandas.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image68.png" alt="" width="750"/>
</p>

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image11.png" alt="" width="750"/>
</p>

## 7.2 Entendimento dos Dados

Em primeiro lugar foram analisados os dados de consumo com número de registros e variáveis, onde analisamos o número de linhas e colunas para entender a dimensão dos dados. 

Em seguida exceções e ocorrências, em que Investigamos valores únicos em colunas específicas como 'EXCECAO', 'DSC_SIMULTANEA', 'CATEGORIA' e 'DSC_OCORRENCIA' para identificar padrões ou anomalias. E por último tipos de dados e valores nulos, para verificarmos os tipos de dados e a presença de valores nulos, que são essenciais para preparar os dados para a análise.Além dos dados de consumo, analisamos os dados de fraude, a fim de entender sua estrutura e criar um resumo estatístico. A estrutura dos dados consiste na análise do formato dos dados de fraudes, incluindo a verificação do número de registros, tipos de dados e valores nulos, enquanto o resumo estatístico consiste na geração de estatísticas descritivas para entender melhor a distribuição dos dados.

## 7.3 Visualização dos Dados

### 7.3.1 Gráficos

Desenvolvemos um mapeamento das fraudes na região de Campo Grande - MS. Cada ponto representa uma matrícula onde foi registrada fraude e, quanto mais perto da tonalidade amarela, mais fraudes foram detectadas para a mesma matrícula:

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image77.png" alt="" width="750"/>
</p>

O número de fraudes cresce ao passo que a empresa também está crescendo. Para melhor entender as fraudes, as separamos por categorias: pública, industrial, comercial e residencial. Com isso, procuramos pelo valor médio em reais desviado por uma fraude em cada categoria e chegamos no seguinte resultado:

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image52.png" alt="" width="750"/>
</p>

### 7.3.2 Premissas

As fraudes em repartições públicas, apesar de representarem apenas 4% dos locais onde a Aegea fornece abastecimento, representam 60% do volume de água “fraudado” . Entendemos que concentrar esforços nas categorias públicas, industrial e comercial permite maximizar os retornos financeiros com menos recursos, porque cada fraude detectada tem um valor estimado significativamente maior em relação à categoria residencial.

7.4 Conclusão

A análise exploratória realizada até aqui forneceu uma compreensão abrangente dos dados de consumo e fraudes, identificando padrões importantes e características que poderão ser usadas na construção de um modelo de deep learning para predição de fraudes. A inclusão de variáveis temporais, geográficas, socioeconômicas, e de consumo, bem como a identificação de outliers e padrões sazonais, são fundamentais para melhorar a acurácia e a robustez do modelo.

Os próximos passos devem focar em:

- Feature engineering: Criar novas variáveis baseadas nos insights obtidos, como índices de sazonalidade, distâncias geográficas entre fraudes, e agregações temporais.
- Modelagem preliminar: Testar modelos básicos de classificação (como Random Forest ou Gradient Boosting) para identificar quais características são mais importantes (ainda estamos estudando se iremos, de fato, realizar esse passo, mas, por ora, parece ser uma alternativa palpável).
- Desenvolvimento do modelo de deep learning: Com base nas variáveis identificadas, treinar um modelo de deep learning robusto, ajustando parâmetros e arquitetura para maximizar a performance preditiva.

Com esses passos, será possível construir um modelo capaz de determinar a probabilidade de fraudes com alta precisão, contribuindo significativamente para a redução de perdas financeiras e aprimorando as estratégias de prevenção de fraudes da Aegea.

# 8. Pré-processamento e Tratamento dos Dados

O código documentado pode ser acessado diretamente em:

https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/src/Sprint_1/Pr%C3%A9-Processamento%20e%20Limpeza/Pr%C3%A9_Processamento%20e%20Limpeza.ipynb

## 8.1 Limpeza e Pré-Processamento de Dados

**Introdução**

O pré-processamento e a limpeza de dados são etapas cruciais na preparação dos dados para análise e modelagem, especialmente em machine learning e ciência de dados. Essas etapas garantem que os dados estejam em um formato adequado, livre de inconsistências e ruídos que possam afetar a qualidade dos resultados. Isso envolve desde a remoção de valores ausentes e duplicados até a normalização e escalonamento de variáveis, assegurando que os dados estejam prontos para alimentar algoritmos de forma eficiente e precisa.

**1.Setup**

A configuração de setup é o processo de preparar e organizar o ambiente para uso. Envolvendo a instalação de bibliotecas e configuração de outros ajustes necessários. O objetivo é criar um ambiente funcional para executar tarefas específicas.

**1.2 Instalação das bibliotecas**

Primeiro, instala-se as bibliotecas que serão utilizadas no processo de limpeza e pré-processamento dos dados. A Geopy será utilizada para a referenciação de endereços geográficos enquanto que o pandas e numpy servirá para a manipulação e visualização dos dados.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image50.png" alt="" width="750"/>
</p>

**1.3 Leitura do CSV**

Foram disponibilizadas duas bases de dados, uma cuja informação principal é o consumo dos clientes (BASE_CONSUMO) e outra com o apontamento de quais clientes já tiveram fraudes identificadas (BASE_FRAUDES). Para importá-las, basta utilizar a função read do pandas.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image68.png" alt="" width="750"/>
</p>

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image11.png" alt="" width="750"/>
</p>

**1.4 Seleção dos Dados**

**1.4.1 Seleção das Variáveis**

Na Base de Fraudes foram selecionadas as seguintes variáveis que estavam relacionadas à solução do problema e criação do modelo:

MATRICULA: Ligação na qual houve comportamento fraudulento registrado.

DESCRICAO: Tipo de serviço executado que identificou a fraude.

DATACONCLUSAO: Data da indentificação da fraude.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image60.png" alt="" width="750"/>
</p>

Na Base de Consumo foram selecionadas as seguintes variáveis que estavam relacionadas à solução do problema e criação do modelo:

MATRICULA: Índice numérico da ligação da residência do cliente.

DAT_LEITURA: Data da leitura.

CONS_MEDIDO: Valor do consumo em m³.

CATEGORIA: Categoria do cliente (Residencial, Industrial, Comercial ou Pública).

COD_LATITUDE e COD_LONGITUDE: Coordenadas (latitude e longitude) das ligações.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image38.png" alt="" width="750"/>
</p>

**1.4.2  Seleção dos Valores**

Em um primeiro momento, visando focar em fraudes maiores, serão selecionadas matrículas do setor industrial, comercial e pública.

**FUNÇÃO**

Esta função filtra as linhas do DataFrame (df) com base em valores específicos em uma coluna categórica (col). Apenas as linhas onde o valor da coluna corresponde a um dos valores fornecidos na lista values são mantidas.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image38.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image7.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image30.png" alt="" width="750"/>
</p>

**2. Tratamento Geral das Bases**

**2.1 Conversão de Tipos**

As colunas apresentadas na base de dados disponibilizada possui tipos diferentes de formatação, sendo divididos em:

1.float : Responsável por armazenar números reais com precisão de 6 casas decimais;

2.object : Responsável por armazenar qualquer tipo de dado genêrico, utilizado para representar características abstratas;

3.int64 : Dado numérico que pode armazenar valores inteiros de até 64 bits.

Segue abaixo, os tipos de dados encontrados na Base de Fraudes.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image20.png" alt="" width="750"/>
</p>

Segue abaixo, os tipos de dados encontrados na Base de Consumo.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image69.png" alt="" width="750"/>
</p>

**2.2 Conversão para Date**

A função abaixo realiza a conversão das datas para o formato dia-mês-ano. Esta função formata a coluna de datas (col) do DataFrame (df) para string no formato dd-mm-aaaa. Esse tratamento permitirá a manipulação e comparação desse tipo de dado no modelo.

**FUNÇÃO**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image55.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image55.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image46.png" alt="" width="750"/>
</p>

**2.3 Conversão para Inteiro**

O número de matrículas na base de consumo é tipo float e na base de fraude é do tipo inteiro. Com isso, a função abaixo busca padronizar o tipo de dados da variável em inteiro. Esse tratamento tem como mesmo objetivo permitir a manipulação e comparação desse tipo de dado no modelo.

**FUNÇÃO**

Esta função realiza a conversão dos valores de uma coluna (col) do DataFrame (df) para o tipo int.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image4.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image47.png" alt="" width="750"/>
</p>


**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image76.png" alt="" width="750"/>
</p>


**2.4 Conversão das Variáveis Categóricas**

A função abaixo substitui as variáveis categóricas por valores numéricos. Ela converte os valores categóricos de uma coluna (col) do DataFrame (df) para valores numéricos usando um mapeamento predefinido.  Esse tratamento tem como mesmo objetivo permitir uma melhor manipulação e comparação dessa categoria de dado no modelo

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image6.png" alt="" width="750"/>
</p>


**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image23.png" alt="" width="750"/>
</p>


**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image40.png" alt="" width="750"/>
</p>


**3. Criação da Nova Base**

**3.1 Contabilizar Frequência de Fraudes**

A função abaixo visa contabilizar a frequência de fraudes que cada matrícula possui. Ela contabiliza quantas vezes cada valor aparece na coluna de matrícula (col_matricula) do DataFrame (df) e armazena essa contagem em uma nova coluna chamada CONTAGEM_MATRICULA. Este procedimento é essencial para fornecer ao modelo informações sobre a distribuição de fraudes nas matrículas, ajudando a identificar padrões de ocorrência e a treinar o modelo com dados que refletem a frequência e a relevância das fraudes, o que pode melhorar a precisão e a eficácia na detecção de anomalias.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image2.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image46.png" alt="" width="750"/>
</p>


**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image80.png" alt="" width="750"/>
</p>

**3.2 Excluir Dados Repetidos**

A função abaixo busca remover as matrículas duplicadas. Ela remove as linhas duplicadas de um DataFrame com base na coluna de matrícula (col_matricula), mantendo apenas a primeira ocorrência de cada matrícula. Isso é importante para evitar a duplicidade de dados, garantindo a integridade e a qualidade do conjunto de dados para o treinamento do modelo.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image32.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image59.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image81.png" alt="" width="750"/>
</p>

**3.3 Criar Coluna Fraudador**

A função abaixo visa definir as matrículas onde foram identificadas fraudes. Ela adiciona uma nova coluna ao DataFrame (df) com o nome especificado em nome_coluna, preenchendo todas as linhas dessa coluna com o valor 1, indicando que todas as entradas são fraudulentas. Isso é essencial para marcar os casos de fraude, facilitando a análise e a inclusão desses dados no treinamento do modelo.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image61.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image80.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image48.png" alt="" width="750"/>
</p>

**4. Nova Base de Consumo**

**4.1 Selecionar Ano e Mês**

A função abaixo visa organizar melhor os períodos de consumo. Ela extrai o ano e o mês de uma coluna de datas do DataFrame e cria uma nova coluna chamada ANOMES no formato YYYYMM. Isso facilita a análise temporal dos dados, permitindo uma visualização e manipulação mais eficaz dos períodos de consumo.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image71.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image10.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image14.png" alt="" width="750"/>
</p>

**4.2 Seleção das Variáveis**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image78.png" alt="" width="750"/>
</p>

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image67.png" alt="" width="750"/>
</p>

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image34.png" alt="" width="750"/>
</p>

**4.3 Excluir Dados Repetidos**

A função abaixo visa excluir os valores de matrículas duplicadas. Ela remove as linhas duplicadas de um DataFrame com base na coluna de matrícula (col_matricula), mantendo apenas a primeira ocorrência de cada matrícula. Isso garante que o DataFrame contenha apenas entradas únicas, evitando redundâncias e melhorando a qualidade dos dados para análise ou treinamento de modelos.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image25.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image44.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image33.png" alt="" width="750"/>
</p>

**4.4 Variação de Consumo Mensal**

Esta função visa definir uma série temporal do consumo por matrícula. Ela reorganiza o DataFrame para que cada matrícula tenha uma linha única, com os consumos organizados em colunas separadas por mês (cada coluna representa CONSUMO_[ANOMES]). Isso facilita a análise temporal dos dados de consumo, permitindo observar e comparar os padrões de consumo ao longo do tempo.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image12.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image75.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image64.png" alt="" width="750"/>
</p>

**4.5 Variáveis Estatísticas**

A função abaixo realiza cálculos estatísticos do consumo. Ela calcula estatísticas como média, desvio padrão, consumo mínimo e máximo para cada matrícula do DataFrame, com base em colunas de consumo organizadas por ANOMES. Esses cálculos fornecem uma visão geral das tendências e variações no consumo para cada matrícula, auxiliando na análise de padrões e na detecção de anomalias.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image9.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image18.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image43.png" alt="" width="750"/>
</p>

**5. Base Final**

**5.1 União das Bases**

A função abaixo, visa unir as bases de consumo com a de fraudes, ela une três DataFrames (df1, df2, df3) com base em uma coluna de chave comum, como a coluna de matrícula (col_matricula).

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image74.png" alt="" width="750"/>
</p>

**ENTRADA**

Base 1: Variação de Consumo por Matrícula

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image31.png" alt="" width="750"/>
</p>

Base 2: Informações Gerais por Matrícula

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image51.png" alt="" width="750"/>
</p>

Base 3: Informações de Fraude por Matrícula

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image54.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image13.png" alt="" width="750"/>
</p>

**5.2 Substituição de Valores NaN**

A função abaixo visa substituir os dados ausentes por 0. Ela substitui todos os valores NaN do DataFrame (df) por um valor especificado (valor_substituicao). Neste caso, o valor é 0. Isso é importante para garantir que o DataFrame não contenha valores ausentes, evitando erros e facilitando a análise e o treinamento de modelos.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image27.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image56.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image42.png" alt="" width="750"/>
</p>

**5.3 Exportar Dataframe para CSV**

A função abaixo, exporta o DataFrame (df) para um arquivo CSV. Ela exporta o DataFrame (df) para um arquivo CSV.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image22.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image26.png" alt="" width="750"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image57.png" alt="" width="750"/>
</p>

8.2 Features a Serem Implementadas

## O código documentado pode ser acessado diretamente em:

https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/src/Sprint_1/Pr%C3%A9-Processamento%20e%20Limpeza/Feature%20Pr%C3%A9-processamento%20(Em%20implementa%C3%A7%C3%A3o).ipynb

## **Introdução**

Uma das funcionalidades desenvolvidas na Sprint 1 foi a conversão de coordenadas de latitude e longitude em descrições de endereços completos com identificação de bairros. Esse método enriquece o conjunto de dados, adicionando detalhes de localização que podem ser úteis para análises mais profundas, como identificar padrões espaciais ou segmentar dados geograficamente. Contudo, esse método ainda não foi integrado à pipeline final de pré-processamento e limpeza de dados. A implementação dessa feature depende de uma API que apresenta limitações de escalabilidade, dificultando sua aplicação em larga escala. Devido a essas restrições, essa funcionalidade permanece com um funcionamento limitado e não foi incorporada à pipeline principal.

## **1.Setup**

Setup do ambiente para importar bibliotecas e dados.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image3.png" alt="" width="750"/>
</p>

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image8.png" alt="" width="750"/>
</p>

## **2.Conversão De Endereços**

O seguinte script tem como fim converter coordenadas em bairros via a bibloteca do geopy. A função personalizada extrai o bairro e adiciona essa informação ao DataFrame.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image50.png" alt="" width="750"/>
</p>

## **ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image5.png" alt="" width="750"/>
</p>

## **SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image15.png" alt="" width="750"/>
</p>

## **3.Inferir bairros e coluna de bairros**

O dicionário bairro_para_regiao mapeia bairros para suas respectivas regiões urbanas de Campo Grande, facilitando a associação automática de bairros a grandes áreas urbanas predefinidas.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image53.png" alt="" width="750"/>
</p>

A função abaixo recebe uma linha do DataFrame, extrai o bairro e retorna a região urbana correspondente a partir do dicionário.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image73.png" alt="" width="750"/>
</p>

**ENTRADA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image15.png" alt="" width="450"/>
</p>

**SAÍDA**

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image24.png" alt="" width="450"/>
</p>
