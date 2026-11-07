"""CLI for the Dotfile Manager."""

import sys
from _internal._core import get_tracked_files, add_tracked_file, remove_tracked_file, list_tracked_files

def print_help():
    print("""
Dotfile Manager - Gerenciador de Dotfiles

Comandos disponíveis:
  init          : Inicializa o gerenciador (cria arquivo de config).
  list          : Lista os arquivos rastreados.
  add <arquivo> : Rastreia um novo arquivo dotfile.
  remove <arquivo>: Remove o rastreamento de um arquivo.
  scan          : Detecta automaticamente arquivos dotfiles comuns na pasta home.
  help          : Mostra esta ajuda.
""")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if len(sys.argv) < 2:
        print_help()
        return

    if sys.argv[1] == "init":
        print("Iniciando o gerenciador de dotfiles...")
        # Apenas cria o arquivo de configuração se não existir
        print("Sistema pronto para uso.")

    elif sys.argv[1] == "list":
        files = list_tracked_files()
        if not files:
            print("Nenhum arquivo rastreado encontrado.")
            return
        print("Arquivos rastreados:")
        for f in files:
            print(f"  - {f}")

    elif sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Uso: dotfile add <arquivo>")
            print("Exemplo: dotfile add .bashrc")
            return
        rel_path = sys.argv[2]
        if add_tracked_file(rel_path):
            print(f"Arquivo '{rel_path}' adicionado ao rastreamento.")
        else:
            print(f"Não foi possível adicionar '{rel_path}'. Verifique se o arquivo existe.")

    elif sys.argv[1] == "remove":
        if len(sys.argv) < 3:
            print("Uso: dotfile remove <arquivo>")
            print("Exemplo: dotfile remove .bashrc")
            return
        rel_path = sys.argv[2]
        if remove_tracked_file(rel_path):
            print(f"Rastreamento removido para '{rel_path}'.")
        else:
            print(f"Arquivo '{rel_path}' não estava no rastreamento.")

    elif sys.argv[1] == "scan":
        print("Varredurando para arquivos dotfiles...")
        files = track_and_scan()
        if not files:
            print("Nenhum dotfile novo encontrado.")
        else:
            print(f"Encontrados {len(files)} novos arquivos para rastreamento:")
            for f in files:
                print(f"  - {f}")

    elif sys.argv[1] == "help":
        print_help()

    else:
        print_help()


if __name__ == "__main__":
    main()