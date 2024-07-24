# Escreva um programa que pergunte o valor do depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros
#meses. Escreva o total ganho com juros no período.

deposito = float(input('Digite o valor do depósito inicial: '))
taxa_juros = float(input('Digite o valor da taxa de juros: '))
mes = 0
montante = deposito
print(f'O montante no mês {mes} é {montante}')

while mes <= 24:
    if mes >= 1:
        montante = montante + (montante * (taxa_juros / 100))
        print(f'O montante no mês {mes} é {montante}')
    mes = mes + 1
