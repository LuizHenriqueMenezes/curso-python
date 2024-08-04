"""
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. 

Depois disso, mostre a listagem de números gerados e também indique o 
menor e o maior valor que estão na tupla. 

"""
import random, math

tupla = ()
menor = math.inf
maior = 0

for x in range(0, 5):
    n = random.randint(1, 999)
    
    tupla += (n,)
    
    if menor > n:
        menor = n
    
    if maior < n:
        maior = n


print(tupla)
print(f'Menor: {menor}')
print(f'Maior: {maior}')

# :V