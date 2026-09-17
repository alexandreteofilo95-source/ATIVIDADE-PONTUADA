import os
os.system('cls')
# ENTRADA
numero = int(input('digite um numero: '))
numero_2 = int(input('digite outro numero: '))
escolha = input('Escolha uma das operaçês matematica (soma,subtração,multiplicação e divisão): ')

# PROCESSAMENTO
soma = numero + numero_2
subtracao = numero - numero
multiplicacao = numero * numero_2
divisao = numero / numero_2

match escolha:
    case 'soma':
        print(f'resultado: {soma}')
    case 'subtração':
        print(f'resultado: {subtracao}')
    case 'multiplicação':
        print(f'resultado: {multiplicacao}')
    case 'divisão':
        print(f'resultado: {divisao}')
    case _:
        print('escolha uma operação')

