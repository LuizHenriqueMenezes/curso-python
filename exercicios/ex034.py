"""
Escreva um programa que pergunte o salário de um 
funcionário e calcule o calor do seu aumento. 

Para salparios superiores a R$1250,00, calcule um
aumento de 10%. 

Oara os inferiores ou iguais, o aumento é de 15%. 
"""
salary = float(input('Digite seu salário: '))

if salary <= 1250.00:
    print(f'Aumento de 15% no salário. Com isso vai pra {(salary + (0.15 * salary)):.2f}')
else:
    print(f'Aumento de 10%, salário agora é {(salary + (0.10 * salary)):.2f}')
    
# :)