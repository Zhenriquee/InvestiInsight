from requests_html import requisicao_fundo
from transformer import transformacao_requisicao, transformacoes_calculos_ticker, transformacoes_projecao_grafico
from extract import extracao_pdf
from resume import resume_report

class FundoImobiliario:
    def __init__(self, ticker):
        self.ticker = ticker
        self.ticker_selecionado = requisicao_fundo.Requisicao.fundo_imobiliario_biblioteca(ticker)
        self.data_set_ticker = extracao_pdf.Extrair.historico_fundo_imobiliario(self.ticker_selecionado)
        self.data_frame_dividendos = extracao_pdf.Extrair.historico_dividendos_fundo_imobiliario(self.ticker_selecionado)
    
    def analise_gemini(self, nivel_complexidade, nivel_detalhamento):
        requisicao = requisicao_fundo.Requisicao.fundo_imobiliario_web(self.ticker)
        html_formatado = transformacao_requisicao.Transformar.organizar_html(requisicao)
        div = transformacao_requisicao.Transformar.localiza_div_relatorio(html_formatado)
        requisicao_relatorio = requisicao_fundo.Requisicao.relatorio_gerencial(div)
        relatorio_formatado = transformacao_requisicao.Transformar.decode_base_64(requisicao_relatorio)
        informacoes_pdf = extracao_pdf.Extrair.informacoes_pdf(relatorio_formatado)
        resumo_gemini = resume_report.Resumo_texto.resumo_gemini(informacoes_pdf, nivel_complexidade, nivel_detalhamento)
        return resumo_gemini

    def valor_atual_cota(self):
        return transformacoes_calculos_ticker.CalculosTicker.valor_atual_cota(self.data_set_ticker.Close)

    def variacao_percentual_preco_atual(self):
        valor_atual = self.valor_atual_cota()
        valor_dia_anterior = transformacoes_calculos_ticker.CalculosTicker.valor_dia_anterior_cota(
            self.data_set_ticker.Close
        )
        return transformacoes_calculos_ticker.CalculosTicker.variacao_percentual_preco(valor_atual, valor_dia_anterior)

    def valor_mes_anterior_cota(self):
        return transformacoes_calculos_ticker.CalculosTicker.valor_mes_anterior_cota(self.data_set_ticker.Close)

    def variacao_percentual_preco_mes_anterior(self):
        valor_atual = self.valor_atual_cota()
        valor_mes_anterior = self.valor_mes_anterior_cota()
        return transformacoes_calculos_ticker.CalculosTicker.variacao_percentual_preco(valor_atual, valor_mes_anterior)

    def valor_ano_anterior_cota(self):
        return transformacoes_calculos_ticker.CalculosTicker.valor_ano_anterior_cota(self.data_set_ticker.Close)

    def variacao_percentual_preco_ano_anterior(self):
        valor_atual = self.valor_atual_cota()
        valor_ano_anterior = self.valor_ano_anterior_cota()
        return transformacoes_calculos_ticker.CalculosTicker.variacao_percentual_preco(valor_atual, valor_ano_anterior)

    def evolucao_preco_grafico_linha_1_mes(self):
        return transformacoes_projecao_grafico.TransformacaoGraficoLinha.converter_indice_do_mes_para_string(
            self.data_set_ticker
        )

    def evolucao_preco_grafico_linha_1_ano(self):
        return transformacoes_projecao_grafico.TransformacaoGraficoLinha.converter_indice_do_ano_para_string(
            self.data_set_ticker
        )

    def evolucao_dividendos_grafico_barra(self):
        return transformacoes_projecao_grafico.TransformacaoGraficoBarra.dividendos_mes_ano(
            self.data_frame_dividendos
        )
    
    def evolucao_preco_fii_grafico_linha_rsi(self):
        return transformacoes_projecao_grafico.TransformacaoGraficoRSI.calculo_rsi(
           self.data_set_ticker.Close 
        )
    
    def evolucao_preco_fii_grafico_linha_macd(self):
        return transformacoes_projecao_grafico.TransformacaoGraficoMACD.calculo_macd(
           self.data_set_ticker.Close 
        )
    
    def evolucao_preco_fii_grafico_linha_bandas_de_bollinger_sma(self):
        return transformacoes_projecao_grafico.TransformacaoGraficoBandasDeBollinger.calculate_sma(
           self.data_set_ticker.Close
        )
    
    def evolucao_preco_fii_grafico_linha_bandas_de_bollinger_upper_lower(self):
        return transformacoes_projecao_grafico.TransformacaoGraficoBandasDeBollinger.calculate_bollinger_bands(
           self.data_set_ticker.Close
        )