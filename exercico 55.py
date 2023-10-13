maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Peso da {}ª Pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso Lido foi de {}Kg'.format(maior))
print('O Menor Peso Lido foi de {}Kg'.format(menor))


