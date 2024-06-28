#Desenvolva um programa que receba um número e informe se ele é positivo, negativo ou zero.

def positive_or_negative():
    num = int(input('Digite um número: '))
    if type(num) == int:
        if num < 0:
            return print(f'{num} é negativo')
        if num > 0:
            return print(f'{num} é positivo')
        else:
            return print(f'o valor é zero')
    else:
        return print(f'{num} não é um número')
    
positive_or_negative()