# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenanas os operadores de
#soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de doisnúmeros como somas sucessivas de um deles.
# Assim, 4x5 = 5+5+5+5 = 4+4+4+4+4. 

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
condicao = True
x = num1
y = 1

while condicao:
    if condicao:
        print(f'{num1} + ')
        x = x + num1
        y = y + 1
        if y == num2:
            print(num1)
            resultado = x
            condicao = False

print(f'O resultado da multiplicação de {num1} por {num2} é {resultado}')
