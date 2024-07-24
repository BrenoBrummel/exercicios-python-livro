estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijao": [100, 1.50]}
venda = []
item_quantidade = []
item_vendido = input("Digite o item: ")
quantidade_vendida = int(input("Digite a quantidade: "))
item_quantidade.append(item_vendido)
item_quantidade.append(quantidade_vendida)
venda.append(item_quantidade)
total = 0
if item_vendido in estoque:
    print("Vendas:\n")
    for operacao in venda:
        produto, quantidade = operacao
        preco = estoque[produto][1]
        custo = preco * quantidade
        print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
        estoque[produto][0] -= quantidade
        total += custo
    print(f"Custo total: {total:21.2f}\n")
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")
else:
    print(f"Não temos o item {item_vendido} no estoque!")
    