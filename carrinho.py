# Funcoes que tratam do carrinho de compras.
# Devolve None quando corre bem, ou uma mensagem de erro.

def adicionar_ao_carrinho(carrinho, livros, codigo, quantidade):
    try:
        quantidade = int(quantidade)
    except (ValueError, TypeError):
        return "Quantidade invalida"
    if quantidade <= 0:
        return "Quantidade invalida"

    livro = None
    for item in livros:
        if item["codigo"].upper() == codigo.upper():
            livro = item
            break
    if livro is None:
        return "Codigo nao encontrado"

    linha = None  # linha do carrinho que ja tem este livro
    for item in carrinho:
        if item["codigo"] == livro["codigo"]:
            linha = item
            break
    ja_no_carrinho = 0 if linha is None else linha["quantidade"]

    if ja_no_carrinho + quantidade > livro["stock"]:
        return "Stock insuficiente"

    if linha is None:
        carrinho.append({"codigo": livro["codigo"], "quantidade": quantidade})
    else:
        linha["quantidade"] = ja_no_carrinho + quantidade

    return None
