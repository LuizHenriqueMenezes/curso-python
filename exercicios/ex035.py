"""
Desenvolva um programa que leia o comprimento de 
três retas e diga ao usuário se elas podem ou não
formar um triângulo. 

"""
reta1 = int(input('Digite o comprimeiro da primeira reta: '))
reta2 = int(input('Digite o comprimeiro da segunda reta: '))
reta3 = int(input('Digite o comprimeiro da terceira reta: '))

possib = reta1 == reta2 and reta1 != reta3 
possib2 = reta1 == reta3 and reta1 != reta3
possib3 = reta2 == reta3 and reta2 != reta1

if possib == True or possib2 == True or possib3 == True:
    print("Pode se formar uma triângulo!")
else:
    print('Não pode formar um triângulo')
    
# :)