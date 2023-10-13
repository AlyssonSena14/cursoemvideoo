print('{:=^40}'.format(' LOJAS JÚ MODAS '))
preço = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] á Vista dinheiro/cheque
[2] á Vista cartão 
[3] 2x no Cartão
[4] 3x ou mais no Cartão''')
opção = int(input('Qual é a Opção de Pagamento ? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera Parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas Parcelas ? '))
    parcela = total / totparc
    print('Sua Compra será Parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('\033[0:31:40m ERRO OPÇAO INVALIDA DE PAGAMENTO , TENTE NOVAMENTE ')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

