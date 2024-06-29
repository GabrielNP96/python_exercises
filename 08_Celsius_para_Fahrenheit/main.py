import os
#Escreva um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa.

def celsius_to_fahrenheit(number):
     return f'{number}° é igual á {(number * 9/5) + 32}'
def get_user_number():
    i = True
    while i == True:
        celsius_or_fahrenheit = input("Para converter Celsius para Fahrenheit digite 1.\nPara coverter Fahrenheit para Celsius Digite 2.\nDigite aqui: ")
        try:
            if int(celsius_or_fahrenheit) == 1:
                    print('ok')
                    break
            elif int(celsius_or_fahrenheit) == 2:
                    print('ok')
                    break
            else: 
                print('Digite apenas 1 ou 2')
                print('-' * 15)
        except ValueError:
            print('Digite apenas 1 ou 2')
            print('-' * 15)
get_user_number()