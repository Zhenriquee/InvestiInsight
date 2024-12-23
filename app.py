from components import texto,input_text,kpi
from packages import package
from requests_html import requisicao_fundo
from extract import extracao_pdf
from transformer import transformacoes_calculos_ticker
import streamlit as st

texto.Texto.titulo()

with st.sidebar:
    ticker = input_text.Campo_texto.text_input()
    nivel_complexidade = st.selectbox(
        'Qual seria seu nível de conhecimento:',
        ('Iniciante', 'Intermediário', 'Avançado')
    )
    nivel_detalhamento = st.selectbox(
        'Escolha o nível de detalhamento do resumo:',
        ('Informações Principais', 'Resumo', 'Resumo Detalhado')
    )

if not ticker:
    st.warning("Por favor, informe o ticker desejado no campo à esquerda.")
else:
    valor_atual_cota = package.pkg_vl_atual_cota(ticker)
    variacao_percentual = package.pkg_variacao_percentual_preco_atual(ticker)
    kpi.kpi_vl_atual_cota(valor_atual_cota, variacao_percentual)

    if st.button("Gerar Resumo Gemini"):
        resumo_gemini = package.pkg_analise_gemini(ticker, nivel_complexidade, nivel_detalhamento)
        st.markdown(resumo_gemini)