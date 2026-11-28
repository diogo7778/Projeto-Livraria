# ui_terminal.py - interface em modo texto

from logica import filtrar_por_genero

def mostrar_livros(lista):
    if len(lista) == 0:
        print("Não existem livros com esse genero.")
        return 
    for livro in lista:
        print(livro["codigo"], livro["titulo"], livro["genero"], livro["preço"], livro["stock"], sep="|")

def menu(livros):
    while True:
        print("1 - Ver livros / 2 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            genero = input("Qual o genero que procura? ")
            resultado = filtrar_por_genero(livros, genero)
            mostrar_livros(resultado)

        elif opcao == "2":
            break
        else:
            print("Opção inválida!")