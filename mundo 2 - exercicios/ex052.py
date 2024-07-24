"""
Faça um programa que leia um número inteiro e diga se ele é ou não 
um número primo. 

"""
aux = 0
n = int(input('Digite um número: '))

for i in range(1, n+1):
    if(n % i) == 0:
        aux += 1
     
if aux == 2:
    print('É PRIMO')
else:
    print('Não é primo')
    
# :D
