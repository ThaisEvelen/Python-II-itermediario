from rich.progress import track
from time import sleep

def progresso_basico(texto: str, isArquivo: bool):
    """Simula progresso enquanto imprime o texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    for _ in track(range(10), description="Carregando..."):
        sleep(0.1)

    print(conteudo)


def progresso_longo(texto: str, isArquivo: bool):
    """Progresso maior."""
    for _ in track(range(50), description="Processando..."):
        sleep(0.05)