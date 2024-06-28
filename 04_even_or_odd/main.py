#Crie um programa que receba um número e determine se ele é par ou ímpar.

def even_or_odd():
    try:
        number = int(input('Digite um número inteiro: '))
    except ValueError as error:
        return print('Valor não é um número inteiro')