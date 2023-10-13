sexo = cont = ma = fe = idade = 0
while True:
    nome = str(input('Qual é o Nome ? '))
    sexo = str(input('Qual e o seu sexo [M/F] ')).strip().upper()[0]
    idade = int(input('Qual a idade: '))
    nome = ' '
    opçao = ' '
    cont += 1
    if sexo == 'M':
        ma += 1
    else:
        fe += 1
        if idade >= 0:
            velho = idade
        elif idade >= 0:
            nova = idade
    while opçao not in 'SN':
        opçao = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if opçao == 'N':
        break
print('Dado Registrados com sucesso ! foram registrado {} Pessoas'.format(cont))
print('foram Registrados {} Homens e {} Mulheres'.format(ma,fe))
print('O homem mais velho tem {} Anos'.format(velho))
print('A mulher mais nova tem {} Anos'.format(nova))




