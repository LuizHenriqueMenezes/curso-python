"""
Escreva um programa que faça o computador "pensar" em
um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo 
computador.

O programa deverá escrever na tela se o usuário venceu
ou perdeu. 
"""
import random

number = int(input('\nAdvinhe o número entre 0 e 5: '))

pc = random.randint(0, 5)

if number == pc:
    print(f'CONGRATULATIONS! Você acertou o número {pc}')
else:
    print(f'Hum, você chutou {number} e o número correto era {pc} :(')
    
# :)