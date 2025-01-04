from streamlit import radio

class Radio:
    def opcoes_visualizacao():
        opcao_visualizacao = radio(
            "Deseja visualizar por:",
            ["1 Mês", "1 Ano"],
            horizontal=True,
        )
        return opcao_visualizacao
    
    