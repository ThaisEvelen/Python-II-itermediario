from rich.console import Console
from rich.text import Text

console = Console()

def colorir(texto: str, isArquivo: bool):
    """Colore o texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    t = Text(conteudo, style="bold blue")
    console.print(t)


def estilo_alerta(texto: str, isArquivo: bool):
    """Estilo vermelho de alerta."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    console.print(Text(conteudo, style="bold red"))
from rich.console import Console
from rich.text import Text

console = Console()

def colorir(texto: str, isArquivo: bool):
    """Colore o texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    t = Text(conteudo, style="bold blue")
    console.print(t)


def estilo_alerta(texto: str, isArquivo: bool):
    """Estilo vermelho de alerta."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    console.print(Text(conteudo, style="bold red"))