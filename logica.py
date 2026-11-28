<<<<<<< HEAD
# logica.py - logica do programa, sem interface.
# Tem as funções que tratam dos dados do programa, sem falar com o utilizador (sem print nem input)
=======
# Funcoes que tratam dos dados dos livros.
# Regra deste ficheiro: nao imprime nada e nao pede input nenhum.
>>>>>>> 4255a101d749ccd7f70e89c7d6e47cf30c9d0647

def carregar_livros(nome_arquivo):
    livros = []
    with open(nome_arquivo, "r", encoding="utf-8") as file:
<<<<<<< HEAD
        linhas = file.readlines()
    for i in range(1, len(linhas)):
        campos = linhas[i].strip().split(";")  # divisao dos campos
        livro = {"codigo": campos[0], "titulo": campos[1], "autor": campos[2],
                 "genero": campos[3], "preço": float(campos[4]),
                 "stock": int(campos[5])}  # dicionário com as informações do livro
        livros.append(livro)
    return livros


def filtrar_por_genero(livros, genero=""):
    """Devolve a lista de livros do género indicado (lista completa se vazio)."""
    if genero == "":
        return list(livros)
    resultado = []
    for livro in livros:
        if genero.lower() == livro["genero"].lower():
            resultado.append(livro)
    return resultado
=======
        linhas = file.readlines()  # lista com as linhas do ficheiro
    for i in range(1, len(linhas)):  # a linha 0 e o cabecalho
        campos = linhas[i].strip().split(";")  # divisao dos campos
        livro = {"codigo": campos[0], "titulo": campos[1], "autor": campos[2],
                 "genero": campos[3], "preço": float(campos[4]), "stock": int(campos[5])}
        livros.append(livro)

    return livros


def escolher_livro(livros, genero=""):
    resultado = []
    for livro in livros:
        # genero vazio significa mostrar todos
        if genero == "" or genero.lower() == livro["genero"].lower():
            resultado.append(livro)
    return resultado

>>>>>>> 4255a101d749ccd7f70e89c7d6e47cf30c9d0647
