'''Faça um programa que leia um número de
0 a 9999 e mostre na tela cada um dos dígitos
separados.

Ex:
Digite um número:1834

unidade:4
dezena:3
centena:8
milhar:1'''
numero = str(input('Digite um número: '))
print('unidade: ',numero[3])
print('dezena: ',numero[2])
print('centena: ',numero[1])
print('milhar: ',numero[0])