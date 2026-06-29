codigo_produto = int(input('Código de origem do produto: '))

regioes = {
    1: 'Sul',
    2: 'Norte',
    3: 'Leste',
    4: 'Oeste',
    5: 'Nordeste',
    6: 'Nordeste',
    7: 'Sudeste',
    8: 'Sudeste',
    9: 'Sudeste',
    10: 'Centro-Oeste',
    11: 'Noroeste',
}

procedencia = regioes.get(codigo_produto, 'Importado')

print(procedencia)
