ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))
while True:
    print(f"Existem {len(fila1)} clientes na fila 1")
    print(f"Fila 1 atual: {fila1}")
    print("Digite F para adicionar um cliente ao fim da fila 1,")
    print(f"Existem {len(fila2)} clientes na fila 2")
    print(f"Fila 1 atual: {fila2}")
    print("\nDigite F para adicionar um cliente ao fim da fila 2,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, G, A, B ou S): ")
    x = 0
    while x < len(operacao):
        y = operacao[x]
        if y == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido na fila 1")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif y == "F":
            ultimo += 1
            fila1.append(ultimo)
        elif y == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido na fila 2")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif y == "G":
            ultimo += 1
            fila2.append(ultimo)
        elif y == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, G, A, B ou S!")
        x += 1
