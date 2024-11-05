# Detalhamento da solução desenvolvida.
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
