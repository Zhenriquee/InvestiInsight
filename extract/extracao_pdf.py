class Extrair:

    def informacoes_pdf(relatorio_formatado):
        texto = ""
        for page in relatorio_formatado.pages:
                texto += page.extract_text()
        return texto
    

    def valor_atual_cota(ticker_escolhido):
        vl_atual_cota = ticker_escolhido.history(period="5d")['Close'][-1]
        return vl_atual_cota.round(2)
    
    def valor_dia_anterior_cota(ticker_escolhido):
        vl_dia_anterior_cota = ticker_escolhido.history(period="5d")['Close'][-2]
        return vl_dia_anterior_cota.round(2)