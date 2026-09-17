import os
os.system('cls')

produto = input('Digite o nome do produto: ')
quantidade = float(input('Digite a quantidade do produto: '))
valor = float(input('Digite o valor unitario do produto: '))
total = quantidade * valor
total_1 = total * 0.2
desconto = total - total_1
total_2 = total  * 0.3
desconto_2 = total - total_2
total_3 = total * 0.5
desconto_3 = total - total_3
if quantidade <= 5:
    print(f'total: {desconto}')
elif quantidade > 5 and quantidade <= 10:
    print(f'total: {desconto_2}')
elif quantidade > 10:
    print(f'total: {desconto_3}')
else:
    ('=== FIM DO PROGRAMA ===')