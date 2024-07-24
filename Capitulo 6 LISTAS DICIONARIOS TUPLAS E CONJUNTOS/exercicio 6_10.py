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
if encontrou_valor1:
    print(f"{p} encontrado na posição {posicao1}")
else:
    print(f"{p} não foi encontrado")
if encontrou_valor2:
    print(f"{v} encontrado na posição {posicao2}")
else:
    print(f"{v} não foi encontrado")
