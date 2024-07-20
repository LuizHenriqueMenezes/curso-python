#Crie um programa que leia o nome de uma pessoa
#e diga se ela tem "SILVA" no nome. 

nome = input('Digite seu nome completo: ')

result = 'SILVA' in nome.upper()

if result == True:
    print(f'{nome.upper()} tem SILVA no nome')
else:
    print(f'{nome.upper()} não tem SILVA no nome')
    
# :)