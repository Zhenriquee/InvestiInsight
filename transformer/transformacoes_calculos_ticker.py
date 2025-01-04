import pandas as pd

class CalculosTicker:

    def variacao_percentual_preco(vl_atual_cota,vl_dia_anterior_cota):
        variacao_percentual = ((vl_atual_cota - vl_dia_anterior_cota)/vl_dia_anterior_cota) * 100
        return variacao_percentual.round(2)
    
    def valor_atual_cota(ticker_escolhido):
        vl_atual_cota = ticker_escolhido.iloc[-1]
        return vl_atual_cota.round(2)
    
    def valor_dia_anterior_cota(ticker_escolhido):
        vl_dia_anterior_cota = ticker_escolhido.iloc[-2]
        return vl_dia_anterior_cota.round(2)
    
    def valor_mes_anterior_cota(ticker_escolhido):
    
        if len(ticker_escolhido) >= 21:
            vl_dia_anterior_cota = ticker_escolhido.iloc[-21]
        else:
            vl_dia_anterior_cota = ticker_escolhido.iloc[0]  # Primeiro registro disponível
            print(f"Aviso: ticker_escolhido contém apenas {len(ticker_escolhido)} registros. Pegando o primeiro valor disponível.")
        return vl_dia_anterior_cota.round(2)

    def valor_ano_anterior_cota(ticker_escolhido):
        if len(ticker_escolhido) >= 251:
            vl_dia_anterior_cota = ticker_escolhido.iloc[-251]
        else:
            vl_dia_anterior_cota = ticker_escolhido.iloc[0]  # Primeiro registro disponível
            print(f"Aviso: ticker_escolhido contém apenas {len(ticker_escolhido)} registros. Pegando o primeiro valor disponível.")
        return vl_dia_anterior_cota.round(2)
        
    