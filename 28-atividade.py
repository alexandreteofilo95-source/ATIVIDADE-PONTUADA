import os
os.system('cls')

('''    COR:              PROÇO:
        VERDE             R$10,00
        AZUL              R$20,00
        AMARELO           R$30,00
        VERMELHO          R$40,00

''')

escolha = input('Escolha uma cor: ')

match escolha:
    case 'verde' | ' VERDE' | 'Verde':
        print('valor: R$10,00')
    case 'azul' | 'AZUL' | 'Azul':
        print('valor: R$20,00')
    case 'amarelo' | ' AMARELO' | 'Amarelo':
            print('valor: R$30,00')
    case 'vermelho' | ' VERMELHO' | 'Vermelho':
        print('valor: R$40,00')
        