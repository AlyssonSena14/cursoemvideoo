a = float(input('Digite sua altura ? (m) '))
p = float(input('Digite seu Peso ? (Kg) '))
r = p / (a * 2)
print('O IMC Dessa Pessoa é De {:.1f} '.format(r))
if r <= 18.5:
    print('Abaixo do Peso normal !')
elif 18.5 <= r < 25:
    print('Parabens, Voce Está com o PESO NORMAL !')
elif 25 <= r < 30:
    print('Voce Está Com SOBRE PESO')
elif 30 <= r < 40:
    print('Voce Está com OBESIDADE !')
else:
    print('Voce Está com OBESIDADE MÓRBIDA, CUIDADO !')
