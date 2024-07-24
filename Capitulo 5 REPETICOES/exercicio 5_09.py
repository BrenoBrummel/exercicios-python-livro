# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
#os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a
#quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20:4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
x = num1
y = 0
condicao = True

while condicao:
    if condicao:
        x = x - num2
        y = y + 1
        if y > x:
            condicao = False
            resultado = y

print(f'O resultado da divisão de {num1} por {num2} é {resultado} e o resto da divisão é {x}')
