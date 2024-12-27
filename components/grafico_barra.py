import plotly.graph_objects as go
from streamlit import plotly_chart

class Grafico_Barra:

    def grafico_barra_comparacao_dividendos(dividendos_df):

        anos_disponiveis = dividendos_df["Ano"].unique()
        ultimo_ano, penultimo_ano = sorted(anos_disponiveis)[-2:]

        dados_ultimo_ano = dividendos_df[dividendos_df["Ano"] == ultimo_ano]
        dados_penultimo_ano = dividendos_df[dividendos_df["Ano"] == penultimo_ano]

    
        dados_ultimo_ano = dados_ultimo_ano.groupby("Mes", observed=False)["Dividend"].sum()
        dados_penultimo_ano = dados_penultimo_ano.groupby("Mes", observed=False)["Dividend"].sum()

    
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
        ]
        dados_ultimo_ano = dados_ultimo_ano.reindex(meses, fill_value=0)
        dados_penultimo_ano = dados_penultimo_ano.reindex(meses, fill_value=0)


        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=meses,
                y=dados_ultimo_ano,
                name=f"{ultimo_ano}",
                marker_color="royalblue",
                text=[f"R${v:.2f}" for v in dados_ultimo_ano],
                textposition="auto",
                width=0.4,
                hoverinfo="x+y", 
                hovertemplate='<b>%{x}</b><br>Dividendos: <b>R$ %{y:.2f}</b>',
            )
        )
        fig.add_trace(
            go.Bar(
                x=meses,
                y=dados_penultimo_ano,
                name=f"{penultimo_ano}",
                marker_color="orange",
                text=[f"R${v:.2f}" for v in dados_penultimo_ano],
                textposition="auto",
                width=0.4,
                hoverinfo="x+y",  
                hovertemplate='<b>%{x}</b><br>Dividendos: <b>R$ %{y:.2f}</b>',
            )
        )

        fig.update_layout(
            title="Comparativo de Dividendos Mensais por Ano",
            xaxis_title="Mês",
            yaxis_title="Dividendos (R$)",
            barmode="group", 
            xaxis=dict(tickangle=45),
            template="plotly_white",
            hovermode="x unified", 
        )

        return plotly_chart(fig)