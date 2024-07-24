#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos
#quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km_percorridos = int(input('Digite a quantidade de quilômetros percorridos: '))
dias = int(input('Digite a quantidade de dias em que o carro esteve alugado: '))

valor_pagar = (dias * 60) + (km_percorridos * 0.15)

print(f'O preço a pagar é R${valor_pagar:.2f}.')
