#Escreva um programa que pergunte a quantidade de km 
#percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule
#o preço a pagar, sabendo que o carro custa R$60 por 
#dia e R$0,15 por km rodado

km = float(input('Quantos km rodou?\n'))
dias = int(input('Por quantos dias ele ficou alugado?\n'))

pay = (60 * dias) + (0.15 * km)

print(f'Você tem que pagar R${pay:.2f}')

# :)