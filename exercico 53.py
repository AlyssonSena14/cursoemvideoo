frase = str(input('Digite a Frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')

