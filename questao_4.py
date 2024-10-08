def criar_produto(nome, codigo, preco, estoque):

    try: codigo = int(codigo)
    except: print(f"[Produto: {nome}] Código '{codigo}' inválido, precisa ser número inteiro")

    try: preco = float(preco)
    except: print(f"[Produto: {nome}] Preço '{preco}' inválido, precisa ser um número")

    try: estoque = int(estoque)
    except: print(f"[Produto: {nome}] Estoque '{estoque}' inválido, precisa ser número inteiro")

    return (nome, int(codigo), float(preco), int(estoque))

def atualizar_estoque(produto, quantidade):

    try: quantidade = int(quantidade)
    except: print(f"[Atualizando {produto[0]}] Quantidade '{quantidade}' inválida, precisa ser número inteiro")

    return (produto[0], produto[1], produto[2], produto[3] + int(quantidade))

def listar_produtos(produtos):
    for produto in produtos:
        print(f"Produto: {produto[0]} | Cód.: {produto[1]} | Preço: {produto[2]} | Estoque: {produto[3]}")

produtos = []

# Utilização das funções
try:
    produtos.append(criar_produto("Produto A", 1, 2.99, 10))
    produtos.append(criar_produto("Produto B", 2, 4.99, 5))
    produtos.append(criar_produto("Produto C", 3, 17.00, 25))
    produtos.append(criar_produto("Produto D", 4, 49.50, 50))

    produtos[1] = atualizar_estoque(produtos[1], (100))

    listar_produtos(produtos)
except:
    print("Operação inválida, verifique os valores passados")