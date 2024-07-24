numero = int(input("Digite um número: "))
if numero == 2:
    print(f"O número {numero} é um número primo!")
elif numero > 2:
    if numero % 2 == 1:
        contador = 3
        while True:
            if numero % contador == 0:
                if contador > numero:
                    print(f"O número {numero} não é um número primo pois é divisível por {contador}")
                    break
                if contador < numero:
                    print(f"O número {numero} não é um número primo pois é divisível por {contador}")
                    break
                if contador == numero:
                    print(f"O número {numero} é um número primo!")
                    break
            contador += 2
    else:
        print(f"O número {numero} não é um número primo!")
else:
    print("Os números 0, 1 e todos os números negativos não são aceitos nesse programa")
