"""
Escreva um programa que leia a velocidade de um 
carro. 

Se ele ultrapassar 80km/h, mostre uma mensagem 
dizendo que ele foi multado. 

A multa vai custar R$7,00 por cada km acima do limite. 
"""
import emoji

car = int(input('\nDigite a velocidade do carro: '))
difference = car - 80

if car > 80:
    print(f'Parado ai Dominic Toretto {emoji.emojize(':hand_with_fingers_splayed:')}\n'
          f'Você está sendo multado em {difference * 7} reais')
else:
    print('Não fez mais que sua obrigação')

# :)