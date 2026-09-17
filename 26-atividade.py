import os
os.system('cls')

usuario = input('Digite seu nome: ')
nota_1 = float(input('Digite sua nota: '))
nota_2 = float(input('Digite sua outra nota: '))
divisao = (nota_1 + nota_2) / 2
media = divisao
print(f'sua media foi: {media} ')
if media >= 6:
    print('\nparabéns, APROVADO')
elif media >= 4.1 and media <= 5.9:
    print('RECUPERAÇÃO')
elif media < 4:
    print('REPROVADO')