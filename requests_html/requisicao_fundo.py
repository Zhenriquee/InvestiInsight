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
       
        if not ticker.endswith('11'):
            raise ValueError("Ticker inválido. Apenas fundos imobiliários (que terminam com '11') são aceitos.")

        try:
            fii = yf.Ticker(ticker + '.SA')
           
            if fii.history(period="5D").empty:
                raise ValueError("Ticker não encontrado em nossa base de dados.")
            return fii
        except Exception as e:
            raise ValueError(f"Erro ao buscar ticker: {str(e)}")
        
    def requisicao_detalhada_fii(ticker):
        try:
            url = "https://investidor10.com.br/fiis/"+ticker
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                resposta = response
            else: 
                resposta = ("Nao encontramos nada aqui")
            return resposta
        except Exception as e:
            excecao = "Não encontramos esse fundo imobiliario: "+ e
            return excecao    
    