"""
Faça um programa que leia o nome completo de uma 
pessoa, mostrando em seguida o primeiro e o último
nome separadamente. 

Ex: Beatriz Feitosa da Silva
primeiro = Beatriz
último = Silva
"""
name = input('\nDigite seu nome: ')

divide = name.split()
first = divide[0]
last = divide[-1]

print(f"""Primeiro nome: {first}
Último nome: {last}""")

# :)