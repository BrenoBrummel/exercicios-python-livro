a = []
b = []
c = []

while True:
    print("Adicione os itens da primeira lista")
    adicionar = int(input('Digite um número (0 sai): '))
    if adicionar == 0:
        break
    a.append(adicionar)

while True:
    print("Adicione os itens da segunda lista")
    adicionar = int(input('Digite um número (0 sai): '))
    if adicionar == 0:
        break
    b.append(adicionar)

c.extend(a)
c.extend(b)
print(c)
