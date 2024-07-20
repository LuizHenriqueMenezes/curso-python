"""
Crie um programa que leia o nome completo de uma 
pessoa e mostre:

- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome. 

"""
nome = input('Digite seu nome completo: ')
dividido = nome.split()
letras = nome.replace(" ", "")

print(f"""\nSeu nome em letras MAIÚSCULAS: {nome.upper()}
SEU NOME EM LETRAS minúsculas: {nome.lower()}
Quantas letras tem o primeiro nome: {len(dividido[0])}
Quantas letras ao todo: {len(letras)}""")

# :)


