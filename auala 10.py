#nome = str(input('Digite o seu nome:'))
#if nome == 'alysson':
  #  print('que nome Lindo gostoso!')
#else:
   # print('seu nome e tão normal')
#print('Bem vindo, {}!'.format(nome))


n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('digite a sua segunda nota:'))
n = (n1+n2)/2
print('A sua Media foi {:.1f}'.format(n))
if n >= 6.0:
    print('é uma Boa nota')
else:
    print('voce precisa melhorar')
