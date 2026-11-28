# Aqui fica a parte da interface em texto.

from logica import escolher_livro

def menu(livros):
    while True:
        print("1 - Ver livros / 2 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            genero = input("Qual o genero que procura? ")
            resultado = escolher_livro(livros, genero)
            if len(resultado) == 0:
                print("Não existem livros com esse genero")
            else:
                for livro in resultado:
                    print(livro["codigo"], livro["titulo"], livro["genero"],
                          livro["preço"], livro["stock"], sep="|")
        elif opcao == "2":
            break
        else:
            print("Opcao invalida")
