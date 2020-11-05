'''Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou
perdeu'''
from random import randint
from time import sleep
valor = randint(0 , 5)
print('Pensando em um número...')
sleep(3)
n = int(input('Descubra o número que estou pensando entre 0 e 5: '))
if n == valor:
    print('Você acertou o número é',valor)
else:
    print('Você errou o número é',valor)

