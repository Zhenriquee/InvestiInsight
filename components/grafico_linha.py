import plotly.graph_objects as go
from streamlit import plotly_chart

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
            yaxis_tickformat="R$,.2f"
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
            yaxis_tickformat="R$,.2f"
        )
        fig_1_year.update_yaxes(tickprefix="R$ ", tickformat=".2f")

        return plotly_chart(fig_1_year)