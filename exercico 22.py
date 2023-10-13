frase = str(input('qual o seu nome Completo ?:')).strip()
print('Analisando seu nome...')
print('Seu nome em Letras Maiusculas é {} '.format(frase.upper()))
print('seu nome em Letras Minuscula é  {}'.format(frase.lower()))
print('seu nome tem ao todo {} Letras'.format(len(frase)-frase.count(' ')))
frase = frase.split()
frase = frase[0]
print('seu primeiro nome é {} e ele tem '.format(frase),len(frase),'Letras')
