'''
    Crie um programa que gere e imprima a sequência de Fibonacci até um número n, definido pelo usuário. A sequência de Fibonacci é uma série de números em que cada termo é a soma dos dois termos anteriores, 
    começando por 0 e 1.
'''

def get_fibonacci_end():
    i = True
    while i == True:
        try:
            user_number = int(input('Digite um número inteiro positivo que será o fim aproximado da sequência de Fibonacci: '))
            if user_number < 1:
                print('O número não pode ser negativo.')
                continue
            return user_number
        except ValueError:
            print(f'Digite apenas um número inteiro.\n{'-' * 40}')

def fibonacci_sequence(fibonacci_end):
    fibonacci_sequence = [1,1]
    i = 0
    while i < fibonacci_end:
        i = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if i > fibonacci_end:
            break
        fibonacci_sequence.append(i)
    return fibonacci_sequence

def show_fibonnaci_sequence(fibonnaci_list):
    fibonacci_str = 'A sequência fibonacci com o fim aproximado ao informado é '
    for fibonnaci_number in fibonnaci_list:
        fibonacci_str += f'{fibonnaci_number} '
    return fibonacci_str
       

fibonacci_end = get_fibonacci_end()
fibonacci_list = fibonacci_sequence(fibonacci_end)
print(show_fibonnaci_sequence(fibonacci_list))



