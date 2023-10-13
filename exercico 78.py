valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print(f'Você Digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ',end=' ')
for i,v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...',end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ',end='')
for i,v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...',end=' ')