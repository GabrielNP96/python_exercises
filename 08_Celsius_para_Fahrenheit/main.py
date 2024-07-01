#Escreva um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa.

def celsius_to_fahrenheit(number):
      try:
        fahrenheit =  (float(number) * 9/5) + 32   
        return f'{number}° é igual á {fahrenheit:.2f}°'
      except ValueError:
          return print('Você não digitou um número')
          

def fahrenheit_to_celciusus(number):
     try:
        celsius = (float(number) - 32) * 5/9
        return f'{number}° é igual á {celsius:.2f}°'
     except ValueError:
         return print('Você não digitou um número')

def conversor():
    i = True
    while i == True:
        celsius_or_fahrenheit = input("Para converter Celsius para Fahrenheit digite 1.\nPara coverter Fahrenheit para Celsius Digite 2.\nDigite aqui: ")
        try:
            if int(celsius_or_fahrenheit) == 1:
                    celsius =input('Digite a quantidade á ser convertida: ')
                    print(celsius_to_fahrenheit(celsius))
                    break
            elif int(celsius_or_fahrenheit) == 2:
                    fahrenheit =input('Digite a quantidade á ser convertida: ')
                    print(fahrenheit_to_celciusus(fahrenheit))
                    break
            else: 
                print('Digite apenas 1 ou 2')
                print('-' * 15)
        except ValueError:
            if celsius_or_fahrenheit != 1 or celsius_or_fahrenheit != 2: 
                print('Digite apenas 1 ou 2')
                print('-' * 15)
conversor()