lista = ('làpis', 1.75,
         'Borracha',  2.00,
         'Caderno', 15.90,
         'Estojo ', 25.00,
         'Transferidor',  4.20,
         'Compasso',  9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print(60*'-')
print(F'{"LISTA DE PREÇOS":^50}')
print(60*'-')
for m in range(0, len(lista),2):
   print(f'{lista[m]:.<50}R$ {lista[m+1]}')
print(60*'-')


