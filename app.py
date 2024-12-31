from components import texto, input_text, kpi, grafico_linha, grafico_barra
from packages import package
from requests_html import requisicao_fundo
from extract import extracao_pdf
from transformer import transformacoes_projecao_grafico, transformacoes_calculos_ticker
import streamlit as st
import time
import streamlit.components.v1 as components

# Script para injetar a tag <meta> no <head>
inject_meta_script = """
<script>
    const meta = document.createElement('meta');
    meta.name = 'monetag';
    meta.content = '6c2d4c36a04f2a0d19370e98acb224ce';
    document.getElementsByTagName('head')[0].appendChild(meta);
</script>
"""

# Renderizando o script
components.html(inject_meta_script, height=0)


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

        graf1,graf2,graf3 = st.tabs(["📈 RSI","📈 MACD","📈 Bollinger"])
        with graf1:
            calculo_transformado_rsi = fundo.evolucao_preco_fii_grafico_linha_rsi()
            grafico_linha.GraficoLinha.grafico_rsi(calculo_transformado_rsi, ticker)
            with st.expander("Explicação Grafico RSI"):
                st.markdown(''' O **RSI**  (**Relative Strength Index**) é um indicador de momentum que mede a velocidade e a mudança dos movimentos de preços. Ele ajuda a identificar condições de **sobrecompra** ou **sobrevenda** de um ativo.

### Cálculo:
\[
RSI = 100 - {100}/{1 + RS}
\]
Onde **RS** é a média dos fechamentos em alta dividida pela média dos fechamentos em baixa.

### Análise:
- **Sobrecompra (>70):** Pode indicar que o ativo está sobrecomprado e que o preço pode cair em breve.
- **Sobrevenda (<30):** Pode indicar que o ativo está sobrevendido e que o preço pode subir em breve.
- **Reversão em torno de 50:** Pode indicar uma possível mudança na direção do preço.


'''
                            )

        with graf2:
            calculo_transformado_macd, calculo_transformado_sinal_linha = fundo.evolucao_preco_fii_grafico_linha_macd()
            grafico_linha.GraficoLinha.grafico_macd(calculo_transformado_macd, calculo_transformado_sinal_linha, ticker)
            with st.expander("Explicação Grafico MACD"):
                st.markdown('''O **MACD** (**Moving Average Convergence Divergence**) é um indicador de tendência que analisa a relação entre duas médias móveis exponenciais (EMAs) para identificar pontos de compra e venda.

### Cálculo:
\[
MACD = EMA(12) - EMA(26)
\]
- **Linha de sinal:** EMA de 9 períodos do MACD.
- **Histograma:** Diferença entre o MACD e a linha de sinal.

### Análise:
- **Cruzamento de linhas:**
  - **MACD cruza acima da linha de sinal:** Sinal de compra.
  - **MACD cruza abaixo da linha de sinal:** Sinal de venda.
- **Divergência:**
  - Se o preço faz novos máximos, mas o MACD não acompanha, pode ser sinal de fraqueza na tendência de alta (e vice-versa para a baixa).
- **Histograma:**
  - Indica a força da tendência. Um histograma crescente sinaliza tendência forte, enquanto um histograma decrescente pode indicar fraqueza.

''')

        with graf3:
            linha_central, close = fundo.evolucao_preco_fii_grafico_linha_bandas_de_bollinger_sma()
            upper, lower = fundo.evolucao_preco_fii_grafico_linha_bandas_de_bollinger_upper_lower()
            grafico_linha.GraficoLinha.grafico_bandas_de_bollinger(close, linha_central, upper, lower, ticker)
            with st.expander("Explicação Grafico Bandas de Bollinger"):
                st.markdown('''As **Bandas de Bollinger** são compostas por uma média móvel simples (SMA) e duas bandas baseadas no desvio padrão, que ajudam a medir a volatilidade do mercado.

### Cálculo:
\[
Banda Superior = SMA + (2 \times SD)
\]
\[
Banda Inferior = SMA - (2 \times SD)
\]

### Análise:
- **Preços tocando a banda superior:** Indicam possível condição de sobrecompra.
- **Preços tocando a banda inferior:** Indicam possível condição de sobrevenda.
- **Squeeze (estreitamento das bandas):** Pode sinalizar baixa volatilidade, antecipando um movimento significativo de preço.
- **Expansão das bandas:** Indica alta volatilidade, sugerindo que o ativo pode estar em uma forte tendência.

---

### Resumo:
- **RSI:** Mede sobrecompra (>70) e sobrevenda (<30) e pode antecipar reversões.
- **MACD:** Identifica tendências e cruzamentos (compra ou venda).
- **Bandas de Bollinger:** Indicam volatilidade e condições extremas de preço (sobrecompra/sobrevenda).

''')


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
