PRECO_COMBUSTIVEL = 2.90

odometro_inicio_dia = float(input('Odômetro início do dia (Km): '))
odometro_fim_dia = float(input('Odômetro fim do dia (Km): '))
litros_consumidos = float(input('Litros de combustível gastos: '))
receita_passageiros = float(input('Valor total recebido dos passageiros: R$ '))

quilometragem_dia = odometro_fim_dia - odometro_inicio_dia
media_consumo_kml = quilometragem_dia / litros_consumidos
gasto_combustivel = litros_consumidos * PRECO_COMBUSTIVEL
lucro_liquido_dia = receita_passageiros - gasto_combustivel

print(f'Média de consumo: {media_consumo_kml:.2f} km/L')
print(f'Lucro líquido do dia: R$ {lucro_liquido_dia:.2f}')
