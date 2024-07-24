"""
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daquelas que forem pares. Se o valor digitado for 
ímpar, desconsidere-o. 
"""

ns = []
nsPar = []
aux = 0

for i in range(0, 6):
    ns.append(int(input('Digite um número: ')))
    
    if (ns[i] % 2) == 0:
        aux += ns[i]
        nsPar.append(ns[i])
        
print(f'A soma dos valores {nsPar} (pares) é {aux}')

# :D