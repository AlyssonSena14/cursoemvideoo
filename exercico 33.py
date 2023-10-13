from time import sleep
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('digite o terceiro numero:'))
print('verificando quem é o menor numero...')
sleep(2)
print('Verificando quem é o maior numero...')
sleep(2)
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
menor =
print('O Menor Numero é {}!'.format(menor))
print('O Maior numero é {}!'.format(maior))
