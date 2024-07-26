"""
Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo. 

"""

import random
wins = 0

while True:
    pc = random.randint(1, 10)
    user = int(input('\nDigite um número pra jogar par ou ímpar (1 - 10): '))
    choice = input('Você quer par(P) ou ímpar(I)? ').upper()
    sum = pc + user
    
    if sum % 2 == 0 and choice == 'P':
        wins += 1
        print(f'\nVocê ganhou - {sum} é ímpar')
        
    if sum % 2 != 0 and choice == 'I':
        wins += 1
        print(f'\nVocê ganhou - {sum} é ímpar')
        
    if sum % 2 != 0 and choice == 'P':
        print(f'\nVocê perdeu - {sum} é ímpar')
        break
    
    if sum % 2 == 0 and choice == 'I':
        print(f'\nVocê perdeu - {sum} é par')
        break
    
print(f'\nO usuário ganhou {wins} vezes')
    
# :D
    
    
