#Escreva um programa que leia um valor em metros e o
#exiba convertido em centímetros e milímetros. 

v = float(input('\nDigite o valor em metros: '))

print(f'{v} metros equivale a {v * 100}cm\n'
      f'{v} metros equivale a {v * 1000}mm\n')