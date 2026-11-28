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


def filtrar_livros(livros, genero="", autor="", titulo="", preco_min=None, preco_max=None):
    resultado = []
    for livro in livros:
        # cada filtro vazio significa que o utilizador nao o pediu
        if genero != "" and genero.lower() != livro["genero"].lower():
            continue
        if autor != "" and autor.lower() not in livro["autor"].lower():
            continue
        if titulo != "" and titulo.lower() not in livro["titulo"].lower():
            continue
        if preco_min is not None and livro["preço"] < preco_min:
            continue
        if preco_max is not None and livro["preço"] > preco_max:
            continue
        resultado.append(livro)
    return resultado
