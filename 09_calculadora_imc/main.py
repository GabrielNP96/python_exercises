#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) a partir da altura e do peso informados pelo usuário.

def get_user_data():
    i = True
    while i == True:
        try:
            get_user_weight = float(input('Digite seu peso: '))
            get_user_height = float(input('Digite sua altura: '))

            if get_user_weight > 25 and get_user_weight < 370 and get_user_height > 0.627 and get_user_height < 2.52:
                return (get_user_weight, get_user_height)
            
            print('Um ou os dois valores são inválidos...\n')
            print('-' *15 + '\n')
        except ValueError:
            print('Dados inválidos\n')
            print('-' *15 + '\n')
            
            

def IMC(weight, height):
    imc = weight / (height **2)

    if imc < 16.9:
        return f'Seu imc é {imc:.2f} e você está muito abaixo do peso.\nProcure um médico.'
    elif imc >= 17 and imc <= 18.4:
        return f'Seu imc é {imc:.2f} e você está abaixo do peso\nProcure um médico.'
    elif imc > 18.4 and imc < 25:
        return f'Seu imc é {imc:.2f} e você está no peso ideal.'
    elif imc >= 25 and imc < 30:
        return f'Seu imc é {imc:.2f} e você está acima do peso.\nProcure um médico'
    elif imc >= 30 and imc < 35:
        return f'Seu imc é {imc:.2f} e você está com obesidade grau I.\nProcure um médico'
    elif imc >= 35 and imc <= 40:
        return f'Seu imc é {imc:.2f} e você está com obesidade grau II.\nProcure um médico'
    else:
        return f'Seu imc é {imc:.2f} e você está com obesidade grau III.\nProcure um médico'
    
user_data = get_user_data()
print(IMC(user_data[0],user_data[1]))
