#Faça um programa que leia a largura e a altura de 
#uma parede em metros, calcule a sua área e a 
#quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta, pinta uma área de 2m².

b = float(input('\nDigite a base/largura da parede: '))
a = float(input('Digite a altura da parede: '))

area = b * a
litros = area / 2

print(f'Area = {area} metros')
print(f'Logo, será necessario {litros} litros de tinta!')

# :)