"""
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura
while. 
"""

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(' -> {}'.format(termo), end='')
    termo += razao
    cont += 1
    
# :D