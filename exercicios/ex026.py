"""
Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra "A". 
- Em que posição ela aparece a primeira vez. 
- Em que posição ela aparece a última vez. 

"""
frase = input('Digite uma frase: ').upper()
letra = input('Digite a letra que quer procurar: ').upper()

a = frase.count(letra)
positionOne = frase.find(letra)
positionTwo = frase.rfind(letra)

print(f"""\nA letra "{letra}" aparece um total de {a} vezes.
Posições:
primeira vez: índice {positionOne}
última vez: índice {positionTwo}""")

# :)