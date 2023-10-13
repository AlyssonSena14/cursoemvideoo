nomes = ('APRENDER', 'PROGAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGAMADOR', 'FUTURO')
for c in nomes:
    print(f'\nNa Palavra {c.upper()} temos: ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')



