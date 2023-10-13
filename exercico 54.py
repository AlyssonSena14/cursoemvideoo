from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
   ano = int(input('Em que ano a {}ª Pessoa nasceu ?'.format(pessoas)))
   idade = atual - ano
   if idade >= 21:
       totmaior += 1
   else:
       totmenor += 1
print('ao todo tivemos {} Pessoas maiores de idade '.format(totmaior))
print('ao todo ivemos {} Pessoas menores de idade '.format(totmenor))

