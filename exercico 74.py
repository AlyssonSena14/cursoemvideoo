import random
from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\n O maior numero sorteado foi {max(numeros)} ')
print(f' o menor numero sorteado foi {min(numeros)}')
