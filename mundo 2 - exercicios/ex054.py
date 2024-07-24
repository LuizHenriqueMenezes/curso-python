"""
Crie um programa que leia o ano de nascimento de sete pessoas. No 
final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas ja são de maiores. 

"""
import datetime 

years = []
aux = 0

for x in range(0, 7):
    years.append(int(input(f'Digite o ano de nascimento da {x+1}º pessoa: ')))
    
    if (datetime.datetime.now().year) - years[x] >= 18:
        aux += 1
        
    
print(f'Quantidade de pessoa maiores de idade: {aux}')
print(f'Quantidade de pessoas menores de idade: {len(years) - aux}')

# :D