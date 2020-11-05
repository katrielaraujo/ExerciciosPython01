'''Crie um programa que leia o nome de uma
cidade e diga se ela começa ou não com o 
nome "Santo".'''
cidade = str(input('Digite o nome da cidade: ')).strip()
comeco = cidade.split()
resposta = 'SANTO' in comeco[0].upper()
print(resposta)