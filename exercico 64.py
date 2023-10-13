nu = cont = soma = 0
nu = int(input('Digite um número [999 para parar]: '))
while nu != 999:
    soma += nu
    cont += 1
    nu = int(input('digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles  foi {}.'.format(cont, soma))