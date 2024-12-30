from requests_html import requisicao_fundo
from transformer import transformacao_requisicao,transformacoes_calculos_ticker,transformacoes_projecao_grafico
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
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    valor_atual_cota = transformacoes_calculos_ticker.CalculosTicker.valor_atual_cota(data_set_ticker.Close)
    return valor_atual_cota

def pkg_variacao_percentual_preco_atual(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    valor_atual_cota = transformacoes_calculos_ticker.CalculosTicker.valor_atual_cota (data_set_ticker.Close)
    valor_dia_anterior_cota = transformacoes_calculos_ticker.CalculosTicker.valor_dia_anterior_cota(data_set_ticker.Close)
    variacao_percentual_atual = transformacoes_calculos_ticker.CalculosTicker.variacao_percentual_preco(valor_atual_cota,valor_dia_anterior_cota)
    return variacao_percentual_atual

def pkg_vl_mes_anterior_cota(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    valor_mes_aterior_cota = transformacoes_calculos_ticker.CalculosTicker.valor_mes_anterior_cota(data_set_ticker.Close)
    return valor_mes_aterior_cota

def pkg_variacao_percentual_preco_mes_anterior(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    valor_atual_cota = transformacoes_calculos_ticker.CalculosTicker.valor_atual_cota (data_set_ticker.Close)
    valor_mes_anterior_cota = transformacoes_calculos_ticker.CalculosTicker.valor_mes_anterior_cota(data_set_ticker.Close)
    variacao_percentual_mes_anterior = transformacoes_calculos_ticker.CalculosTicker.variacao_percentual_preco(valor_atual_cota,valor_mes_anterior_cota)
    return variacao_percentual_mes_anterior

def pkg_vl_ano_anterior_cota(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    valor_mes_aterior_cota = transformacoes_calculos_ticker.CalculosTicker.valor_ano_anterior_cota(data_set_ticker.Close)
    return valor_mes_aterior_cota

def pkg_variacao_percentual_preco_ano_anterior(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    valor_atual_cota = transformacoes_calculos_ticker.CalculosTicker.valor_atual_cota (data_set_ticker.Close)
    valor_mes_anterior_cota = transformacoes_calculos_ticker.CalculosTicker.valor_ano_anterior_cota(data_set_ticker.Close)
    variacao_percentual_mes_anterior = transformacoes_calculos_ticker.CalculosTicker.variacao_percentual_preco(valor_atual_cota,valor_mes_anterior_cota)
    return variacao_percentual_mes_anterior

def pkg_evolucao_preco_grafico_linha_1_mes(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    dataset_1_mes = transformacoes_projecao_grafico.TransformacaoGraficoLinha.converter_indice_do_mes_para_string(data_set_ticker)
    return dataset_1_mes

def pkg_evolucao_preco_grafico_linha_1_ano(ticker):
    ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
    data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(ticker_selecionado)
    dataset_1_ano = transformacoes_projecao_grafico.TransformacaoGraficoLinha.converter_indice_do_ano_para_string(data_set_ticker)
    return dataset_1_ano