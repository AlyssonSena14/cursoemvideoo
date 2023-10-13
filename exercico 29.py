velocidade = float(input('Qual a Velocidade Atual do Carro ?'))
if velocidade > 80:
    print('Voce Passou do Limite de 80Km/h!')
    multa = (velocidade-80) * 7
    print('Voce Foi Multado voce deve paga R${:.2f}!'.format(multa))
print('Tenha Um Bom Dia, Dirija Com Segurança!')
