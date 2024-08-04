"""
Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. No final, mostre: 

a) Quantas vezes apareceu o valor 9. 
b) Em que posição foi digitado o primeiro valor 3. 
c) Quais foram os números pares. 

"""
tupla = ()
pares = ()
aux = 0
auxPar = 0

for x in range(0, 4):
    n = int(input(f'Digite o {x+1}° valor: '))
    tupla += (n,)
    
    if n % 2 == 0:
        pares += (n,)
        auxPar += 1
    
    if n == 9:
        aux += 1
        
print(f'\nTodos os números: {tupla}')
print(f'Quantas vezes apareceu o número 9: {aux}')

if 3 in tupla:
    print(f'Posição que foi digitado o primeiro 3: {tupla.index(3)}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

if auxPar > 0:
    print(f'Números pares: {pares}')
    
# :V


    
    