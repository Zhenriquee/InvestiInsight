from streamlit import text_input


class Campo_texto:

    def text_input():
        valor_texto = text_input(label="Digite um Fundo Imobiliario")
        return valor_texto
