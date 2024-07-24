#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
operacao = str(input('Digite a operação que você deseja realizar: '))
resultado = 0

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else:
    print('Operação inesperada.')

print(f'O resultado de {num1} {operacao} {num2} = {resultado}')
