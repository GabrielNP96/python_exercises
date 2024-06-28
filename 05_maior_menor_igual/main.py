#Escreva um programa que compare dois números e informe qual é o maior, o menor ou se eles são iguais.

def receive_user_number():
    try:
        number = input('Digite um número: ')
        try:
            number = int(number)
            return number
        except ValueError:
            number = float(number)
            return number
    except ValueError as error:
         number = None
         return number

def greater_less_equal(num1,num2):

    if num1 == None or num2 == None:
        return 'Erro...\nUm ou ambos os valores é inválido.'
    elif num1 > num2:
        return f'{num1} é maior que {num2}.'
    elif num1 < num2:
        return f'{num1} é menor que {num2}.'
    else:
        return f'{num1} é igual á {num2}.'
    
first_user_number = receive_user_number()
second_user_number = receive_user_number()

print(greater_less_equal(first_user_number, second_user_number))