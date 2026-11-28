# colocar as promoçoes em formato de dicionario;

def carregar_promocoes(nome_ficheiro):  # Recebe o nome do ficheiro de promoções

    promocoes = {}  # Criar um dicionário vazio

    try:  # Tentar abrir e ler o ficheiro

        with open(nome_ficheiro, "r", encoding="utf-8") as file:  # Abrir o ficheiro em modo de leitura

            linhas = file.readlines()  # Guardar todas as linhas numa lista

    except OSError:  # Verificar se ocorreu um erro ao abrir ou ler o ficheiro

        return promocoes  # Devolver um dicionário vazio caso ocorra um erro

    for i in range(1, len(linhas)):  # Percorrer as linhas, ignorando o cabeçalho

        campos = linhas[i].strip().split(";")  # Separar o género e o desconto

        if len(campos) != 2:  # Verificar se existem exatamente dois campos

            continue  # Ignorar a linha inválida e passar à seguinte

        genero = campos[0].strip().lower()  # Remover espaços e converter o género para minúsculas

        try:  # Tentar converter o desconto num número decimal

            desconto = float(campos[1])  # Converter o desconto para float

        except ValueError:  # Verificar se o desconto não é um número válido

            continue  # Ignorar a linha e passar à seguinte

        if genero != "" and 0 <= desconto <= 100:  # Validar o género e os limites do desconto

            promocoes[genero] = desconto  # Adicionar o género e o desconto ao dicionário

    return promocoes  # Devolver o dicionário com todas as promoções válidas

# O objetivo desta função é receber um livro, verificar se existe uma promoção para o seu género literário
# Devolver o preço final com o desconto aplicado.

def preco_com_desconto(livro, promo):   # funcao recebe o livro e as promocoes
        
    genero = livro["genero"].lower()    # género do livro

    preco = livro["preço"]              # preço original do livro 

    desconto = promo.get(genero, 0)     # procura o desconto correspondente a cada livro.  

    preco_final = preco * (1 - desconto / 100) # preço final com o desconto aplicado

    return round(preco_final, 2)    # preço do livro com 2 casas decimais


# calcular o preço total de todos os livros que estão no carrinho de compras, antes e depois de aplicar os descontos.

def total_carrinho(livros, carrinho, promo):

    # Inicializar as variaveis com 0 para depois acumular

    subtotal = 0
    total_a_pagar = 0

    for livro in livros:    # Percorrer os livros

        codigo = livro["codigo"]

        if codigo in carrinho:  # Verificar se o livro está no carrinho
                                ## Se o código não existir no carrinho, passa para o livro seguinte.

            quantidades = carrinho[codigo]  # valor associado ao código do livro no dicionário.

            subtotal += livro["preço"] * quantidades

            total_a_pagar += preco_com_desconto(livro, promo) * quantidades

    return round(subtotal, 2), round(total_a_pagar, 2)
