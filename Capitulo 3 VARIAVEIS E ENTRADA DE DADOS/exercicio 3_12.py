#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia_a_percorrer = float(input('Digite a distância a percorrer: '))
velocidade_media = int(input('Digite a velocidade média esperada para a viagem: '))

tempo_viagem = distancia_a_percorrer / velocidade_media

print(f'O tempo de viagem esperado para percorrer {distancia_a_percorrer}km a {velocidade_media}km/h é {int(tempo_viagem)}h.')