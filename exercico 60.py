from math import factorial
n = int(input('Digite um valor para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' X 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(n,f ))