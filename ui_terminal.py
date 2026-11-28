<<<<<<< HEAD
# ui_terminal.py - interface em modo texto

from logica import filtrar_por_genero

def mostrar_livros(lista):
    if len(lista) == 0:
        print("Não existem livros com esse genero.")
        return 
    for livro in lista:
        print(livro["codigo"], livro["titulo"], livro["genero"], livro["preço"], livro["stock"], sep="|")
=======
# Aqui fica a parte da interface em texto.

from logica import escolher_livro
>>>>>>> 4255a101d749ccd7f70e89c7d6e47cf30c9d0647

def menu(livros):
    while True:
        print("1 - Ver livros / 2 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            genero = input("Qual o genero que procura? ")
<<<<<<< HEAD
            resultado = filtrar_por_genero(livros, genero)
            mostrar_livros(resultado)

        elif opcao == "2":
            break
        else:
            print("Opção inválida!")
=======
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
>>>>>>> 4255a101d749ccd7f70e89c7d6e47cf30c9d0647
