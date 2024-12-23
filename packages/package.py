from requests_html import requisicao_fundo
from transformer import transformacao_requisicao,transformacoes_calculos_ticker
from extract import extracao_pdf
from resume import resume_report

def pkg_analise_gemini(ticker,nivel_complexidade,nivel_detalhamento):
    requisicao = requisicao_fundo.Requisicao.fundo_imobiliario_web(ticker)
    html_formatado = transformacao_requisicao.Transformar.organizar_html(requisicao)    
    div = transformacao_requisicao.Transformar.localiza_div_relatorio(html_formatado)
    requisicao_relatorio = requisicao_fundo.Requisicao.relatorio_gerencial(div)
    relatorio_formatado = transformacao_requisicao.Transformar.decode_base_64(requisicao_relatorio)
    informacoes_pdf = extracao_pdf.Extrair.informacoes_pdf(relatorio_formatado)
    resumo_gemini = resume_report.Resumo_texto.resumo_gemini(informacoes_pdf,nivel_complexidade,nivel_detalhamento)
    return resumo_gemini

def pkg_vl_atual_cota(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    valor_atual_cota = extracao_pdf.Extrair.valor_atual_cota(ticker_selecionado)
    return valor_atual_cota

def pkg_variacao_percentual_preco_atual(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    valor_atual_cota = extracao_pdf.Extrair.valor_atual_cota(ticker_selecionado)
    valor_dia_anterior_cota = extracao_pdf.Extrair.valor_dia_anterior_cota(ticker_selecionado)
    variacao_percentual = transformacoes_calculos_ticker.CalculosTicker.variacao_percentual_preco_atual(valor_atual_cota,valor_dia_anterior_cota)
    return variacao_percentual
