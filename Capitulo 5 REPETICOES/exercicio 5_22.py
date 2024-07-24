# Escreva um programa que exiba uma lista de opções(menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
# Repita até que a opção saída seja escolhida.
while True:
    print("Tabuada")
    operador = str(input("Menu: adição(+), subtração(-), divisão(/), multiplicação(x) e sair(0)\nDigite o operador: "))
    if operador == "0":
        break
    tabuada = 1
    while tabuada <= 10:
        numero = 1
        while numero <= 10:
            if operador == "+":
                print(f"{tabuada} {operador} {numero} = {tabuada + numero}")
            elif operador == "-":
                print(f"{tabuada} {operador} {numero} = {tabuada - numero}")
            elif operador == "/":
                print(f"{tabuada} {operador} {numero} = {tabuada / numero}")
            elif operador == "x":
                print(f"{tabuada} {operador} {numero} = {tabuada * numero}")
            else:
                print("Operador inválido! Apenas +, -, /, x e 0 são aceitos.")
                break
            numero += 1
        tabuada += 1
