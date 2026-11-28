# GRUPO: ...

# Desenvolvam o trabalho neste ficheiro.
# Podem criar outros ficheiros e importá-los aqui.

import sys
from logica import carregar_livros
from ui_terminal import menu

def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else "livros.txt" # permite outro ficheiro de livros
    livros = carregar_livros(nome)
    menu(livros)



if __name__ == "__main__":
    main()

