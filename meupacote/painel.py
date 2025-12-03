from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_normal(texto: str, isArquivo: bool):
    """Exibe texto dentro de um painel."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    console.print(Panel(conteudo, title="Painel"))


def painel_destacado(texto: str, isArquivo: bool):
    """Painel com destaque."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    console.print(Panel(conteudo, title="Destaque!", border_style="bold yellow"))