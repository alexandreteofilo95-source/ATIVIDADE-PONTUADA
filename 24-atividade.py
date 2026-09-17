import os
os.system('cls')
print(''' FRUTAS:                 ATE 5KG:                             ACIMA DE 5KG:
MORANGO                  R$2,50 POR KG                       R$2,20 POR KG
MAÇA                     R$1,80 POR KG                       R$1,50 POR KG



''')
frutas = input('Qual fruta voçê quer: ')
quantidade = int(input(f'Quantas {frutas} voçê quer:'))
sem_desconto = quantidade * 2.50
calculo_2 = sem_desconto * 0.10
calculo_3 = sem_desconto - calculo_2
com_desconto = quantidade * 2.20
calculo = com_desconto * 0.10
calculo_1 = com_desconto - calculo

match frutas:
    case 'morango':
        kg = int(input('Quantas kg de fruta voçê quer: '))
    case 'maça':
        kg = int(input('Quantas kg de fruta voçê quer: '))
    case _:
        print('escolhas uma das frutas')
if kg > 5:
    print(f'sua compra deu: {calculo_1}')
elif kg < 5:
    print(f'sua compra deu: {calculo_3}')
    


        
