"""
ex 009 - Faça um programa que leia um número inteiro qualquer e mostre 
na tela a sua tabuada. 

ex 049 - Refaça o desafio 009, mostrando a tabuada de um número que o 
usuário escolher, só que agora utilizando um laço for. 

"""
x = int(input('Digite um número: '))

for h in range(0, 11):
    print(f'{x} x {h} = {x * h}')

# :D