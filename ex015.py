'''Escreva um programa que pergunta a quantidade de km
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado.Calcule o preço a pagar,Sabendo
que o carro custa R$60 por dia e R$0.15 por km rodado.'''
dias = int(input('Quantos dias você usou o carro: '))
km = float(input('Quantos km você percorreu: '))
custo = dias*60 + km*0.15
print('Você deve pagar R$ {:.2f}'.format(custo))