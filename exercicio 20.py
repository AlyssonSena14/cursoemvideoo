import random
nome1 = str(input('digite o primeiro nome:'))
nome2 = str(input('digite o segundo nome:'))
nome3 = str(input('digite o terceiro nome:'))
nome4 = str(input('digite o quarto nome:'))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(' a ordem de apresentaçao sera:')
print(lista)