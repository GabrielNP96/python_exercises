'''
    Escreva um programa que calcule o valor do desconto simples de um produto, 
    com base no preço original e na porcentagem de desconto.
'''

def get_user_data():
    print(f'Bem vindo ao programa de descontos\n{'-' * 25}')

    i = True
    while i == True:
        try:
            price_of_the_product = float(input('Digite o preço do seu produto: '))
            discount_amount = float(input('Agora digite o valor do desconto: '))
            if price_of_the_product >= 0.01 and discount_amount >= 0.01:
                return (price_of_the_product, discount_amount)
            print('Digite valores válidos')
        except ValueError:
            print('Digite valores válidos')

def simple_discount(price, discount):
    full_discount = price - ((price / 100) * discount)
    return f'Sua compra vai ser de {price}R$ com {discount}% de desconto por {full_discount:.2f}R$ '

user_data = get_user_data()
print(simple_discount(user_data[0], user_data[1]))