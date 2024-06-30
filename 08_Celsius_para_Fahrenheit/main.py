#Escreva um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa.

def celsius_to_fahrenheit(number):
      fahrenheit =  (number * 9/5) + 32   
      return f'{number}° é igual á {fahrenheit:.2f}'
          

def fahrenheit_to_celciusus(number):
     celsius = (number - 32) * 5/9
     return f'{number}° é igual á {celsius:.2f}'

def conversor():
    i = True
    while i == True:
        celsius_or_fahrenheit = input("Para converter Celsius para Fahrenheit digite 1.\nPara coverter Fahrenheit para Celsius Digite 2.\nDigite aqui: ")
        try:
            if int(celsius_or_fahrenheit) == 1:
                    Celsius = float(input('Digite a quantidade á ser convertida: '))
                    print(celsius_to_fahrenheit(Celsius))
                    break
            elif int(celsius_or_fahrenheit) == 2:
                    fahrenheit = float(input('Digite a quantidade á ser convertida: '))
                    print(fahrenheit_to_celciusus(fahrenheit))
                    break
            else: 
                print('Digite apenas 1 ou 2')
                print('-' * 15)
        except ValueError:
            if celsius_or_fahrenheit != 1 or celsius_or_fahrenheit != 2: 
                print('Digite apenas 1 ou 2')
                print('-' * 15)
            if Celsius != float or fahrenheit != float:
                 print('Digite apenas números')
conversor()