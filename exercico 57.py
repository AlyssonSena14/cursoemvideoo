sexo =  str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalido. Por favor, Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} Registrado com Sucesso'.format(sexo))