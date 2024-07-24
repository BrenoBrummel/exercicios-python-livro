T = [-10, -8, 0, 1, 2, 5, -2, -4]
maximo = T[0]
minimo = T[0]
soma = 0
for m in T:
    if m > maximo:
        maximo = m
for mi in T:
    if mi < minimo:
        minimo = mi
for e in T:
    soma += e
media = soma / len(T)
print(f"Máximo: {maximo}. Mínimo: {minimo}. Média: {media}")
