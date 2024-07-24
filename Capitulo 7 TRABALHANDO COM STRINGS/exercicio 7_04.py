string = input("Digite uma string: ")
caracteres = set(string)
print(caracteres)
for e in caracteres:
    print(f"{e}: {string.count(e)}x")