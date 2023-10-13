temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar ? [SIM/NÃO] ')).strip().upper()[0]
    if resp in 'nN':
        break
print(f'Ao todo foram cadastrados {len(princ)} Pessoas')
print(f'O maior peso foi {mai}kg, peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {men}kg, peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')

        