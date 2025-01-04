from streamlit import metric, markdown

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

def kpis_informacoes_gerais(informacoes):
    custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

    .info-box {
        padding: 0;
        margin-bottom: 20px;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
    }

    .info-container {
        display: flex;
        flex-wrap: wrap;
        gap: 15px; /* Espaçamento entre os itens */
    }

    .info-item {
        flex: 1 1 calc(33.333% - 15px); /* 3 itens por linha com espaçamento */
        margin: 0;
        padding: 15px;
        font-size: 1em;
        border-radius: 12px;
        background: linear-gradient(145deg, #1e1e2f, #252537);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
    }

    .info-item:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.6), 0 0 10px rgba(0, 200, 255, 0.6);
    }

    .info-item span {
        font-weight: 500;
        color: rgba(255, 255, 255, 0.8);
        margin-right: 5px;
    }

    .info-item .value {
        font-weight: bold;
        color: #ffffff;
    }

    /* Efeito de luz neon no hover */
    .info-item::before {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 12px;
        padding: 2px;
        background: linear-gradient(145deg, rgba(0, 200, 255, 0.8), rgba(0, 255, 200, 0.8));
        opacity: 0;
        z-index: -1;
        transition: opacity 0.3s ease;
    }

    .info-item:hover::before {
        opacity: 1;
    }

    /* Responsividade para dispositivos menores */
    @media (max-width: 768px) {
        .info-item {
            flex: 1 1 calc(50% - 10px); /* 2 itens por linha */
        }
    }

    @media (max-width: 480px) {
        .info-item {
            flex: 1 1 100%; /* 1 item por linha */
        }
    }
</style>
"""
        # Adicionar CSS ao Streamlit
    markdown(custom_css, unsafe_allow_html=True)

        # Gerar o conteúdo da div com os dados
    html_content = '<div class="info-box">'
    html_content += '<div class="info-container">'

    for key, value in informacoes.items():
        if key not in ["Razão Social", "CNPJ","Mandato","Público-Alvo"]:
         html_content += f'<div class="info-item"><span>{key}:</span> <span class="value">{value}</span></div>'

    html_content += '</div>'  # Fechar o container
    html_content += '</div>'  # Fechar a info-box

        # Exibir a div no Streamlit
    resultado = markdown(html_content, unsafe_allow_html=True)
    return resultado