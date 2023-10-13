km = float(input('Digite a Distancia da Viagem em Km!: '))
#pagamento = 1 * 0.50
if km <= 200:
    print('voce vai fazer uma viagem de {}Km '.format(km))
    pagamento = (km * 0.50 )
    print('O Valor da viagem será R${:.2f}'.format(pagamento))
else:
    print('voce vai fazer uma viagem de {}Km'.format(km))
    pagamento2 = (km * 0.45)
    print('entao sua viagem irá custar R${:.2f}'.format(pagamento2))