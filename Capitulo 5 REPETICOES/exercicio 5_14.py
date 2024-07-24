# Escreva um progrma que leia números inteiros no teclado. O programa de ler os números até que o usuário digite 0 (zero). No final da execução,
#exiba a quantidade de números digitados, assim como a soma e a média aritmética.

contador = 0
soma = 0

while True:
    numeros = int(input('Digite um número: '))
    if numeros == 0:
        break
    soma += numeros
    contador += 1
print(f'Você digitou {contador} números. A soma desses números é {soma} e a média é {soma / contador}')
