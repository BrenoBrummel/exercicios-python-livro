# Modifique o progrma para também trabalhar com notas de R$100.

#Progrmama 5.1 - Contagem de cédulas
valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédulas(s) de R${atual}')
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
