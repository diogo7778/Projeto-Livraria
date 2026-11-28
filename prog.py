# GRUPO: P14H

import sys
<<<<<<< HEAD
=======

>>>>>>> 4255a101d749ccd7f70e89c7d6e47cf30c9d0647
from logica import carregar_livros
from ui_terminal import menu

def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else "livros.txt"
    livros = carregar_livros(nome)
    menu(livros)

if __name__ == "__main__":
    main()
