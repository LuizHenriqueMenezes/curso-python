"""
Crie um programa que leia vários números inteiros pelo teclado. No 
final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores. 
"""
import math

x = 1
aux = 0
maior = 0 
menor = math.inf
y = 0

while (x != 0):
    n = int(input('\nDigite um número: '))
    x = int(input('Quer continuar? 0. não 1. sim: '))
    
    if n > maior:
        maior = n
    
    if n < menor:
        menor = n
        
    aux += n
    y += 1
    
media = aux / y

print(f'\nA média entre todos os números foi {media}, o maior foi {maior} e o menor foi {menor}')

# :D

