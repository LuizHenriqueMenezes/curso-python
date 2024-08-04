"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois 
mostre:

a) Apenas os 5 primeiros colocados. 
b) Os últimos 4 colocados da tabela. 
c) Uma lista com os times em ordem alfabética. 
d) Em que posição na tabela está o time da Chapecoense. 

* quando o professor gravou a aula o corinthians estava em primeiro :(

"""
brasileirao = ('Botafogo', 'Flamengo', 'Palmeiras', 'Fortaleza', 
               'Cruzeiro', 'São Paulo', 'Bahia', 'Athletico-PR',
               'Atlético-MG', 'Bragantino', 'Vasco da Gama', 'Criciúma'
               'Vitória', 'Juventude', 'Internacional', 'O TODO PODEROSO COLOSSAL DA ZL - CORINTHIANS',
               'Grêmio', 'Cuiabá', 'Fluminense', 'Atlético-GO')

print('\nBRASILEIRÃO 2024 - 04/08 | 10:42\n')
print('-=-'*20)
print(f'Lista de time do Brasileirão: {brasileirao}')
print('-=-'*20)
print(f'Os cinco primeiros são: {brasileirao[:5]}')
print('-=-'*20)
print(f'Os quatro últimos são: {brasileirao[-4:]}')
print('-=-'*20)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=-'*20)

if 'Chapecoense' in brasileirao:
    print(f'A Chape está em {brasileirao.index('Chapecoense')} na tabela\n')
else:
    print('Chapecoense não está no campeonato brasileiro 2024\n')

# :V