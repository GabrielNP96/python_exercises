#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) a partir da altura e do peso informados pelo usuário.

def get_user_data():
    i = True
    while i == True:
        try:
            get_user_weight = float('Digite seu peso: ')
            get_user_height = float('Digite sua altura: ')

            return (get_user_weight, get_user_height)
        except ValueError:
            print('Dados inválidos')

def IMC(weight, height):
    imc = weight / (height **2)

    if imc < 16.9:
        return f'Seu imc é {imc:.2f} e você está muito abaixo do peso.\nProcure um médico.'
    elif imc >= 17 and imc >= 18.4:
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
    
    
