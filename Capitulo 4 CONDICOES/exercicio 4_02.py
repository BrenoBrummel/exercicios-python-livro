#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h.

velocidade = int(input('Digite sua velocidade: '))
multa = float

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Você dirigiu a {velocidade}km/h e foi autuado em R${multa:.2f} por excesso de velocidade.')

if velocidade <= 80:
    print('Parabéns você é um ótimo condutor e não foi autuado!')
