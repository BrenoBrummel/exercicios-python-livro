num1 = int(input('Digite um número: '))
num2 = int(input('Digite o número que dividirá o primeiro: '))
while True:
    if num1 < num2:
        break
    num1 -= num2
print(f'O resto da divisão é {num1}')
