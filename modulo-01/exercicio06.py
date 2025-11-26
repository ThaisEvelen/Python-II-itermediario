#Implemente uma função recursiva em Python que 
# realiza a travessia em pré-ordem de uma árvore binária
# representada por listas aninhadas. Na travessia em pré-ordem
# (ou pré-fixada), o nó raiz é visitado primeiro, 
# seguido pela subárvore esquerda e, por fim,
#  pela subárvore direita. 
# A questão fixa as constantes RAIZ_IDX, ESQ_IDX, DIR_IDX 
# representando os índices da lista onde se encontra o valor raíz,
# o nó a esquerda e o nó a direita.

RAIZ_IDX, ESQ_IDX, DIR_IDX = 0, 1, 2

arvore = [
    4,                      # raiz
    [
        2,                  # filho da esquerda
        [1, None, None],    # filho esquerdo de 2
        [3, None, None]     # filho direito de 2
    ],
    [
        5,                  # filho da direita
        None,               # esquerda de 5
        None                # direita de 5
    ]
]


def pre_ordem(no):

    if no is None:
        return []
    
    raiz = no[RAIZ_IDX]
    
    esquerda = no[ESQ_IDX]
    direita  = no[DIR_IDX]
    
    return [raiz] + pre_ordem(esquerda) + pre_ordem(direita)

print(pre_ordem(arvore))
