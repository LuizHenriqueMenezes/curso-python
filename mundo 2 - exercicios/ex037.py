"""
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:

1. para binário
2. para octal
3. para hexadecimal

"""
n = int(input('Digite um número inteiro: '))
choice = int(input("""Escolha uma das opções de conversão:
1. Binário
2. Octal
3. Hexadecimal

Opção escolhida: """))

if choice == 1:
    print(f'\n{n} convertido pra binário é {bin(n) [2:]}')
elif choice == 2:
    print(f'\n{n} convertido para octal é {oct(n) [2:]}')
elif choice == 3:
    print(f'\n{n} convertido pra hexadecimal é {hex(n) [2:]}')
else:
    print('\nEscolha uma opção válida!')

# :D

