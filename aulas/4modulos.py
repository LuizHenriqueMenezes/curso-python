"""
Utilizando Módulos

math: 
- ceil arredonda pra cima
- floor arredonda pra baixo
- trunc vai eliminar da virgula pra frente
- pow potência
- sqrt raiz quadrada
- factorial fatorial 

https://docs.python.org/3/library/index.html !!

pesquisar modulo na comunidade: https://pypi.org/

"""
#pra importar tudo da biblioteca
import math

#pra importar algo exclusivamente
from math import sqrt 
from math import sqrt, ceil 

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'Raiz: {raiz:.2f}') #:.2f pra deixar só 2 casas decimais

#pra gerar número aleatório entre 0 e 1
import random 

n = random.random()
m = random.randint(1, 10) # numero inteiro entre 1 e 10 por exemplo
print(f'\nn: {n} || m: {m}')

#emoji :D
# pip install emoji
import emoji 

print(emoji.emojize('bora :thumbs_up:'))

# :)  