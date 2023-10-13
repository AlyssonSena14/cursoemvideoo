#nome= input ('qual e o seu nome ?')
#print('prazer em te conhecer {:>30} !'.format(nome))
n1 = int(input('digite um numero:'))
n2 = int(input('digite um segundo numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
rd= n1 % n2
sb = n1 - n2
print('a soma e {}  a multiplicaçao e {}'.format(s, m), end= "")
print(' a soma da divisao {:.3f} e divisao inteira e {}'.format(d, di))
print('a potencia e {} o resto da divisao e {}'.format(p, rd))
print('a subtraçao e {}'.format(sb))
