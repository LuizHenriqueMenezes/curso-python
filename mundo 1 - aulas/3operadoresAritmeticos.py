"""
Operadores Aritméticos 

* multiplicação    |  // divisão inteira (o result da divisão em int)
% resto da divisão |  ** potência (5**2 == 5² ou 5 * 5 ) (também tem pow(5,2), mas ai perde a ordem de precedência)
/ divisão          |  + adição 
- divisão          |  == igual

ORDEM DE PRECEDÊNCIA
1 - ()
2 - ** 
3 - *, /, //, % (vai quem aparecer primeiro)
4 - +, - 

obs. criar a raiz quadrada de um número é a mesma coisa que fazer a 
potência dele por meio == 25**(1/2)
ou a raiz cubica 25**(1/3)
"""
#é possível fazer esse tipo de coisa:
print('te amo bea '*20)

nome = input('\nQual seu nome? ')
print(f'Prazer em te conhecer, {nome:20}!') 
#esse :20 serve pra aumentar a quantidade de caracteres 
# se colocar :>20 ele fica a direita
# < na esquerda  
# ^ no meio 
# :=^20 ele deixa centralizado, com 20 caracteres, e com varios =


# :)