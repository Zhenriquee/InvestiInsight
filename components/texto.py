from streamlit import title,markdown,subheader

class Texto:

    def titulo(ticker,html_formatado):
        tt = title(f"Fii: {ticker}")  # Mostrar o ticker como título principal
        sb1 = subheader(f"Razão Social: {html_formatado.get('Razão Social', 'Razão Social não encontrada')}")
        sb2 = subheader(f"CNPJ: {html_formatado.get('CNPJ', 'CNPJ não encontrado')}")
        return tt,sb1,sb2
    
class Markdown:
    def explicacao_grafico_rsi():

        resumo =(''' O **RSI**  (**Relative Strength Index**) é um indicador de momentum que mede a velocidade e a mudança dos movimentos de preços. Ele ajuda a identificar condições de **sobrecompra** ou **sobrevenda** de um ativo.

### Cálculo:
\[
RSI = 100 - {100}/{1 + RS}
\]
Onde **RS** é a média dos fechamentos em alta dividida pela média dos fechamentos em baixa.

### Análise:
- **Sobrecompra (>70):** Pode indicar que o ativo está sobrecomprado e que o preço pode cair em breve.
- **Sobrevenda (<30):** Pode indicar que o ativo está sobrevendido e que o preço pode subir em breve.
- **Reversão em torno de 50:** Pode indicar uma possível mudança na direção do preço.''') 
        return markdown(resumo)
    
    def explicacao_grafico_macd():
        resumo =('''O **MACD** (**Moving Average Convergence Divergence**) é um indicador de tendência que analisa a relação entre duas médias móveis exponenciais (EMAs) para identificar pontos de compra e venda.

### Cálculo:
\[
MACD = EMA(12) - EMA(26)
\]
- **Linha de sinal:** EMA de 9 períodos do MACD.
- **Histograma:** Diferença entre o MACD e a linha de sinal.

### Análise:
- **Cruzamento de linhas:**
  - **MACD cruza acima da linha de sinal:** Sinal de compra.
  - **MACD cruza abaixo da linha de sinal:** Sinal de venda.
- **Divergência:**
  - Se o preço faz novos máximos, mas o MACD não acompanha, pode ser sinal de fraqueza na tendência de alta (e vice-versa para a baixa).
- **Histograma:**
  - Indica a força da tendência. Um histograma crescente sinaliza tendência forte, enquanto um histograma decrescente pode indicar fraqueza.''')
        return markdown(resumo)
    
    def explicacao_grafico_bandas_de_bollinger():
        resumo =('''As **Bandas de Bollinger** são compostas por uma média móvel simples (SMA) e duas bandas baseadas no desvio padrão, que ajudam a medir a volatilidade do mercado.

### Cálculo:
\[
Banda Superior = SMA + (2 \times SD)
\]
\[
Banda Inferior = SMA - (2 \times SD)
\]

### Análise:
- **Preços tocando a banda superior:** Indicam possível condição de sobrecompra.
- **Preços tocando a banda inferior:** Indicam possível condição de sobrevenda.
- **Squeeze (estreitamento das bandas):** Pode sinalizar baixa volatilidade, antecipando um movimento significativo de preço.
- **Expansão das bandas:** Indica alta volatilidade, sugerindo que o ativo pode estar em uma forte tendência.

---

### Resumo:
- **RSI:** Mede sobrecompra (>70) e sobrevenda (<30) e pode antecipar reversões.
- **MACD:** Identifica tendências e cruzamentos (compra ou venda).
- **Bandas de Bollinger:** Indicam volatilidade e condições extremas de preço (sobrecompra/sobrevenda).''')
        return markdown(resumo)
    
    