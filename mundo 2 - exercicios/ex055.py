"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre
qual foi o maior e o menor peso lidos. 

"""
import math
maior = 0
menor =  math.inf
pesos = []

for x in range(0, 5):
    pesos.append(float(input(f'Digite o peso da {x+1}º pessoa: ')))
    
    if pesos[x] > maior:
        maior = pesos[x]
        
    if pesos[x] < menor:
        menor = pesos[x]
        
print(f'O maior peso foi {maior} e o menor {menor}')

# :D