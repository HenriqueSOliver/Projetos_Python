time = ('Internacional', 'São Paulo', 'Flamengo', 'Atlético-MG', 'Palmeiras', 'Grêmio', 'Fluminense', 'Ceará-SC', 'Corinthians', 'Santos', 'Athético-PR', 'Atlético-GO', 'Bragantino', 'Sport Recife', 'Vasco da Gama', 'Fortaleza', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')

print('-'*80)
print(f'{"Classificação do Brasileirão 2021":^80}')
print('-'*80)

print(f'Lista de times do Brasileirão: {time}')
print('-'*80)

print(f'Os 5 primeiros são {time[:5]}')
print('-'*80)

print(f'Os 4 últimos lanterninhas são: {time[-4:]}')
print('-'*80)

print(f'Times em ordem alfabética: {sorted(time)}')
print('-'*80)

print(f'O Corinthians está na {time.index("Corinthians")+1}º posição.')






