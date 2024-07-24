#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

conversao_para_segundos = segundos + 60 * (minutos + 60 * (horas + 24 * dias))

print(f'A conversão de {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para segundos somados é {conversao_para_segundos} segundos.')
