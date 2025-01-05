from IPython.display import display
from config import config_resume
from transformer import tranformacoes_independentes
import pandas as pd


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

            return resposta.text
        except Exception as e:
            print("Erro ao analisar o texto com o Gemini:", e)
            return None
        
class ResumoDataFrameGraficos:
    def resumo_analitico_rsi(dataset_fii_rsi,dataset_fii,ticker):

        valor_fechamento_df = dataset_fii.to_frame(name='Close')
        valor_rsi_df = dataset_fii_rsi.to_frame(name='RSI')
        valor_fechamento_df = valor_fechamento_df.join(valor_rsi_df)

        try:
            rsi_data = valor_fechamento_df[['Close', 'RSI']].dropna()
            ultima_rsi = rsi_data['RSI'].iloc[-1]
            tendencia = (
                "Compra" if ultima_rsi < 30 else
                "Venda" if ultima_rsi > 70 else
                "Neutra"
            )

            texto = (
                f"Análise dos dados do gráfico RSI para o fundo {ticker}.\n\n"
                f"- Período analisado: {rsi_data.index.min().strftime('%d/%m/%Y')} a {rsi_data.index.max().strftime('%d/%m/%Y')}\n"
                f"- Último valor de fechamento: {rsi_data['Close'].iloc[-1]}\n"
                f"- Último valor do RSI: {ultima_rsi}\n"
                f"- Tendência atual com base no RSI: {tendencia}\n\n"
                "Resumo da evolução do fundo:\n"
                f"- Valores de fechamento variaram de {rsi_data['Close'].min()} a {rsi_data['Close'].max()} durante o período.\n"
                f"- RSI variou entre {rsi_data['RSI'].min()} (mínimo) e {rsi_data['RSI'].max()} (máximo).\n"
                "Abaixo estão os últimos valores registrados:\n"
                + rsi_data.tail(5).to_string(index=True)
            )

            prompt = (
                "Analise os dados fornecidos sobre o gráfico RSI do fundo e forneça um diagnóstico claro. O objetivo é:\n"
                "- Indicar se o momento atual sugere uma tendência de compra ou venda com base no RSI.\n"
                "- Resumir a evolução do fundo durante o período analisado, destacando variações nos valores de fechamento e no RSI.\n\n"
                "Certifique-se de iniciar o texto com:\n"
                "'Analise detalhada com base no gráfico RSI em relação ao fundo {ticker}'.\n\n"
                "Segue o relatório:\n\n" + texto
            )
            response = config_resume.model.generate_content(prompt)

            return response.text
        except Exception as e:
            print("Erro ao preparar ou analisar os dados do gráfico RSI:", e)
            return None  
        
    def resumo_analitico_macd(dataset_macd,dataset_sinal_linha,ticker):
        valor_macd_df = dataset_macd.to_frame(name='MACD')
        valor_signal_line_df = dataset_sinal_linha.to_frame(name='Signal_Line')
        valor_macd_df = valor_macd_df.join(valor_signal_line_df)

        try:

            macd_data = valor_macd_df[['MACD', 'Signal_Line']].dropna()


            ultima_macd = macd_data['MACD'].iloc[-1]
            ultima_signal = macd_data['Signal_Line'].iloc[-1]
            ultima_data = macd_data.index[-1].strftime('%d/%m/%Y')
            tendencia = (
                "Alta" if ultima_macd > ultima_signal else
                "Baixa" if ultima_macd < ultima_signal else
                "Neutra"
            )
            texto = (
                f"**Análise detalhada com base no gráfico MACD em relação ao fundo {ticker}**\n\n"
                f"- **Período analisado:** {macd_data.index.min().strftime('%d/%m/%Y')} a {macd_data.index.max().strftime('%d/%m/%Y')}\n"
                f"- **Última data registrada:** {ultima_data}\n"
                f"- **Último valor do MACD:** {ultima_macd:.4f}\n"
                f"- **Último valor da Linha de Sinal (Signal Line):** {ultima_signal:.4f}\n"
                f"- **Tendência atual com base no MACD:** {tendencia}\n\n"
                "### Resumo da evolução do fundo\n"
                f"- O MACD variou entre **{macd_data['MACD'].min():.4f}** (mínimo) e **{macd_data['MACD'].max():.4f}** (máximo).\n"
                f"- A Linha de Sinal variou entre **{macd_data['Signal_Line'].min():.4f}** (mínimo) e **{macd_data['Signal_Line'].max():.4f}** (máximo).\n\n"
                "### Últimos valores registrados\n\n"
                + macd_data.tail(5).to_markdown(index=True)
            )
        
            prompt = (
                "Analise os dados fornecidos sobre o gráfico MACD do fundo e forneça um diagnóstico claro. O objetivo é:\n"
                "- Indicar se o momento atual sugere uma tendência de alta ou baixa com base no MACD e na Signal Line.\n"
                "- Resumir a evolução do fundo durante o período analisado, destacando variações no MACD e na Linha de Sinal.\n\n"
                "Certifique-se de iniciar o texto com:\n"
                "'Analise detalhada com base no gráfico MACD em relação ao fundo {ticker}'.\n\n"
                "Segue o relatório em formato Markdown:\n\n" + texto
            )
            response = config_resume.model.generate_content(prompt)


            resposta_limpa = response.text.split("\nEspero que")[0].strip()

            return resposta_limpa
        except Exception as e:
            print("Erro ao preparar ou analisar os dados do gráfico MACD com Gemini:", e)
            return e  
        
    def analisar_bandas_bollinger_com_gemini(data,ticker, sma, close,lower_band,upper_band,insigth, window=20, num_std_dev=2):

        try:

            insights_sma = [f"Última SMA: {sma.iloc[-1]:.4f}"]
            insights_bollinger = [
                f"Última banda superior: {upper_band.iloc[-1]:.4f}",
                f"Última banda inferior: {lower_band.iloc[-1]:.4f}"
            ]
            insights_volatilidade = insigth

            df_insights = pd.DataFrame({
                "Tipo de Insight": ["SMA", "Bandas de Bollinger", "Volatilidade"],
                "Detalhes": ["; ".join(insights_sma), "; ".join(insights_bollinger), "; ".join(insights_volatilidade)]
            })

            texto = (
                f"**Análise detalhada com base no gráfico de Bandas de Bollinger em relação ao fundo {ticker}**\n\n"
                f"- **Período analisado:** {data.index.min().strftime('%d/%m/%Y')} a {data.index.max().strftime('%d/%m/%Y')}\n"
                f"- **Última data registrada:** {data.index[-1].strftime('%d/%m/%Y')}\n"
                f"\n### Resumo consolidado dos insights\n"
                + df_insights.to_markdown(index=False)
            )
            prompt = (
                "Analise os dados fornecidos sobre o gráfico de Bandas de Bollinger do fundo e forneça um diagnóstico claro. O objetivo é:\n"
                "- Indicar se o momento atual sugere uma tendência de alta, baixa ou consolidação.\n"
                "- Resumir a evolução do fundo durante o período analisado, destacando toques nas bandas e a volatilidade.\n"
                "- Fornecer uma previsão baseada nos dados passados e presentes.\n\n"
                "Segue o relatório em formato Markdown:\n\n" + texto
            )
            response = config_resume.model.generate_content(prompt)

            resposta_limpa = response.text.split("\nEspero que")[0].strip()

            return resposta_limpa
        except Exception as e:
            print("Erro ao preparar ou analisar os dados do gráfico de Bandas de Bollinger com Gemini:", e)
            return None    