quantidade = int(input("Digite um número: "))
numero = 2
impresso = 1
while impresso < quantidade:
    if numero == 2:
        print(numero)
    else:
        if numero % 2 == 1:
            contador = 3
            while True:
                if numero % contador == 0:
                    if contador > numero:
                        break
                    if contador < numero:
                        break
                    if contador == numero:
                        print(numero)
                        impresso += 1
                        break
                contador += 2
    numero += 1
