'''Desenvolva um programa que leia o
comprimento de três retas e diga ao 
usuário se elas podem ou não formar 
um triângulo.'''
a = float(input('Digite lado a: '))
b = float(input('Digite lado b: '))
c = float(input('Digite lado c: '))
if  (c < a + b) and (b < c + b) and (a < c + b):
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo!')