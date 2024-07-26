"""
Faça um programa que mostre a tabuada de vários números, um de 
cada vez, para cada valor digitado pelo usuário. O programa será 
interrompido quando o número solicitado for negativo. 

"""

while True:
    n = int(input('\nDigite um número: '))
    
    if n < 0:
        print('\nnão é possível ler números negativos')
        break
    
    print(f'\nTabuada do {n}:')
    for x in range(0, 11):
        print(f'{n} * {x} = {n*x}')
        
    