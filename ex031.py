'''Desenvolva um programa que pergunte a distância
de uma viagem em km. Calcule o preço da passagem, cobrando
R$0.50 por km para viagens de até 200km e R$0.45 para viagens
mais longas.'''
distancia = float(input('Digite a distância da sua viagem: '))
if distancia > 200:
    print('A sua viagem custa {}'.format(distancia*0.45))
else:
    print('A sua viagem custa {}'.format(distancia*0.50))