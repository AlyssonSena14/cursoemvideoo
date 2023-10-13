dias = int(input('quantos dias o carro foi alugado ?'))
km = float(input('quantos km foram rodados ?'))
d = dias*60
k = km*0.15
s = d+k
print('total a pagar! R${:.2f}'.format(s))