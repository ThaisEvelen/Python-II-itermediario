# Constantes
NUMERO_MAXIMO = 150  # Número total de Pokémon da 1ª geração
TIPOS = (
    'Normal', 'Fogo', 'Água', 'Planta', 'Elétrico', 'Gelo',
    'Lutador', 'Venenoso', 'Terra', 'Voador', 'Psíquico', 'Inseto',
    'Pedra', 'Fantasma', 'Dragão', 'Metálico', 'Fada'
)

# Funções
def verificar_tipo_pokemon(tipo):
    """Verifica se um tipo de Pokémon é válido."""
    return tipo in TIPOS

def verificar_numero_pokemon(numero):
    """Verifica se um número de Pokémon é válido."""
    return 1 <= numero <= NUMERO_MAXIMO
