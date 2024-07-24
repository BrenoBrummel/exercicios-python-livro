# Altere o programa anterior de forma a perguntar também  o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e
#você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito_inicial = float(input('Digite o valor do depósito inicial: '))
taxa_juros = float(input('Digite o valor da taxa de juros: '))
mes = 0
montante = deposito_inicial
print(f'O montante no mês {mes} é {montante}')

while mes <= 24:
    if mes >= 1:
        deposito_mensal = float(input('Digite o valor do seu depósito: '))
        montante = montante + deposito_mensal
        montante = montante + (montante * (taxa_juros / 100))
        print(f'O montante no mês {mes} é {montante}')
    mes = mes + 1
