'''Faça um programa que leia um ângulo 
qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.'''
from math import sin,cos,tan,radians
x = float(input('Digite um angulo: '))
angulo = radians(x)
print('O seno do angulo é: {:.2f}\n'.format(sin(angulo)))
print('O cosseno do angulo é: {:.2f}\n'.format(cos(angulo)))
print('A tangente é: {:.2f}'.format(tan(angulo)))