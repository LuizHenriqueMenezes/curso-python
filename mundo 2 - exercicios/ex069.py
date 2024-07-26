"""
Crie um programa que leia a idade e o sexo de várias pessoas. A 
cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:

a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados. 
c) quantas mulheres tem menos de 20 anos. 

"""
idade = []
sexo = []
pessoa = 0
maioridade = mans = menorquevinte = 0

while True:
    print(f'\nDigite as informações da pessoa {pessoa+1}')
    age = int(input('\nidade: '))
    sex = input('sexo [F/M]: ').upper()

    while sex != 'F' and sex != 'M':
        sex = input('sexo [F/M]: ').upper()
    
    idade.append(age)
    sexo.append(sex)
    
    if age > 18:
        maioridade += 1
        
    if sex == 'M':
        mans += 1
        
    if age < 20 and sex == 'F':
        menorquevinte += 1
        
    pessoa += 1 
    
    yesno = input('Quer continuar? [S/N]: ').upper()
    
    while yesno != 'S' and yesno != 'N':
        yesno = input('Quer continuar? [S/N]: ').upper()
    
    if yesno == 'N':
        break
    
print(f"""Tem {maioridade} pessoas com mais de 18 anos. 
E {mans} homens cadastrados. 
E {menorquevinte} mulheres com menos de 20 anos.""")

# :D