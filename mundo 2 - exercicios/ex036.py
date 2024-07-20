"""
Escreva um programa para aprovar o empréstimo 
bancário para a compra de uma casa. O programa
vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar. 

Calcule o valor da prestação mensal, sabendo 
que ela não pode esceder 30% do salário ou então 
o empréstimo será negado. 
"""

vl_casa = float(input('\nDigite o valor da casa: '))
salary = float(input('Digite o valor do seu salário: '))
years = int(input('Digite em quantos anos a casa vai ser paga: '))

meses = years * 12
parcelas = vl_casa / meses

if parcelas > (0.30 * salary):
    print(f"""\nSinto muito, mas 30% do seu salário é {0.30 * salary} reais, e
e a parcela da casa financiada em {years} anos é {parcelas:.2f} reais""")
else:
    print(f'\nParabéns, financiamento aprovado! {parcelas:.2f} reais pagos mensalmentes durantes {years} anos! \n30% do seu salário: {0.30*salary} reais')

# :D