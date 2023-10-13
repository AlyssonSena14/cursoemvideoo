valores = []
while True:
    valores.append(int(input('Digite Um valor: ')))
    print('Valor Adicionado com sucesso...')
    lista = valores[-1]
    opção = ' '
    if valores.count(lista) > 1:
        print('valor Duplicado! não vou adicionar...')
        valores.pop(-1)
    while opção not in 'SN':
        opção = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if opção == 'N':
        break
valores.sort()
print(f'Voce digitou os valores {(valores)}')