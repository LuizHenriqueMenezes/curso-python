"""
Interrompendo repetições while

no python não existe literalmente não existe do while
"""
n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    
print(f'A soma vale {s}')

# :D


