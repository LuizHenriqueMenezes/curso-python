#Faça um programa que leia algo pelo teclado e motre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ele. 
algo = input("\nDigite algo: ")

print(f'-- Informações sobre "{algo}" --\n' 
      f'Tipo primitivo: {type(algo)}\n'
      f'É alfanumérico? {algo.isalnum()}\n'
      f'É alfabético? {algo.isalpha()}\n'
      f'É um ASCII? {algo.isascii()}\n'
      f'É decimal? {algo.isdecimal()}\n'
      f'É string apenas com números? {algo.isdigit()}\n'
      f'É identificador? {algo.isidentifier()}\n'
      f'Está tudo em minusculo? {algo.islower()}\n')

# :)