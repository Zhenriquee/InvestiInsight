from streamlit import selectbox

class Sidebar:
    def nivel_complexidade():
        nivel_complexidade = selectbox(
            'Qual seria seu nível de conhecimento:',
            ('Iniciante', 'Intermediário', 'Avançado')
        )
        return nivel_complexidade
    
    def nivel_detalhamento():
        nivel_detalhamento = selectbox(
            'Escolha o nível de detalhamento do resumo:',
            ('Informações Principais', 'Resumo', 'Resumo Detalhado')
        )
        return nivel_detalhamento
