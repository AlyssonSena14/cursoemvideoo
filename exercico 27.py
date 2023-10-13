nome = str(input('Qual e o seu nome ?')).strip().upper()
nome = nome.split()
print('o seu primeiro nome é {}'.format(nome[0]))
print('o seu ultimo nome é {}'.format(nome[len(nome)-1]))
