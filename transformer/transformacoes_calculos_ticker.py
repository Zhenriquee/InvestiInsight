import pandas as pd

class CalculosTicker:

    def variacao_percentual_preco(vl_atual_cota,vl_dia_anterior_cota):
        variacao_percentual = ((vl_atual_cota - vl_dia_anterior_cota)/vl_dia_anterior_cota) * 100
        return variacao_percentual.round(2)
    
    def valor_atual_cota(ticker_escolhido):
        vl_atual_cota = ticker_escolhido[-1]
        return vl_atual_cota.round(2)
    
    def valor_dia_anterior_cota(ticker_escolhido):
        vl_dia_anterior_cota = ticker_escolhido[-2]
        return vl_dia_anterior_cota.round(2)
    
    def valor_mes_anterior_cota(ticker_escolhido):
        vl_dia_anterior_cota = ticker_escolhido[-21]
        return vl_dia_anterior_cota.round(2)
    
    def valor_ano_anterior_cota(ticker_escolhido):        
        vl_dia_anterior_cota = ticker_escolhido[-251]
        return vl_dia_anterior_cota.round(2)
    
    