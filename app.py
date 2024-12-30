from components import texto, input_text, kpi, grafico_linha, grafico_barra
from packages import package
from requests_html import requisicao_fundo
from extract import extracao_pdf
from transformer import transformacoes_projecao_grafico, transformacoes_calculos_ticker
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
    try:
        # Valida o ticker e inicializa a classe FundoImobiliario
        fundo = package.FundoImobiliario(ticker)

        # Inicializa os KPIs e gráficos
        col1, col2, col3 = st.columns(3)

        # Obtem os valores e variações para os KPIs
        valor_atual_cota = fundo.valor_atual_cota()
        variacao_percentual_atual = fundo.variacao_percentual_preco_atual()

        valor_mes_anterior_cota = fundo.valor_mes_anterior_cota()
        variacao_percentual_mes_anterior = fundo.variacao_percentual_preco_mes_anterior()

        valor_ano_anterior_cota = fundo.valor_ano_anterior_cota()
        variacao_percentual_ano_anterior = fundo.variacao_percentual_preco_ano_anterior()

        # Exibe os KPIs
        with col1:
            kpi.kpi_vl_atual_cota(valor_atual_cota, variacao_percentual_atual)
        with col2:
            kpi.kpi_vl_mes_anterior_cota(valor_mes_anterior_cota, variacao_percentual_mes_anterior)
        with col3:
            kpi.kpi_vl_ano_anterior_cota(valor_ano_anterior_cota, variacao_percentual_ano_anterior)

        # Opções de visualização
        opcao_visualizacao = st.radio(
            "Deseja visualizar por:",
            ["1 Mês", "1 Ano"],
            horizontal=True,
        )

        if opcao_visualizacao == "1 Mês":
            dataset_1_mes = fundo.evolucao_preco_grafico_linha_1_mes()
            grafico_linha.GraficoLinha.grafico_linha_evolucao_1_mes(dataset_1_mes)
        else:    
            dataset_1_ano = fundo.evolucao_preco_grafico_linha_1_ano()
            grafico_linha.GraficoLinha.grafico_linha_evolucao_1_mes(dataset_1_ano)

        dataframe_dividendos_transformado = fundo.evolucao_dividendos_grafico_barra()
        grafico_barra.Grafico_Barra.grafico_barra_comparacao_dividendos(dataframe_dividendos_transformado)

        calculo_transformado_rsi = fundo.evolucao_preco_fii_grafico_linha_rsi()
        grafico_linha.GraficoLinha.grafico_rsi(calculo_transformado_rsi, ticker)

        calculo_transformado_macd, calculo_transformado_sinal_linha = fundo.evolucao_preco_fii_grafico_linha_macd()
        grafico_linha.GraficoLinha.grafico_macd(calculo_transformado_macd, calculo_transformado_sinal_linha, ticker)

        linha_central, close = fundo.evolucao_preco_fii_grafico_linha_bandas_de_bollinger_sma()
        upper, lower = fundo.evolucao_preco_fii_grafico_linha_bandas_de_bollinger_upper_lower()
        grafico_linha.GraficoLinha.grafico_bandas_de_bollinger(close, linha_central, upper, lower, ticker)

        # Gerar Resumo
        if st.button("Gerar Resumo do Relatório"):
            progress_bar = st.progress(0)
            for i in range(1, 101, 20):
                time.sleep(0.5) 
                progress_bar.progress(i)

            resumo_gemini = fundo.analise_gemini(nivel_complexidade, nivel_detalhamento)
            progress_bar.progress(100)
            st.success("Resumo gerado com sucesso!")
            st.markdown(resumo_gemini)

    except ValueError as e:
        # Caso haja erro, exibe a mensagem no Streamlit
        st.error(str(e))
