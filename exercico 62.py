print('       Gerador de PA      ')
print(10*'-=-')
termo = int(input('O primeiro termo: '))
razao = int(input('Razão: '))
total = termo
cont = 1
totall = 0
mais = 10
while mais != 0:
    totall = mais+totall
    while cont <= totall:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    mais = int(input('Qual termo voce quer ver a mais ? '))
print('Fim. foram mostrados um total de {} termos'.format(totall))