#Crie um programa que receba um número e determine se ele é par ou ímpar.

def even_or_odd():
    try:
        number = int(input('Digite um número inteiro: '))
        if number % 2 == 0:
            return print(f'{number} é par')
        else:
            return print(f'{number} é ímpar')
            
    except ValueError as error:
        return print('Valor não é um número inteiro')
    
even_or_odd()