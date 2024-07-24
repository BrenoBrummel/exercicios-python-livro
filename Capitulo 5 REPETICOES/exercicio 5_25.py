#Obtive ajuda do site, pois não entendi muito bem como fazia
n = float(input('Digite um número: '))
b = 2
while abs((n - b * b)) > 0.0001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}")
