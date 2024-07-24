primeira = input("Digite uma string: ")
segunda = input("Digite outra string: ")
terceira = list(primeira)
caracteres = set(segunda)
for a in caracteres:
    x = 0
    while x < len(terceira):
        if a == terceira[x]:
            del terceira[x]
            x -= 1
        x += 1
t = "".join(terceira)
print(f"1º string: {primeira}\n2º string: {segunda}\n3º string: {t}")