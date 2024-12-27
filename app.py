from components import texto,input_text,kpi,grafico_linha, grafico_barra
from packages import package
from requests_html import requisicao_fundo
from extract import extracao_pdf
from transformer import transformacoes_projecao_grafico,transformacoes_calculos_ticker
import streamlit as st
import time
st.set_page_config(layout="wide")

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
    col1, col2, col3 = st.columns(3)

    valor_atual_cota = package.pkg_vl_atual_cota(ticker)
    variacao_percentual_atual = package.pkg_variacao_percentual_preco_atual(ticker)

    valor_mes_anterior_cota = package.pkg_vl_mes_anterior_cota(ticker)
    variacao_percentual_mes_anterior = package.pkg_variacao_percentual_preco_mes_anterior(ticker)

    valor_ano_anterior_cota = package.pkg_vl_ano_anterior_cota(ticker)
    variacao_percentual_ano_anterior = package.pkg_variacao_percentual_preco_ano_anterior(ticker)

    with col1:
        kpi.kpi_vl_atual_cota(valor_atual_cota, variacao_percentual_atual)
    with col2:
        kpi.kpi_vl_mes_anterior_cota(valor_mes_anterior_cota,variacao_percentual_mes_anterior)
    with col3:
        kpi.kpi_vl_ano_anterior_cota(valor_ano_anterior_cota, variacao_percentual_ano_anterior)

#--------------------------------------------#
    opcao_visualizacao = st.radio(
        "Deseja visualizer por:",
        ["1 Mês", "1 Ano"],
        horizontal= True,)
    
    if opcao_visualizacao == "1 Mês":
        dataset_1_mes = package.pkg_evolucao_preco_grafico_linha_1_mes(ticker)
        grafico_linha.GraficoLinha.grafico_linha_evolucao_1_mes(dataset_1_mes)
    else:    
        dataset_1_ano = package.pkg_evolucao_preco_grafico_linha_1_ano(ticker)
        grafico_linha.GraficoLinha.grafico_linha_evolucao_1_mes(dataset_1_ano) 

    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    dataframe_dividendos = extracao_pdf.Extrair.historico_dividendos_fundo_imobiliario(ticker_selecionado)
    dataframe_dividendos_transformado = transformacoes_projecao_grafico.TransformacaoGraficoBarra.dividendos_mes_ano(dataframe_dividendos)
    grafico_barra.Grafico_Barra.grafico_barra_comparacao_dividendos(dataframe_dividendos_transformado)

    if st.button("Gerar Resumo Gemini"):
        
        progress_bar = st.progress(0)

        for i in range(1, 101, 20):
            time.sleep(0.5) 
            progress_bar.progress(i)

        resumo_gemini = package.pkg_analise_gemini(ticker, nivel_complexidade, nivel_detalhamento)
        
        progress_bar.progress(100)
        st.success("Resumo Gemini gerado com sucesso!")
        
        st.markdown(resumo_gemini)