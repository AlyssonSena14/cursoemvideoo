import math
angulo = int(input('digite o angulo!:'))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.atan(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('o angulo de {} tem o coseno de {:.2f}'.format(angulo, coseno))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))
