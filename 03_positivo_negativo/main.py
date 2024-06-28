#Desenvolva um programa que receba um número e informe se ele é positivo, negativo ou zero.

def positive_or_negative():
    try:
        num = int(input('Digite um número inteiro: '))
        if type(num) == int:
            if num < 0:
                return print(f'{num} é negativo.')
            if num > 0:
                return print(f'{num} é positivo.')
            else:
                return print(f'o valor é zero.')
    except ValueError as error:
        return print(f'O valor não é um número.')
    
positive_or_negative()