"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar. 
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que 
passou do prazo.  

"""
import datetime

year_that_born = int(input('\nDigite o ano do seu nascimento: '))

current_year = datetime.datetime.now().year 

if current_year - year_that_born <= 17:
    print(f'Você ainda vai se alistar! Contagem regressiva: {18 - (current_year - year_that_born)} anos')
elif current_year - year_that_born == 18:
    print(f'É hora de se alistar! (Orando por vc)')
else: 
    print(f'Já passou da hora de se alistar! Caso não tenha feito, você está {(current_year - year_that_born) - 18} anos atrasado!')
    
# :D