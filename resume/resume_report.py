from IPython.display import display
from config import config_resume
from transformer import tranformacoes_independentes


class Resumo_texto:
    def resumo_gemini(informacoes_pdf,nivel_resumo,nivel_detalhamento):
        try:
            prompt = (
            f"Analise o seguinte relatório e produza um resumo adaptado ao nível selecionado: {nivel_resumo}. "
            f"Adapte também o nível de detalhamento conforme especificado: {nivel_detalhamento}. "
            "Ajuste a profundidade e linguagem conforme os níveis indicados: "
            "1. Nível de Resumo (Iniciante, Intermediário, Avançado): "
            "    - Iniciante: Resumo claro, acessível e didático para leitores iniciantes. "
            "    - Intermediário: Resumo com mais detalhes técnicos, para leitores com alguma experiência em fundos imobiliários. "
            "    - Avançado: Resumo aprofundado e técnico, voltado para leitores experientes. "
            "2. Nível de Detalhamento (Informações Principais, Resumo, Resumo Detalhado): "
            "    - Informações Principais: Apenas os pontos mais relevantes, sem detalhes ou explicações. "
            "    - Resumo: Um resumo conciso, com pontos principais e explicações breves. "
            "    - Resumo Detalhado: Texto abrangente, com explicações completas e aprofundadas. "
            "Independente do nível, organize o conteúdo nos seguintes tópicos:"
            "1. Resumo Geral: Visão panorâmica do relatório, destacando o contexto e os objetivos principais do fundo. "
            "2. Evolução do Fundo: Destaque a trajetória e desempenho ao longo do período analisado, apontando ganhos, perdas ou mudanças relevantes. "
            "3. Segmentação do Fundo: Explique as principais áreas de atuação ou categorias, como setores econômicos ou mercados-alvo. "
            "4. Pontos-Chave: Liste dados, tendências e eventos significativos descritos no relatório. "
            "5. Pontos Positivos e Negativos: "
            "    - Pontos Positivos: Destaque aspectos favoráveis, como crescimento ou melhorias. "
            "    - Pontos Negativos: Apresente aspectos desfavoráveis ou riscos, explicando detalhadamente suas implicações. "
            "6. Detalhes Essenciais: Explique conceitos técnicos ou termos difíceis, ajustando a profundidade ao nível de detalhamento. "
            "7. Conclusão e Recomendações: Resuma as descobertas principais e apresente sugestões ou implicações. "
            "Certifique-se de começar diretamente com o resumo, sem introduções ou explicações prévias. Ajuste o texto para clareza e formatação adequada. "
            f"Segue o relatório a ser analisado: \n\n{informacoes_pdf}")
            
            resposta = config_resume.model.generate_content(prompt)

            formato_markdown = tranformacoes_independentes.Transformacoes.texto_markdown(resposta.text)
            display(formato_markdown)
            return resposta.text
        except Exception as e:
            print("Erro ao analisar o texto com o Gemini:", e)
            return None