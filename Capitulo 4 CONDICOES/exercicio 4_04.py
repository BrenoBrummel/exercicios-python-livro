#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$1250.00, calcule um
#aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input('Digite o valor do seu salário: '))

aumento = int

if salario > 1250:
    aumento = 10
    print(f'O seu salário terá um aumento de {aumento}%, subindo de {salario:.2f} para {salario * (1 + aumento / 100):.2f}.')

if salario <= 1250:
    aumento = 15
    print(f'O seu salário terá um aumento de {aumento}%, subindo de {salario:.2f} para {salario * (1 + aumento / 100):.2f}.')
