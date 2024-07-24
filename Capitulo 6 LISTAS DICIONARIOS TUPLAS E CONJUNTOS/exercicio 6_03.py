a = []
b = []
c = []
d = []

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
x = 0
while x < len(c):
    y = 0
    while y < len(d):
        if c[x] == d[y]:
            break
        y += 1
    if y == len(d):
        d.append(c[x])
    x += 1
print(d)
    