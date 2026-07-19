import argparse

lista = []


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest='comando')

# Comando: adicionar
adicionar = subparsers.add_parser('adicionar')
adicionar.add_argument('texto', type=str)
args = parser.parse_args()

if args.comando == 'adicionar':
    lista.append(args.texto)
    print("Lista:", lista)

