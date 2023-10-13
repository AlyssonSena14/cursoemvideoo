times = ('América-MG','Athletico-PR','Atlético-MG','Bahia','Botafogo',
         'Corinthians','Coritiba','Cruzeiro','Cuiabá','Flamengo'
         ,'Fluminense''Fortaleza','Goiás','Grêmio','Internacional',
         'Palmeiras','Bragantino','Santos','São Paulo','Vasco da Gama')
print('-=-'*15)
print(f'Lista de times Brasileirão 2023: {times} ')
print('-=-'*15)
print(f'A lista dos 5 primeiro São: {times[0:5]}')
print('-=-'*15)
print(f'A Lista dos 4 ultimos são: {times[15:20]}')
print('-=-'*15)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-=-'*15)
print(f'O time Cruzeiro está na {times.index("Cruzeiro")+1} Posicão')
print('-=-'*15)