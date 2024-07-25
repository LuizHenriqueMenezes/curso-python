"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite 
valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
até ter um valor correto. 
"""

sexo = str(input('Digite o seu sexo: ')).upper()

while((sexo != "M") and (sexo != "F")):
    sexo = str(input('Por favor, digite apenas M ou F: ')).upper()
    
print('Obrigado por informar!')

# :D