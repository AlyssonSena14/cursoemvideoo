from random import randint
print('Seu computador... Acabei de chutar um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar ?')
n = int (randint(0, 10))
p = 0
t = 0
while p != n:
    p = int(input('Seu palpite: '))
    p += 1
    t += 1
    if p == n:
        print('Prabéns, Você acertou placar %i ' % t)
    elif p < n:
        print('Chute um valor maior ')
    else:
        print('Chute um valor menor ')
print('com {} Tentativas '.format(p))