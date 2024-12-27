class Extrair:

    def informacoes_pdf(relatorio_formatado):
        texto = ""
        for page in relatorio_formatado.pages:
                texto += page.extract_text()
        return texto
    
    def historico_fundo_imobiliario(ticker):
        historico = ticker.history(period="max")
        dataset = historico[['Close']].copy()
        dataset['Date'] = historico.index
        return dataset

    def historico_dividendos_fundo_imobiliario(ticker):
        historico_dividendos = ticker.dividends.resample("ME").sum()
        return historico_dividendos