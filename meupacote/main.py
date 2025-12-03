import argparse
import layout
import painel
import progresso
import estilo

funcoes = {
    "mostrar_layout": layout.mostrar_layout,
    "layout_simples": layout.layout_simples,
    "painel_normal": painel.painel_normal,
    "painel_destacado": painel.painel_destacado,
    "progresso_basico": progresso.progresso_basico,
    "progresso_longo": progresso.progresso_longo,
    "colorir": estilo.colorir,
    "estilo_alerta": estilo.estilo_alerta,
}

modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo,
}

parser = argparse.ArgumentParser(description="Ferramenta Rich personalizada")

parser.add_argument("texto", help="Texto OU caminho do arquivo")
parser.add_argument("-a", "--arquivo", action="store_true", help="Habilita modo arquivo")
parser.add_argument("-m", "--modulo", help="Escolhe o módulo")
parser.add_argument("-f", "--funcao", help="Escolhe a função")

args = parser.parse_args()

if args.funcao:
    func = funcoes.get(args.funcao)
    if func:
        func(args.texto, args.arquivo)
    else:
        print("Função não encontrada.")

elif args.modulo:
    print("Funções disponíveis no módulo", args.modulo)
    for nome in dir(modulos[args.modulo]):
        if not nome.startswith("_"):
            print(" -", nome)