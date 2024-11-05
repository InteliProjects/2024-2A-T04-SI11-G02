# Novo frontend com funções de pré-processamento integradas
import streamlit as st
import pandas as pd
import requests
import numpy as np
import sys
import os

# Adicionar o caminho do diretório 'backend/app' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app')))

# URL da API FastAPI
API_URL = 'http://localhost:8000/predict'

# Enviar dados de consumo para a API FastAPI
def obter_predicao(dados):
    response = requests.post(API_URL, json={"dados": dados})
    if response.status_code == 200:
        return response.json()["predictions"]
    else:
        # Mostrar a mensagem de erro detalhada
        raise Exception(f"Erro ao obter predição: {response.status_code} - {response.text}")

# Definição do layout da página
st.set_page_config(page_title="Predição de Fraudes", layout="wide")

# Estilização dos elementos
st.markdown("""
    <style>
    /* Garantir que todas as abas tenham o mesmo tamanho */
    .stTabs [data-baseweb="tab"] {
        background-color: #cbe2eb;
        color: #2e647b;
        border-radius: 8px 8px 0 0;
        padding: 10px;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: #add8e6;
    }

    .stTabs [aria-selected="true"] {
        background-color: #62a6c7;
        color: white;
    }

    /* Estilo dos cards */
    .card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-size: 24px;
        color: #333333;
    }

    .card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        margin-bottom: 20px;
    }

    /* Estilizando botões */
    .stButton button {
        background-color: #1A73E8;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
    }

    .stButton button:hover {
        background-color: #0F5BB3;
    }

    </style>
""", unsafe_allow_html=True)

# Inicializando estados
if 'dados_pre_processados' not in st.session_state:
    st.session_state.dados_pre_processados = None
if 'erro_ao_carregar' not in st.session_state:
    st.session_state.erro_ao_carregar = False
if 'arquivo_carregado' not in st.session_state:
    st.session_state.arquivo_carregado = False
if 'df_dados' not in st.session_state:
    st.session_state.df_dados = None

# Criar o contêiner da página
st.markdown('<div class="page-container">', unsafe_allow_html=True)

# Criar as abas
abas = st.tabs(["Upload de dados", "Modelo de previsão"])

# Conteúdo da Aba 1 - Upload de dados
with abas[0]:
    st.title("Inserção de dados de consumo")
    st.write("Nesta etapa, você deve adicionar os dados de consumo referentes aos últimos 6 meses.")

    if st.session_state.erro_ao_carregar:
        st.markdown('<div class="erro">❌ Falha na importação do arquivo<br>Para tentar novamente, basta buscar um novo arquivo.</div>', unsafe_allow_html=True)
    else:
        uploaded_files = st.file_uploader("Carregar arquivos", type=["csv", "xlsx"], accept_multiple_files=False)

        if uploaded_files:
            st.session_state.arquivo_carregado = True
            st.success(f"Arquivo {uploaded_files.name} carregado com sucesso!")
        else:
            st.session_state.arquivo_carregado = False

        st.markdown("Para dar início ao processo de predição de fraudes, é necessário carregar os dados.")

        if st.session_state.dados_pre_processados is None:
            if st.button("Iniciar pré-processamento", disabled=not st.session_state.arquivo_carregado):
                try:
                    # Verifica a extensão do arquivo e faz a leitura adequada
                    if uploaded_files.name.endswith('.csv'):
                        try:
                            df_consumo = pd.read_csv(uploaded_files, sep=',')  
                        except:
                            df_consumo = pd.read_csv(uploaded_files, sep=';')  
                    elif uploaded_files.name.endswith('.xlsx'):
                        df_consumo = pd.read_excel(uploaded_files)
                    
                    # Armazena os dados originais para visualização
                    st.session_state.df_dados = df_consumo  
                    
                    st.session_state.dados_pre_processados = df_consumo
                    st.session_state.erro_ao_carregar = False
                except Exception as e:
                    st.session_state.erro_ao_carregar = True
                    st.session_state.dados_pre_processados = None
                    st.session_state.df_dados = None
                    st.error(f"Ocorreu um erro durante o carregamento dos dados: {e}")

        if st.session_state.dados_pre_processados is not None:
            st.subheader(f"Dados carregados")
            st.write(st.session_state.dados_pre_processados)
            
# Conteúdo da Aba 2 - Modelo de Previsão
with abas[1]:
    st.title("Resultados do modelo de previsão")
    if st.session_state.df_dados is None:
        st.warning("Nenhum dado carregado ainda. Por favor, vá para a aba 'Upload de dados' para carregar um arquivo.")
    else:
        st.write("Nesta seção, é possível visualizar os principais resultados do modelo de previsão de fraudes.")

        if st.session_state.dados_pre_processados is not None:
            dados_para_predicao = st.session_state.dados_pre_processados.to_dict(orient="records")
            
            # Obter a predição através da API
            try:
                resposta_api = obter_predicao(dados_para_predicao)
                predicoes = [item['fraude_predita'] * 100 for item in resposta_api if 'fraude_predita' in item]
                if predicoes:
                    st.subheader("Previsão de fraudes")
                    if len(predicoes) == len(st.session_state.dados_pre_processados):
                        resultado = st.session_state.dados_pre_processados.copy()
                        resultado['PREDICAO'] = predicoes
                        def highlight_rows(row):
                            if row['PREDICAO'] > 50:
                                return ['background-color: #ffcccc; color: #8b0000'] * len(row)
                            else:
                                return ['background-color: #ccffcc; color: #006400'] * len(row)
                        styled_result = resultado.head(100).style.apply(highlight_rows, axis=1)
                        st.write(styled_result)
                    else:
                        st.error("Erro: O número de previsões retornadas não corresponde ao número de registros de entrada.")
                else:
                    st.warning("Não foi possível gerar predições para os dados fornecidos.")
            except Exception as e:
                st.error(f"Erro ao obter predições (app.py): {e}")

st.markdown('</div>', unsafe_allow_html=True)