n = cont = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
##print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
          
