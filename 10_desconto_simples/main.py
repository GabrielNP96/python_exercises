'''
    Escreva um programa que calcule o valor do desconto simples de um produto, 
    com base no preço original e na porcentagem de desconto.
'''

def get_user_data():
    print('Bem vindo ao programa de descontos')

    i = True
    while i == True:
        try:
            price_of_the_product = float(input('Digite o preço do seu produto'))
            discount_amount = float(input('Agora digite o valor do desconto: '))
            if price_of_the_product < 0.01 and discount_amount < 0.01:
                ...
        except ValueError:
            print('Digite valores válidos')