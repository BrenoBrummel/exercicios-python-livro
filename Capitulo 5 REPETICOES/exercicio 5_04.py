# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, desta vez, apenas números ímpares. O programa
#citado está localizado na página 87 do livro.

fim = int(input('Digite o último número a imprimir: '))
x = 0
while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1
