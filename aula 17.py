num = []
for cont in range(0,5):
    num.append(int(input('Digite um valor: ')))
num [2] = 6
num.append(7)
num.sort(reverse=True)
num.insert(2,4)
num.insert(2,2)
if 11 in num:
    num.remove(11)
else:
    print('não achei o número 11')
for c,n in enumerate(num):
    print(f'Na posição {c} encontrei o valor {n}!')
print('Cheguei ao final da Lista !')
