núm = [[], []]
valor = 0
for valor in range(1, 8):
    valor = int(input('digite o valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print(40*'-=-')
print(f'Os valores são {núm}')
núm[0].sort()
núm[1].sort()
print(f'Os Valores pares são {núm[0]}')
print(f'Os valores impares são {núm[1]}')