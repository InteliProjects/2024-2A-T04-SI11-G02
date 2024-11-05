# Documentação Oficial - Grupo 2 - Modelo de Deep Learning para Detecção de Fraudes (Parceria Aegea)

# Sumário

1. Introdução	

   1.1 Definição do Problema	

   1.2 Solução Proposta	

2. Persona

3. Antipersona

4. Jornada do Usuário

   4.1 Fases da Jornada

5. Canva Proposta de Valor

   5.1 Perfil do Cliente	

   5.2 Proposta de Valor	

6. Matriz de Risco

7. Análise Exploratória	

   7.1 Introdução aos Dados	

   7.2 Entendimento dos Dados

   7.3 Visualização dos dados

      7.3.1 Gráficos	

      7.3.1 Premissas	

   7.4 Conclusão	

8. Pré-processamento e Tratamento dos Dados	

   8.1 Introdução aos Dados	

   8.2 Limpeza dos dados	

   8.3 Tratamento dos dados



9. User Stories

10. Wireframe

11. Business Model Canvas

12. Análise Pestel

13. Protótipo Navegável

14.  Análise de Erros e Curva de Aprendizado do Modelo

15. Comparação entre os Modelos

16. Discussão sobre Generalização no Modelo

17.  Relatório de Avaliação e Visualização das Métricas

18. Front-end do Projeto

      18.1 Guia de Utilização

      18.2 Verificação de Acessibilidade

      18.3 Usabilidade, Design System e Heurísticas de Nielsen Aplicados

      
19. Modelo Final

20. Análise Financeira

21. Referências Bibliográficas


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

# 9. User Stories

As User Stories são fundamentais no processo de desenvolvimento de software ágil. Elas representam uma descrição simples e concisa das funcionalidades desejadas, escritas do ponto de vista do usuário final. As User Stories ajudam a alinhar a equipe de desenvolvimento com as necessidades reais do usuário, priorizando entregas que gerem valor de forma iterativa e incremental. Além disso, as User Stories facilitam a comunicação entre todos os envolvidos no projeto, promovendo uma melhor compreensão dos requisitos e expectativas.

## Tabela de User Stories

| **User Story** | **Descrição** | **Critérios de Aceitação** | **Prioridade** | **Estimativa de Tempo e Esforço** | 
| --- | --- | --- | --- | --- |
| **User Story 1** | Como um engenheiro de dados, quero visualizar os padrões de consumo suspeitos para que eu possa identificar possíveis fraudes de forma mais eficiente. | - O sistema exibe um dashboard com os padrões de consumo suspeitos, incluindo gráficos de anomalias no consumo.<br>- O usuário pode filtrar os dados por período e tipo de cliente. | Média | Esta é uma função interessante e qua vai custar uma semana de trabalho com esforço alto. |
| **User Story 2** | Como um engenheiro de dados, quero acessar um histórico de padrões suspeitos para que eu possa analisar a evolução dos comportamentos anômalos ao longo do tempo. | - O sistema deve manter o acesso a um banco de dados com todos os padrões suspeitos detectados, acessível através de um histórico navegável.<br>- O usuário pode filtrar o histórico por data, região, e outros parâmetros relevantes. | Média | A análise pode ser feita no mesmo dia com esforço baixo. |
| **User Story 3** | Como um engenheiro de dados, quero visualizar a performance do modelo em diferentes períodos e regiões para que eu possa garantir que ele esteja funcionando adequadamente em cenários variados. | - O sistema gera dashboards com a acurácia e taxa de falsos positivos/negativos do modelo segmentadas por região e período (sazonalidade, épocas de chuvas).<br>- Os resultados devem ser apresentados com gráficos e estatísticas, incluindo a porcentagem de casos bem-sucedidos versus erros. | Alto | É estimado que disponibilizar o modelo atendendo esses critérios custe 3 dias de trabalho com esforço médio. |
| **User Story 4** | Como um engenheiro de dados, quero poder reportar fraudes detectadas manualmente dentro dos dados do sistema para registrar detalhes de fraudes não detectadas, para que esses dados possam ser integrados ao sistema e melhorar as previsões futuras. | - O sistema permite ao engenheiro inserir dados sobre fraudes detectadas, incluindo o tipo de fraude, localização, método utilizado, e status da correção.<br>- O relatório é vinculado ao histórico do cliente e influenciará futuras previsões do modelo. | Baixo | Demoraria uma semana para implementar um sistema de inputs manuais e com um esforço alto. |
| **User Story 5** | Como um engenheiro de dados, quero fornecer ao agente de campo uma lista de locais prioritários para fiscalização com base nos resultados do modelo de fraude para que eu possa planejar minhas visitas de forma eficiente. | - O sistema gera uma lista de locais prioritários para fiscalização com base na detecção de fraudes.<br>- A lista inclui informações como localização geográfica, tipo de anomalia, e histórico de consumo suspeito. | Baixo | Essa feature também depende de inputs manuais e também é estimada em uma semana com esforço alto. |

## Testes de Aceitação

| **User Story** | **Critérios de Aceitação** | **Testes de Aceitação** | 
| --- | --- | --- |
| **User Story 1** | CR-01: O sistema exibe um dashboard com os padrões de consumo suspeitos, incluindo gráficos de anomalias no consumo.<br>CR-02: O usuário pode filtrar os dados por período e tipo de cliente. | CR-01: O dashboard mostra padrões suspeitos com pelo menos 85% de precisão.<br>- Correto = Padrões exibidos com pelo menos 85% porcento de precisão.<br>- Errado = Não exibido, revisar processo.<br>CR-02: O sistema aceita e aplica filtros por período e tipo de cliente adequadamente.<br>- Correto = Filtros aplicados.<br>- Errado = Filtros não funcionam, revisar código. |
| **User Story 2** | CR-01: O sistema deve manter o acesso a um banco de dados com todos os padrões suspeitos detectados.<br>CR-02: O usuário pode filtrar o histórico por data, região e outros parâmetros. | CR-01: O histórico é acessível e contém todos os dados esperados.<br>- Correto = Histórico acessível.<br>- Errado = Histórico inacessível, revisar banco de dados.<br>CR-02: Filtros por data e região estão funcionando corretamente.<br>- Correto = Filtros aplicados.<br>- Errado = Filtros não funcionam, revisar processo. |
| **User Story 3** | CR-01: Os resultados são apresentados com gráficos e estatísticas. | CR-01: Gráficos e estatísticas são apresentados de maneira clara e correta.<br>- Correto = Resultados claros.<br>- Errado = Resultados não exibidos, revisar lógica de visualização. |
| **User Story 4** | CR-01: O sistema permite ao engenheiro inserir dados sobre fraudes detectadas manualmente.<br>CR-02: O relatório é vinculado ao histórico do cliente e influencia futuras previsões do modelo. | CR-01: O sistema aceita inserção manual de fraudes com todos os detalhes.<br>- Correto = Dados inseridos corretamente.<br>- Errado = Não aceitou, revisar lógica de inserção.<br>CR-02: Dados manuais afetam corretamente as previsões futuras.<br>- Correto = Previsões ajustadas.<br>- Errado = Previsões não alteradas, revisar integração. |
| **User Story 5** | CR-01: O sistema gera uma lista de locais prioritários para fiscalização com base na detecção de fraudes.<br>CR-02: A lista inclui localização, tipo de anomalia, e histórico de consumo suspeito. | CR-01: A lista de locais prioritários é gerada corretamente.<br>- Correto = Lista gerada.<br>- Errado = Lista não gerada, revisar algoritmo de priorização.<br>CR-02: Todas as informações relevantes estão presentes na lista.<br>- Correto = Informações completas.<br>- Errado = Informações ausentes, revisar preenchimento de dados. |

Concluindo, as User Stories são essenciais no desenvolvimento ágil, assegurando que as funcionalidades entregues estejam diretamente alinhadas com as necessidades dos usuários. As histórias apresentadas vão além do esperado ao detalhar critérios específicos e fornecer uma visão abrangente das funcionalidades, o que garante uma entrega de valor ainda maior. Além disso, elas facilitam a comunicação entre a equipe e os stakeholders, promovendo entregas iterativas que se ajustam rapidamente às mudanças e elevam a qualidade do produto final.

# 10. Wireframe

O wireframe deste sistema foi projetado para garantir uma experiência de usuário eficiente, com uma navegação simples e foco na apresentação clara dos dados. A organização em blocos e a consistência na interface oferecem um fluxo contínuo entre o upload de dados, sua visualização e as previsões geradas pelo modelo, facilitando o monitoramento do consumo e a detecção de fraudes.

# Documentação Wireframe

Link do Wireframe: https://www.figma.com/design/GCXUScRHhtpvmnf8NBzkMQ/Mockup-sprint-3?node-id=9-22668&node-type=frame&t=9SsDMW88dfv90UX7-0

## 1. Tela de Upload de Dados

![image](https://github.com/user-attachments/assets/ebd93560-f4b2-4b2b-9581-dbd66ebc3ffe)

![image](https://github.com/user-attachments/assets/edb9cb5e-de46-4261-b231-d4fefd95c42a)


### Estrutura e Organização
- **Cabeçalho:**
  - Navegação principal com abas ou links para acessar outras partes do sistema (Upload de dados, Visualização, Modelo de Previsão).

- **Área Central:**
  - Bloco de upload de arquivo, com uma zona principal para arrastar/soltar ou clicar para carregar o arquivo.
  
- **Rodapé:**
  - Botão de ação para iniciar o pré-processamento após o upload do arquivo.

---

## 2. Tela de Visualização dos Dados

![image](https://github.com/user-attachments/assets/890dcccf-f848-4d2a-aea8-2111934b97ec)

### Estrutura e Organização
- **Cabeçalho:**
  - Continuando com a navegação principal visível, destacando a aba "Visualização".

- **Área Central:**
  - Tabela de visualização de dados, ocupando o espaço central.
  - Tabela organizada em colunas e linhas, exibindo os dados de consumo já processados.

- **Rodapé:**
  - Indicadores de status ou opções de navegação para ver mais dados, se aplicável.


## 3. Tela de Modelo de Previsão de Fraudes

![image](https://github.com/user-attachments/assets/78a4024e-06bc-4ec1-b2c7-4a8fbeff97da)

### Estrutura e Organização
- **Cabeçalho:**
  - Navegação principal com a aba "Modelo de Previsão" ativa.

- **Área Central:**
  - Tabela com previsões de fraudes, organizada em colunas para apresentar dados de matrícula, localização, categoria, volume consumido e probabilidade de fraude.
  - Abaixo, blocos resumindo os volumes fraudulentos, número de fraudes detectadas, responsáveis e estimativa de perdas financeiras.

- **Rodapé:**
  - Paginação da tabela, permitindo navegar por mais dados de previsões.

# 11. Business Model Canvas

A Aegea Saneamento é uma das maiores empresas privadas de saneamento básico do Brasil, desempenhando um papel fundamental no desenvolvimento da infraestrutura de água e esgoto em diversas regiões do país, como Rio de Janeiro e Mato Grosso do Sul. Fundada com o propósito de melhorar a saúde pública e a qualidade de vida da população, a Aegea atua por meio de concessões públicas, operando em cidades de diferentes portes, desde grandes centros urbanos até áreas mais remotas e vulneráveis. Sua missão vai além da simples prestação de serviços de abastecimento de água e esgotamento sanitário: a empresa busca impactar positivamente o meio ambiente e contribuir para a sustentabilidade, integrando tecnologias inovadoras e processos operacionais eficientes.

Com um foco claro em responsabilidade social e ambiental, a Aegea busca soluções que garantam o acesso universal ao saneamento básico, promovendo um uso racional dos recursos hídricos e reduzindo o impacto ambiental de suas operações. Dentro dessa missão se enquadra a necessidade de prever e mitigar fraudes. O compromisso da empresa é sustentado por parcerias estratégicas com governos, instituições financeiras e organizações não-governamentais, que auxiliam na captação de recursos e no desenvolvimento de programas voltados à inclusão social e à preservação ambiental.

Nesse contexto, o Business Model Canvas da Aegea fornece uma visão detalhada de como a empresa organiza seus recursos, atividades e parcerias para garantir a entrega de valor ao seu público, ao mesmo tempo em que mantém a eficiência operacional e o compromisso com o crescimento sustentável.

<img width="611" alt="Captura de tela 2024-09-12 112023" src="https://github.com/user-attachments/assets/2bf7d2dd-b053-46f1-a366-5474b42cf39f">

### 11.1 Proposta de Valor
A principal proposta de valor da Aegea é oferecer soluções de saneamento de alta qualidade que impactam diretamente a saúde pública, o bem-estar social e a sustentabilidade ambiental. A empresa se compromete com a eficiência operacional e a entrega de serviços que garantam o fornecimento contínuo de água tratada e o tratamento adequado de esgoto, contribuindo para a redução de doenças e a melhoria das condições de vida da população. Além disso, a Aegea busca inovar e integrar tecnologias que mitiguem o uso indevido dos recursos hídricos, alinhando-se às exigências ambientais e à responsabilidade social.

### 11.2 Segmentos de Clientes
Os principais clientes da Aegea são os municípios com os quais a empresa firma contratos de concessão para operar os serviços de água e esgoto. A empresa também atende diretamente a população dessas cidades, incluindo residências, comércios e indústrias, além de parcerias com o governo para alcançar novas áreas de concessão e garantir o acesso ao saneamento básico.

### 11.3 Canais
Os serviços da Aegea são entregues por meio de contratos de concessão, que estabelecem a operação dos sistemas de água e esgoto nas cidades.

### 11.4 Relacionamento com Clientes
A Aegea mantém um relacionamento baseado em confiança, transparência e suporte contínuo. A empresa oferece um atendimento ágil e eficiente, com foco em resolver as demandas dos clientes por meio de canais diversos, como centrais de atendimento e aplicativos. Mensalmente há a aferição de tarifas. A empresa também realiza campanhas educacionais para conscientizar a população sobre o uso responsável da água e a importância do saneamento, criando um relacionamento que vai além da prestação de serviços.

### 11.5 Fontes de Receita
As receitas da Aegea vêm principalmente das tarifas cobradas pelo fornecimento de água tratada e pela coleta e tratamento de esgoto. Esses valores são regulados por contratos de concessão firmados com os municípios e ajustados conforme as agências reguladoras. Além disso, a empresa pode receber recursos por meio de parcerias público-privadas (PPPs), financiamentos para projetos de expansão de saneamento e programas de subsídios governamentais destinados a áreas de vulnerabilidade social.

### 11.6 Recursos Principais
A Aegea depende de uma extensa infraestrutura para a operação eficiente de seus serviços. Isso inclui estações de tratamento de água e esgoto, redes de distribuição e coleta, além de tecnologia avançada para monitoramento dos sistemas e redução de perdas. A empresa também conta com uma equipe técnica especializada, que atua na operação, manutenção e expansão da rede de saneamento. As parcerias com governos e agências reguladoras são cruciais para a continuidade dos contratos de concessão e o cumprimento das normas.

### 11.7 Atividades Principais
As atividades-chave da Aegea englobam a operação, manutenção e expansão dos sistemas de água e esgoto nos municípios onde atua. Isso inclui o tratamento de água potável, a coleta e tratamento de esgoto, bem como a gestão e monitoramento de toda a infraestrutura envolvida. A empresa também realiza investimentos contínuos na modernização de suas operações e na implementação de tecnologias que melhorem a eficiência dos processos, mitiguem fraudes e reduzam impactos ambientais.

### 11.8 Parcerias Principais
A Aegea colabora com governos municipais, estaduais e federais por meio de contratos de concessão, sendo esses parceiros essenciais para a operação de seus serviços. A empresa também estabelece parcerias com instituições financeiras para a captação de recursos destinados a investimentos em infraestrutura e com fornecedores de tecnologia e equipamentos para garantir a eficiência de suas operações. Além disso, parcerias com ONGs e organizações internacionais reforçam o compromisso da Aegea com projetos de sustentabilidade e responsabilidade social.

### 11.9 Estrutura de Custos
A estrutura de custos da Aegea é composta principalmente por despesas operacionais, como custos com energia, mão de obra, manutenção e aprimoramento da infraestrutura de saneamento. A empresa também investe constantemente em tecnologia para modernizar seus processos e garantir a eficiência dos serviços. Além disso, há custos associados a programas sociais e ambientais, alinhados ao compromisso da empresa com o desenvolvimento sustentável e a melhoria da qualidade de vida das comunidades atendidas.

# 12. Análise PESTEL 

### 12.1 Objetivo

A análise PESTEL é uma ferramenta utilizada para avaliar os fatores macroambientais que podem impactar um projeto, negócio ou organização. O acrônimo PESTEL refere-se a seis categorias de fatores: Políticos, Econômicos, Sociais, Tecnológicos, Ambientais e Legais. Essa análise ajuda a identificar as influências externas que podem afetar a estratégia e o desempenho de uma empresa ou projeto, permitindo uma visão abrangente do ambiente em que a organização opera. 

O objetivo desta análise é identificar os fatores externos que podem impactar a empresa de saneamento do segmento privado Aegea.

### 12.1.2 Empresa

A Aegea Saneamento e Participações S.A. é uma empresa privada brasileira, criada em 2010, que atua como referência no setor de saneamento básico no Brasil. Seu foco é fornecer serviços essenciais de abastecimento de água e tratamento de esgoto, contribuindo diretamente para a melhoria da qualidade de vida e saúde da população nas regiões onde opera, ao mesmo tempo que respeita o meio ambiente e promove a sustentabilidade. A empresa atende mais de 31 milhões de pessoas em mais de 500 cidades distribuídas em 15 estados brasileiros, de norte a sul do país.

### 12.1.3 Modelo de Negócios

A Aegea opera por meio de concessões comuns (plenas ou parciais), subconcessões e parcerias público-privadas (PPPs), atuando em toda a cadeia do ciclo da água — desde o abastecimento até a coleta e tratamento de esgoto. Cada operação é adaptada às características e necessidades do município, o que permite flexibilidade e eficiência na gestão dos serviços de saneamento.

## 12.2 Descrição dos Fatores

### 12.2.1 Político

### Eleições Municipais

A regionalização do saneamento trouxe novas instâncias de governança e formas de deliberar sobre a prestação dos serviços, a regulação, os planos regionais de saneamento básico e os instrumentos de controle social. Seguem abaixo as competências dos municípios, estados e União:

- **Municípios**:
  - Responsáveis pela criação de uma entidade reguladora, importante para fiscalizar a prestação dos serviços;
  - Adequação dos contratos para garantir o cumprimento de metas e da qualidade;
  - Avaliar a possibilidade de aderir à prestação regionalizada instituída na região.

- **Estados**:
  - Junto aos municípios, são responsáveis pela estruturação das microrregiões;
  - Apoio na nova governança e desenvolvimento de agências estaduais de regulação;
  - Fornecer canais de apoio aos municípios.

- **Federal**:
  - A Agência Nacional de Águas e Saneamento Básico (ANA) tem o papel de elaborar normas de referência sobre a Lei 14.026/20;
  - Articulação com estados e municípios para a execução dos planos regionais de saneamento básico.

As eleições municipais de 2024 podem impactar a Aegea em aspectos como aumento da fiscalização, revisões contratuais e adoção de modelos regionalizados, criando tanto oportunidades quanto desafios de gestão.

### 12.2.2 Políticas Públicas de Sustentabilidade

Os projetos e incentivos governamentais relacionados à sustentabilidade podem impactar a Aegea de várias maneiras:

- **Oportunidades de Expansão**: Investimentos governamentais em infraestrutura hídrica, como os previstos no Novo PAC (R$ 30,5 bilhões até 2026), podem beneficiar a Aegea em licitações para expansão de serviços em áreas carentes, especialmente no Norte e Nordeste do Brasil.

- **Acesso a Financiamentos e PPPs**: Projetos sustentáveis podem atrair financiamento de instituições como o BNDES e o BID, permitindo a expansão em novos mercados.

- **Pressão Reguladora e Normas Ambientais**: Com o marco regulatório do saneamento (Lei 14.026/2020), que visa universalizar os serviços de água e esgoto até 2033, a Aegea enfrentará pressão para melhorar práticas de sustentabilidade, exigindo investimentos em eficiência hídrica e gestão de resíduos.

- **Desafios Operacionais**: O cumprimento de metas de sustentabilidade pode exigir a adaptação de processos e capacitação das equipes.

### 12.2.3 Burocracia e Concessões

A obtenção e renovação de concessões no setor de saneamento envolve processos burocráticos e legislativos complexos, como licitações regidas por legislações rigorosas, que exigem requisitos técnicos, financeiros e ambientais. A negociação de termos contratuais com municípios, estados ou consórcios regionais pode gerar incertezas, especialmente em cenários de instabilidade política.

### 12.2.4 Econômico

A Aegea pode ser impactada por diversos fatores econômicos destacados na Visão Geral da Conjuntura de julho de 2024:

- **Impacto da Reforma Tributária**: A elevação das tarifas de água e esgoto em até 18%, devido à reforma tributária, pode aumentar os custos dos serviços, impactando a empresa.

- **Cenário Macroeconômico**: O aumento da renda domiciliar pode sustentar o pagamento das tarifas, mas a alta na Selic e pressões inflacionárias podem afetar o custo de captação de recursos e aumentar a inadimplência.

- **Taxa de Câmbio**: A desvalorização do real frente ao dólar (projetada para R$ 5,30 em 2024 e R$ 5,40 em 2025) pode encarecer insumos e equipamentos importados, aumentando os custos operacionais da empresa.

## 12.3 Investimentos em Infraestrutura

O setor de saneamento no Brasil exige investimentos contínuos e substanciais em infraestrutura para alcançar a universalização dos serviços de água e esgoto, conforme estipulado pelo marco legal de 2020. Essa demanda por investimentos é impulsionada pela necessidade de modernizar as redes de saneamento, expandir o atendimento e melhorar a qualidade dos serviços, especialmente em regiões que historicamente carecem de infraestrutura adequada.

> **Nota:** Recentemente a Aegea e a Iguá realizaram a emissão de debêntures, com a participação de instituições como o Banco Nacional de Desenvolvimento Econômico e Social (BNDES) e o Banco Interamericano de Desenvolvimento (BID).

No entanto, o sucesso desses investimentos depende fortemente de dois fatores interligados: **a estabilidade econômica** e **a capacidade de financiamento de grandes projetos**. Uma economia estável, com baixa inflação, taxa de juros controlada e crescimento sustentável, oferece um cenário mais favorável para a execução de projetos de longo prazo, como os do setor de saneamento.

A capacidade de financiar grandes projetos é central para o desenvolvimento do setor, sendo necessário que o setor continue a atrair investidores privados e explore novos mecanismos de financiamento, como parcerias público-privadas (PPPs), concessões e privatizações, para alcançar a escala de investimentos demandada.

## 12.4 Social

### 12.4.1 Crescimento Populacional

O aumento da população nas cidades onde a Aegea opera pode impactar diretamente a demanda por serviços de água e esgoto. Esse crescimento populacional exigirá uma expansão significativa da infraestrutura. Um estudo da Agência Nacional de Águas (ANA) destaca que o uso consuntivo da água deve crescer 24% até 2030, com o abastecimento urbano sendo uma das principais fontes de demanda.

Isso significa que, nas áreas urbanas atendidas pela empresa, pode haver maior pressão para garantir o fornecimento de água de qualidade e o tratamento adequado de esgoto para uma população crescente. A crescente demanda, combinada com a previsão de maior consumo per capita, especialmente em áreas metropolitanas, exigirá um investimento intenso na ampliação das redes de abastecimento e coleta de esgoto.

Além disso, será necessário melhorar a eficiência dos sistemas para reduzir perdas de água e investir em tecnologias para tratar e reusar água, especialmente em regiões mais afetadas pela escassez hídrica.

### 12.4.2 Expectativas da Sociedade

A pressão por práticas mais sustentáveis e transparentes por parte de consumidores, ONGs e comunidades locais influencia significativamente as operações e a reputação da Aegea. Um estudo da Union + Webster, divulgado pela Federação das Indústrias do Estado do Paraná (Fiep), indica que 87% da população brasileira prefere comprar produtos e serviços de empresas sustentáveis, e 70% dos entrevistados estão dispostos a pagar um pouco mais por isso.

A crescente preocupação da sociedade com a sustentabilidade força a Aegea a incorporar práticas mais responsáveis e transparentes em suas operações. Isso fortalece sua posição no mercado e contribui para a longevidade da empresa em um ambiente cada vez mais competitivo. Por outro lado, a falta de alinhamento com essas demandas pode resultar em críticas públicas e danos à reputação.

## 12.5 Tecnológico

### 12.5.1 IoT e Inteligência Artificial

No cenário do Saneamento 4.0, a Aegea deve investir em tecnologias de ponta que otimizem o tratamento de água e esgoto. Isso inclui sistemas inteligentes de tratamento baseados em **Internet das Coisas (IoT)** e **Inteligência Artificial (IA)**. Tecnologias como membranas avançadas e biorreatores monitorados por sensores IoT permitem ajustes imediatos nos processos, melhorando a eficiência e garantindo maior sustentabilidade.

Além disso, a automação no tratamento de esgoto permite um controle mais eficiente de cada fase do processo, desde a coleta até a destinação final dos efluentes.

### 12.5.2 Digitalização de Processos

A aplicação de IoT no saneamento está revolucionando o setor. A Aegea pode capitalizar essas inovações para digitalizar seus processos operacionais. Sensores conectados distribuídos em redes de água e esgoto podem monitorar continuamente vazamentos, qualidade da água e a condição das infraestruturas. A automação permite o acionamento de válvulas e bombas de forma remota, reduzindo a necessidade de intervenções manuais.

### 12.5.3 Sistemas Integrados

O uso de sistemas integrados de informação no Saneamento 4.0 é fundamental para garantir a eficiência da gestão dos serviços prestados pela Aegea. Com a digitalização dos dados de consumo de água, manutenção e reparos, a empresa pode tomar decisões em tempo real, otimizando suas operações. Além disso, a comunicação com os consumidores pode ser aprimorada, oferecendo-lhes acesso a informações detalhadas sobre consumo, vazamentos ou consumo excessivo.

## 12.6 Ambiental

### 12.6.1 Impacto nas Operações

O tratamento e a distribuição de água e esgoto têm um impacto ambiental direto, especialmente em termos de emissões de poluentes, consumo energético e geração de resíduos. A Aegea precisa gerenciar esses aspectos de forma eficiente para mitigar seus impactos nos corpos hídricos e nos ecossistemas.

O relatório da **Agência Nacional de Águas e Saneamento Básico (ANA)** destaca que a gestão inadequada dos resíduos pode comprometer a qualidade da água, algo que é medido pelos indicadores do **ODS 6** (Objetivos de Desenvolvimento Sustentável), como a proporção de corpos hídricos com boa qualidade ambiental (indicador 6.3.2).

## 12.7 Práticas de ESG

Para empresas como a Aegea, a crescente pressão do mercado e dos consumidores em relação às práticas de ESG é um fator determinante. Demonstrar comprometimento com políticas ambientais inovadoras pode se traduzir em vantagens competitivas. No contexto do ODS 6, o foco na eficiência do uso da água (indicador 6.4) e na proteção dos ecossistemas aquáticos (indicador 6.6) são exemplos de práticas que podem ser implementadas ou aprimoradas como parte da estratégia ESG. O compromisso com metas ambientais rigorosas, além de proporcionar benefícios ambientais, também pode fortalecer a imagem da empresa perante acionistas e consumidores que priorizam a sustentabilidade.

### 12.7.1 Gestão de Recursos Hídricos

A gestão sustentável da água é um desafio crucial, e o relatório destaca a importância de reduzir o estresse hídrico (indicador 6.4.2) e aumentar a eficiência no uso da água (indicador 6.4.1). A Aegea, atuando em diversas regiões, deve enfrentar as realidades de escassez hídrica em algumas áreas e se preparar para crises futuras de abastecimento. Isso envolve a implementação de tecnologias que minimizem o desperdício de água, como redes inteligentes de distribuição e monitoramento, e o incentivo ao uso responsável da água pelos consumidores.

### 12.7.2 Legal

O novo marco legal do saneamento básico no Brasil, promulgado em 2020, reformula e atualiza diversas normas existentes, atribuindo novas competências à Agência Nacional de Águas e Saneamento Básico (ANA), além de estabelecer diretrizes para a regulação dos serviços públicos de saneamento, com o objetivo de ampliar a cobertura e melhorar a qualidade do saneamento no país. Entre os pontos principais da lei estão:

- **Competências da ANA:** A agência passa a ser responsável por instituir normas de referência para a regulação dos serviços de saneamento, estabelecendo padrões de qualidade, eficiência, regulação tarifária e metas de universalização.
- **Regionalização do Saneamento:** A lei incentiva a prestação regionalizada dos serviços de saneamento, criando unidades regionais e promovendo a viabilidade técnica e econômica para municípios menores.
- **Novas Regras para Contratos:** Os contratos de concessão de serviços públicos de saneamento devem incluir metas de universalização, redução de perdas e eficiência no uso da água, além de possibilitar a subdelegação de até 25% das atividades.
- **Prazo para Universalização:** Estabelece que até 2033, 99% da população deverá ter acesso a água potável e 90% à coleta e tratamento de esgoto.
- **Financiamento e Participação Privada:** Autoriza a criação de fundos para financiar a estruturação de projetos de concessão e parcerias público-privadas, com vistas a aumentar os investimentos no setor.

Além disso, a Política Nacional de Recursos Hídricos (Lei nº 9.433/1997), somada às normas contidas nas Resoluções ANA nº 174/2023 e ANA nº 192/2024, reforça a importância de uma gestão integrada e rigorosa dos recursos hídricos nas operações da empresa. Segue abaixo, uma análise considerando essas três regulamentações:

### 12.7.3 Política Nacional de Recursos Hídricos (Lei nº 9.433/1997)

Estabelece que as empresas de saneamento precisam garantir que todos os seus usos de água (captação e lançamento de efluentes) estejam devidamente licenciados e respeitem as condições impostas pelas outorgas. Somado a isso, que sejam adotadas práticas que assegurem o uso racional da água, prevenindo o desperdício e contribuindo para a sustentabilidade dos mananciais.

### Resolução ANA nº 174/2023

A empresa deve garantir que suas operações estejam em conformidade com as normativas regionais, particularmente em áreas críticas de gestão hídrica, além de seguir rigorosos procedimentos de monitoramento da quantidade e qualidade da água utilizada, implementando estações hidrológicas para auto-monitoramento.

### Resolução ANA nº 192/2024

Reforça a necessidade de manter condições adequadas de operação em sistemas hídricos críticos e garantir a segurança de barragens. Qualquer falha nesse monitoramento pode resultar em sanções severas.

## 12.8 Análise do Impacto

Segue abaixo, uma análise geral do impacto de cada um dos fatores na empresa.

### 12.8.1 Político

- **Impacto Positivo/Negativo:** As eleições municipais e políticas públicas de sustentabilidade apresentam oportunidades, como a expansão para novas regiões por meio da regionalização do saneamento e acesso a novos projetos governamentais. No entanto, pode haver desafios, como maior rigor regulatório e revisões contratuais que podem elevar os custos de conformidade.
- **Probabilidade:** Alta
- **Estratégias:**
  - **Mitigação:** Estabelecer um diálogo contínuo com órgãos reguladores e prefeituras para garantir que a empresa esteja em conformidade com as exigências locais, minimizando os riscos de revisões contratuais onerosas.
  - **Capitalização:** Participar ativamente das licitações e PPPs, além de investir em práticas de sustentabilidade para atender às políticas públicas, o que pode fortalecer a imagem da empresa e facilitar o acesso a novos mercados.

### 12.8.2 Econômico

- **Impacto Positivo:** O aumento da renda domiciliar e os investimentos em infraestrutura, impulsionados por PPPs, podem fortalecer a capacidade de financiamento para grandes projetos.
- **Impacto Negativo:** A reforma tributária pode aumentar os custos operacionais com elevação das tarifas de água e esgoto, enquanto a oscilação da taxa de câmbio pode encarecer equipamentos importados. Pressões inflacionárias e aumento da inadimplência também podem impactar o fluxo de caixa.
- **Probabilidade:** Alta
- **Estratégias:**
  - **Mitigação:** Diversificar fornecedores de equipamentos e materiais para reduzir a dependência de produtos importados. Negociar contratos de longo prazo com cláusulas de ajuste cambial também pode minimizar os impactos da variação da taxa de câmbio.
  - **Capitalização:** Focar em captar recursos por meio de debêntures e financiamentos de longo prazo, além de aumentar a eficiência operacional para compensar o aumento dos custos. Explorar parcerias com instituições como o BNDES para financiamentos vantajosos.

### 12.8.3 Social

- **Impacto Positivo:** O crescimento populacional aumenta a demanda pelos serviços de saneamento, gerando oportunidades de expansão. A crescente expectativa por práticas sustentáveis também pode beneficiar a Aegea, caso a empresa alinhe suas operações às demandas da sociedade.
- **Probabilidade:** Alta
- **Estratégias:**
  - **Mitigação:** Melhorar a infraestrutura de saneamento para garantir que a empresa esteja preparada para atender ao crescimento populacional e reduzir perdas de água. Monitorar continuamente as práticas de responsabilidade social corporativa.
  - **Capitalização:** Investir em programas de sustentabilidade e práticas transparentes pode aumentar a confiança do consumidor e permitir que a Aegea tenha vantagem competitiva em um mercado que valoriza práticas sustentáveis.

### 12.8.4 Tecnológico

- **Impacto Positivo:** A adoção de tecnologias como IoT e IA pode aumentar a eficiência operacional, reduzir custos e melhorar a gestão de recursos hídricos. As tecnologias do Saneamento 4.0 também oferecem novas oportunidades para a empresa.
- **Probabilidade:** Média
- **Estratégias:**
  - **Mitigação:** Realizar estudos de viabilidade tecnológica antes de grandes investimentos e começar a adoção por pilotos em áreas estratégicas para minimizar riscos financeiros.
  - **Capitalização:** Estabelecer parcerias com startups e fornecedores de tecnologia que possam facilitar a adoção do Saneamento 4.0. Promover a digitalização de processos para melhorar a eficiência e reduzir custos operacionais.

### 12.8.5 Ambiental

- **Impacto Negativo:** A gestão inadequada de recursos hídricos pode trazer sérias consequências ambientais e financeiras. O cumprimento dos indicadores do ODS 6 é desafiador, especialmente em áreas de escassez hídrica.
- **Probabilidade:** Média
- **Estratégias:**
  - **Mitigação:** Investir em tecnologias para monitoramento da qualidade da água e reduzir o consumo energético nas operações. Estabelecer políticas de preservação de bacias hidrográficas e trabalhar com a comunidade para evitar o uso inadequado de recursos.
  - **Capitalização:** Implementar iniciativas que possam ser usadas para destacar o compromisso da empresa com as metas de ESG e os Objetivos de Desenvolvimento Sustentável (ODS), o que pode melhorar sua imagem e atrair investidores focados em sustentabilidade.

### 12.8.6 Ambiental (Regulatório)

- **Impacto Negativo:** O novo marco regulatório e as leis relacionadas ao saneamento impõem maior rigidez nas concessões e outorgas, além de aumentar a necessidade de conformidade com normas ambientais e de uso racional da água.
- **Probabilidade:** Alta
- **Estratégias:**
  - **Mitigação:** Criar uma equipe especializada em compliance para monitorar as mudanças legais e garantir que todas as operações estejam em conformidade com as normas ambientais e de saneamento.
  - **Capitalização:** Proatividade no cumprimento das metas de universalização e nas normas da ANA pode colocar a Aegea em uma posição de liderança no setor, facilitando a participação em novas concessões e financiamentos públicos.

# 13. Protótipo Navegável

1. Neste [link](https://www.figma.com/design/GCXUScRHhtpvmnf8NBzkMQ/Mockup-sprint-3?node-id=125-4852&t=WMBwTBZf5uu3KobF-1), , detalhamos as interações e fluxos de navegação. 
2. Já [neste](https://app.zeplin.io/project/66e82bfa703635846d63d440) link, a documentação foi desenvolvida e está disponível por meio do Zeplin, um plugin essencial para entregar o projeto de maneira organizada para a equipe de desenvolvimento.
3. Por fim, [neste aqui](https://www.figma.com/proto/GCXUScRHhtpvmnf8NBzkMQ/Mockup-sprint-3?node-id=55-2192&node-type=frame&t=PE4UAVAcPxMCiCad-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=55%3A2192&show-proto-sidebar=1), é possível navegar nas soluções desenvolvidas (versões desktop e mobile).

  O protótipo navegável que desenvolvemos buscou seguir os princípios do design atômico, proposto por Brad Frost, com o objetivo de criar uma interface intuitiva, modular e responsiva. Ao adotarmos essa metodologia, buscamos garantir qu cada elemento da interface fosse componentizado e organizado de maneira clara, permitindo a fácil reutilização e adaptação desses componentes em diferentes partes do sistema. 
  
  A estrutura atômica divide o design em cinco níveis: átomos, moléculas, organismos, templates e páginas. Essa abordagem não só facilita a manutenção da consistência visual e funcional, mas também promove escalabilidade, um fator essencial para um sistema que, como o desenvolvido, precisa crescer e se adaptar às necessidades de usuários e às novas funcionalidades.

  A componentização iniciou-se na criação dos átomos, que representam os blocos fundamentais do design. Elementos como botões, campos de entrada e ícones foram desenhados de maneira coesa e padronizada, garantindo a consistência estética em toda a interface. Cada átomo foi pensado para ser funcional de forma isolada, mas também flexível o suficiente para ser combinado com outros componentes, sem perder sua integridade visual ou de usabilidade. 
  
  Em seguida, na formação das moléculas, combinamos átomos para formar componentes mais complexos, mas que ainda mantêm sua simplicidade estrutural. Por exemplo, o campo de busca, composto por um campo de entrada e um botão de envio, é um exemplo clássico de molécula. Esse tipo de combinação permite que o sistema cresça de forma modular, com componentes que podem ser replicados ou ajustados em diversos contextos.
  
  Os organismos, por sua vez, representam conjuntos ainda maiores e mais complexos de moléculas e átomos, como o painel de monitoramento de consumo ou a tabela de previsão de fraudes. Esses organismos foram projetados para desempenhar funções específicas dentro da interface, com foco na organização de informações e na clareza visual. Cada organismo foi testado em diferentes resoluções e contextos de uso, garantindo que seu comportamento fosse adequado tanto em dispositivos móveis quanto em desktop. 
  
  Avançando para os templates, nós os construímos no decorrer do desenvolvimento das páginas, não sendo possível visualizá-los na entrega final. O principal objetivo dessa etapa foi definir e estruturar as páginas com base na disposição lógica dos organismos e moléculas. Aqui, o foco foi organizar os componentes dentro de um layout coeso, que facilitasse a navegação e o fluxo de informações. O template serviu como uma espécie de "esqueleto" para que pudéssemos visualizar a hierarquia de informações e como elas seriam apresentadas ao usuário final. 

  Por fim, as páginas são a instância final dos templates, preenchidas com conteúdo real e interações verdadeiras. Essa etapa foi crucial para validar todas as decisões de design tomadas anteriormente, permitindo que o sistema fosse testado em cenários reais de uso. Cada página foi projetada para ser responsiva, garantindo uma experiência consistente tanto em dispositivos móveis quanto em desktop.

![Página inicial (1)](https://github.com/user-attachments/assets/20ddd88b-97ae-4d41-b562-9788ee2caa0b)
_[Imagem 1] - Página inicial da interface._

O protótipo navegável foi essencial para mapear o comportamento esperado do sistema em cada cenário possível. Como mostrado na [Imagem 2], também desenvolvemos cenários de erro e sucesso para garantir que o sistema estivesse preparado para lidar com diferentes situações. Isso adiciona uma camada importante de realidade ao protótipo, assegurando que ele não só seja funcional em condições ideais, mas também reaja adequadamente a falhas, como no caso de um upload de arquivo mal-sucedido ou de um dado inconsistente.

![Página de erro (1)](https://github.com/user-attachments/assets/04b56b5e-b9f5-4aeb-b611-9517dabe777f)
_[Imagem 2] Página de erro da interface inicial_


![Página de sucesso (1)](https://github.com/user-attachments/assets/e39202c5-c9e5-4f93-8934-dd1b330f0575)
_[Imagem 3] Página de sucesso da interface inicial_


![Dados carregados (1)](https://github.com/user-attachments/assets/a822212d-3b77-4abb-9552-97ea7a69e57c)
_[Imagem 4] Página com os dados carregados_


![Tela de dashboard (4)](https://github.com/user-attachments/assets/9071338d-dbab-42e3-8f22-ae7b4f8c47c8)
_[Imagem 5] Página com os gráficos dos dados inseridos._ 


![Modelo de previsão (1)](https://github.com/user-attachments/assets/e5bbe77b-1f05-4b2a-b8ff-f3d2606e8a35)
_[Imagem 6] Página com o resultado do modelo de previsão e os gráficos analíticos._

  ![Frame 33625](https://github.com/user-attachments/assets/ab737c90-d6c8-4215-9726-e68ef29d3902)
_[Imagem 7] Demonstração da responsividade do design desenvolvido._

A prototipagem interativa permitiu que testássemos, revisássemos e ajustássemos cada uma das interações antes da implementação final. Esse ciclo iterativo foi fundamental para identificar potenciais pontos de fricção e corrigi-los de maneira eficiente. Além disso, conseguimos testar a responsividade de cada página, ajustando os layouts para dispositivos móveis e garantindo que a experiência do usuário fosse fluida e consistente independentemente do dispositivo utilizado.

Para garantir que o sistema fosse escalável e pudesse crescer com o tempo, seguimos rigorosamente os padrões de componentização, sempre focados em garantir que novos átomos, moléculas e organismos pudessem ser facilmente adicionados ou modificados sem comprometer a arquitetura do projeto. O uso dessa abordagem modular proporcionou uma grande flexibilidade ao projeto, o que será crucial para o futuro da solução.

Em suma, o desenvolvimento do projeto focou-se em criar uma solução robusta, modular e escalável, utilizando a metodologia de design atômico como base para garantir consistência e flexibilidade. A criação de um protótipo navegável e a preocupação com a responsividade foram elementos centrais na entrega de um produto de alta qualidade e funcionalidade, pronto para atender às demandas tanto dos usuários finais quanto dos desenvolvedores.

# 14. Análise de Erros e Curva de Aprendizado do Modelo

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

# 15. Comparação entre os Modelos

1. **Modelo RNNs com LSTM**

Para a construção e aprimoramento do modelo para a Sprint 4, primeiro foi necessário a junção das bases de dados de consumo dos anos de 2019 até 2024, como segue na imagem abaixo:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao1.png)

Depois disso, tem-se um novo dataframe com todos os dados de todos os anos juntos. E então, para a detecção de fraudes e modelo preditivo que identifica se é fraude, ou não, é necessário juntar nesse ‘df_total’ a base de dados que possui todos os dados que estão relacionados a fraudes. Logo, isso é feito em seguida no código, da seguinte forma abaixo:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao2.png)

Portanto, agora temos o dataframe com todos os dados que precisamos. No entanto, alguns pré-processamentos e tratamento são necessários, como por exemplo, em uma parte do código, teve-se a criação da coluna “Fraudador” para a base de dados de fraude, em que todos os valores, recebem o valor de 1, ou seja, é fraude.

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao3.png)

Além disso, é importante ressaltar que por conta da base de dados ser muito extensa, durante o código foi definida uma amostra de 30% dos dados de cada base.

No df atualizado, que é o que recebe todos os dados, tanto de fraude quanto de consumo, para os dados que não vieram da base de fraude, ou seja, vieram da base de dados de consumo, os valores da coluna ‘Fraudador’ ficam Nan, e portanto, o código abaixo atribui o valor de 0 para esses casos:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao4.png)

Em seguida, foi necessário realizar o tratamento dos dados, o qual preenche os valores Nan das colunas numéricas com a média:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao5.png)

Um outro tratamento importante, é a normalização dos dados, o qual tem como objetivo normalizar as colunas numéricas do dataframe df usando o MinMaxScaler da biblioteca sklearn. A normalização ajusta os valores das colunas numéricas para que fiquem entre 0 e 1, preservando as relações e proporções dos dados originais, o que pode ser útil para algoritmos de machine learning que são sensíveis à escala das variáveis (como redes neurais e SVMs), ajudando a melhorar a performance do modelo.

Essa normalização pode ser vista na imagem do código abaixo:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao6.png)

Um outro tratamento importante, é a conversão de valores categóricos em valores numéricos, utilizando um mapeamento de strings para inteiros na coluna 'CATEGORIA' do dataframe df. Isso é útil quando precisa-se transformar variáveis categóricas e numéricas, já que muitos algoritmos de machine learning requerem que as variáveis estejam em formato numérico.

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao7.png)

- 'RESIDENCIAL' será mapeado para 0.
- 'COMERCIAL' será mapeado para 1.
- 'PUBLICA' será mapeado para 2.
- 'INDUSTRIAL' será mapeado para 3.

Após isso, é feita a seleção de features e a definição de amostra dos dados:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao8.png)

**1.1 Explicação da Preparação do Modelo**

****Essa etapa da documentação tem como objetivo explicar como foi preparar os dados para o treinamento de um modelo de machine learning, especificamente aplicando técnicas de balanceamento, imputação de valores ausentes e divisão dos dados entre treino e teste.

- Primeiro, os dados são organizados. As variáveis independentes, ou seja, aquelas que serão usadas para prever se há fraude ou não, são armazenadas na variável X, enquanto a variável dependente, que contém as informações sobre se o caso é de fraude ('FRAUDADOR'), é armazenada na variável y.
- Em seguida, os dados em X são redimensionados para um formato apropriado para modelos que exigem uma estrutura de múltiplos passos no tempo, como redes neurais recorrentes. Isso é feito ao usar a função reshape, que reorganiza o array X para que cada amostra tenha um número específico de "timesteps" (passos de tempo) e "num_features" (número de variáveis ou características).
- Depois, o código lida com valores ausentes. Para garantir que o modelo possa ser treinado adequadamente, é necessário substituir (ou "imputar") esses valores. No caso, a biblioteca scikit-learn (importada usando o comando !pip install sklearn e o módulo SimpleImputer) é utilizada para substituir os valores ausentes pela média das respectivas colunas, o que é uma estratégia comum de imputação. O SimpleImputer é aplicado após os dados terem sido reduzidos de uma forma multidimensional para uma forma bidimensional (ou seja, uma linha por amostra).
- Após a imputação dos valores ausentes, os dados são novamente redimensionados para o formato original com os "timesteps" e "num_features".
- Para lidar com o problema de **desbalanceamento de classes** (onde pode haver muito mais casos de não fraude do que de fraude), o código aplica uma técnica chamada **SMOTE** (Synthetic Minority Over-sampling Technique), que cria novas amostras sintéticas da classe minoritária (neste caso, casos de fraude), para equilibrar o número de exemplos entre as classes. No entanto, como o SMOTE requer que os dados estejam em uma forma bidimensional, os dados são temporariamente reduzidos novamente para aplicar a técnica. Depois, os dados resultantes são reorganizados de volta para o formato adequado.
- Por fim, com os dados balanceados, eles são divididos em conjuntos de treino e teste usando a função train_test_split da biblioteca scikit-learn.
    - Cerca de 70% dos dados serão usados para treinar o modelo (X_train, y_train), e;
    - 30% serão usados para testar sua performance (X_test, y_test).

Essa divisão é feita aleatoriamente, mas com um "random_state" fixo, o que garante que os resultados sejam reproduzíveis.

O código abaixo treina um modelo de **rede neural** chamado **LSTM**, que é usado para lidar com **dados sequenciais**, como séries temporais. A ideia é ensinar o modelo a fazer previsões sobre os dados.

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao9.png)

Primeiro, é feita uma divisão dos dados, em que eles são divididos em duas partes: uma para treinar o modelo (treino) e outra para testar sua performance (test).

Em seguida o modelo é montado com várias camadas, incluindo camadas LSTM que são especializadas para dados sequenciais, camadas de Dropout, as quais ajudam a evitar que o modelo aprenda demais e fique muito específico, e camadas Dense, que são como "nós" que ajudam a tomar decisões.

Sendo assim, o modelo é treinado usando os dados de treino por 30 rodadas (épocas), ajustando-se com o tempo para melhorar sua capacidade de prever corretamente.

Após o treinamento, o modelo faz previsões sobre os dados de teste. Ele retorna uma probabilidade de cada exemplo ser da classe 1 (verdadeiro), e essa probabilidade é comparada a um limite (threshold) de 0.3 para decidir se o resultado final será 0 ou 1.

1. **Refatoração do Modelo**

Com toda a refatoração do modelo para essa Sprint, com ajustes no tratamento dos dados, alteração das amostras de dados, número de épocas, alterações nas camadas do modelo e na arquitetura em si, o modelo em sua última época treinada, atingiu o seguinte resultado:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao10.png)

- Loss: 0.6753
- Acurácia 0.5736

Segue abaixo a imagem de sua matriz de confusão:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao11.png)

No entanto, um outro modelo também foi treinado e com outras técnicas foi treinado de uma outra maneira. Esse modelo é denominado de modelo de rede neural recorrente com long short term memory, e o resultado obtido desse modelo em si foi o seguinte:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao12.png)

- Loss: 0.6380
- Acurácia: 0.6285

Os dois modelos têm semelhanças, pois ambos utilizam redes neurais recorrentes para lidar com dados sequenciais. No entanto, existem algumas diferenças importantes em termos de arquitetura, regularização e avaliação. Aqui estão as principais distinções entre o primeiro modelo (LSTM) e o segundo (GRU):

1. **Arquitetura da Rede**:

**Primeiro modelo (LSTM)**: usa camadas LSTM (Long Short-Term Memory), que são uma versão mais complexa das redes recorrentes, capazes de capturar dependências de longo prazo. O modelo começa com uma camada LSTM de 128 unidades, seguida por outra LSTM de 64 unidades, ambas com a função de ativação 'tanh'. O LSTM tem uma estrutura interna mais sofisticada, com uma célula de memória separada que gerencia o fluxo de informações.

**Segundo modelo (GRU)**: usa camadas GRU (Gated Recurrent Units), que são uma variação mais simples das LSTM, com menos parâmetros e um mecanismo mais direto de controle de informações. As GRUs tendem a ser mais rápidas para treinar e podem funcionar tão bem quanto as LSTMs em muitos casos, especialmente quando se trabalha com dados temporais que não exigem uma modelagem tão complexa das dependências de longo prazo.

1. **Regularização (Dropout)**: ambos os modelos aplicam dropout para reduzir o overfitting.

No primeiro modelo (LSTM), o dropout é aplicado após cada camada LSTM com uma taxa de 0.2;

Enquanto no segundo modelo (GRU), também há dropout aplicado com a mesma taxa de 0.2 após cada camada GRU.

1. **Métricas e Compilação**:

**Primeiro modelo (LSTM)**: compila o modelo com o otimizador **Adam**, função de perda **binary_crossentropy** e mede a acurácia ('accuracy'). As métricas se concentram principalmente na acurácia durante o treinamento e validação.

**Segundo modelo (GRU)**: compila o modelo também com o otimizador **Adam**, mas com métricas adicionais: **Precision**, **Recall**, e **AUC (Area Under the Curve)**. Essas métricas fornecem uma visão mais completa do desempenho do modelo, especialmente em problemas de classificação binária desequilibrada. Além disso, é calculada a **F1-Score** após o treinamento para combinar a precisão e recall, oferecendo uma métrica robusta em cenários de classes desbalanceadas.

1. **Estratégia de Treinamento**:

**Primeiro modelo (LSTM)**: usa uma simples divisão de treino e teste com o método train_test_split, treinando o modelo por 30 épocas e avaliando a performance apenas no conjunto de teste.

**Segundo modelo (GRU)**: implementa uma validação cruzada com **K-Fold**, o que significa que o modelo é treinado em diferentes partes dos dados e validado em outras, repetidamente, para garantir que os resultados não sejam influenciados pela aleatoriedade de uma única divisão de dados. Além disso, utiliza **EarlyStopping**, que para o treinamento caso o modelo pare de melhorar após um certo número de épocas, prevenindo o overfitting.

1. **Predição e Decisão Final**:

**Primeiro modelo (LSTM)**: faz previsões sobre os dados de teste e compara as probabilidades com um limite (threshold) de 0.3 para decidir entre 0 e 1 (binário).

**Segundo modelo (GRU)**: cada fold é avaliado com várias métricas após o treinamento. Não há uma menção específica de threshold no código, o que sugere que as métricas como precisão e recall já consideram essa divisão implicitamente durante o treinamento e avaliação.

No entanto, há um outro modelo que em comparação a esses dois modelos, obteve uma melhor performance:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao13.png)

- Loss: 0.187
- Acurácia: 0.9852

A imagem abaixo mostra a sua matriz de confusão:

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao14.png)

Portanto, abaixo, segue a comparação e diferença desses três modelos apresentados:

No **primeiro** modelo, é utilizada uma arquitetura de redes neurais LSTM com duas camadas, sendo a primeira com 128 unidades e a segunda com 64 unidades, ambas com dropout de 0.2. A divisão dos dados é feita de maneira simples entre treino e teste, com 70% para treino e 30% para teste. A única métrica usada para avaliar o desempenho do modelo é a acurácia, e o treinamento ocorre por 30 épocas sem early stopping. Esse modelo é direto, focando em uma simples avaliação de acurácia e uma estrutura básica de rede neural recorrente.

Já o **segundo** modelo opta pelo uso de GRU em vez de LSTM. As camadas GRU possuem 64 e 32 unidades, respectivamente, com dropout de 0.2 após cada camada. Diferentemente do primeiro modelo, ele usa K-Fold Cross-Validation com dois folds, o que permite avaliar o modelo em diferentes divisões de treino e validação, aumentando a robustez da avaliação. Além disso, várias métricas são utilizadas, como acurácia, precisão, recall, AUC e F1-Score, oferecendo uma análise mais detalhada do desempenho do modelo. A introdução de early stopping com uma paciência de 5 épocas ajuda a evitar overfitting e ajustar automaticamente o número de épocas necessário.

No **terceiro** modelo, que também usa GRU, a arquitetura é bastante semelhante ao segundo modelo, com camadas de 64 e 32 unidades, e dropout de 0.3, o que indica uma regularização mais forte para prevenir overfitting. Ele também adota uma abordagem mais simples em relação à validação, dividindo o conjunto de dados em 80% para treino e 20% para validação, sem o uso de K-Fold. As mesmas métricas detalhadas de precisão, recall, AUC e F1-Score são calculadas, tornando a análise do desempenho igualmente detalhada. No entanto, uma diferença significativa é a inclusão de uma matriz de confusão que é gerada e plotada ao final, permitindo uma visualização clara dos verdadeiros positivos, falsos positivos, verdadeiros negativos e falsos negativos, o que facilita a análise qualitativa do modelo. Além disso, o modelo também utiliza early stopping com paciência de 5 épocas, como no segundo exemplo, para otimizar o processo de treinamento.

1. **Relatório de avaliação de métricas**

Após a criação desses 3 modelos, abaixo segue a documentação do relatório de avaliação de métricas primeiramente para o primeiro modelo, e em seguida para o terceiro modelo.

### **3.1 Relatório de Métricas do Modelo 1**

O modelo foi treinado durante **30 épocas** com um **batch size de 64**, utilizando o conjunto de dados de treino e validando com o conjunto de teste. Durante o treinamento, houve uma melhora progressiva tanto na **perda (loss)** quanto na **acurácia (accuracy)** em ambos os conjuntos de treino e validação.

**Desempenho ao longo das épocas**

- **Perda de Treinamento (loss):** Iniciou em 0.6855 e terminou em 0.6753.
- **Acurácia de Treinamento (accuracy):** Iniciou em 0.5514 e aumentou gradualmente para 0.5736.
- **Perda de Validação (val_loss):** Iniciou em 0.6825 e finalizou em 0.6736.
- **Acurácia de Validação (val_accuracy):** Iniciou em 0.5564 e finalizou em 0.5782.

### **Métricas de avaliação no conjunto de teste**

Após o treinamento, o modelo foi avaliado no conjunto de teste, utilizando um threshold de 0.3 para classificação. Os resultados de precisão, recall e F1-Score foram gerados para as duas classes (0 e 1).

### **Desempenho por Classe**

- Classe 0 (negativa):
    - Precisão: 0.77
    - Recall: 0.06
    - F1-Score: 0.11
    - Total de exemplos (support): 192,101
- Classe 1 (positiva):
    - Precisão: 0.51
    - Recall: 0.98
    - F1-Score: 0.67
    - Total de exemplos (support): 191,917

### **Desempenho Geral**

- Acurácia Geral: 0.52
- Média Macro:
    - Precisão: 0.64
    - Recall: 0.52
    - F1-Score: 0.39
- Média Ponderada:
    - Precisão: 0.64
    - Recall: 0.52
    - F1-Score: 0.39

### **Observações**

- **Acurácia geral:** é relativamente baixa, situando-se em 0.52. Isso sugere que o modelo está tendo dificuldades em classificar corretamente os dados, apesar de um bom **recall** para a classe positiva.
- **Desempenho nas classes:** a precisão para a **classe 0** é alta (0.77), mas o **recall** é extremamente baixo (0.06), indicando que o modelo quase não identifica verdadeiros negativos. Para a **classe 1**, o recall é excelente (0.98), mas a precisão é mais baixa (0.51), indicando que o modelo classifica muitos exemplos como positivos, mesmo que sejam falsos positivos.
- **F1-Score:** para a classe 0 é bastante baixo (0.11), o que confirma o fraco desempenho na detecção dessa classe.

Logo, este modelo tem um desempenho claramente enviesado para a classe 1 (positiva), onde obtém um recall elevado, mas à custa de uma baixa precisão. O modelo pode estar enfrentando dificuldades com um dataset desbalanceado, onde a classe 0 está sub-representada em termos de verdadeira detecção. Estratégias como ajuste do threshold, balanceamento de classes ou tuning do modelo podem melhorar o desempenho geral.

### **3.2 Relatório de Métricas do Modelo 3**

Este relatório apresenta o desempenho do modelo baseado em redes GRU, que foi treinado e avaliado em um conjunto de dados com uma divisão de 80% para treino e 20% para validação. O modelo foi treinado com early stopping, configurado para monitorar a métrica de perda (val_loss) com uma paciência de 5 épocas, e utilizou uma arquitetura com duas camadas GRU (64 e 32 unidades, respectivamente) e Dropout para regularização.

### **Métricas de Treinamento**

- **Loss (Perda):** 0.0187
- **Accuracy (Acurácia):** 99.34%
- **Precision (Precisão):** 99.45%
- **Recall:** 99.23%
- **AUC (Área sob a Curva ROC):** 0.9995

As métricas de treinamento indicam que o modelo apresenta uma perda muito baixa (0.0187) e uma acurácia extremamente alta (99.34%), o que sugere que o modelo está capturando muito bem os padrões presentes nos dados de treino.

Além disso, a precisão de 99.45% indica que o modelo realiza previsões corretas na maior parte das vezes, enquanto o recall de 99.23% demonstra que ele consegue identificar a maioria dos casos positivos.

O AUC próximo de 1 (0.9995) indica uma excelente capacidade de discriminar entre classes positivas e negativas.

### **Métricas de Validação**

- **Validation Loss (Perda de Validação):** 0.0431
- **Validation Accuracy (Acurácia de Validação):** 98.52%
- **Validation Precision (Precisão de Validação):** 98.98%
- **Validation Recall (Recall de Validação):** 98.05%
- **Validation AUC (Área sob a Curva ROC de Validação):** 0.9980
- **Validation F1 Score:** 98.51%

Os resultados de validação mostram que o modelo se generaliza bem para dados não vistos, com uma perda de validação de 0.0431, um leve aumento em relação à perda de treino, o que é esperado.

A acurácia de validação de 98.52% também indica um excelente desempenho, embora seja ligeiramente inferior à acurácia de treino.

A precisão de 98.98% e o recall de 98.05% mostram que o modelo tem um excelente equilíbrio entre prever corretamente as classes positivas e capturar a maioria dos exemplos positivos.

O F1-Score de 98.51%, uma métrica que combina precisão e recall, confirma esse bom desempenho geral.

O AUC de 0.9980 continua muito próximo de 1, confirmando que o modelo tem uma excelente capacidade de distinção entre as classes.

Os resultados gerais indicam que o modelo treinado é altamente preciso e robusto, tanto nos dados de treino quanto de validação. A diferença mínima entre as métricas de treino e validação sugere que o modelo não está superajustado (overfitting), o que é evidenciado pelo uso eficaz de dropout para regularização e early stopping. O alto valor de AUC (> 0.99) reforça que o modelo consegue discriminar com alta eficiência entre as classes, enquanto o F1-Score alto (98.51%) demonstra um excelente balanço entre precisão e recall.

Com base nas métricas observadas, este modelo GRU é uma solução altamente eficaz para o problema em questão, oferecendo alta precisão e generalização. Ele é adequado para aplicações em cenários onde uma excelente discriminação entre classes e um equilíbrio entre precisão e recall são essenciais, como em sistemas de detecção de fraudes, análise preditiva e outros problemas binários, sendo assim está dentro dos critérios do projeto e representa o melhor modelo para a Sprint em questão.

1. **Comparação dos Modelos**

O modelo que teve o desempenho foi o terceiro e é possível notar pelos seguintes gráficos a grande diferença em comparação com o modelo 1:

**Modelo 1 - RNNs com LSTM (rede neural recorrente com long short term memory) com 30 épocas com um batch size de 64.**

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao15.jpeg)
Acima, observa-se o desempenho de uma RNN com LSTM durante o treinamento e validação, com duas métricas principais: perda (loss) e acurácia ao longo das épocas.

1. **Perda (Loss):**

A curva de perda diminui constantemente tanto para os dados de treinamento quanto para os dados de validação, indicando que o modelo está aprendendo a reduzir o erro ao longo do tempo.

As curvas de treinamento e validação estão bem próximas, o que sugere que não há um overfitting significativo até o momento.

1. **Acurácia:**

A acurácia aumenta tanto no conjunto de treinamento quanto no de validação, o que é um bom sinal.

Há variações mais acentuadas na curva de validação, indicando oscilações nas predições de validação, possivelmente devido a uma sensibilidade maior aos dados de validação (podem estar menos balanceados ou mais diversos).

Para melhorar o modelo, podemos fazer o seguinte:

1. Adicionar camadas como Dropout ou L2 regularization pode ajudar a estabilizar a performance e reduzir oscilações.
2. Ajuste de hiperparâmetros, ou seja, alterar a taxa de aprendizado ou o número de unidades LSTM pode melhorar o aprendizado.

Logo, pode-se concluir que o modelo de melhor aprendizado é o terceiro.

**Modelo 3 - Modelo de rede neural recorrente com long short term memory (GRU)**

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao16.jpeg)

![image](https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_comparacao17.jpeg)

O gráfico de perda (loss) ao longo das épocas para o Modelo 3, mostra tanto a perda de treinamento quanto a perda de validação.

A perda de treinamento e validação diminuem de forma consistente ao longo das épocas, sugerindo que o modelo está aprendendo com os dados e está ajustando seus parâmetros de forma adequada.

As curvas de treinamento e validação são bastante próximas, indicando que o modelo não está superajustando aos dados de treinamento, ou seja, não há overfitting.

A perda para ambos os conjuntos (treinamento e validação) estabiliza nas últimas épocas, o que indica que o modelo está se aproximando do seu limite de aprendizado, mas sem grandes flutuações, o que sugere um comportamento estável.

# 16. Discussão sobre Generalização no Modelo

## Análise Crítica da Capacidade de Generalização do Modelo

A análise crítica da capacidade de generalização do modelo de detecção de fraudes na rede da Aegea, baseada nos resultados do conjunto de teste, envolve avaliar o quão bem o modelo se comporta diante de dados que não foram utilizados no seu treinamento. Para isso, é essencial observar as métricas de desempenho em um ambiente mais próximo ao real, considerando a diversidade e a representatividade dos dados de teste em relação ao problema que se deseja resolver.

Os resultados de teste geralmente são avaliados através de métricas como precisão, recall, F1 score e AUC (Área sob a Curva ROC). O modelo apresenta um bom desempenho nessas métricas nos dados de teste, isso sugere que ele está conseguindo generalizar bem, ou seja, identificar fraudes em padrões de consumo diferentes daqueles vistos durante o treinamento. No entanto, uma análise crítica deve ir além dessas métricas tradicionais e considerar a robustez do modelo em cenários mais desafiadores.

## Diversidade dos Dados de Teste

Um aspecto relevante a ser analisado é a diversidade dos dados de teste. Uma carecterística notada no modelo é que ele tende a classificar falsos positivos como fraude quando há uma volumetria muito comum para verdadeiros casos de fraude, fazendo com que essa volumetria específica seja classificada como fraude, sendo verdadeira ou não. Por outro lado, quando os dados de teste contêm variações significativas, como mudanças nos padrões de consumo devido a sazonalidades ou a inclusão de diferentes regiões (como áreas urbanas e rurais), o modelo mantém um bom desempenho, indicando que ele possui uma capacidade de generalização robusta. Portanto, é fundamental garantir que o conjunto de teste reflita a variabilidade do ambiente real, o que é um ponto de atenção a se considerar no nosso balanceamento.

## Fraudes Raras e Anomalias

Outro ponto crítico é avaliar como o modelo lida com anomalias ou fraudes raras. Os dados de teste podem não conter uma grande quantidade de fraudes, o que pode levar o modelo a ter um desempenho aparente superior ao esperado. Nesse sentido, uma análise cuidadosa deve considerar o comportamento do modelo diante de fraudes que são incomuns, mas altamente impactantes. O modelo pode apresentar altos índices de precisão, mas se falha em detectar essas fraudes raras, isso indica uma limitação significativa na sua capacidade de generalização.

## Cenários Adversos

Além disso, é importante observar o comportamento do modelo em cenários adversos. A introdução de dados sintéticos ou perturbados no conjunto de teste pode ser uma maneira eficaz de avaliar como o modelo reage a situações inesperadas ou incomuns. Se o desempenho do modelo degrada significativamente com pequenas mudanças nos dados, isso pode ser um indicativo de que ele está "frágil" e não generaliza bem em contextos reais.

## Overfitting

A tendência ao overfitting também deve ser considerada na análise. Se o modelo apresenta uma performance excepcional nos dados de treinamento e seu desempenho mantem-se nos dados de teste, isso é um sinal de que não há excessivos padrões específicos do conjunto de treinamento, mantendo sua capacidade de generalizar para novos dados. Com isso, demonstra-se um equilíbrio saudável entre aprendizado específico e capacidade de generalização.

## Acompanhamento Contínuo

Finalmente, o acompanhamento contínuo dos resultados ao longo do tempo é essencial. Se o modelo for testado em dados mais recentes, o desempenho tende a continuar bom, isso sugere que ele está conseguindo se adaptar às mudanças nos padrões de consumo e nos métodos de fraude. No entanto, se o desempenho começar a deteriorar-se à medida que novos dados são introduzidos, isso pode indicar a necessidade de re-treinamento ou ajustes no modelo para garantir que ele continue generalizando adequadamente.

# 17. Relatório de Avaliação e Visualização das Métricas

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

# 18.  Front-end do Projeto

## 18.1 Guia de Utilização - Predição de Fraudes

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

## 18.2 Verificação de Acessibilidade

## Introdução

A acessibilidade é fundamental para garantir que pessoas com diferentes capacidades possam usar uma aplicação de forma eficiente e pode ser validada utilizando o WCGA. Então a seguir, destacam-se os aspectos em relação à acessibilidade, identificados nas imagens fornecidas, e os principais critérios do WCAG que foram seguidos.

## 1. Contraste de Cor (Critério WCAG 1.4.3)

O contraste entre o texto e o fundo em várias partes da interface parece atender bem ao critério WCAG de contraste mínimo de 4.5:1. Esse bom contraste facilita a legibilidade para usuários com baixa visão ou condições como daltonismo.

**Exemplos**
- O botão azul "Iniciar pré-processamento" tem um excelente contraste contra o fundo branco, facilitando sua visibilidade e uso. 
- A barra azul de ações, como "Adicionar um novo arquivo", segue o mesmo padrão, tornando as ações visíveis e acessíveis.

![image](https://github.com/user-attachments/assets/35db4f57-14bf-4050-89b8-f7515fd70360)

**WCAG aplicado:**
- **Critério 1.4.3 (Contraste de cor):** O contraste entre o texto e o fundo atende aos requisitos de acessibilidade.

## 2. Texto Claro e Legível (Critério WCAG 1.4.4)

A interface utiliza textos grandes e bem espaçados, particularmente nos rótulos das abas e nos botões. Isso garante uma leitura mais fácil, especialmente para usuários com dificuldades visuais. A hierarquia visual bem estruturada, com tamanhos de texto maiores para áreas importantes, também contribui para a acessibilidade cognitiva.

**Exemplo**
- As abas "Upload de dados", "Visualização", e "Modelo de previsão" são claramente visíveis e facilmente legíveis.
- Os dados da tabela, como a coluna "MATRICULA" e "CONS_MEDIDO", têm um tamanho adequado e estão organizados de forma a facilitar a leitura.
![image](https://github.com/user-attachments/assets/d81d5768-0284-49ac-b8e9-562921b004ae)
![image](https://github.com/user-attachments/assets/c2bcd709-7154-40a9-aced-41b84f36c775)

**WCAG aplicado:**
- **Critério 1.4.4 (Redimensionamento do texto):** O texto é legível e dimensionado adequadamente para a maioria dos usuários.

## 3. Navegação Simples e Intuitiva (Critério WCAG 2.4.3)

A navegação pela interface parece bem organizada, com cada seção claramente marcada por abas. Essa estrutura facilita a localização de informações e permite que o usuário compreenda o fluxo do sistema sem esforço cognitivo excessivo. Embora as imagens não permitam verificar completamente a navegação por teclado, a presença de botões grandes e bem definidos sugere que a navegação pode ser simples, o que atende ao princípio da navegação acessível.

**Exemplo**
- As seções estão claramente divididas em abas ("Upload de dados", "Visualização"), o que facilita a navegação.
- O uso de botões grandes e visíveis como "Iniciar pré-processamento" facilita a interação, sugerindo que o sistema segue uma navegação simples e previsível.
![image](https://github.com/user-attachments/assets/d81d5768-0284-49ac-b8e9-562921b004ae)

**WCAG aplicado:**
- **Critério 2.4.3 (Ordenação de foco):** A interface apresenta uma estrutura de navegação clara e intuitiva.

## 4. Foco Visual e Botões Claros (Critério WCAG 2.4.7)

Embora as capturas de tela não mostrem diretamente o foco visual ao navegar por teclado, o design sugere que os botões e elementos interativos estão bem posicionados e são facilmente acessiveis, quando utilizada a tecla "TAB". Isso proporciona uma boa experiência de navegação para usuários que dependem do teclado.

**Exemplo**
- O botão "Iniciar pré-processamento" e o botão "Adicionar um novo arquivo" são grandes, possuem rótulos claros e são chamativos e quando a tecla "TAB" é utilizada, pula direto para o botão de ação.

![image](https://github.com/user-attachments/assets/9b7afad6-1f47-4ee3-8218-75ae966ca679)

**WCAG aplicado:**
- **Critério 2.4.7 (Foco visível):** A interface parece ter um bom destaque visual nos botões, que pode ser aprimorado com a implementação de um foco visível ao navegar por teclado.

## 5. Organização e Hierarquia da Informação (Critério WCAG 1.3.1)

A organização visual da interface é clara, com cada seção bem definida. As informações estão agrupadas de forma lógica, e os títulos são destacados, o que ajuda os usuários a encontrar o que procuram rapidamente. Essa hierarquia de informação é crucial para a acessibilidade cognitiva, permitindo que todos, inclusive pessoas com dificuldade de compreenção, consigam navegar e usar o sistema.

**Exemplo**
- O "Painel de monitoramento de consumo" apresenta os dados de maneira clara e segmentada, com indicadores de volume consumido e matrículas atendidas em destaque, mostrando visualmente primeiro os gráficos mais importantes.
- A distribuição de gráficos e dados está bem organizada, facilitando a leitura e compreensão das informações apresentadas.

![image](https://github.com/user-attachments/assets/ae2a3845-c1d1-48ff-9925-440e5783cbf2)
![image](https://github.com/user-attachments/assets/7547cb44-1f55-4070-8167-1e1563502c87)
![image](https://github.com/user-attachments/assets/2cbd6f05-3a3e-4a86-9460-1dbff9457074)

**WCAG aplicado:**
- **Critério 1.3.1 (Informação e relacionamentos):** A interface organiza as informações de forma clara e acessível, utilizando uma hierarquia visual adequada.

## 18.3 Usabilidade, Design System e Heurísticas de Nielsen Aplicados

Link para documento com fotos e prints com maior qualidade referentes a essa seção: https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/document/Sprint_5/Usabilidade%2C%20Design%20System%20e%20Heur%C3%ADsticas%20de%20Nielsen%20Aplicados%20ao%20Front-End.pdf

## Introdução

A Aegea é uma empresa líder no setor privado de saneamento básico no Brasil, operando em 507 municípios e atendendo mais de 31 milhões de pessoas de norte a sul do país. Este projeto visa desenvolver uma solução de Machine Learning para identificar padrões fraudulentos no consumo de água, impactando diretamente o faturamento e a eficiência operacional da empresa.

Além do modelo preditivo, o projeto inclui uma interface web desenvolvida com **Streamlit**, para fornecer uma experiência intuitiva e simples aos colaboradores, facilitando o acesso aos insights gerados pelo modelo.

## Interface

A interface foi projetada com foco em modularidade e simplicidade, utilizando princípios de design atômico para garantir eficiência no uso e consistência visual.

### Principais Funcionalidades:

1. **Upload de Dados**: Permite o carregamento de arquivos de consumo de água em formatos CSV ou Excel, com pré-processamento automático.
2. **Visualização de Dados Gerais**: Exibe gráficos interativos, mapas geoespaciais e KPIs para uma visão geral do consumo.
3. **Modelo de Previsão de Fraudes**: Executa o modelo preditivo nos dados carregados e exibe os resultados de forma interativa e visual.

## Tecnologia Utilizada

O **Streamlit** foi escolhido por sua capacidade de facilitar a criação rápida de interfaces web voltadas para análise de dados e visualização de modelos de Machine Learning. Seus principais benefícios incluem:

- **Prototipagem rápida**: Permite criar interfaces interativas com poucas linhas de código.
- **Integração nativa**: Integra-se facilmente com bibliotecas como Pandas, Plotly e Scikit-learn.
- **Hospedagem**: O aplicativo pode ser hospedado em servidores ou plataformas de nuvem para uso interno.

## Estrutura do Código

O código é escrito em Python e utiliza **Streamlit** para criar a interface com três abas principais:

1. **Upload de Dados**: Permite o carregamento de arquivos CSV ou Excel.
2. **Visualização**: Exibe gráficos interativos e KPIs com dados gerais de consumo de água.
3. **Modelo de Previsão**: Exibe os resultados do modelo de detecção de fraudes.

### Principais Componentes do Código:

- **Layout e Estilização**: Utiliza `st.set_page_config()` para definir título e layout "wide". Estilos personalizados em CSS garantem uma aparência uniforme.
- **Função de Pré-Processamento**: Remove valores nulos, converte datas, aplica técnicas de clustering com **KMeans**, e transforma variáveis categóricas em dummies.
- **Gerenciamento de Estados**: `st.session_state` é utilizado para gerenciar o estado do carregamento, pré-processamento e armazenamento de dados.

## Solução em Funcionamento

### Primeira Tela - Upload de Dados

![image](https://github.com/user-attachments/assets/8246cfa1-d9bc-4607-b899-9c2d6220ce9f)
![image](https://github.com/user-attachments/assets/42b66b52-60a7-41ef-91a3-82685b85472f)
![image](https://github.com/user-attachments/assets/40428cac-7461-4fe4-9351-e29fe8879abf)


Na primeira tela, o usuário carrega os dados necessários para o modelo preditivo. 

Após o carregamento, o botão "Iniciar pré-processamento" fica disponível, permitindo que o usuário pré-processa os dados, que são então exibidos em uma tabela.

### Segunda Tela - Visualização

![image](https://github.com/user-attachments/assets/f926d6c0-8402-4b9a-aba9-6c150cc2ce19)

Na aba "Visualização", o usuário visualiza:

- **Métricas de Consumo**: Volume total, matrículas atendidas, responsáveis pelo consumo, e valor estimado arrecadado.
- **Gráficos Interativos**: Gráfico de linha para evolução do consumo ao longo do tempo e gráfico de bolhas representando o consumo médio por região e categoria.
- **Mapeamento Geoespacial**: Exibe o consumo por região, destacando casos de anomalias, como medidores de difícil acesso e imóveis desocupados.
- **Análise de Ocorrências**: Gráficos que mostram anomalias categorizadas e análises de consumo.

![image](https://github.com/user-attachments/assets/86e7ab68-cae9-4db6-aaee-5e654373ffa4)


### Terceira Tela - Modelo de Previsão

![image](https://github.com/user-attachments/assets/cc9b9542-8a35-416a-b7e6-9f092ca584c1)

Na aba "Modelo de Previsão", o usuário tem acesso aos resultados do modelo de detecção de fraudes. A tabela exibe os dados pré-processados com uma nova coluna indicando se o caso é uma fraude ou não.


## Explicabilidade do Sistema

A explicabilidade se refere à capacidade de um sistema de comunicar de maneira clara e compreensível como e por que certos resultados ou recomendações foram alcançados. Isso aumenta a transparência e a confiança do usuário nas decisões tomadas pelo sistema.

### Explicabilidade no Processo de Upload de Dados e Modelo de Previsão

Durante o upload de dados, a interface oferece instruções diretas como: “Nessa etapa, você deve adicionar os dados de consumo referentes aos últimos 6 meses” e, após isso, a primeira tela explica a necessidade desse upload: “Para dar início ao processo de predição de fraudes, é necessário carregar os dados”.

Após o pré-processamento dos dados, uma tabela é exibida, mostrando visualmente ao usuário como os dados foram manipulados. Isso reforça a compreensão sobre o que ocorreu com os dados fornecidos.

### Explicabilidade no Processo de Visualização de Dados

Ao acessar a aba de visualização, o usuário vê métricas e gráficos, com uma explicação: “Nesta seção, você pode acompanhar os dados de consumo de água ao longo do período”, informando que os gráficos são construídos com base nos dados inseridos.

Os gráficos possuem títulos claros (ex: “Consumo médio por região da cidade e categoria”) que explicam o conteúdo exibido.

## Design System Utilizado

Durante a Sprint 3, foi criado um Design System para o desenvolvimento do Wireframe. Abaixo está uma descrição de como esse sistema foi aplicado ao front-end em produção.

### Links do Design System:

- **Figma**: [Design no Figma](https://www.figma.com/design/GCXUScRHhtpvmnf8NBzkMQ/Mockup-sprint-3?node-id=177-5152&node-type=section&t=kliDHYIcNvyFivrk-0)
- **Zeplin**: [Projeto no Zeplin](https://app.zeplin.io/project/66e82bfa703635846d63d440)

### Aplicação da Paleta de Cores

A paleta de cores do Design System consistia principalmente em variações de azul e branco, baseando-se nas cores oficiais da Aegea. No front-end, foi aplicado um tom mais “embraquecido”, criando uma aparência mais formal do que a prevista inicialmente.

- **Botões**: Mantiveram-se azuis escuros, sugerindo ações, mas a tonalidade foi levemente ajustada.
- **Gráficos**: As cores foram diversificadas, permitindo melhor distinção entre elementos, utilizando vermelho e verde, além do azul.

### Aplicação das Grades e Organização dos Componentes

As grades e a organização dos componentes seguiram de perto o Design System original. Houve pequenas alterações no layout da tela de upload, enquanto a tela de visualização manteve a organização dos componentes conforme planejado, com exceção de uma leve redução no gráfico de distribuição de consumo.

### Aplicação das Fontes

Durante a transposição para o front-end, as fontes foram parcialmente alteradas por motivos técnicos. O Streamlit ofereceu templates mais acessíveis, mas foi mantida a aparência geral. Houve um aumento no tamanho das fontes dos títulos, destacando-os, enquanto as fontes dos botões ficaram menores.

## Heurísticas de Nielsen Aplicadas

O design da interface foi guiado por várias heurísticas de Nielsen, com destaque para três:

### 1. Visibilidade do Status do Sistema

A interface oferece feedback em tempo real para o usuário, com indicadores de progresso durante o upload de arquivos e pré-processamento. Após o sucesso do carregamento, o sistema mostra uma mensagem verde de confirmação e habilita o botão "Iniciar pré-processamento", cuja cor muda de branco (inabilitado) para azul (habilitado).

### 2. Design Estético e Minimalista

A interface é projetada para ser visualmente simples, com uso de espaço em branco para organizar os elementos. Os textos, botões e gráficos são essenciais, e as instruções são curtas e objetivas. A hierarquia visual é clara, com cores como preto e azul para guiar a interação do usuário.

### 3. Reconhecimento em vez de Memorização

As abas "Upload de dados", "Visualização" e "Modelo de previsão" são bem visíveis e rotuladas de forma clara, guiando o usuário pelas etapas sem a necessidade de memorizar o processo. A navegação segue uma ordem lógica (upload -> visualização -> previsão), e os botões de ação são destacados na tela, garantindo fácil reconhecimento.

Ícones universais, como a nuvem para upload de arquivos e o "X" para cancelamento de ações, ajudam a tornar a interface mais intuitiva.


# 19. Modelo Final

## Pré-Processamento das Bases de Dados

## **1. Configuração de Setup**

processo de preparar e organizar o ambiente para uso. Envolvendo a instalação de bibliotecas e configuração de outros ajustes necessários. O objetivo é criar um ambiente funcional para executar tarefas específicas.

- Instalação de bibliotecas;

```python
import pandas as pd
import numpy as np
```

- Leitura dos arquivos em CSV;

```python
!gdown 1GPoFBPAkj6LHckemF-YqVGtuzYJAbUR6
!gdown 1VqnuZFz0bytf5kPoo4wS5kRTsIwJZGC4
!gdown 1ntv-nmBjrlnl4ikAbb6qck5rULcw17CA
!gdown 1MhPn324v5381tWSrbSur63pwHBPtz0cJ
!gdown 1NcdByBduhY0sk_bKxSXlJJdd3yXZsknn
!gdown 1X8B08S8HomStfeVsLHfxgGQIq1Xugu1D
!gdown 11jUOSbtfbE4Gn77il59uLktMjRdFHOMJ
```

Para download das bases de dados, nós utilizamos o código acima, baixando as bases de dados de consumo de 2019 até 2024 e também a base de fraudes.

Portanto, as bases são lidas e carregadas para o ambiente de desenvolvimento colab:

```python
BASE_CONSUMO_2019 = pd.read_csv('/content/CONSUMO_2019.zip', delimiter=';')
BASE_CONSUMO_2020 = pd.read_csv('/content/CONSUMO_2020.zip', delimiter=';')
BASE_CONSUMO_2021 = pd.read_csv('/content/CONSUMO_2021.zip', delimiter=';')
BASE_CONSUMO_2022 = pd.read_csv('/content/CONSUMO_2022.zip', delimiter=';')
BASE_CONSUMO_2023 = pd.read_csv('/content/CONSUMO_2023.zip', delimiter=';')
BASE_CONSUMO_2024 = pd.read_csv('/content/CONSUMO_2024.zip', delimiter=';')
BASE_FRAUDES = pd.read_csv('/content/FRAUDES_HIST.zip', delimiter=';')
```

## **2. Tratamento Geral das Bases**

### 2.1 Merge das Bases de Dados de Consumo

Após o download e carregamento dos dados, foi necessário realizar a junção dessas bases de consumo, que foi feita da seguinte maneira:

```python
DF_COMPLETO = pd.concat([BASE_CONSUMO_2021, BASE_CONSUMO_2022, BASE_CONSUMO_2023, BASE_CONSUMO_2024])
DF_COMPLETO
```

<aside>
💡

Esse DataFrame completo possui:

- 16266189 linhas;
- 37 colunas.
</aside>

### **2.2 Selecionar Ano e Mês**

Com a nova base de consumo, visamos organizar melhor os períodos de consumo, criando uma função que extrai o ano e o mês de uma coluna de datas do DataFrame, criando uma nova coluna chamada ANOMES no formato YYYYMM.

```python
def extrairAnomes(df, col):

    df[col] = pd.to_datetime(df[col], format='%Y-%m-%d')

    df['ANOMES'] = df[col].dt.strftime('%Y%m')

    return df
```

### **2.3 Seleção das Variáveis**

Colunas atuais:

```
Index(['Unnamed: 0', 'EMP_CODIGO', 'REFERENCIA', 'COD_GRUPO',
       'COD_SETOR_COMERCIAL', 'NUM_QUADRA', 'COD_ROTA_LEITURA', 'MATRICULA',
       'SEQ_RESPONSAVEL', 'ECO_RESIDENCIAL', 'ECO_COMERCIAL', 'ECO_INDUSTRIAL',
       'ECO_PUBLICA', 'ECO_OUTRAS', 'LTR_ATUAL', 'LTR_COLETADA', 'DAT_LEITURA',
       'DIAS_LEITURA', 'CONS_MEDIDO', 'TIPO_LIGACAO', 'CATEGORIA',
       'SUB_CATEGORIA', 'DSC_OCORRENCIA', 'COD_LEITURA_INF_1',
       'COD_LEITURA_INF_2', 'COD_LEITURA_INF_3', 'HORA_LEITURA',
       'DSC_SIMULTANEA', 'VOLUME_ESTIMADO', 'VOLUME_ESTIMADO_ACUM',
       'FATURADO_MEDIA', 'COD_LEITURA_INT', 'STA_TROCA', 'EXCECAO',
       'STA_ACEITA_LEITURA', 'COD_LATITUDE', 'COD_LONGITUDE', 'ANOMES'],
      dtype='object')
```

Colunas selecionadas para a construção e aplicação do modelo:

```python
BASE_VARIACAO_CONSUMO = NOVA_BASE_CONSUMO[['MATRICULA', 'CONS_MEDIDO', 'ANOMES', 
'COD_LATITUDE', 'COD_LONGITUDE', 'ECO_INDUSTRIAL', 'ECO_COMERCIAL', 'ECO_PUBLICA', 
'ECO_OUTRAS', 'CATEGORIA', 'COD_GRUPO', 'COD_SETOR_COMERCIAL', 'COD_SETOR_COMERCIAL', 
'NUM_QUADRA', 'COD_ROTA_LEITURA']]
```

Portanto a base de variação de consumo acima, possui 15 colunas.

### **2.4 Retirando os Dados Nulos**

```python
BASE_GERAL_CONSUMO.dropna()
```

Sendo assim, a base final possui: 16244941 linhas e 15 colunas.

## **3. Base Final**

Inicialmente foi criada uma função que contabiliza quantas vezes cada valor aparece na coluna de matrícula (col_matricula) do DataFrame (df) e armazena essa contagem em uma nova coluna chamada CONTAGEM_MATRICULA.

```python
def contabilizarFrequencia(df, col_matricula):

    df['CONTAGEM_MATRICULA'] = df.groupby(col_matricula)[col_matricula].transform('count')

    return df
   
NOVA_BASE_FRAUDES = contabilizarFrequencia(BASE_FRAUDES, 'MATRICULA')
```

### 3.1 Criação da Coluna Fraudador

```
def definirFraudador(df, nome_coluna):

    df[nome_coluna] = 1

    return df
```

### 3.2 Seleção de Variáveis da Nova Base de Fraudes

```python
NOVA_BASE_FRAUDES = NOVA_BASE_FRAUDES[['MATRICULA', 'CONTAGEM_MATRICULA', 'FRAUDADOR']] 
```

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image_preprocessamento.png" alt="Imagem de Preprocessamento">
</p>

### 3.3 Junção das Tabelas de Consumo e de Fraude

Está função une três DataFrames (df1, df2, df3) com base em uma coluna de chave comum, como a coluna de matrícula (col_matricula).

```python
def unirBases(df1, df2, col_matricula):
    # Unir a base 1 e 2
    df_merged = pd.merge(df1, df2, on=col_matricula, how='outer')
    return df_merged
```

```python
# Fazer um merge entre BASE_GERAL_CONSUMO e NOVA_BASE_FRAUDES para identificar fraudes
BASE_FINAL = BASE_GERAL_CONSUMO.merge(NOVA_BASE_FRAUDES[['MATRICULA', 'FRAUDADOR', 'CONTAGEM_MATRICULA']],
                                      on='MATRICULA',
                                      how='left')

# Substituir os NaN na coluna 'FRAUDE' por 0 (matrículas que não aparecem na tabela de fraudes)
BASE_FINAL['FRAUDADOR'] = BASE_FINAL['FRAUDADOR'].fillna(0).astype(int)
```

Sendo assim, a nossa base final ficou da seguinte maneira:

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image1_preprocessamento.png" alt="Imagem de Preprocessamento">
</p>

### 3.4 **Substituição de Valores NaN**

```python
BASE_FINAL['CONTAGEM_MATRICULA'] = BASE_FINAL['CONTAGEM_MATRICULA'].fillna(0)
```

Está função substitui todos os valores NaN do DataFrame (df) por um valor especificado (valor_substituicao). Neste caso, o valor é 0.

### 3.5 **Criação de Quadrantes por Localização**

```
from sklearn.cluster import KMeans
import pandas as pd
kmeans = KMeans(n_clusters=4, random_state=42)
BASE_FINAL['CLUSTER'] = kmeans.fit_predict(BASE_FINAL[['COD_LATITUDE', 'COD_LONGITUDE']])

# Criar colunas para cada quadrante
BASE_FINAL['QUADRANT_1'] = (BASE_FINAL['CLUSTER'] == 0).astype(int)
BASE_FINAL['QUADRANT_2'] = (BASE_FINAL['CLUSTER'] == 1).astype(int)
BASE_FINAL['QUADRANT_3'] = (BASE_FINAL['CLUSTER'] == 2).astype(int)
BASE_FINAL['QUADRANT_4'] = (BASE_FINAL['CLUSTER'] == 3).astype(int)

# Exibir as primeiras linhas do DataFrame resultante
BASE_FINAL
```

### 3.6 **Normalização e One Hot Encoding das Colunas de Matrícula**

1. **Cópia dos Dados**:
Primeiro, os dados originais são copiados para garantir que qualquer alteração no código não modifique os dados principais.
2. **Tratamento de Datas**:
Uma coluna chamada "ANOMES" (que combina ano e mês) é convertida em um formato de data reconhecível para o sistema, de forma que possamos ordenar e analisar os dados de forma cronológica. Os dados são então organizados por "MATRICULA" (identificador de cada cliente) e pela data.
3. **Filtragem dos Dados**:
Todos os registros onde o valor de "CONS_MEDIDO" (consumo de água medido) é inválido, ou seja, está vazio ou é zero, são removidos. Isso garante que só usamos dados relevantes.
4. **Selecionar Últimos 36 Meses**:
Para cada matrícula (cliente), o código pega os últimos 36 registros de consumo (meses) disponíveis. Se o cliente tiver menos de 36 registros, ele é excluído.
5. **Criação de Colunas para Cada Mês**:
Cada cliente agora tem 36 colunas, uma para cada mês de consumo. Assim, podemos ver como o consumo de água variou mês a mês, em vez de ter todos os registros numa única coluna.
6. **Adicionar Outras Informações**:
Junto com os dados de consumo, o código mantém outras informações sobre cada cliente, como sua localização (latitude e longitude), tipo de atividade (industrial, comercial, etc.) e outros detalhes. Isso é importante porque essas informações podem influenciar o consumo de água.
7. **Transformação de Categorias**:
Algumas colunas, como "CATEGORIA", são convertidas em números. Por exemplo, se a categoria de um cliente for "industrial", isso é transformado numa coluna chamada "CATEGORIA_INDUSTRIAL" com valores de 0 ou 1 (presente ou ausente). Isso facilita a análise, já que os modelos de machine learning lidam melhor com números do que com texto.
8. **Normalização dos Dados**:
O consumo medido é escalado (ajustado) para ficar numa faixa padrão, usando uma técnica que minimiza o impacto de valores extremos (muito altos ou muito baixos). Isso é útil para que os dados sejam tratados de maneira mais uniforme no modelo de machine learning.
9. **Resultado Final**:
Ao final, o código apresenta um novo conjunto de dados (DataFrame) que pode ser usado para treinar um modelo de machine learning. Esse conjunto contém as informações relevantes de cada cliente, organizadas de forma que o consumo de água dos últimos 36 meses e outras características do cliente estejam prontas para análise.

Este processo prepara os dados para serem utilizados em um modelo de previsão de fraudes, já que temos um histórico detalhado do consumo de cada cliente, junto com outras informações que podem ser importantes.

Sendo assim, as colunas da base final, são as seguintes:

```
Index(['MATRICULA', 'CONS_MEDIDO', 'ANOMES', 'COD_LATITUDE', 'COD_LONGITUDE',
       'ECO_INDUSTRIAL', 'ECO_COMERCIAL', 'ECO_PUBLICA', 'ECO_OUTRAS',
       'COD_GRUPO', 'COD_SETOR_COMERCIAL', 'COD_SETOR_COMERCIAL', 'NUM_QUADRA',
       'COD_ROTA_LEITURA', 'FRAUDADOR', 'CONTAGEM_MATRICULA', 'CLUSTER',
       'QUADRANT_1', 'QUADRANT_2', 'QUADRANT_3', 'QUADRANT_4', 'MES_1',
       'MES_2', 'MES_3', 'MES_4', 'MES_5', 'MES_6', 'MES_7', 'MES_8', 'MES_9',
       'MES_10', 'MES_11', 'MES_12', 'MES_13', 'MES_14', 'MES_15', 'MES_16',
       'MES_17', 'MES_18', 'MES_19', 'MES_20', 'MES_21', 'MES_22', 'MES_23',
       'MES_24', 'MES_25', 'MES_26', 'MES_27', 'MES_28', 'MES_29', 'MES_30',
       'MES_31', 'MES_32', 'MES_33', 'MES_34', 'MES_35', 'MES_36',
       'CATEGORIA_COMERCIAL', 'CATEGORIA_INDUSTRIAL', 'CATEGORIA_PUBLICA',
       'CATEGORIA_RESIDENCIAL'],
      dtype='object')
```

<aside>
💡

Logo, a base final possui:

- 367257 linhas;
- 61 colunas.
</aside>

### 3.7 **Exportando o Dataframe para CSV**

A função abaixo, exporta o DataFrame (df) para um arquivo CSV.

```python
def exportarCSV(df, nome_arquivo):

    df.to_csv(nome_arquivo, index=False)
   
nome_arquivo = 'DADOS_PROCESSADOS.csv'

exportarCSV(df_final, nome_arquivo)

from google.colab import files

def baixar_csv(dataframe, nome_arquivo='dados.csv'):
    # Salvar o DataFrame como um arquivo CSV
    path = f'{nome_arquivo}'
    dataframe.to_csv(path, index=False)

    # Gerar um link para download
    files.download(path)

baixar_csv(df_final)
```

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/image2_preprocessamento.png" alt="Imagem de Preprocessamento">
</p>

## Modelo de Rede Neural - Final

### 1. **Importação das Bibliotecas Necessárias**

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
from tensorflow.keras.optimizers import Adam, RMSprop
from imblearn.over_sampling import SMOTE
import tensorflow_addons as tfa
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

```

**O que está acontecendo aqui:**

- **Importação de Ferramentas:** O código começa importando várias "ferramentas" (bibliotecas) que serão usadas para manipular dados, construir e treinar o modelo de inteligência artificial, visualizar resultados, e muito mais.
    - **Pandas (`pd`):** Usado para trabalhar com tabelas de dados.
    - **TensorFlow (`tf`) e Keras:** Usados para construir e treinar redes neurais (um tipo de inteligência artificial).
    - **Plotly e Matplotlib:** Ferramentas para criar gráficos e visualizar dados.
    - **Scikit-learn (`sklearn`):** Oferece várias ferramentas para pré-processamento de dados, divisão de dados em conjuntos de treino e teste, e avaliação de modelos.
    - **Imbalanced-learn (`imblearn`):** Ferramentas para lidar com conjuntos de dados onde uma classe (por exemplo, fraude) é muito menos frequente que a outra.
    - **TensorFlow Addons (`tfa`):** Extensões para o TensorFlow que oferecem métricas adicionais e outras funcionalidades.

### 2. **Definindo a Semente Aleatória**

```python
tf.random.set_seed(42)

```

### 3. **Carregando os Dados**

```python
df = pd.read_csv('/content/DADOS_PROCESSADOS (1).csv', delimiter=',')
df

df_ext = pd.read_csv('/content/DADOS_PROCESSADOS_COMPLETOS.csv', delimiter=',')
df_ext

```

**O que está acontecendo aqui:**

- **Leitura de Arquivos CSV:** Estamos carregando dois conjuntos de dados a partir de arquivos CSV (tabelas de dados separadas por vírgulas) para dentro do Python, usando o Pandas.
    - `df`: Um conjunto de dados principal.
    - `df_ext`: Um conjunto de dados estendido ou adicional.

### 4. **Descrição dos Dados Utilizados**

```python
Os dados utilizados no modelo apresentado a seguir foram selecionados com base nos insights obtidos durante a análise exploratória. Decidimos focar em três variáveis principais: consumo, localização e categoria. Essa escolha foi motivada pelo nosso objetivo de avaliar se essas variáveis isoladas seriam suficientes para que o modelo compreendesse os padrões de consumo e comportamento dos clientes da Aegea.

Os resultados preliminares indicaram que o modelo foi capaz de alcançar uma performance razoável utilizando apenas essas três variáveis. No entanto, durante a apresentação, nosso parceiro de projeto expressou preocupação com a limitação imposta pela utilização de apenas três variáveis. Reconhecemos a validade dessa observação e, embora tenhamos decidido manter a abordagem inicial para fins comparativos, planejamos incorporar outras variáveis em etapas subsequentes para aprimorar o desenvolvimento do modelo.

```

**O que está acontecendo aqui:**

- **Explicação do Processo de Seleção de Dados:** Este parágrafo explica que, inicialmente, o foco foi em três características dos dados (consumo, localização e categoria) para ver se eram suficientes para o modelo entender padrões de comportamento dos clientes. Apesar de funcionar razoavelmente bem, há planos para adicionar mais características no futuro para melhorar o modelo.

### 5. **Selecionando Colunas Específicas do Conjunto de Dados**

```python
df = pd.read_csv('/content/DADOS_PROCESSADOS.csv', delimiter=',')
df

df = df[['MATRICULA','QUADRANT_1', 'QUADRANT_2', 'QUADRANT_3', 'QUADRANT_4',
         'MES_13', 'MES_14', 'MES_15', 'MES_16', 'MES_17', 'MES_18', 'MES_19',
         'MES_20', 'MES_21', 'MES_22', 'MES_23', 'MES_24',
         'CATEGORIA_COMERCIAL', 'CATEGORIA_INDUSTRIAL', 'CATEGORIA_PUBLICA',
         'CATEGORIA_RESIDENCIAL']]
df

```

**O que está acontecendo aqui:**

- **Leitura e Seleção de Colunas:** Carregamos outro arquivo de dados e selecionamos apenas algumas colunas específicas que consideramos importantes para o nosso modelo. Isso ajuda a simplificar os dados e focar nas informações relevantes.

### 6. **Selecionando uma Amostra dos Dados**

```python
# Selecionar uma amostra aleatória de 10% dos dados
amostra_10 = df.sample(frac=0.1, random_state=42)

df = df.drop(columns=[ 'MES_13', 'MES_14', 'MES_15',
       'MES_16', 'MES_17', 'MES_18', 'MES_19', 'MES_20', 'MES_21', 'MES_22',
       'MES_23', 'MES_24', 'MES_25', 'MES_26', 'MES_27', 'MES_28', 'MES_29',
       'MES_30', 'MES_31', 'MES_32', 'MES_33', 'MES_34', 'MES_35', 'MES_36'])

```

**O que está acontecendo aqui:**

- **Amostragem Aleatória:** Selecionamos aleatoriamente 10% dos dados para trabalhar, o que pode ajudar a reduzir o tempo de processamento.
- **Remoção de Colunas:** Eliminamos várias colunas relacionadas a meses específicos (`MES_13` a `MES_36`) porque decidimos que elas não são necessárias para o nosso modelo atual.

### 7. **Preparando o Conjunto de Dados Estendido**

```python
df_ext = df_ext.drop(columns=['MATRICULA', 'CONS_MEDIDO', 'ANOMES', 'COD_LATITUDE', 'COD_LONGITUDE', 'CLUSTER', 'CONTAGEM_MATRICULA',  'MES_13', 'MES_14', 'MES_15',
       'MES_16', 'MES_17', 'MES_18', 'MES_19', 'MES_20', 'MES_21', 'MES_22',
       'MES_23', 'MES_24', 'MES_25', 'MES_26', 'MES_27', 'MES_28', 'MES_29',
       'MES_30', 'MES_31', 'MES_32', 'MES_33', 'MES_34', 'MES_35', 'MES_36'])

```

**O que está acontecendo aqui:**

- **Limpeza do Conjunto de Dados Estendido:** Removemos várias colunas do conjunto de dados estendido (`df_ext`) para focar apenas nas informações que consideramos úteis para o modelo.

### 8. **Separando as Características e o Alvo**

```python
X = df.drop(columns=['FRAUDADOR'])
y = df['FRAUDADOR']
X

X_ext = df_ext.drop(columns=['FRAUDADOR'])
y_ext = df_ext['FRAUDADOR']
X_ext

```

**O que está acontecendo aqui:**

- **Características (X) e Alvo (y):** Dividimos os dados em duas partes:
    - **X:** Contém todas as informações que o modelo usará para aprender (como consumo, localização, etc.).
    - **y:** É o que queremos que o modelo preveja, neste caso, se a pessoa é um "fraudador" ou não.

### 9. **Analisando o Desequilíbrio das Classes**

```python
# Analisando o desequilíbrio das classes
y.value_counts().plot(kind='bar')
plt.title('Distribuição das Classes')
plt.show()

```

**O que está acontecendo aqui:**

- **Visualização das Classes:** Criamos um gráfico de barras para ver quantos exemplos temos de cada classe (fraudador vs. não fraudador). Isso nos ajuda a entender se temos muitas mais instâncias de uma classe do que da outra.

### 10. **Balanceando os Dados com SMOTE**

```python
# Aplicando SMOTE para balanceamento
smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(X, y)

# Verificando a nova distribuição das classes
y_balanced.value_counts().plot(kind='bar')
plt.title('Distribuição das Classes Após SMOTE')
plt.show()

```

**O que está acontecendo aqui:**

- **SMOTE (Synthetic Minority Over-sampling Technique):** É uma técnica usada para equilibrar conjuntos de dados onde uma classe é muito menos frequente que a outra. Aqui, estamos criando mais exemplos da classe minoritária (por exemplo, fraudadores) para que o modelo possa aprender melhor.
- **Verificação do Balanceamento:** Após aplicar o SMOTE, criamos outro gráfico de barras para confirmar que as classes agora estão equilibradas.

### 11. **Repetindo o Balanceamento para o Conjunto de Dados Estendido**

```python
# Analisando o desequilíbrio das classes
y_ext.value_counts().plot(kind='bar')
plt.title('Distribuição das Classes')
plt.show()

# Aplicando SMOTE para balanceamento
smote = SMOTE(random_state=42)
X_balanced_ext, y_balanced_ext = smote.fit_resample(X_ext, y_ext)

# Verificando a nova distribuição das classes
y_balanced_ext.value_counts().plot(kind='bar')
plt.title('Distribuição das Classes Após SMOTE')
plt.show()

```

**O que está acontecendo aqui:**

- **Balanceamento do Conjunto Estendido:** Repetimos o processo de balanceamento usando SMOTE para o conjunto de dados estendido (`df_ext`), garantindo que também esteja equilibrado.

### 12. **Dividindo os Dados em Conjuntos de Treino, Validação e Teste**

```python
# Primeiro, divisão dos dados em treino (70%) e teste (30%)
X_train_full, X_test, y_train_full, y_test = train_test_split(X_balanced, y_balanced, test_size=0.3, random_state=42)

# Agora, dividimos o conjunto de treino em treino (70% do total) e validação (30% do total)
X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.3, random_state=42)

# Repetindo para o conjunto de dados estendido
X_train_full_ext, X_test_ext, y_train_full_ext, y_test_ext = train_test_split(X_balanced_ext, y_balanced_ext, test_size=0.3, random_state=42)
X_train_ext, X_val_ext, y_train_ext, y_val_ext = train_test_split(X_train_full_ext, y_train_full_ext, test_size=0.3, random_state=42)

```

**O que está acontecendo aqui:**

- **Divisão dos Dados:**
    - **Treino (70%) e Teste (30%):** Primeiro, separamos 70% dos dados para treinar o modelo e 30% para testar como ele se sai em dados novos.
    - **Treino e Validação:** Dentro dos 70% de treino, separamos mais 30% para validar o modelo enquanto ele está aprendendo, ajudando a ajustar os parâmetros.
    - **Repetição para Conjunto Estendido:** Realizamos o mesmo processo para o conjunto de dados estendido.

### 13. **Construindo o Modelo de Rede Neural**

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

# Resumo da arquitetura do modelo
model.summary()

```

**O que está acontecendo aqui:**

- **Definição da Rede Neural:**
    - **Sequential:** Estamos criando um modelo "sequencial", onde as camadas são adicionadas uma após a outra.
    - **Camadas (`Dense`):** Cada camada é composta por um certo número de "neurônios" (nós), que são unidades que processam informações.
        - **128 Neurônios:** Primeira camada com 128 neurônios, recebendo todos os dados de entrada (`input_dim`).
        - **Camadas Subsequentes:** Reduzimos o número de neurônios em cada camada subsequente (64, 32, 16, 8).
        - **Camada de Saída:** A última camada tem apenas 1 neurônio e usa a função de ativação `sigmoid`, que é adequada para prever probabilidades entre 0 e 1 (por exemplo, fraude ou não).
- **Compilação do Modelo:**
    - **Função de Perda (`loss`):** Usamos a "entropia cruzada binária", apropriada para problemas de classificação binária.
    - **Otimizador (`optimizer`):** Usamos o RMSprop, que ajuda o modelo a aprender ajustando os pesos de forma eficiente.
    - **Métricas:** Estamos medindo a "acurácia" do modelo, ou seja, a porcentagem de previsões corretas.
- **Resumo do Modelo:** `model.summary()` mostra uma visão geral das camadas e parâmetros do modelo.

### 14. **Construindo um Segundo Modelo (Modelo Extendido)**

```python
model_ext = Sequential()
model_ext.add(Dense(128, input_dim=X_train_ext.shape[1], activation='relu'))
model_ext.add(Dense(64, activation='relu'))
model_ext.add(Dense(32, activation='relu'))
model_ext.add(Dense(16, activation='relu'))
model_ext.add(Dense(8, activation='relu'))
model_ext.add(Dense(1, activation='sigmoid'))
# Compilando o modelo
model_ext.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])

# Resumo da arquitetura do modelo
model_ext.summary()

```

**O que está acontecendo aqui:**

- **Segundo Modelo (`model_ext`):** Criamos outro modelo de rede neural com a mesma estrutura, mas usando um otimizador diferente (`Adam`). Isso nos permite comparar qual otimizador funciona melhor para nosso problema.

### 15. **Aprimorando a Compilação dos Modelos com Mais Métricas**

```python
# Compilação do modelo com mais métricas
optimizer = RMSprop(learning_rate=0.001)

model.compile(loss='binary_crossentropy',
              optimizer='RMSprop',
              metrics=[
                  'accuracy',
                  tfa.metrics.F1Score(num_classes=1, threshold=0.5),
                  tf.keras.metrics.Precision(),
                  tf.keras.metrics.Recall()
              ])

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

**O que está acontecendo aqui:**

- **Ajuste dos Otimizadores:**
    - **RMSprop:** Definimos uma taxa de aprendizado específica para o RMSprop.
    - **Adam:** Definimos uma taxa de aprendizado específica para o Adam.
- **Adição de Mais Métricas:**
    - **F1-Score:** Uma métrica que combina precisão e recall, útil para avaliar o desempenho em dados desbalanceados.
    - **Precisão (`Precision`):** Mede a proporção de verdadeiros positivos entre todas as previsões positivas.
    - **Recall (`Recall`):** Mede a proporção de verdadeiros positivos entre todas as instâncias reais positivas.
    
    Essas métricas nos dão uma visão mais completa de como o modelo está se saindo, especialmente em casos onde uma classe é mais importante que a outra (por exemplo, detectar fraudes).
    

### 16. **Treinando o Modelo**

```python
# Definir EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
# class_weight = {0: 1.0, 1: 1.3}  # Pese mais a classe positiva (classe 1)
history = model.fit(X_train, y_train, epochs=100, batch_size=64,
                    validation_data=(X_test, y_test),
                    callbacks=[early_stopping],
                    # class_weight=class_weight
                    )

```

**O que está acontecendo aqui:**

- **Early Stopping:** Uma técnica que para o treinamento se o modelo não está melhorando, evitando overfitting (quando o modelo aprende demais os dados de treino e não generaliza bem).
    - **Monitor:** Estamos observando a "val_loss" (perda no conjunto de validação).
    - **Patience:** Se a perda não melhorar por 5 épocas, o treinamento para.
    - **Restore Best Weights:** Retorna os melhores pesos do modelo encontrados durante o treinamento.
- **Treinamento do Modelo (`model.fit`):**
    - **X_train e y_train:** Dados usados para treinar o modelo.
    - **epochs=100:** Tentaremos treinar o modelo por até 100 vezes, mas o Early Stopping pode parar antes.
    - **batch_size=64:** Processamos 64 amostras de cada vez.
    - **validation_data:** Usamos os dados de teste para validar o modelo durante o treinamento.
    - **callbacks:** Incluímos o Early Stopping como um "callback" para monitorar o treinamento.
    - **class_weight (comentado):** Poderíamos dar mais peso para a classe de fraude, mas está comentado (não está sendo usado).

### 17. **Avaliando o Modelo no Conjunto de Teste**

```python
# Avaliar o modelo no conjunto de teste
loss, accuracy, f1_score, precision, recall = model.evaluate(X_test, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}, F1-Score: {f1_score}, Precision: {precision}, Recall: {recall}')

```

**O que está acontecendo aqui:**

- **Avaliação do Modelo:** Depois de treinar, verificamos quão bem o modelo está se saindo nos dados de teste que não foram usados no treinamento.
    - **Loss:** A perda total (quanto o modelo errou).
    - **Accuracy:** A porcentagem de previsões corretas.
    - **F1-Score, Precision, Recall:** As métricas adicionais que adicionamos anteriormente.
- **Impressão dos Resultados:** Mostramos esses valores para entender o desempenho do modelo.

### 18. **Exemplo de Saída do Treinamento e Avaliação**

```
Epoch 1/100
...
Loss: 0.5502932667732239, Accuracy: 0.6965527534484863, F1-Score: [0.61451143], Precision: 0.8399287462234497, Recall: 0.48448655009269714

```

**O que está acontecendo aqui:**

- **Progresso do Treinamento:** Mostramos as informações de cada "época" (cada vez que o modelo passa por todo o conjunto de dados de treino).
    - **Loss e Accuracy:** Mostram como o modelo está melhorando a cada época.
    - **F1-Score, Precision, Recall:** Mostram métricas mais detalhadas sobre o desempenho do modelo.
- **Resultados Finais:** Após o treinamento, os valores finais dessas métricas são exibidos.

### 19. **Treinando o Modelo Estendido**

```python
# Definir EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
# class_weight = {0: 1.0, 1: 1.3}  # Pese mais a classe positiva (classe 1)
history_ext = model_ext.fit(X_train_ext, y_train_ext, epochs=100, batch_size=32,
                    validation_data=(X_test_ext, y_test_ext),
                    callbacks=[early_stopping],
                    # class_weight=class_weight
                    )

```

**O que está acontecendo aqui:**

- **Treinamento do Segundo Modelo (`model_ext`):** Repetimos o processo de treinamento para o segundo modelo que criamos, usando o conjunto de dados estendido.
    - **Batch Size Diferente:** Aqui usamos um tamanho de lote menor (32 em vez de 64).
    - **Outros Parâmetros:** Mantemos o Early Stopping e as mesmas métricas.

### 20. **Avaliando o Modelo Estendido**

```python
# Avaliar o modelo no conjunto de teste
loss, accuracy, f1_score, precision, recall = model_ext.evaluate(X_test_ext, y_test_ext)
print(f'Loss: {loss}, Accuracy: {accuracy}, F1-Score: {f1_score}, Precision: {precision}, Recall: {recall}')

```

**O que está acontecendo aqui:**

- **Avaliação do Segundo Modelo:** Verificamos o desempenho do segundo modelo nos dados de teste estendidos, assim como fizemos com o primeiro modelo.

### 21. **Exemplo de Saída do Treinamento e Avaliação do Modelo Estendido**

```
Epoch 1/100
...
Loss: 0.584962010383606, Accuracy: 0.6700549721717834, F1-Score: [0.61723995], Precision: 0.7345695495605469, Recall: 0.5322293639183044

```

**O que está acontecendo aqui:**

- **Progresso do Treinamento e Resultados Finais:** Assim como fizemos para o primeiro modelo, vemos como o segundo modelo melhorou ao longo das épocas e quais são suas métricas finais de desempenho.

### **Resumo Geral:**

1. **Importação de Ferramentas:** Preparamos todas as ferramentas necessárias para manipular dados e construir o modelo.
2. **Carregamento e Limpeza dos Dados:** Carregamos os dados, selecionamos apenas as partes importantes e removemos informações desnecessárias.
3. **Balanceamento das Classes:** Usamos técnicas para garantir que o modelo aprenda bem ambas as classes (fraude e não fraude).
4. **Divisão dos Dados:** Separamos os dados em partes para treinar o modelo, validar durante o treinamento e testar no final.
5. **Construção e Compilação dos Modelos:** Criamos redes neurais com diferentes configurações para ver qual funciona melhor.
6. **Treinamento dos Modelos:** Alimentamos os dados no modelo para que ele aprenda a identificar fraudes.
7. **Avaliação dos Modelos:** Verificamos quão bem os modelos se saíram ao prever fraudes em novos dados.

### 22. Resultados da Avaliação do Modelo

### Modelo Original

**Conjunto de Teste:**

- **Loss:** 0.5503
- **Accuracy:** 0.6966
- **F1-Score:** 0.6145
- **Precision:** 0.8399
- **Recall:** 0.4845

**Conjunto de Validação:**

- **Loss:** 0.5497
- **Accuracy:** 0.6946
- **F1-Score:** 0.6153
- **Precision:** 0.8411
- **Recall:** 0.4851

---

### Modelo Estendido

**Conjunto de Teste:**

- **Loss:** 0.5850
- **Accuracy:** 0.6701
- **F1-Score:** 0.6172
- **Precision:** 0.7346
- **Recall:** 0.5322

**Conjunto de Validação:**

- **Loss:** 0.5851
- **Accuracy:** 0.6692
- **F1-Score:** 0.6163
- **Precision:** 0.7337
- **Recall:** 0.5312

---

### Análise dos Resultados

- O modelo original apresenta uma **precisão** (Precision) maior que o modelo estendido, indicando que ele tem um desempenho melhor em identificar corretamente as classes positivas.
- A **recall** do modelo original é inferior ao do modelo estendido, sugerindo que o modelo estendido consegue identificar uma maior proporção de instâncias positivas entre todas as instâncias que realmente pertencem à classe positiva.
- A **F1-Score** é um bom indicador para avaliar o desempenho geral, e ambos os modelos têm resultados semelhantes nesse aspecto, com o modelo estendido apresentando uma leve vantagem.

Gráfico de Perda Durante o Treinamento

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot%20(11).png" alt="Imagem de Preprocessamento">
</p>

Gráfico de Acurácia Durante o Treinamento

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot%20(12).png" alt="Imagem de Preprocessamento">
</p>

Matriz de Confusão

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot%20(13).png" alt="Imagem de Preprocessamento">
</p>

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/newplot%20(13).png" alt="Imagem de Preprocessamento">
</p>

## Conclusão

O **Modelo 1** utilizou três variáveis principais (consumo, localização e categoria), enquanto o **Modelo 2** incorporou um conjunto mais amplo de variáveis.

keyboard_arrow_down
**Justificativas de escolha**

A escolha do **Modelo 1** foi baseada em uma abordagem minimalista, visando testar a capacidade do modelo em identificar padrões de fraude utilizando um número reduzido de variáveis. Essa escolha foi feita com o objetivo de simplificar o modelo e reduzir a complexidade computacional. Por outro lado, o **Modelo 2** foi configurado para explorar a possibilidade de capturar padrões mais complexos ao incluir um conjunto mais abrangente de variáveis, buscando melhorar a performance do modelo.

### Análise dos resultados obtidos

Os resultados dos modelos mostraram uma diferença clara em termos de desempenho:

- **Modelo 1** apresentou uma acurácia em torno de 71% e um F1-Score de aproximadamente 0,65, tanto no conjunto de teste quanto no de validação. No entanto, a precisão foi alta (cerca de 82%), enquanto o recall ficou em torno de 54%. Isso indica que o modelo era bom em identificar casos positivos de fraude quando os detectava, mas falhou em identificar todos os casos de fraude, resultando em um número significativo de falsos negativos.
- **Modelo 2** superou o Modelo 1 em todas as métricas principais, alcançando uma acurácia de aproximadamente 80% e um F1-Score de 0,75 nos conjuntos de teste e validação. O modelo apresentou uma precisão semelhante (cerca de 82%), mas um recall significativamente melhorado (cerca de 69%), indicando uma capacidade maior de identificar fraudes.

### Viabilidade para o negócio

Do ponto de vista de viabilidade para o negócio, o **Modelo 2** é mais adequado devido à sua maior capacidade de detecção de fraudes, o que é crucial para a Aegea. A melhora no recall significa que o Modelo 2 é menos propenso a deixar fraudes passarem despercebidas, reduzindo o risco financeiro e aumentando a confiabilidade do sistema de detecção.

### Possíveis preocupações

Apesar da superioridade do **Modelo 2**, algumas preocupações devem ser consideradas:

1. O Modelo 2 é mais complexo devido ao maior número de variáveis utilizadas, o que pode implicar em maiores requisitos computacionais para treinamento e inferência. Em cenários de produção, isso pode resultar em tempos de resposta mais longos e maior custo operacional.
2. Embora o Modelo 2 tenha mostrado bom desempenho nos conjuntos de teste e validação, o uso de mais variáveis aumenta o risco de overfitting. Isso pode limitar a generalização do modelo para novos dados, o que é uma preocupação em ambientes de produção com dados variáveis ao longo do tempo.
3. A inclusão de muitas variáveis também pode dificultar a interpretação dos resultados e a explicação das decisões do modelo, o que pode ser problemático em cenários onde a transparência é importante, como na conformidade regulatória.

Enquanto o **"Modelo 2"** demonstra uma viabilidade superior para o negócio, é essencial balancear a necessidade de precisão e recall com as limitações práticas e operacionais, considerando também a possibilidade de ajustes futuros para mitigar os riscos identificados.

## Salvando o Modelo

```python
# Instalar as bibliotecas necessárias
!pip install joblib tensorflow-addons

import joblib
from tensorflow.keras.models import load_model

# Salvar o modelo com joblib
joblib.dump(model, 'modelo_fraude.pkl')

# Salvar o modelo Keras no formato HDF5
model.save('modelo_fraude_final.h5')  # Salva no formato HDF5

# Para carregar o modelo salvo com joblib
modelo_carregado = joblib.load('modelo_fraude.pkl')

# Para carregar o modelo Keras
modelo_keras_carregado = load_model('modelo_fraude_final.h5')

# Agora você pode usar os modelos carregados para fazer previsões ou continuar o treinamento

```

### Notas:

1. **Instalação de Pacotes**: O comando `pip install` deve ser executado em uma célula separada ou em um terminal de comando, dependendo do ambiente que você está usando. Em um Jupyter Notebook, `!pip install` instala pacotes diretamente em uma célula.
2. **Salvar e Carregar**: O `joblib` é mais adequado para salvar objetos do Python que não são especificamente modelos Keras. Para modelos Keras, use `model.save()` para salvar no formato HDF5 ou SavedModel.
3. **Carregamento**: Após salvar o modelo, usamos `joblib.load()` para o modelo salvo com `joblib` e `load_model()` para o modelo Keras.
4. **Formatos de Salvamento**: O formato `.h5` é amplamente utilizado para salvar modelos Keras. O formato SavedModel é outra opção que pode ser mais útil para alguns casos, especialmente quando se utiliza funcionalidades específicas do TensorFlow.

# 20. Análise Financeira 

### Análise Financeira e Documentação dos Custos no Combate à Fraude de Consumo de Água

A Aegea Saneamento e Participações S.A., uma das principais empresas do setor de saneamento no Brasil, enfrenta um desafio significativo relacionado às fraudes no consumo de água. As fraudes não apenas comprometem a receita da empresa, mas também afetam a qualidade dos serviços prestados, resultando em impactos financeiros e operacionais severos.  <br><br>
Este documento apresenta uma análise financeira detalhada do projeto de detecção de fraudes, destacando os custos envolvidos, a capacidade do modelo de gerar reduções de custos e o impacto esperado no negócio.


## 1. Custo do Projeto de Detecção de Fraudes

A seguir estão detalhados os custos envolvidos no desenvolvimento e implementação do projeto de detecção de fraudes para a Aegea. O foco é a alocação de recursos humanos e ferramentas necessárias para o desenvolvimento do modelo de Machine Learning que visa melhorar a eficiência na identificação de fraudes no consumo de água. A estimativa foi realizada devido à ausência de informações detalhadas sobre o investimento previsto pelo parceiro.

| **Item**                                   | **Custo mês (R$)**              |
|--------------------------------------------|---------------------------------|
| Gastos com 6 cientistas de dados júnior    | R$36.000,00 (R$6.000,00 cada (Glassdoor)) |
| Ferramentas de colaboração (Monday)        | R$276,00                        |
| Google Colab Pro (ambiente de programação) | R$304,00                        |
| Google Drive (armazenamento adicional)     | R$300,00                        |
| Internet (300 Mbps)                        | R$100,00                        |
| Licença Excel (Microsoft 365 pessoal)      | R$180,00                        |
| **Custo Total por Mês**                    | **R$37.160,00**                 |

Considerando que nosso projeto foi realizado por pessoas em nível universitário ou estagiário, podemos assumir que, com profissionais juniores especializados, o mesmo projeto poderia ser concluído em aproximadamente duas semanas a menos, ou seja, em torno de 8 semanas no total, o que equivale a cerca de dois meses.

Assim, o custo total do projeto poderia ser estipulado:

**CUSTO X MESES = TOTAL**

**R$37.160,00 X 2 = R$74.320,00**

Assim, o custo total estipulado pelo projeto é de **R$74.320,00**.

---

## 2. Capacidade do Modelo de Gerar Redução de Custos na Empresa

O maior impacto financeiro de implementar um modelo de detecção de fraudes está relacionado à redução dos custos operacionais e perdas associadas às fraudes de consumo. A seguir estão algumas das áreas onde a Aegea pode experimentar benefícios:

- **Redução nas Perdas com Fraudes**: O consumo clandestino e adulterações podem causar grandes perdas anuais à Aegea. A implementação de um modelo eficaz pode ajudar a identificar padrões suspeitos de consumo, permitindo intervenções mais rápidas e eficientes, evitando perdas financeiras significativas.
- **Otimização de Equipes de Fiscalização**: Atualmente, a Aegea possui equipes dedicadas à fiscalização de fraudes, com uma lista de alvos estabelecida diariamente. Um modelo de Machine Learning pode fornecer alvos mais precisos e assertivos, reduzindo o número de fiscalizações desnecessárias e permitindo uma atuação mais estratégica das equipes.
- **Melhora da Qualidade de Serviço**: A fraude também impacta negativamente o abastecimento de água e a qualidade do serviço, resultando em danos à rede de distribuição, vazamentos e intermitências. Reduzir fraudes pode minimizar esses problemas, reduzindo custos com manutenção e reparo de infraestrutura.

O principal objetivo deste projeto é desenvolver e implementar um modelo de Machine Learning capaz de identificar padrões de consumo suspeitos e reduzir as fraudes no consumo de água. A análise financeira busca:
- Avaliar os custos iniciais do projeto.
- Estimar a economia potencial derivada da implementação do modelo.
- Avaliar a redução do valor perdido com as fraudes.
- Identificar os benefícios operacionais e financeiros a longo prazo.


---

## 3. Economia Potencial com a Redução de Fraudes

### 3.1 Capacidade do Modelo de Gerar Redução de Custos

A implementação do modelo de detecção de fraudes possui um potencial considerável para gerar economia em várias áreas: redução nas perdas com fraudes, otimização de equipes de fiscalização, economia potencial com redução de fraudes e impacto total no negócio da Aegea.

### 3.2.1 Redução nas Perdas com Fraudes

A Aegea é líder em saneamento privado no país. Está presente em 507 cidades em 15 estados brasileiros, sendo eles Amazonas, Ceará, Espírito Santo, Maranhão, Mato Grosso, Mato Grosso do Sul, Pará, Paraná, Piauí, Rio de Janeiro, Rio Grande do Sul, Rondônia, Santa Catarina, Minas Gerais e São Paulo. Criada em 2010, atualmente detém 56% do market share do setor, atendendo mais de 31 milhões de pessoas.
A Companhia atua no gerenciamento de ativos de saneamento por meio de concessões plenas ou parciais e parcerias público-privadas (PPPs), como administradora de concessões públicas em todo processo do ciclo integral da água – abastecimento, coleta e tratamento de esgoto.
A solidez e o dinamismo da Aegea possibilitam o desenvolvimento de soluções de saneamento sob medida para os municípios, buscando sempre o cuidado com o meio ambiente e, principalmente, com a qualidade de vida da população. 

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G02/blob/main/assets/clientes_aegea.png" alt="Imagem de Preprocessamento">
</p>

Fonte: https://ri.aegea.com.br/a-aegea/historico-e-perfil-corporativo/#:~:text=A%20Companhia%20atua%20no%20gerenciamento,coleta%20e%20tratamento%20de%20esgoto.

### **Faturamento Anual e Perdas Totais:**

- **Faturamento Anual da Aegea**: R$ 20 bilhões.
- **Perda de água total estimada**: 25% do faturamento, ou seja, R$ 5 bilhões de água não faturada (perda técnica e operativa).

A Aegea, com um faturamento estimado de R$ 20 bilhões, enfrenta perdas significativas devido a diversos fatores. A perda de água é estimada em 25%, o que representa uma perda de R$ 5 bilhões relacionada à perda técnica (água não faturada ou desperdiçada pela fraude).

Se o modelo de detecção de fraudes for eficiente e conseguir reduzir as fraudes em 50%, representaria uma economia de aproximadamente R$ 2,5 bilhões por ano, ajudando a mitigar as perdas financeiras causadas pelas fraudes.

### **Perdas Mensais:**

Distribuindo essas perdas igualmente ao longo dos meses:

- **Perda total mensal devido a fraudes**: R$ 5 bilhões / 12 meses = **R$ 416,67 milhões por mês em fraudes**.

Com base na perda total mensal de R$ 416,67 milhões devido a fraudes, e considerando que o modelo de detecção de fraudes pode identificar 60% dessas fraudes, podemos calcular o valor que será recuperado mensalmente.

### **Cálculo da Receita Recuperada Mensalmente:**

- **Perda total mensal devido a fraudes**: R$ 416,67 milhões
- **Fraudes detectadas pelo modelo (60%)**:

Valor recuperado = R$ 416,67 milhões × 0,60 = R$ 250 milhões por mês

### **Cálculo da Receita Recuperada Anualmente:**

- **Valor recuperado mensalmente**: R$ 250 milhões
- **Valor recuperado anualmente**:

Valor recuperado anual = R$ 250 milhões × 12 = R$ 3 bilhões por ano

### **Resultado:**

Com o modelo de detecção de fraudes, a Aegea poderá recuperar R$ 250 milhões por mês, totalizando R$ 3 bilhões por ano.

### **Quantidade de Água Perdida (em metros cúbicos):**

Vamos assumir que o preço médio cobrado por metro cúbico de água seja de **R$ 5**.

- **Perda por fraudes (R$ 5 bilhões)**:
    - R$ 5 bilhões anuais / R$ 5 por metro cúbico ≈ **1 bilhão de metros cúbicos de água fraudados por ano**.
    - Por mês, isso representa: 1 bilhão de m³ / 12 ≈ **83,33 milhões de metros cúbicos de água fraudados**.

### **Impacto nas Residências:**

Considerando que uma residência consome em média **15 metros cúbicos de água por mês**:

- **Água perdida por fraudes em número de residências**:
    - 83,33 milhões de m³ por mês / 15 m³ por residência = **5,55 milhões de residências**.

### **Impacto de um Modelo de Prevenção de Fraudes:**

Se o modelo de prevenção de fraudes conseguir reduzir essas perdas em 50%, a economia seria:

- **Economia por ano**: **R$ 2,5 bilhões** (metade dos R$ 5 bilhões perdidos por fraudes).
- **Economia por mês**: **R$ 208,33 milhões por mês**.

### 3.2.2 Otimização de Equipes de Fiscalização

A Aegea atualmente destina recursos significativos para equipes de fiscalização. Com a implementação do modelo de Machine Learning, o foco das fiscalizações pode ser realocado para clientes identificados como de alto risco, resultando em uma redução de 50% nas fiscalizações desnecessárias. Isso não só economiza tempo, mas também recursos financeiros consideráveis.

### 3.3 Economia Potencial com a Redução de Fraudes

A tabela a seguir resume os diferentes cenários baseados em estimativas de perdas e redução de custos associados às fraudes:

| **Cenário** | **Perda Total Estimada (R$ bilhões/ano)** | **Fraudes Detectadas Atualmente (20%)** | **Fraudes Detectadas com Modelo (60%)** |
| --- | --- | --- | --- |
| **1** | R$ 1 bilhão | R$ 200 milhões | R$ 600 milhões |
| **2** | R$ 2 bilhões | R$ 400 milhões | R$ 1,2 bilhões |
| **3** | R$ 3 bilhões | R$ 600 milhões | R$ 1,8 bilhões |
| **4** | R$ 4 bilhões | R$ 800 milhões | R$ 2,4 bilhões |
| **5** | R$ 5 bilhões | R$ 1 bilhão | R$ 3 bilhões |

**3.4 Impacto Total no Negócio da Aegea**

**Comparação: Situação Atual vs. Com o Modelo**

Atualmente, a Aegea detecta apenas 20% das fraudes, o que significa que uma grande parte das fraudes passa despercebida, gerando enormes perdas financeiras. Por exemplo, em um cenário de R$ 5 bilhões de fraudes, apenas R$ 1 bilhão é identificado.  <br><br>
Com a implementação do modelo preditivo de fraudes, o percentual de detecção aumentaria para 60%. Isso significa que, em um cenário de R$ 5 bilhões de fraudes, R$ 3 bilhões seriam identificados, o que representa um aumento significativo em comparação ao atual sistema.  <br><br>
Com o modelo, a quantidade de fraudes detectadas triplica em relação à situação atual. Por exemplo, no cenário de R$ 5 bilhões, o modelo detectaria R$ 3 bilhões, em vez de R$ 1 bilhão. Essa melhoria resultaria em uma redução direta das perdas de receita, uma vez que a empresa conseguiria intervir em mais fraudes e evitar as perdas que estão sendo causadas.

**Por que o Modelo Detecta Mais?**
- Uso de Dados e Inteligência Artificial: O modelo preditivo usa grandes volumes de dados históricos e algoritmos avançados de inteligência artificial para identificar padrões de comportamento anômalos, que muitas vezes passam despercebidos no processo de detecção tradicional.
- Capacidade de Antecipação: Diferente do processo atual, o modelo é capaz de prever possíveis fraudes antes mesmo que elas ocorram, permitindo que a equipe de campo tome medidas preventivas e não apenas corretivas.
- Análise Granular e Multidimensional: O modelo analisa um conjunto mais amplo de variáveis, como padrões de consumo, geolocalização, perfis de clientes, entre outros, proporcionando uma visão mais abrangente e precisa. <br><br>
Portanto, o modelo não só detecta um volume maior de fraudes, mas também oferece uma solução mais eficiente e pró-ativa, que contribui diretamente para a diminuição das perdas de receita e melhora a qualidade dos serviços prestados pela Aegea. Isso fortalece o combate às fraudes e gera economia significativa para a empresa.

## 4. Argumentação
As fraudes no consumo de água representam um desafio significativo que impacta tanto as finanças da Aegea quanto a qualidade do serviço prestado. A adoção de um modelo de Machine Learning não apenas mitiga as perdas financeiras, mas também otimiza a alocação de recursos operacionais. <br><br>
A utilização de dados para identificar padrões de consumo suspeitos permite que a Aegea concentre suas fiscalizações onde realmente são necessárias. Isso resulta em uma maior taxa de sucesso na identificação de fraudes, melhorando a eficiência das operações e a satisfação do cliente. <br><br>
Além disso, a implementação de tecnologias inovadoras, como o Machine Learning, coloca a Aegea em uma posição de vanguarda em relação à concorrência, fortalecendo sua reputação e permitindo um crescimento sustentável.

## 5. Conclusão
Portanto, o projeto de detecção de fraudes representa uma oportunidade crucial para a Aegea Saneamento. O investimento inicial de aproximadamente R$74.320,00 é relativamente baixo em comparação com as economias potenciais anuais de até R$ 3 bilhões. Com a implementação deste modelo, a Aegea não apenas protegerá sua receita contra perdas significativas, mas também melhorará a qualidade do serviço, garantindo um abastecimento de água mais confiável e eficiente para todos os seus clientes. Este projeto, portanto, não é apenas uma medida de contenção de custos, mas um passo estratégico em direção a um futuro mais sustentável e lucrativo para a empresa. <br><br>
Logo, ao usar um modelo de detecção de fraudes, identificar melhor quem pode estar fraudando, reduzir as visitas a clientes que são honestos, economizando tempo e dinheiro, melhorar a eficiência da equipe, garantindo que o foco esteja nas verdadeiras fraudes. Assim, a empresa não só economiza dinheiro com fiscalização, mas também melhora a qualidade do serviço para todos os clientes, mantendo a água limpa e disponível para quem realmente adquire esse serviço.

---

# 21. Referências Bibliográficas

1. [Why Personas Fail - Nielsen Norman Group](https://www.nngroup.com/articles/why-personas-fail/)
2. [Research on Neural Networks - ICMC USP](https://sites.icmc.usp.br/andre/research/neural/)
3. [Video - Neural Networks](https://www.youtube.com/watch?v=4L86D_fU6sQ)
4. [PDF - Maxwell VRAC PUC-Rio](https://www.maxwell.vrac.puc-rio.br/16580/16580_4.PDF)
5. [Thesis - Lucas Francisco Amaral Orosco Pellicer Corr](https://www.teses.usp.br/teses/disponiveis/3/3139/tde-31032021-163248/publico/LucasFranciscoAmaralOroscoPellicerCorr20.pdf)
6. [Video - Neural Networks Discussion](https://www.youtube.com/watch?si=6XPbdSspZ4lRJ_LY&v=vMh0zPT0tLI&feature=youtu.be)
7. [TensorFlow CNN Tutorial](https://www.tensorflow.org/tutorials/images/cnn?hl=pt-br)
8. [Atomic Design - Brad Frost](https://atomicdesign.bradfrost.com/chapter-2/)
9. [Video - Understanding RNNs](https://www.youtube.com/watch?v=UNmqTiOnRfg)
10. [TensorFlow Guide - Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns)
11. [Video - Sequence Models](https://www.youtube.com/watch?v=YCzL96nL7j0%20e%20t=676s)
12. [PyTorch Tutorial - Sequence Models](https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html)
13. [Video - Flask REST API Tutorial](https://www.youtube.com/watch?si=PTF3z5RotwzcraJz+e+t%3D830&v=WLwjvWq0GWA&feature=youtu.be)
14. [PyTorch Tutorial - Flask REST API](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html)
15. [Introduction to Deep Learning - MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-864-deep-learning-spring-2016/)
16. [Stanford CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/)
17. [Understanding Convolutional Neural Networks with a Practical Application - Medium](https://medium.com/@csyan233/understanding-convolutional-neural-networks-with-a-practical-application-79c41b192e69)
18. [Deep Learning for NLP - Stanford](https://cs224d.stanford.edu/)
19. [Fast.ai: Practical Deep Learning for Coders](https://course.fast.ai/)
20. [Keras Documentation](https://keras.io/guides/)
21. [Building Machine Learning Powered Applications - O'Reilly](https://www.oreilly.com/library/view/building-machine-learning/9781492041199/)
22. [Web Development with Flask - Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/tutorial/)
23. [Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning - Coursera](https://www.coursera.org/learn/introduction-tensorflow)
24. [Designing Data-Intensive Applications - Martin Kleppmann](https://dataintensive.net/)
