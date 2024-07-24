# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
#de meses para que a dívida seja paga, o total pago e o total de juros pago.

valor_divida_inicial = float(input('Digite o valor da sua dívida: '))
juro_mensal = float(input('Digite o valor da taxa de juros mensal: '))
valor_mensal = float(input('Você pagará por mês R$:  '))
mes = 1
valor_divida_restante = valor_divida_inicial

while valor_divida_restante > 0:
    valor_divida_restante = valor_divida_restante + valor_divida_restante * (juro_mensal / 100)
    if valor_divida_restante > valor_mensal:
        valor_divida_restante = valor_divida_restante - valor_mensal
    if valor_divida_restante < valor_mensal:
        ultimo_valor_pago = valor_divida_restante
        valor_divida_restante = valor_divida_restante - valor_divida_restante
    mes = mes + 1

total_pago = (mes * valor_mensal) + ultimo_valor_pago
print(f'Você pagará sua dívida em {mes} meses. Total pago: R${total_pago}. Total de juros pago: R${total_pago - valor_divida_inicial} ')
