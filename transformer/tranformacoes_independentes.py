from IPython.display import  Markdown
import textwrap

class Transformacoes:
    
    def texto_markdown(text):
        text = text.replace("•", "  *")
        return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))