#Desenvolva um programa que gere a tabuada de multiplicação de um número inteiro positivo informado pelo usuário.
#função para pegar o número informado pelo usuário.
def get_user_number():
    try:
        user_number = int(input('Digite um número inteiro positivo para gerar sua tabuada de multiplicação: '))
        if user_number < 0 :
            return None
        return user_number
    except ValueError:
        return None
#tabuada do número do usuário.
def multiplication_table(number):
    if number == None:
        return None

    multiplication_table_of_number = []
    for i in range(11):
        multiplication_table_of_number.append(f'{i} x {number} = {number * i}')
    return multiplication_table_of_number
            
#mostar tabuada no terminal.
def show_results_to_the_user(results):
    if results == None:
        return print('Erro o valor digitado não é um número inteiro positivo.')
    for result in results:
        print(f'{result}')

#declaração de váriaveis e funções.
number_to_be_multiplied = get_user_number()
user_multiplication_table = multiplication_table(number_to_be_multiplied)
show_results_to_the_user(user_multiplication_table)
