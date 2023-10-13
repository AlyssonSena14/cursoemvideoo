from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('-==-'*20)
print('Vou pensar em um Número entre 0 e 5 Tente Adivinhar...')
print('-==-'*20)
jogador = int(input('Em qual Número Pensei ? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns Voce Acertou!')
else:
    print('Voce Errou o Numero Correto É {} Não {}'.format(computador, jogador))
