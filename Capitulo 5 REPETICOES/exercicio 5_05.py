# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3. O programa citado está localizado na página 87.

x = 1
condicao = True

while condicao:
    if x % 3 == 0:
        print(x)
        if x / 3 == 10:
            condicao = False    
    x = x + 1
