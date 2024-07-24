texto = input("Digite um texto: ")
caracteres_encontrados = {}
for letra in texto:
    if letra in caracteres_encontrados:
        caracteres_encontrados[letra] += 1
    else:
        if letra == " ":
            pass
        else:
            caracteres_encontrados[letra] = 1
print(caracteres_encontrados)