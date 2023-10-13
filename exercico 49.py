n = int(input('Digite o numero : '))
s = 0
for c in range(1, 11, ):
    for b in range(1, n+1):
        s = b * c
    print('{} X {} = {} '.format(c, b, s))