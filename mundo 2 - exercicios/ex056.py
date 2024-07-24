"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos. 
"""
groupNames = []
groupAges = []
groupFM = []
maisVelho = 0
maisVelhoNome = ''
twentyWomans = 0
media = 0

for x in range(0, 4):

    groupNames.append(input(f'\nDigite o nome do {x+1}º integrande: '))
    groupAges.append(int(input(f'Digite a idade do {x+1}º integrande: ')))
    groupFM.append(int(input(f'Qual o sexo? 1. Masculino 2.Feminino: ')))
    
    media += groupAges[x]
            
    if groupFM[x] == 1:
        groupFM[x] = 'Masculino'
    elif groupFM[x] == 2:
        groupFM[x] = 'Feminino'
    
    if groupAges[x] < 20 and groupFM[x] == 'Feminino':
        twentyWomans += 1
        
    if groupAges[x] > maisVelho and groupFM[x] == 'Masculino':
        maisVelho = groupAges[x]
        maisVelhoNome = groupNames[x]
            
    
media /= 4

print(f'\nMédia de idade do grupo = {media} anos.')
print(f'Homem mais velho = {maisVelhoNome} com {maisVelho} anos.')
print(f'Tem {twentyWomans} mulheres com menos de 20 anos.')

# :D