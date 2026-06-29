anos_vividos = int(input('Anos: '))
meses_vividos = int(input('Meses: '))
dias_vividos = int(input('Dias: '))
total_dias_vividos = (anos_vividos * 365) + (meses_vividos * 30) + dias_vividos

print(f'Total de dias vividos: {total_dias_vividos} dias')
