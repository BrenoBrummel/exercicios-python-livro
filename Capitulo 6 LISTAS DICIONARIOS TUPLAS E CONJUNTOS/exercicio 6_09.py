L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))
x = 0
encontrou_valor1 = False
encontrou_valor2 = False
while x < len(L):
    if L[x] == p:
        encontrou_valor1 = True
        posicao1 = x
    if L[x] == v:
        encontrou_valor2 = True
        posicao2 = x
    x += 1
if posicao1 < posicao2:
    print(f"O valor {p} foi achado primeiro do que o {v}")
elif posicao1 > posicao2:
    print(f"O valor {v} foi achado primeiro do que o {p}")
elif posicao1 == posicao2:
    print(f"Os valores {p} e {v} foram encontrados ao mesmo tempo!")
else:
    print("Alguns ou todos os valores não foram encontrados")
