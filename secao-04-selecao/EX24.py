quantidade_macas = int(input('Quantidade de maçãs compradas: '))

if quantidade_macas < 12:
    custo_total = quantidade_macas * 1.30
else:
    custo_total = quantidade_macas * 1.00

print(f'Custo total: R$ {custo_total:.2f}')
