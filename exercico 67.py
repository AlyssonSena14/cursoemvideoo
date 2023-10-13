print(10*'-=-')
print('        Progama Tabuada        ')
while True:
    n = int(input('Digite o valor para a tabuada: '))
    if n < 0:
        break
    print(20*'--')
    for c in range(1, 11):
        s = c*n
        print('{} x {} = {}'.format(n, c, s))
    print(20*'--')
print('Fim do pragama Tabuada ! Volte sempre.')

