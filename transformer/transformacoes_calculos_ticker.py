class CalculosTicker:

    def variacao_percentual_preco_atual(vl_atual_cota,vl_dia_anterior_cota):
        variacao_percentual = ((vl_atual_cota - vl_dia_anterior_cota)/vl_dia_anterior_cota) * 100
        return variacao_percentual.round(2)