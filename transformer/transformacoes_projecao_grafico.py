import pandas as pd

class TransformacaoGraficoLinha:

    def converter_indice_do_mes_para_string(ticker):
        ultimo_dia_mes = ticker.index[-1] - pd.DateOffset(months=1)
        datas_1_mes = ticker[ticker.index >= ultimo_dia_mes]
        datas_1_mes['Date'] = datas_1_mes.index.strftime("%d/%m/%Y")
        return datas_1_mes
    
    def converter_indice_do_ano_para_string(ticker):
        ultimo_ano_mes = ticker.index[-1] - pd.DateOffset(years=1)
        datas_1_ano = ticker[ticker.index >= ultimo_ano_mes]
        datas_1_ano['Date'] = datas_1_ano.index.strftime("%b %Y")
        return datas_1_ano
    
class TransformacaoGraficoBarra:

    def dividendos_mes_ano(ticker_escolhido):
        dividendos_df = ticker_escolhido.reset_index()
        dividendos_df.columns = ["Date", "Dividend"]  
        dividendos_df["Ano"] = dividendos_df["Date"].dt.year
        dividendos_df["Mes"] = dividendos_df["Date"].dt.strftime("%B")
        dividendos_df["Mes"] = pd.Categorical(
            dividendos_df["Mes"],
            categories=[
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December",
            ],
            ordered=True,
        )
        meses_portugues = {
        "January": "Janeiro", "February": "Fevereiro", "March": "Março",
        "April": "Abril", "May": "Maio", "June": "Junho",
        "July": "Julho", "August": "Agosto", "September": "Setembro",
        "October": "Outubro", "November": "Novembro", "December": "Dezembro",
            }
        dividendos_df["Mes"] = dividendos_df["Mes"].map(meses_portugues)
        
        return dividendos_df
    
