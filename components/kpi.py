from streamlit import metric

def kpi_vl_atual_cota(valor_atual_cota,variacao):
    valor_cota = metric(label="Valor Atual da Cota", value= f"R$ {valor_atual_cota}", delta=f"{variacao} %" )
    return valor_cota

def kpi_vl_mes_anterior_cota(valor_mes_anterior_cota,variacao):
    valor_cota = metric(label="Valor Mês Anterior da Cota", value= f"R$ {valor_mes_anterior_cota}", delta=f"{variacao} %")
    return valor_cota

def kpi_vl_ano_anterior_cota(valor_mes_anterior_cota,variacao):
    valor_cota = metric(label="Valor Mês Anterior da Cota", value= f"R$ {valor_mes_anterior_cota}", delta=f"{variacao} %")
    return valor_cota

def kpi_vl_ano_anterior_cota(valor_mes_anterior_cota,variacao):
    valor_cota = metric(label="Valor Ano Anterior da Cota", value= f"R$ {valor_mes_anterior_cota}", delta=f"{variacao} %")
    return valor_cota