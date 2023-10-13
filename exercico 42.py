s1 = float(input('Digite O Primeiro Segmento: '))
s2 = float(input('Digite O Segundo Segmento:  '))
s3 = float(input('Digite O Terceiro Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('os seguimento acima podem formar um triangulo ')
    if s1 == s2 == s3:
        print('EQUILÁTERO ! ')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO ! ')
    else:
        print('ISÓSCELES ! ')
else:
    print('Os Seguimento acima não Podem Formar um Triangulo ! ')
