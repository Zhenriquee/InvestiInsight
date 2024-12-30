import pandas as pd

class TransformacaoGraficoLinha:

    def converter_indice_do_mes_para_string(ticker):
        ultimo_dia_mes = ticker.index[-1] - pd.DateOffset(months=1)
        datas_1_mes = ticker[ticker.index >= ultimo_dia_mes]
        datas_1_mes = datas_1_mes.copy()
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
    
class TransformacaoGraficoRSI:

    def calculo_rsi(dataset, window=14):
        delta = dataset.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
class TransformacaoGraficoMACD:
    def calculo_macd(dataset, slow=26, fast=12, signal=9):
        exp1 = dataset.ewm(span=fast, adjust=False).mean()
        exp2 = dataset.ewm(span=slow, adjust=False).mean()
        macd = exp1 - exp2
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        return macd, signal_line
    
class TransformacaoGraficoBandasDeBollinger:

    def calculate_sma(dataset, window=20):
        sma = dataset.rolling(window=window).mean()
        close = dataset
        return sma,close
    

    def calculate_bollinger_bands(data, window=20, num_std_dev=2):
        rolling_mean = data.rolling(window=window).mean()
        rolling_std = data.rolling(window=window).std()
        upper_band = rolling_mean + (rolling_std * num_std_dev)
        lower_band = rolling_mean - (rolling_std * num_std_dev)
        return lower_band, upper_band