'''Escreva um programa que leia a velocidade de um
carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$7.00 por cada km acima do limite.'''
velocidade = float(input('Digite sua velocidade: '))
if velocidade > 80:
    print('Você foi multado em {:.2f} por está a {}km'.format((velocidade-80)*7.00,velocidade))
else:
    print('Muito bem você está transitando de forma regular!')