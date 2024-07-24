primeira = input("Digite uma string: ")
segunda = input("Digite outra string: ")
terceira = ""
for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra

if terceira == "":
    print("As strings não têm nenhum caractere em comum!")
else:
    print(terceira)