import requests
import yfinance as yf

class Requisicao:

    def fundo_imobiliario_web(ticker):
        try:
            url = "https://www.fundsexplorer.com.br/funds/"+ticker
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                resposta = response
            else: 
                resposta = ("Nao encontramos nada aqui")
            return resposta
        except Exception as e:
            excecao = "Não encontramos esse fundo imobiliario: "+ e
            return excecao
    
    def relatorio_gerencial(relatorio):
        url = relatorio
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            resposta = response
        else: 
            resposta = ("Nao encontramos nada aqui")
        return resposta
    
    def fundo_imobiliario_biblioteca(ticker):
        fii = yf.Ticker(ticker+'.SA')
        return fii
    