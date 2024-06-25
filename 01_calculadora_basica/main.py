"""
    Crie um programa que realize as operações básicas de matemática
    (soma, subtração, multiplicação e divisão) entre dois números.
"""

def calc(num1,operator, num2):
    match operator:
        case '+':
            return print(f'{num1} {operator} {num2} = {num1 + num2}')
        case '-':
            return print(f'{num1} {operator} {num2} = {num1 - num2}')
        case '*':
            return print(f'{num1} {operator} {num2} = {num1 * num2}')
        case '/':
            if(num2 == 0):
                return print('Você não pode dividir por zero.')
            return print(f'{num1} {operator} {num2} = {num1 / num2}')
        case _:
            return print('Operador inválido')

def get_user_data():
    print('Bem vindo a calculadora básica.')

    i = True
    while i == True:
        first_user_number = int(input('Digite um número: '))
        user_operator = input('Digite um operador matemático: + - * /: ')
        second_user_number = int(input('Digite outro número: '))

        calc(first_user_number, user_operator, second_user_number)

        calculate_again = input('Calcular novamente? digite apenas sim ou não :')
        if(calculate_again.lower() == 'sim'):
            i = True
        elif(calculate_again.lower() == 'não'):
            print('Encerrando programa...')
            i = False
        else:
            print('Resposta inválida...\nEncerrando programa...')
            i = False

get_user_data()