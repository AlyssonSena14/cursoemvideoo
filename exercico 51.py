print(' {:=^40}'.format('10 TERMOS DE UMA PA'))
n1 = int(input('Digite o Primeiro Termo: '))
n2 = int(input('Digite A RAZÃO: '))
decimo = n1 + (10 - 1) * n2
for c in range(n1, decimo + n2, n2):
    print('{} '.format(c), end='->')
print('ACABOU')
