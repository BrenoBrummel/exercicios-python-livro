#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input('Digite o preço da mercadoria: '))
porcen_desconto = float(input('Digite o percentual de desconto: '))

preco_descontado = preco - preco * (porcen_desconto / 100)

print(f'O valor do desconto foi R${preco * (porcen_desconto / 100):.2f} e o preço a pagar é {preco_descontado:.2f}')
