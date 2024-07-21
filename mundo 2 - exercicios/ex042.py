"""
035 - Desenvolva um programa que leia o comprimento de 
três retas e diga ao usuário se elas podem ou não
formar um triângulo. 

042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso 
de mostrar que tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais 
- ESCALENO: todos os lados diferentes 

"""
reta1 = int(input('Digite o comprimeiro da primeira reta: '))
reta2 = int(input('Digite o comprimeiro da segunda reta: '))
reta3 = int(input('Digite o comprimeiro da terceira reta: '))

possib = reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2

equilatero = reta1 == reta2 and reta2 == reta3
isoscelas = (reta1 == reta2 and reta2 != reta3) or (reta1 == reta3 and reta3 != reta2) or (reta2 == reta3 and reta3 != reta1)
escaleno = reta1 != reta2 and reta1 != reta3 and reta2 != reta3

if possib == True:
    print("\nPode se formar uma triângulo!")
    if equilatero == True:
        print('\nVai formar um triângulo Equilátero, pois todos os lados são iguais.')
    elif isoscelas == True:
        print('\nVai formar um triângulo Isósceles, pois existem dois lados iguais.')
    elif escaleno == True:
        print('\nVai formar um triângulo Escaleno, pois todos os lados são diferentes.')
else:
    print('Não pode formar um triângulo')
    
# :) :D