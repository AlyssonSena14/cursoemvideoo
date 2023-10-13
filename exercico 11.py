print('ola, seja bem vindo!')
n1 = float(input('digite o numero de metros da altura:'))
n2 = float(input('digite o numero de metoros da largura:'))
n3 = n1*n2
n4 = n3/2
print('a dimensão da sua parede é de {}x{} a area total da parede e de {}m² vai ser preciso {}L de tinta para pintar '.format(n1, n2, n3, n4))