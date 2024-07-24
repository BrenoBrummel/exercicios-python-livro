L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0
while x < len(L):
    if L[x] == p:
        break
    x += 1
if x < len(L):
    print(f"{p} foi encontrado na posição {x}")
else:
    print(f"{p} não foi encontrado")
#Resolvido com a ajuda do livro. Eu já havia resolvido, porém estava totalmente diferente da lógica que o autor queria