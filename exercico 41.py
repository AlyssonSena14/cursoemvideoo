from datetime import date
ano = int(input('Qual O Seu ano de nascimento ? '))
ano1 = date.today().year-ano
print('O Atleta tem {} Anos.'.format(ano1))
if ano1 <= 9:
    print('Classificação: MIRIM ')
elif ano1 <= 14:
    print('Classificação: INFANTIL ')
elif ano1 <= 19:
    print('Classificação: JÚNIOR ')
elif ano1 <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
