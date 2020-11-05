'''Faça um programa que leia três números
e mostre qual é o maior e qual é o menor.'''
n1 = float(input('Digite um número: '))
n2 = float(input('Digite segundo número: '))
n3 = float(input('Digite terceiro número: '))
if (n1 > n2) and (n2 > n3):
    print('O maior número é :',n1)
    print('o menor número é :',n3)
elif (n1 > n3) and (n3 > n2):
    print('O maior número é :',n1)
    print('o menor número é :',n2)
elif (n3 > n1) and (n1 > n2):
    print('O maior número é :',n3)
    print('o menor número é :',n2)
elif (n3 > n2) and (n2 > n1):
    print('O maior número é :',n3)
    print('o menor número é :',n1)
elif (n2 > n3) and (n3 > n1):
    print('O maior número é :',n2)
    print('o menor número é :',n1)
elif (n2 > n1) and (n1 > n3):
    print('O maior número é :',n2)
    print('o menor número é :',n3)
else:
    print('Os números são iguais!')