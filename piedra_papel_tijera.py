user_option = input('piedra, papel o tijera= ')
user_option = user_option.lower()
computer_option = 'papel'

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra le gana a tijera')
        print('user ganó!')
    else:
        print('Papel le gana a piedra')
        print('Computer ganó!')    
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel le gana a piedra')
        print('User ganó')
    else:
        print('Tijera le gana a papel')
        print('Computer ganó!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('Tijera le gana a papel')
        print('User ganó!')
    else:
        print('Piedra le gana a tijera')
        print('Computer ganó!')