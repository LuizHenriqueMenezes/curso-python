"""
Melhore o jogo do desafio 028 onde o computador vai "pensar" em 
um número entre 0 e 10. Só que agora o jogador vai tentar advinhar
até acertar, mostrando no final quantos palpites foram necessários
para vencer.
"""
import random

number = int(input('\nAdvinhe o número entre 0 e 10: '))
pc = random.randint(0, 10)
aux = 1

while(number != pc):
    number = int(input('sNova tentativa, acerte o número entre 0 e 10: '))
    aux+=1
    
print(f'\nParabéns, vc advinhou! Em {aux} tentativas')

# :D