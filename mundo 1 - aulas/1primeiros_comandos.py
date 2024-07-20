print('hello world')
print(7+4)
print('7'+'4')
print('olá', 5)

#variaveis 
nome = 'luiz'

print(f"olá {nome}")

#interatividade
idade = input('Qual sua idade?\n')
print(f"a idade é {idade}")

# DESAFIOS DO VÍDEO 

#crie um script python que leia o nome de uma pessoa e mostre uma mensagem
#de boas-vindas de acordo com o valor digitado 
bem_vindo = input('Qual seu nome de treinador pokemon?\n')
print(f'Bem-vindo ao pokemon center, {bem_vindo}!')

#crie um script python que leia o dia, o mês, e o ano de nascimento
#de uma pessoa e mostre uma mensagem com a data informada
print('\nANIVERSÁRIO\n')
dia = input('Dia = ')
mes = input('Mes = ')
ano = input('Ano = ')
print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto?")

#crie um script python que leia dois números e tente mostrar a soma 
#entre eles 
print('\nSOMA\n')
num1 = int(input('digite o primeiro número'))
num2 = int(input('digite o primeiro número'))

print(f'a soma de {num1} + {num2} é {num1 + num2}')