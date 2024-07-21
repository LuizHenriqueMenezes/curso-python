"""
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento: 

- a vista dinheiro 10% de desconto
- a vista no cartão 5% de desconto 
- em até 2x no cartão preço normal 
- 3x ou mais no cartão 20% de juros

"""
price = float(input('\nDigite o valor do produto: '))
option = int(input(f"""\n -- Escolha uma opção 
1. A vista no dinheiro
2. A vista no débito 
3. 2x no crédito 
4. 3x ou mais vezes no crédito
\nOpção escolhida: """))

if option == 1:
    print(f'\nVocê ganhou 10% de desconto, com isso o total a pagar é {(price - (0.10 * price)):.2f} reais')
elif option == 2:
    print(f'\nVocê ganhou 5% de desconto, com isso o total a pagar é {(price - (0.05 * price)):.2f} reais')
elif option == 3:
    print(f'\nO valor não se altera: {price:.2f} reais')
elif option == 4:
    print(f'\nCom isso será inserido 20% de juros: total a pagar {(price + (0.20 * price)):.2f} reais')
else:
    print('\nDigite uma opção válida!')