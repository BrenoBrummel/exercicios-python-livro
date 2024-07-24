primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
if segunda in primeira:
    print(f"{segunda} encontrado na posição {primeira.find(segunda)} de {primeira}")
else:
    print("Não encontrado!")