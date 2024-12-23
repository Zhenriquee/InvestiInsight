from streamlit import metric

def kpi_vl_atual_cota(valor_atual_cota,variacao):
    valor_cota = metric(label="Valor Atual da Cota", value= f"R$ {valor_atual_cota}", delta=f"{variacao} %" )
    return valor_cota