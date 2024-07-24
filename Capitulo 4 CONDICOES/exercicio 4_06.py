#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0.50 por km
#para viagens de até 200km, e R$ 0.45 para viagens mais longas.

distancia = int(input('Digite a distância a ser percorrida: '))

if distancia <= 200:
    print(f'Para percorrer uma distância de {distancia}km você desembolsará um total de R${distancia * 0.5}.')

else:
    print(f'Para percorrer uma distância de {distancia}km você desembolsará um total de R${distancia * 0.45}.')
