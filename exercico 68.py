from random import randint
print(10*'-=-')
print('VAMOS JOGAR PAR OU IMPAR ')
print(10*'-=-')
v = 0
while True:
    jogador = int(input('Digite Um Valor: '))
    computador = randint(0, 11)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print('Voce Jogou {} e o Computador {}. Total de {} '.format(jogador, computador, soma), end='')
    print('DEU PAR ' if soma % 2 == 0 else 'DEU IMPAR' )
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif v == 0:
        print('Você acertou {} precisa melhorar!'.format(v))
    else:
        print('Muito bom você Acertou {} Vezes'.format(v))
    print('Vamos jogar Novamente...')
print('Game Over, você Acertou {} vezes'.format(v))