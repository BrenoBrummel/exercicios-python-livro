#Escreva um programa que converta uma temperatura digitada em °C em °F.

celsius = int(input('Digite a temperatura em °C: '))

conversao = ((9 * celsius) / 5) + 32

print(f'{celsius}°C convertido em °F é {conversao}°F.')
