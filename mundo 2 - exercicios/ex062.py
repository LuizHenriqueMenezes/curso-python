"""
Melhore o desafio 061, perguntando para o usuário 
se ele quer mostrar mais alguns termos. O programa 
encerra quando ele disser que quer mostrar 0 termos.
"""

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while(mais != 0):
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1 
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    
print(f'Progressão finalizada com {total} termos mostrados')

# :D