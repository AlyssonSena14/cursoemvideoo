print(10*'-=-')
valor = int(input('Qual valor você Deseja sacar ? '))
print(10*'-=-')
total = valor
cèd = 50
totcèd = 0
while True:
    if total >= cèd:
        total -= cèd
        totcèd += 1
    else:
        print('Total de {} cèdulas de R$ {}'.format(totcèd, cèd))
        if cèd == 50:
            cèd == 20
        elif cèd == 20:
            cèd == 10
        elif cèd == 10:
            cèd == 1
            totcèd = 0
        if total == 0:
            break






