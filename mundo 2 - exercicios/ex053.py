"""
Crie um programa que leia uma frase qualquer e diga se ela é um 
palíndromo, desconsiderando os espaços. 
"""

frase = input('Digite uma frase: ')

fraseNotSpace = frase.replace(' ', '')

aoContrario = fraseNotSpace[::-1]

if aoContrario == fraseNotSpace:
    print(f'{frase} é palíndromo!')
else:
    print('Não é palíndromo')
    
# :D