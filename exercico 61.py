print('        Gerador de PA    ')
print(10*'-=-')
n1 = int(input('Digite o Primeiro termo: '))
n2 = int(input('Razão do PA: '))
termo = n1
cont = 1
while cont <= 10:
    print(' {} -> '.format(n1), end='')
    n1 += n2
    cont += 1
print('Fim.')
