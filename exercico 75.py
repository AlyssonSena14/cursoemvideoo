n = int(input('Digite um numéro: '))
n2 = int(input('Digite outro numéro: '))
n3 = int(input('Digite mais um numéro: '))
n4 = int(input('Digite o último numéro: '))
numeros = (n,n2,n3,n4)
print('Você Digitou os valores: ',end=' ')
for mostrar in numeros:
    print(mostrar,end=' ')
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'o valor 3 apareceu na {numeros.index(3)+1}ª posiçao')
else:
    print('O valor 3 não apareceu ! ')
print('Os valores pares digitados foram ',end=' ')
for r in numeros:
    if r % 2 == 0:
        print(r,end=' ')






