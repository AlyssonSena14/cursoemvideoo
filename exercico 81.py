valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
print(30*'-=-')
valores.sort(reverse=True)
print(f'Voce digitou {len(valores)} Elementos: ')
print(f'Os valores digitados em ordem decrescente são: {valores} ')
if 5 in valores:
    print('O numero 5 está na Lista !')
else:
    print('O numero 5 não está na Lista !')