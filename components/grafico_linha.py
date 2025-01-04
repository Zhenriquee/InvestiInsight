import plotly.graph_objects as go
from streamlit import plotly_chart
import pandas as pd



class GraficoLinha:

    def grafico_linha_evolucao_1_mes(dataset_1_mes):
        fig_1_month = go.Figure(data=go.Scatter(
        x=dataset_1_mes['Date'],
        y=dataset_1_mes['Close'],
        mode='lines+markers',
        name='Fechamento 1 Mês',
        line=dict(shape='spline', color='blue', width=3),  # Linha curva e azul
        marker=dict(color='red', size=8)  # Pontos vermelhos
    ))
        fig_1_month.update_layout(
            title="Evolução do Valor de Fechamento - Último Mês",
            xaxis_title="Data",
            yaxis_title="Fechamento (R$)",
            template="plotly_white",
            yaxis_tickformat="R$,.2f",
            
            height=750

        )
        fig_1_month.update_yaxes(tickprefix="R$ ", tickformat=".2f")

        return plotly_chart(fig_1_month)
    
    def grafico_linha_evolucao_1_ano(dataset_1_mes):
        fig_1_year = go.Figure(data=go.Scatter(
        x=dataset_1_mes['Date'],
        y=dataset_1_mes['Close'],
        mode='lines+markers',
        name='Fechamento 1 Ano',
        line=dict(shape='linear', color='green', width=3), 
        marker=dict(color='orange', size=6)
    ))
        fig_1_year.update_layout(
            title="Evolução do Valor de Fechamento - Último Ano",
            xaxis_title="Data",
            yaxis_title="Fechamento (R$)",
            template="plotly_white",
            yaxis_tickformat="R$,.2f",
            height=750
        )
        fig_1_year.update_yaxes(tickprefix="R$ ", tickformat=".2f")

        return plotly_chart(fig_1_year)
    
    def grafico_rsi(dataset_fii,ticker):
        rsi_fig = go.Figure()
        rsi_fig.add_trace(go.Scatter(x=dataset_fii.index, y=dataset_fii, mode='lines', name='RSI', line=dict(color='purple')))
        rsi_fig.add_trace(go.Scatter(x=dataset_fii.index, y=[70]*len(dataset_fii), mode='lines', name='Sobrecompra (70)', line=dict(color='red', dash='dash')))
        rsi_fig.add_trace(go.Scatter(x=dataset_fii.index, y=[30]*len(dataset_fii), mode='lines', name='Sobrevenda (30)', line=dict(color='green', dash='dash')))
        rsi_fig.update_layout(title=f'{ticker} - RSI', xaxis_title='Data', yaxis_title='RSI', template='plotly_white',height=750)
        return plotly_chart(rsi_fig)
    
    def grafico_macd(dataset_fii_macd,dataset_fii_sinal_linha,ticker):
        macd_fig = go.Figure()
        macd_fig.add_trace(go.Scatter(x=dataset_fii_macd.index, y=dataset_fii_macd, mode='lines', name='MACD', line=dict(color='blue')))
        macd_fig.add_trace(go.Scatter(x=dataset_fii_macd.index, y=dataset_fii_sinal_linha, mode='lines', name='Linha de Sinal', line=dict(color='orange')))
        macd_fig.add_trace(go.Scatter(x=dataset_fii_macd.index, y=[0]*len(dataset_fii_macd), mode='lines', name='Linha Zero', line=dict(color='red', dash='dash')))
        macd_fig.update_layout(title=f'{ticker} - MACD', xaxis_title='Data', yaxis_title='Valor', template='plotly_white',height=750)
        return plotly_chart(macd_fig)
    
    def grafico_bandas_de_bollinger(resultado_fechamento, resultado_linha_central, resultado_linha_compra, resultado_linha_venda, ticker):
    
        trace1 = go.Scatter(x=resultado_linha_central.index, 
                        y=resultado_fechamento, 
                        mode='lines', 
                        name=f'Preço de Fechamento (R$)', 
                        line=dict(color='blue'),
                        text=[f'R${x:.2f}' for x in resultado_fechamento], 
                        hovertemplate='%{text}' 
                       )
        trace2 = go.Scatter(x=resultado_linha_central.index, y=resultado_linha_central, mode='lines', name='Média Móvel (SMA)', line=dict(color='orange', dash='dash'))
        trace3 = go.Scatter(x=resultado_linha_central.index, y=resultado_linha_compra, mode='lines', name='Banda Inferior', line=dict(color='green', dash='dash'))
        trace4 = go.Scatter(x=resultado_linha_central.index, y=resultado_linha_venda, mode='lines', name='Banda superior', line=dict(color='red', dash='dash'))
        
      
        fill = go.Scatter(
            x=resultado_linha_central.index, 
            y=resultado_linha_compra, 
            mode='lines', 
            fill='tonexty', 
            fillcolor='rgba(169,169,169,0.2)',  
            line=dict(color='rgba(255,255,255,0)'),
            showlegend=False
        )
        
        # Layout do gráfico
        layout = go.Layout(
            title=f'Bandas de Bollinger - {ticker}',
            xaxis=dict(title='Data', tickformat='%m/%Y', tickmode='array'),
            yaxis=dict(title='Preço de Fechamento (R$)'),
            showlegend=True,
            template='plotly_white',  
            xaxis_tickangle=-45, 
            plot_bgcolor='rgba(0,0,0,0)',  
            height=750
        )
        fig = go.Figure(data=[trace1, trace2, trace3, trace4, fill], layout=layout)

       
        plotly_chart(fig)