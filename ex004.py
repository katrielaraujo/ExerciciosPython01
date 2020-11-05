#faça um programa que leia algo pelo teclado
#e mostre na tela o seu tipo primitivo e todos
#as informações possíveis sobre ele.
n = input('Digite um valor: ')
print('Qual o tipo primitivo: '.format(type(n)))
print('É um número: {}'.format(n.isnumeric()))
print('É uma letra: {}'.format(n.isalpha()))
print('É alfanúmerico: {}'.format(n.isalnum()))
print('É letra maúscula: {}'.format(n.isupper()))
print('É letra minúscula: {}'.format(n.islower()))
print('É um número décimal: {}'.format(n.isdecimal()))
print('É um espaço: '.format(n.isspace(n)))