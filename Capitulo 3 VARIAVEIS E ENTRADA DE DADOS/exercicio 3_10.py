#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário.

salario = float(input('Digite o valor do salário: '))
porcentagem_aumento = float(input('Digite a porcentagem do aumento: '))

salario_aumentado = salario + salario * (porcentagem_aumento / 100)

print(f'O valor do aumento foi R${salario * (porcentagem_aumento / 100):.2f} e seu novo salário agora é R${salario_aumentado:.2f}')
