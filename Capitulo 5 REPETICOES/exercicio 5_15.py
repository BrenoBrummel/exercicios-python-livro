# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
#comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto : [código] = [preço], 1 = 0.50, 2 = 1.00, 3 = 4.00, 5 = 7.00 e 
#9 = 8.00. Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código
# Inválido".

codigo = int
valor_total = 0
quantidade = 0
preco = 0

while True:
    codigo = int(input('Digite o código do produto: '))
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.5
        quantidade = int(input('Digite a quantidade: '))
    elif codigo == 2:
        preco = 1.0
        quantidade = int(input('Digite a quantidade: '))
    elif codigo == 3:
        preco = 4.0
        quantidade = int(input('Digite a quantidade: '))
    elif codigo == 5:
        preco = 7.0
        quantidade = int(input('Digite a quantidade: '))
    elif codigo == 9:
        preco = 8.0
        quantidade = int(input('Digite a quantidade: '))
    else:
        print('Código Inválido!')
    valor_total += quantidade * preco

print(f'O valor total da suas compras é R${valor_total:.2f}')
