# Guia para Rodar o Projeto Localmente no VS Code

## 1. Pré-requisitos

Antes de começar, certifique-se de ter instalado os seguintes softwares:

- [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)
- [VS Code](https://code.visualstudio.com/) (com a extensão de Python instalada)
- [Git](https://git-scm.com/)

## 2. Estrutura do Projeto

O projeto é dividido em duas principais partes:

- **backend/**: Contém a API e a lógica do backend.
- **frontend/**: Contém a interface da aplicação.

## 3. Configuração do Ambiente Virtual

Dentro da pasta `app` do backend, já existe um ambiente virtual configurado. Para ativá-lo, siga os seguintes passos:

### No Windows:
1. Abra o terminal no VS Code.
2. Navegue até a pasta onde o ambiente está localizado:
    ```bash
    cd src/backend/app
    ```
3. Ative o ambiente virtual:
    ```bash
    .\venv\Scripts\activate
    ```

### No Linux/Mac:
1. Abra o terminal no VS Code.
2. Navegue até a pasta onde o ambiente está localizado:
    ```bash
    cd src/backend/app
    ```
3. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```

Depois de ativar o ambiente, todas as dependências já estarão disponíveis a partir do arquivo `requirements.txt`.

## 4. Rodando o Backend

### Estrutura do Backend

O backend contém a API e a lógica de processamento de dados para a aplicação. Aqui estão os principais arquivos que compõem essa parte do projeto:

- **`main.py`**: O arquivo principal da API, que contém os endpoints e a lógica para rodar o servidor usando `FastAPI` e `Uvicorn`.
- **`processing.py`**: Este arquivo contém a lógica de pré-processamento dos dados. Embora esteja implementado, a integração completa com o sistema ainda não foi finalizada. Nele, você encontra funções que manipulam e transformam os dados para serem usados no modelo de detecção de fraudes.
- **`modelo_fraude_final.h5`**: O modelo de rede neural treinado para prever fraudes. Esse modelo está salvo em formato `.h5` e é carregado pela API para realizar predições.

### Rodando o Backend

1. Abra o terminal no VS Code.
2. Navegue até a pasta da sprint 4:
    ```bash
    cd src/Sprint_4/backend/app
    ```
3. Execute o comando para iniciar o servidor da API:
    ```bash
    uvicorn main:app --reload
    ```

Isso irá iniciar o servidor da API, que pode ser acessado no navegador pelo endereço `http://127.0.0.1:8000`.

### Dicas para Navegação
- Use o comando `cd <nome_da_pasta>` para entrar em uma pasta.
- Use o comando `cd ..` para voltar uma pasta.

## 5. Rodando o Frontend

### Estrutura do Frontend

O frontend da aplicação foi desenvolvido com **Streamlit**, uma ferramenta usada para criar interfaces de dados interativas. Os arquivos mais importantes do frontend são:

- **`app.py`**: O arquivo principal que define a interface do usuário. Ele contém os elementos visuais, como botões, gráficos e entradas de dados. Este arquivo se comunica com o backend para enviar os dados e receber as predições de fraudes.
- **`.streamlit/`**: Contém configurações adicionais do Streamlit.

### Rodando o Frontend

Para rodar o frontend, você precisará abrir uma **nova janela de terminal** no VS Code. Em seguida, siga estes passos:

1. Navegue até a pasta do frontend:
    ```bash
    cd src/frontend
    ```
2. Execute o seguinte comando para iniciar o frontend com o Streamlit:
    ```bash
    streamlit run app.py
    ```

Isso vai abrir o frontend da aplicação em uma nova aba do navegador. Caso o frontend não abra automaticamente, você pode clicar no link exibido no terminal enquanto pressiona a tecla `Ctrl`.

## 6. Configuração do CSV Pré-Processado

Para rodar a aplicação corretamente, você precisa adicionar um arquivo CSV pré-processado no formato correto. Esse arquivo contém os dados que serão utilizados pela API e pelo frontend para gerar predições.

**Observação:** O arquivo `processing.py` contém a lógica para o tratamento dos dados, mas devido ao tempo, a integração completa dessa parte com a aplicação ainda não foi realizada. Portanto, é necessário garantir que o CSV esteja formatado corretamente antes de usá-lo.

## 7. Finalizando

Agora você deve ser capaz de rodar tanto o backend quanto o frontend localmente no seu VS Code! Se tiver alguma dúvida, entre em contato com o time de suporte do projeto.
