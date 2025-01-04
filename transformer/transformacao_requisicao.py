from bs4 import BeautifulSoup
import re
import base64
from io import BytesIO
from PyPDF2 import PdfReader

class Transformar:

    def organizar_html(requisicao):
        html_fundo_imobiliario = requisicao
        html_formatado = BeautifulSoup(html_fundo_imobiliario.text,'html.parser')
        return html_formatado
    
    def localiza_div_relatorio(html_formatado):
        localiza_div = html_formatado.find_all("div", class_="communicated__grid__row")
        relatorios = []

        for div in localiza_div:
                text = div.get_text()
                if "Relatório Gerencial" in text:
                    match = re.search(r'(\d{2}/\d{4})', text)
                    if match:
                        capitura_link = div.find("a", href= True)
                        link = capitura_link['href'] if capitura_link else "Link não encontrado"
                        relatorios.append((text, match.group(1), link))
        if relatorios:
                maior_competencia = max(relatorios, key=lambda x: x[1])
                link_pdf = maior_competencia[2]
        else:
                link_pdf = 'Relatório não encontrado galera =/'
        return link_pdf
    
    def decode_base_64(requisicao_relatorio):
        pdf_content = base64.b64decode(requisicao_relatorio.text)
        pdf_file = BytesIO(pdf_content)
        pdf_reader = PdfReader(pdf_file)
        return pdf_reader
    
    def organizar_detalhamento_informacoes_fii(requisicao_detalhada):
        html_detalhado = requisicao_detalhada
        html_formatado = BeautifulSoup(html_detalhado.text,'html.parser')
        all_reports = html_formatado.find_all("div", class_="value")
        extracted_data = [report.get_text(strip=True) for report in all_reports]
        labels = [
            "Razão Social", "CNPJ", "Público-Alvo", "Mandato", "Segmento", "Tipo de Fundo",
            "Prazo de Duração", "Tipo de Gestão", "Taxa de Administração", "Vacância",
            "Número de Cotistas", "Cotas Emitidas", "Valor Patrimonial por Cota",
            "Valor Patrimonial", "Último Rendimento"
        ]
        data_dict = dict(zip(labels, extracted_data[:len(labels)]))
        return data_dict