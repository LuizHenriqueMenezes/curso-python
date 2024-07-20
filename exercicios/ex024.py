#Crie um programa que leia o nome de uma cidade
#e diga se ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade: ')

first = cidade.upper().split()

result = 'SANTO' in first[0]

if result == True:
    print(f'{cidade} - Começa com SANTO')
else:
    print(f'{cidade} - Não começa com SANTO')
    
# :)