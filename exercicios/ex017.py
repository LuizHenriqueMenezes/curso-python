#Faça um programa que leia o comprimento do cateto 
# oposto e do cateto adjacente de um triângulo 
# retângulo, calcule e mostre o comprimento da 
# hipotenusa.

import math 

comp_cateto = int(input('\nDigite o comprimento do cateto oposto: '))
cateto_adjacente = int(input('Digite o comprimento do cateto adjacente: '))

print(f'Resultado da hipotenusa: {math.sqrt((math.pow(comp_cateto,2) + math.pow(cateto_adjacente, 2)))}')

# :)