primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = input("Digite a terceira string: ")
resultado = []
for a in primeira:
    x = 0
    while True:
        if x == len(segunda):
            resultado.append(a)
            break
        elif segunda[x] == a:
            resultado.append(terceira[x])
            break
        x += 1
res = "".join(resultado)
print(res)