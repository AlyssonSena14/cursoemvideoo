nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a Segunda nota'))
resultado = nota1+nota2
resultado2 = resultado//2
print('O Aluno tirando nota {} e {} A media do Alundo será {}'.format(nota1, nota2, resultado2))
if resultado2 > 7:
    print('Aluno esta Aprovado !')
elif resultado2 == 5:
    print('O Aluno Está De Recuperação ! ')
else:
    print('O Aluno Está Reprovado !')
