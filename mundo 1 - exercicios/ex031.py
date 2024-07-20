"""
Desenvolva um programa que pergunte a distância de 
uma viagem em KM. Calcule o preço da passagem, 
cobrando R$0,50 por KM para viagens de até 200km
e R$0,45 para viagens mais longas. 
"""

km = int(input('Qual a distância da viagem em km?\n'))

if km <= 200:
    print(f'A viagem de {km}km vai custar {km * 0.50} reais')
else:
    print(f'A viagem de {km} vai custar {km * 0.45} reais')
    
# :)