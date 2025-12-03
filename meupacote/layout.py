from rich.console import Console
from rich.layout import Layout

console = Console()

def mostrar_layout(texto: str, isArquivo: bool):
    """Exibe um layout básico usando Rich."""
    layout = Layout()

    # Carregar texto
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    # Layout dividido
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3),
    )

    layout["header"].update("[bold magenta]Cabeçalho[/]")
    layout["body"].update(conteudo)
    layout["footer"].update("[green]Rodapé[/]")

    console.print(layout)


def layout_simples(texto: str, isArquivo: bool):
    """Layout simples com borda."""
    from rich.panel import Panel

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    console.print(Panel(conteudo, title="Layout simples"))