"""
Faça um programa que leia um ano qualquer e mostre
se ele é bissexto.
"""
year = int(input('Digite um ano: '))

if year % 4 == 0:
    print(f'{year} é ano bissexto')
else:
    print(f'{year} NÃO é ano bissexto')

# :)
