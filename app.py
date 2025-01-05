from components import texto, input_text, kpi, grafico_linha, grafico_barra,sidebar,radio
from packages import package
import streamlit as st
import time

st.set_page_config(layout="wide")
# Espaço reservado para o título
titulo_placeholder = st.empty()

# Exibir o título inicial
titulo_placeholder.title("Seja Bem vindo ao Projeto InvestiInsight")

with st.sidebar:    
    ticker = input_text.Campo_texto.text_input().upper()
    nivel_complexidade = sidebar.Sidebar.nivel_complexidade()
    nivel_detalhamento = sidebar.Sidebar.nivel_detalhamento()

if not ticker:
    st.warning("Por favor, informe o ticker desejado no campo à esquerda.")
else:
    try:
        fundo = package.FundoImobiliario(ticker)
        titulo_placeholder.empty()
        html_formatado = fundo.informacoes_detalhadas_fii()
        texto.Texto.titulo(ticker, html_formatado)

        # Inicializa os KPIs e gráficos
        col1, col2, col3 = st.columns(3)

        # Obtem os valores e variações para os KPIs
        valor_atual_cota = fundo.valor_atual_cota()
        variacao_percentual_atual = fundo.variacao_percentual_preco_atual()

        valor_mes_anterior_cota = fundo.valor_mes_anterior_cota()
        variacao_percentual_mes_anterior = fundo.variacao_percentual_preco_mes_anterior()

        valor_ano_anterior_cota = fundo.valor_ano_anterior_cota()
        variacao_percentual_ano_anterior = fundo.variacao_percentual_preco_ano_anterior()

        with col1:
            kpi.kpi_vl_atual_cota(valor_atual_cota, variacao_percentual_atual)
        with col2:
            kpi.kpi_vl_mes_anterior_cota(valor_mes_anterior_cota, variacao_percentual_mes_anterior)
        with col3:
            kpi.kpi_vl_ano_anterior_cota(valor_ano_anterior_cota, variacao_percentual_ano_anterior)
        opcao_visualizacao = radio.Radio.opcoes_visualizacao()

        if opcao_visualizacao == "1 Mês":
            dataset_1_mes = fundo.evolucao_preco_grafico_linha_1_mes()
            grafico_linha.GraficoLinha.grafico_linha_evolucao_1_mes(dataset_1_mes)
        else:    
            dataset_1_ano = fundo.evolucao_preco_grafico_linha_1_ano()
            grafico_linha.GraficoLinha.grafico_linha_evolucao_1_mes(dataset_1_ano)

        
        dataframe_dividendos_transformado = fundo.evolucao_dividendos_grafico_barra()
        grafico_barra.Grafico_Barra.grafico_barra_comparacao_dividendos(dataframe_dividendos_transformado)

        calculo_transformado_rsi = fundo.evolucao_preco_fii_grafico_linha_rsi()
        calculo_transformado_macd, calculo_transformado_sinal_linha = fundo.evolucao_preco_fii_grafico_linha_macd()
        linha_central, close = fundo.evolucao_preco_fii_grafico_linha_bandas_de_bollinger_sma()
        upper, lower = fundo.evolucao_preco_fii_grafico_linha_bandas_de_bollinger_upper_lower()
        resumo_macd = fundo.resumo_analitico_macd()
        resumo_rsi = fundo.resumo_analitico_rsi()
        resumo_bollinger = fundo.resumo_analitico_bandas_de_bollinger()

        graf1,graf2,graf3 = st.tabs(["📈 RSI","📈 MACD","📈 Bollinger"])
        with graf1:
            grafico_linha.GraficoLinha.grafico_rsi(calculo_transformado_rsi, ticker)
            with st.expander("Explicação Grafico RSI"):
                 texto.Markdown.explicacao_grafico_rsi()
        with graf2:
            grafico_linha.GraficoLinha.grafico_macd(calculo_transformado_macd, calculo_transformado_sinal_linha, ticker)
            with st.expander("Explicação Grafico MACD"):
                texto.Markdown.explicacao_grafico_macd()
            
        with graf3:
            grafico_linha.GraficoLinha.grafico_bandas_de_bollinger(close, linha_central, upper, lower, ticker)
            with st.expander("Explicação Grafico Bandas de Bollinger"):
                texto.Markdown.explicacao_grafico_bandas_de_bollinger()
            
        tex1, tex2, tex3 = st.columns(3)
        with tex1:
            with st.expander(f'Resumo Analitico MACD com Relação ao Fundo {ticker}'): 
                st.markdown(resumo_macd)
        with tex2:
            with st.expander(f'Resumo Analitico RSI com Relação ao Fundo {ticker}'):
                 st.markdown(resumo_rsi) 
        with tex3:
            with st.expander(f'Resumo Analitico Bandas de Bollinger com Relação ao Fundo {ticker}'):
                st.markdown(resumo_bollinger)        

        st.markdown("## Informações Gerais sobre o Fundo")
        kpi.kpis_informacoes_gerais(html_formatado)
        st.markdown("## Resumo")
        st.markdown("Aqui você pode gerar um resumo do ultimo relatório gerencial.")

        if st.button("Gerar Resumo do Relatório"):
            progress_bar = st.progress(0)
            for i in range(1, 101, 20):
                time.sleep(0.5) 
                progress_bar.progress(i)

            resumo_gemini = fundo.analise_gemini(nivel_complexidade, nivel_detalhamento)
            progress_bar.progress(100)
            st.success("Resumo gerado com sucesso!")
            st.markdown(resumo_gemini)

        resumo_macd = fundo.resumo_analitico_macd()
        st.markdown(resumo_macd)
    
    except ValueError as e:
        st.error(str(e))
