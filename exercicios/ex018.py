#Faça um programa que leia um ângulo qualquer e mostre
#na tela o valor do seno, cosseno e tangente. 

import math

angulo = float(input('Digite o ângulo: '))

radi = math.radians(angulo) #passa pra radiano

seno = math.sin(radi) 
cosseno = math.cos(radi)
tangente = math.tan(radi)

print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')