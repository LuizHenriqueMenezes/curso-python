"""
Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos digitos separados. 

Ex:
1834

unidade: 4
dezena: 3
centena: 8
milhar: 1

"""
n = input('\nDigite um numero entre 0 a 9999: ')


print(f'unidade: {n[3]}\n'
      f'dezena: {n[2]}\n'
      f'centena: {n[1]}\n'
      f'milhar: {n[0]}')

# :)