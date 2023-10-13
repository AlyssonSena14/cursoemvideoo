num = int(input('digite um numero inteiro: '))
print('''escolha uma Das opeções de Base de dados
[1] Converter Para BINÁRIO
[2] Converter Para OCTAL
[3] Converter Para HEXADECIMAL''')
opçao = int(input('Digite Sua Opção: '))
if opçao == 1:
    print('O neumro {} Convertido Para BINARIO E IGUAL A {}'.format(num,bin(num)[2:]))
elif opçao == 2:
    print('O numero {} Convertido Para Octal E IGUAL A {}'.format(num,oct(num)[2:]))
elif opçao == 3:
    print('O numero {} Convertido Para HEXADECIMAL E IGUAL A {}'.format(num,hex(num)[2:]))
else:
    print('Opção Invalida. Tente Novamente. ')


