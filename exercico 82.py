lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    opaçao = str(input('Você quer continuar ? [S/N]')).strip().upper()[0]
    if opaçao == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de números pares e {pares}')
print(f'A lista de numeros ímpares é {impares}')





