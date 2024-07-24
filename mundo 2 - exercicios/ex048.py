"""
Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontra, no intervalo de 1 até 500

"""
aux = 0

for x in range(1, 501):
    if(x % 2) != 0:
        if(x % 3) == 0:
            aux += x
        
print(f'A soma é {aux}')

# :D