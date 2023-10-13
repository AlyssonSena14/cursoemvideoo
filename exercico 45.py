from random import  randint
from time import  sleep
intes = ('Pedra','Papel', 'Tesoura')
computador = randint(0, 2)
print('''suas opeção:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a Sua jogada ?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computado jogou {}'.format(intes[computador]))
print('Jogador jogou {}'.format(intes[jogador]))
print('-=' * 11)
if computador == 0:#computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA, TENTE NOVAMENTE !')

elif computador == 1:#computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU ')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU ')
    else:
        print('JOGADA INVÁLIDA, TENTE NOVAMENTE !')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU ')
    elif jogador == 1:
        print('COMPUTADOR VENCEU ')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA, TENTE NOVAMENTE !')
