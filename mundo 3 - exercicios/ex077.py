"""
Crie um programa que tenha uma tupla com várias palavras (não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais são
as suas vogais. 
"""

palavras = ('pato', 'chocolate', 'pokemon', 'amoxinha')

for palavra in palavras:
    vogais = ''  # Reinicia a string de vogais para cada palavra
    for letra in palavra:
        if letra in 'aeiou':  # Verifica se a letra é uma vogal
            vogais += letra + ' '
    print(f'Na palavra {palavra} temos: {vogais}')
    
# :V