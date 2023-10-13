from datetime import date
data = int(input('Digite o ano de aniversário: '))
ano = date.today().year
resultado = ano-data
resultado2 = resultado-18
resultado3 = ano-resultado2
resultado44 = 18-resultado
resultado4 = resultado44+ano
print('Quem nasceu em {} tem {} Anos em {}'.format(data, resultado, ano))
if resultado == 18:
    print('Voce Tem que se alistar urgetemente ! ')
elif resultado > 18:
    print('Voce ja devia ter se Alistado HÁ {} anos '.format(resultado2))
    print('Seu alistamento foi em {}'.format(resultado3))
else:
    print('Ainda faltam {} anos Para o seu Alistamento !'.format(resultado44))
    print('Seu Alistamnto Será Em {}'.format(resultado4))

