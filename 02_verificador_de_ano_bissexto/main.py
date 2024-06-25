"""
    Crie um programa que determine se um ano informado pelo usuário é bissexto ou não.
"""
print('Vamos verificar se um ano é bicesto')
user_year = input(('Digite um ano em formato númerico: '))

def check_if_the_year_is_double(year):
    if year.isdigit() is True:
        if year.endswith('00'):
            if int(year) % 400 == 0:
                print(f'{year} é um ano bissexto.')
            else:
                print(f'{year} não é um ano bissexto.')
        elif int(year) % 4 == 0:
            print(f'{year} é um ano bissexto.')
        elif int(year) % 4 != 0:
            print(f'{year} não é um ano bissexto.')
    else:
        print('Ocorreu um erro...\nProvavelmente você não digitou um ano em formato númerico ')

check_if_the_year_is_double(user_year)
