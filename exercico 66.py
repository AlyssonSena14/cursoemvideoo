n = c = s = 0
while True:
    n = int(input('Digite um Valor [999 para parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print('A soma dos {} valores foi {} !'.format(c, s))
