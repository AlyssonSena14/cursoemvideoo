casa = float(input(' Digite O Valor Da Casa : R$'))
salario = float(input(' Digite O Valor Do Seu Salario : R$'))
tempo = int(input('Digite Quantos Anos De financiamento ? :'))
p = casa / (tempo * 12)
minimo = salario * 30 / 100
print('Para Pagar uma Casa Que Vale R${} EM {}Anos Com O Salario De R${} vai Custar R${:.2f} Por mes '.format(casa,tempo,salario,p))
if p <= minimo:
    print('Emprestimo concedido !')
else:
    print('Emprestimo negado !')
