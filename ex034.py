'''Escreva um programa que pergunta o 
salário de um funcionário e calcule o valor de seu aumento.

Para salários superiores a R$1,250.00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input('Digite seu salário: '))
if salario > 1250.00:
    print('Seu novo salário é {:.2f}'.format(salario*1.10))
else:
    print('Seu novo salário é {:.2f}'.format(salario*1.15))