import random
lista1 = [random.randint(1, 40) for _ in range(10)]
lista2 = [random.randint(1, 40) for _ in range(10)]
conjunto1 = set(lista1)
conjunto2 = set(lista2)

print(f"Conjunto 1 :{conjunto1}")
print(f"Conjunto 2 :{conjunto2}")
print("Os elementos que não mudaram: ", conjunto1 - (conjunto1 - conjunto2))
print("Os novos elementos: ", conjunto2 - conjunto1)
print("Os elementos que foram removidos: ", conjunto1 - conjunto2)
