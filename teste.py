while True:
    n = int(input('Digite o numero da tabuada: '))
    if n <= 0:
        break
    print(20 * '-=-')
    for c in range (1, 11 ):
        print('{} x {} = {}'.format(n, c, n*c))
    print(20 * '-=-')
print('PRGOMA DE TABUADA ENCERRADO. VOLTE SEMPRE')
