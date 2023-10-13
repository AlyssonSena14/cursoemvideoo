print(10 * '-=-')
print('   CADASTRE UMA PESSOA   ')
print(10 * '-=-')
cidade = csexo = cont20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F] ')).strip().upper()[0]
    if idade >= 18:
        cidade += 1
    if sexo == 'M':
        csexo += 1
    if sexo == 'F' and idade < 20:
        cont20 += 1
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if opçao == 'N':
        break
print('total de pessoas com idade maior que 18 anos e {}'.format(cidade))
print('total de homens cadastrado São {} '.format(csexo))
print('Toral de mulheres menor que 20 anos São {}'.format(cont20))




