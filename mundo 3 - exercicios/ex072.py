"""
Crie um programa que tenha uma tupla totalmente preenchida com uma 
contagem por extenso, de zero até vinte. 

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e 
mostrá-lo por extenso. 
"""

nuextenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 
             'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 
             'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
             'Dezenove', "Vinte")

nu = int(input('Digite um número entre 0 e 20: '))
while nu < 0 or nu > 20:
    nu = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    

escolha = nuextenso[nu]

print(f'Você digitou o número {escolha}')

# :V