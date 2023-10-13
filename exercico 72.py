numerosex = ('Zero', 'Um', 'Dois','Três','quatro','Cinco','Seis','sete','oito','nove','dez',''
'onze','doze','treze','quatoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente ',end='')
print(f'Você digitou o número {numerosex[n]}')
