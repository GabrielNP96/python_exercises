#Crie um programa que receba uma lista de números e calcule a média aritmética desses números.

def get_user_number():
    numbers_list = []
    print("Vamos adiconar números para calcularmos a média.")
    i = 0
    while i == 0:
        number = input('Digite um número: ex.: 1 ou 1.5: ')
        try:
            try:
                number = int(number)
                numbers_list.append(number)
            except:
                number = float(number)
                numbers_list.append(number)
        except ValueError:
            print('Você não digitou um número valído')
        if len(numbers_list) <= 1:
            print('Agora Vamos adicionar mais números.')
        else:
        
            out = input('Já adicionou todos os números que você queria? "s" para sim e qualquer tecla para não: ')
            if out.lower() == 's':
                return numbers_list
        

        
            

print(get_user_number())
    
