#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
#ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o 
#total em dias.

cigarros_fumados_dia = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos_fumados = int(input('Digite a quantidade de anos que você já fumou: '))

total_cigarros = cigarros_fumados_dia * (anos_fumados * 365)

dias_vida_perdidos = total_cigarros * 10

print(f'Esse fumante perdeu {dias_vida_perdidos / 60 / 24:.0f} dias de vida.')
