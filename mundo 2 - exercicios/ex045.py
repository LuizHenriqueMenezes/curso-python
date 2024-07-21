"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random 

pc = random.randint(1,3)
escolha = int(input(""" -- Escolha uma opção pra jogar Jokenpô 
1. Pedra
2. Papel
3. Tesoura 

Opção escolhidas: """))

if pc == 1:
    pc = 'Pedra'
elif pc == 2:
    pc = 'Papel'
elif pc == 3:
    pc = 'Tesoura'

if escolha == 1:
    escolha = 'Pedra'
elif escolha == 2:
    escolha = 'Papel'
elif escolha == 3:
    escolha = 'Tesoura'

if pc == escolha:
    print('\nEmpate!')
elif pc == 'Pedra' and escolha == 'Papel':
    print(f'\nO usuário ganhou! Pc escolheu {pc} e o usuário escolheu {escolha}')
elif pc == 'Papel' and escolha == 'Pedra':
    print(f'\nO pc ganhou! Pc escolheu {pc} e o usuário escolheu {escolha}')
elif pc == 'Pedra' and escolha == 'Tesoura':
    print(f'\nO pc ganhou! Pc escolheu {pc} e o usuário escolheu {escolha}')
elif pc == 'Tesoura' and escolha == 'Pedra':
    print(f'\nO usuário ganhou! Pc escolheu {pc} e o usuário escolheu {escolha}')
elif pc == 'Tesoura' and escolha == 'Papel':
    print(f'O pc ganhou! Pc escolheu {pc} e o usuário escolheu {escolha}')
elif pc == 'Papel' and escolha == 'Tesoura':
    print(f'O usuário ganhou! Pc escolheu {pc} e o usuário escolheu {escolha}')
    
# :D