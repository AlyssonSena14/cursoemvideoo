print('Loja da Ju')
cont100 = soma = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: '))
    valor = float(input('Preço do Produto: R$ '))
    cont += 1
    soma += valor
    if valor > 1000:
        cont100 += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Deseja Continuar ? [S/N] ')).strip().upper()[0]
    if opçao == 'N':
        break
print('o total da compra foi de  R${:.2f}'.format(soma))
print('Temos {} Produto custando mais de 1000.00R$'.format(cont100))
print('O produto mais barato foi {} e o valor dele è R${}'.format(barato, menor))
