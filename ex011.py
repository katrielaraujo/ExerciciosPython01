'''Faça um programa
que leia a largura e a
altura de uma parede 
em metros, calcule a
sua área e a quantidade
de tinta necessário para
pintá-la, sabendo que 
cada litro de trinta,
pinta uma área de 2m'''
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura*altura
print('Área da parede é {} e você vai precisar de {}'.format(area,area/2))