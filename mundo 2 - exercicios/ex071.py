"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de
cada valor serão entregues. 

obs: Considerando que o caixa possui cédulas de R$50, R$20, 
R$10 e R$1. 
"""
n = int(input('Qual o valor a ser sacado? '))
total = n

ced = 50
total_cedulas = 0

while True:
    if total >= ced:
        total -= ced
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${ced}')
        
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        
        total_cedulas = 0
        
        if total == 0:
            break
        
# :D 


            
    
        
    
        
            
    