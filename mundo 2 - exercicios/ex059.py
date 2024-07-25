"""
Crie um programa que leia dois valores e mostre um menu na tela:

1. somar
2. multiplicar
3. maior
4. novos números
5. sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. 
"""
n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite outro número: '))

x = int(input("""\n1. somar
2. multiplicar
3. maior
4. novos números
5. sair do programa

Escolha uma opção: """))


while x != 5:
    if x == 1:
        print(f'\nSoma de {n1} + {n2} = {n1 + n2}')
    elif x == 2:
        print(f'\nMultiplicação de {n1} * {n2} = {n1*n2}')
    elif x == 3:
        if n1 > n2:
            print(f'\n{n1} maior que {n2}')
        else: 
            print(f'\n{n2} maior que {n1}')
    elif x == 4:
        n1 = int(input('\nDigite um novo número 1: '))
        n2 = int(input('Digite um novo número 2: '))
    
    x = int(input('\nEscolha uma opção: '))
    
print('\nObrigado por utilizar o programa!')

# :D