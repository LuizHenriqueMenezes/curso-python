"""
Crie um programa que leia várias números inteiros pelo teclado. O 
programa só vai parar quando o usuário digitar o valor 999, que é 
a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag). 
"""
x = 1
cont = 0
aux = 0 

while x != 999:
    x = int(input('Digite um número inteiro [999 pra parar]: '))
    
    if x!= 999:
        cont += x
        aux += 1
        
print(f'Foram digitados {aux} números (tirando 999), somando-os chega a {cont}')

# :D