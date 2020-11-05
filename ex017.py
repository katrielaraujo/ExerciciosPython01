'''Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente de
um triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.'''
from math import hypot
co = int(input('Digite cateto oposto: '))
ca = int(input('Digite cateto adjacente: '))
h = hypot(co,ca)
print('O comprimento da hipotenusa é: ',h)