primeira = input("Digite uma string: ")
segunda = input("Digite outra string: ")
terceira = ""
for letra in segunda:
    if letra in segunda and letra not in primeira:
        terceira += letra
for letra in primeira:
    if letra in primeira and letra not in segunda:
        terceira += letra

if terceira == "":
    print("Os caracteres são iguais!")
else:
    print(terceira)