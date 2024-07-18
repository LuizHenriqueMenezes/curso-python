#Tipos primitivos 

tipoInt = int(input('Digite um valor inteiro:\n'))
tipoFloat = float(input('Digite um valor quebrado:\n'))
tipoString = input("Digite uma frase:\n")

print(f'\n"{tipoInt}" = {type(tipoInt)}\n')
print(f'"{tipoFloat}" = {type(tipoFloat)}\n')
print(f'"{tipoString}" = {type(tipoString)}\n')

#diz se é numérico
print(f'{tipoString} é numérico? {tipoString.isnumeric()}') 

#diz se é alfabético (só roda se verificar string)
print(f'{tipoString} é alfabético? {tipoString.isalpha()}') 

#diz se é alfanumérico (3a por ex)
print(f'{tipoString} é alfanum? {tipoString.isalnum()}\n')

#existe .isupper() etc, mts mts mts 

## DESAFIOS ##

#crie um script python que leia dois números e tente mostrar a soma 
#entre eles 
print('\nSOMA\n')
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o primeiro número: '))
print(f'a soma de {num1} + {num2} é {num1 + num2}')

#Faça um programa que leia algo pelo teclado e motre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ele. 
algo = input("\nDigite algo:\n")
print(f'-- Informações sobre "{algo}" --\n' 
      f'.isalnum()? {algo.isalnum()}\n'
      f'.isalpha()? {algo.isalpha()}\n'
      f'.isascii()? {algo.isascii()}\n'
      f'.isdecimal()? {algo.isdecimal()}\n'
      f'.isdigit()? {algo.isdigit()}\n'
      f'.isidentifier()? {algo.isidentifier()}\n'
      f'.islower()? {algo.islower()}\n')

# :)