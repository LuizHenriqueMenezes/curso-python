"""
Variáveis Compostas (Tuplas)

lanche = () -> tupla
lanche = [] -> lista
lanche = {} -> dicionário 

"""

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
#lanche [-1] pega o último
#lanche [-2] pega o penúltimo, e assim por diante 

#pro for:
for c in lanche:
    print(c)
# vai pegar todas as posições lanche e mostrar o que tem dentro

# TUPLAS SÃO IMUTÁVEIS, OU SEJA, NÃO É POSSÍVEL MUDAR O VALOR
# por exemplo:
# lanche[c] = 'sorvete'

print(lanche[1:3])
print(lanche[-1])

print(sorted(lanche)) #vai organizar em ordem alfabética

#-----------------
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # vai colar uma na outra 

print(sorted(c)) # ordena na ordem crescente
print(c.index(8)) # pra ver em que posição está o 8

#----------------
# no python podem ter vários tipos de dados:
pessoa = ('Luiz', 19, 'M', 80.0)

#-------------------
# ja que a tupla é imutável, existe o del, que da pra excluir qualquer váriavel no python
del(pessoa)

# :V