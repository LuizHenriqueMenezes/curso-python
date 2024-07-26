"""
Crie um programa que leia o nome e o preço de vários produtos. O
programa deverá perguntar se o usuário vai continuar. No final, 
mostre:

a) Qual é o total gasto na compra. 
b) Quantos produtos custam mais de R$1000.
c) Qual é o nome do produto mais barato. 

"""
import math

nome = []
preco = []

barato = math.inf
maisbarato = ''
count = total = milao = 0

while True:
    produto = input(f'\nDigite o nome do produto {count+1}: ')
    precoProduto = float(input(f'Digite o preço do produto {count+1}: '))
    
    nome.append(produto)
    preco.append(preco)
    
    count += 1
    total += precoProduto
    
    if precoProduto > 1000:
        milao += 1
        
    if precoProduto < barato:
        barato = precoProduto
        maisbarato = produto
        
    yesno = input('Quer continuar? [S/N]: ').upper()
    
    while yesno != 'S' and yesno != 'N':
        yesno = input('Quer continuar? [S/N]: ').upper()
    
    if yesno == 'N':
        break
        
print(f"""
O total gasto nas compras é: {total} reais.
{milao} produto(s) custa(m) mais de 1000 reais.
{maisbarato} é o produto mais barato custando {barato}.""")

# :D