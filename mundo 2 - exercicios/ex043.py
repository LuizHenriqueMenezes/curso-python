"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso 
- 30 até 40: obesidade 
- Acima de 40: obesidade mórbida

"""
peso = float(input('Digite seu peso em quilos: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / altura**2

if imc < 18.5:
    print(f'\nIMC ABAIXO DO PESO COM {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print(f'IMC PESO IDEAL COM {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'IMC SOBREPESO COM {imc:.2f}')
elif imc >= 30 and imc < 40:
    print(f'IMC OBESIDADE COM {imc:.2f}')
elif imc >= 40:
    print(f'IMC OBESIDADE MÓRBIDA COM {imc:.2f}')
else:
    print('Você digiou algo errado')
    
# :D