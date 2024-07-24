import random
lista1 = [random.randint(1, 100) for _ in range(15)]
lista2 = [random.randint(1, 100) for _ in range(15)]
print("Lista 1", lista1)
print("Lista 2", lista2)
comuns = []
apenas_primeira = lista1[:]
apenas_segunda = lista2[:]
sem_repetidos = []
primeira_sem_repetidos = []
for a in lista1:
    for b in lista2:
        if a == b:
            comuns.append(b)
print("Valores comuns às duas listas: ", comuns)

x = 0
while x < len(apenas_primeira):
    for e in lista2:
        if apenas_primeira[x] == e:
            del apenas_primeira[x]
    x += 1

print("Valores que só existem na primeira: ", apenas_primeira)

y = 0
while y < len(apenas_segunda):
    for e in lista1:
        if apenas_segunda[y] == e:
            del apenas_segunda[y]
    y += 1

print("Valores que só existem na segunda: ", apenas_segunda)

sem_repetidos.extend(apenas_primeira)
sem_repetidos.extend(apenas_segunda)

print("Lista sem os elementos repetidos: ", sem_repetidos)

primeira_sem_repetidos.extend(lista1)
primeira_sem_repetidos.extend(apenas_segunda)

print("A primeira lista sem os elementos na segunda: ", primeira_sem_repetidos)
