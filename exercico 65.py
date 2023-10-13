resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / quant
print('voce digitou {} Números e a Media foi {:.1f}'.format(quant, média))
print('O maior valor Foi {} e O menor valor foi {}'.format(maior, menor))
