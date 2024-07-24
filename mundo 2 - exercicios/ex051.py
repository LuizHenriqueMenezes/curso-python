"""
Desenvolva um programa que leia o primeiro termo e a razão de uma 
progressão arimética. No final, mostre os 10 primeiros termos 
dessa progressão. 

"""

termo = int(input('\nDigite o primeiro termo: '))
r = int(input('Digite a razão: '))

for x in range(termo, termo+10, r):
    print(x)
    
# :D