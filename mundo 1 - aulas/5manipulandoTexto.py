""" Manipulando Cadeias de Texto """

frase = 'Curso em Vídeo Python'


""" Fatiamento """

#vai mostrar a frase completa, padrão
print(frase)

#vai pegar da posição nove até a 12 (é sempre um a menos)
print(frase[9:13]) 

#a frase no total tem 20 posições, mas mesmo assim pode pegar até o 21, ja que pega a anterior
print(frase[9:21])

#vai pular de 2 em 2 (9, 11, 13, 15...)
print(frase[9:21:2])

#se não põe nada na esquerda, ele começa do comeeço 
print(frase[:5])

#nada na direira quer dizer que a frase vai do 15 até o final
print(frase[15:])

#vai começar no 9, vai até o final (não tem número no meio), e vai pulando de 3 em 3
print(frase[9::3])

# Inverta uma string de trás pra frente
print(frase[::-1])

# Imprime os caracteres nos índices ímpares
print(frase[1::2])

# Busque o último item da lista
print(frase[-1])

""" Análise """

#lenght
print(f'\nO tamanho da string é: {len(frase)}')

# vai contar quantos 'o' tem na string
print(f'tem um total de {frase.count('o')} "o" na frase1')

#faz uma contagem com fatiamento ('o' entre 0 e 12)
print(frase.count('o', 0, 13))

#quantas vezes ele encontrou 'deo', vai mostrar a posição em que começou o 'deo'
#se colocar algo que não existe na string, ele devolve -1
print(frase.find('deo'))

#o in procura se tem tal coisa na string (True / False)
print('Curso' in frase)


""" Transformação """

#técnico pediu substituição
frase = frase.replace('Python', 'Android') #pra salvar a alteração tem que fazer assim 

#GRITA NÃOOOOOOO
print(frase.upper())

#parou de gritar
print(frase.lower())

#Só o primeiro caracter da string em maiusculo 
frase.capitalize()

#Ele Deixa Cada Primeira Palavra Em Maiusculo 
frase.title()

#pra remover os espaços do começo e do fim  
#exemplo _ _ _ O I _ A M I G O _ _ 
#vai remover esses que não serve pra nada
frase.strip()

#vai remover somente os espaços da direita (right strip)
frase.rstrip()

# e esse somente o da esquerda (left strip)
frase.lstrip()


""" Divisão """

#ele gera uma lista com todas as palavras de uma string
#ex: ['Curso', 'em', 'Video', 'Python']
#cada palavra tem uma posição, e dentro da palavra, as letras tem suas posições
#ex: curso posição 0
#dentro de curso: 0-C, 1-u, 2-r etc
frase.split()


""" Junção """

#juntar uma coisa na outra
#pode ser usado pra juntar a lista feita na divisão (acima)
#no exemplo tem tracinho "-" mas é possível colocar espaço ou alguma outra coisa
'-'.join(frase)