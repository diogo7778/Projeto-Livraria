# Funcoes que tratam dos dados dos livros.
# Regra deste ficheiro: nao imprime nada e nao pede input nenhum.

def carregar_livros(nome_arquivo):
    livros = []
    with open(nome_arquivo, "r", encoding="utf-8") as file:
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

