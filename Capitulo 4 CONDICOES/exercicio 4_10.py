#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de
#instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir*. *A tabela
#pode ser encontrada somente no livro (página 83).

energia_consumida = int(input('Digite a quantidade de kWh consumido: '))
tipo_instalacao = str(input('Digite o tipo de instalação: R para residências, I para indústrias e C para comércios. '))
preco = float

if tipo_instalacao == 'R' or 'r':
    if energia_consumida <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif tipo_instalacao == 'I' or 'i':
    if energia_consumida <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif tipo_instalacao == 'C' or 'c':
    if energia_consumida <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Você digitou um valor diferente do solicitado. Valores esperados "R, I ou C".')

print(f'O valor da sua fatura é: R${energia_consumida * preco:.2f}.')
