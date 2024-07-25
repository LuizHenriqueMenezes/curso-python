"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
"""
n = int(input('Digite um número: '))
x = n - 1
conta = n * x

while(x != 0):
    x -= 1
    if x != 0:
        conta *= x
    
print(f'{n}! = {conta}')

# :D