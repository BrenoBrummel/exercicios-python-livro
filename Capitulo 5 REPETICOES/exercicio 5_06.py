# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4, ... O programa citado encontra-se na
#página 87 do livro.

n = int(input('Tabuada de: '))
x = 1
while x <= 10:
    print(f'{n} x {x} = {n * x}')
    x = x + 1
