# logica.py - logica do programa, sem interface.
# Tem as funções que tratam dos dados do programa, sem falar com o utilizador (sem print nem input)

def carregar_livros(nome_arquivo):
    livros = []
    with open(nome_arquivo, "r", encoding="utf-8") as file:
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