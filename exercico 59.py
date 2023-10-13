n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    opção = int(input('Qual e a sua opção ? '))
    if opção == 1:
        soma = n1+n2
        print('A soma de {} e {} e igual a {}'.format(n1,n2,soma))
    elif opção == 2:
        soma = n1 * n2
        print('A Mutiplicação de {} x {} e igual a {}'.format(n1,n2,soma))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opção == 4:
        int(input('Digite um novo número:'))
    elif opção == 5:
        print('Finalizando ....')
    else:
        print('Opção invalida, tente novamente !')
print('fim do progama! volte sempre!')
