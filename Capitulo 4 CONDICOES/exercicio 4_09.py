#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário
#e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o
#valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos_a_pagar = int(input('Anos a pagar: '))

prestacao = valor_casa / (anos_a_pagar * 12)

if prestacao > (salario * 0.3):
    print('Não é possível solicitar o empréstimo, pois o valor da prestação excede o valor de 30% do seu salário.')
elif prestacao <= (salario * 0.3):
    print(f'Empréstimo aprovado! Você irá pagar {prestacao:.2f} por {anos_a_pagar * 12} meses ou {anos_a_pagar} anos.')
else:
    print('Aconteceu um erro!')

print(f'Dados:\nValor da prestação: {prestacao:.2f}\n30% do salário: {salario * 0.3}')
