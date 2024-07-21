"""
A confederação nacional de natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo
com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL 
- Até 19 anos: JUNIOR 
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
import datetime

born_year = int(input('Digite o ano de nascimento: '))

age = (datetime.datetime.now().year) - born_year

if age <= 9:
    print(f'MIRIM com {age} anos')
elif age > 9 and age <= 14:
    print(f'INFANTIL com {age} anos')
elif age > 14 and age <= 19:
    print(f'JUNIOR com {age} anos')
elif age == 20:
    print(f'SÊNIOR com 20 anos')
elif age > 20:
    print(f'MASTER com {age} anos')
else:
    print('Você inseriu algum valor inválido')
    
# :D