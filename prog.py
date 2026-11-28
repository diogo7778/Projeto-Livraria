# GRUPO: ...

# Desenvolvam o trabalho neste ficheiro.
# Podem criar outros ficheiros e importá-los aqui.

import sys

def carregar_livros(nome_arquivo):
    livros = []
    with open(nome_arquivo, "r", encoding="utf-8") as file:
        linhas = file.readlines()         
    for i in range(1, len(linhas)):
        campos = linhas[i].strip().split(";")  # divisao dos campos
        livro = {"codigo": campos[0], "titulo": campos[1], "autor": campos[2],
             "genero": campos[3], "preço": float(campos[4]), "stock": int(campos[5])} #cria um dicionário com as informações do livro
        livros.append(livro)
    
    return livros


def menu(livros):
    while True:                              
        print("1 - Ver livros / 2 - Sair")   
        opcao = input("Opção: ")             
        if opcao == "1":                     
            genero = input("Qual o genero que procura? ")
            if genero == "":                   
                resultado = livros    # se nao especificar o genero, mostra a lista completa       
            else:
                resultado = escolher_livro(livros, genero)
            for livro in resultado:
                print(livro["codigo"], livro["titulo"], livro["genero"], livro["preço"], livro["stock"], sep=("|")) #mostra os livros escolhidos
        elif opcao == "2":                   
            break
        else:
            print("Opcao invalida")

def escolher_livro(livros, genero=None):
    if genero is None:
        genero = input("Qual o genero que procura? ")
    resultado = []
    for livro in livros:
        if genero == "" or genero.lower() == livro["genero"].lower(): #adiciona o livro á lista de resultados
            resultado.append(livro)
    if len(resultado) == 0:
        print("Não existem livros com esse genero")
    return resultado

def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else "livros.txt" # permite outro ficheiro de livros
    livros = carregar_livros(nome)
    menu(livros)



if __name__ == "__main__":
    main()

