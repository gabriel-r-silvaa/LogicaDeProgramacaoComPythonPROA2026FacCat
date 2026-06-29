import math

WATTS_POR_METRO_QUADRADO = 18

potencia_lampada = float(input('Potência da lâmpada (watts): '))
largura_comodo = float(input('Largura do cômodo (m): '))
comprimento_comodo = float(input('Comprimento do cômodo (m): '))

area_comodo = largura_comodo * comprimento_comodo
potencia_necessaria = area_comodo * WATTS_POR_METRO_QUADRADO
quantidade_lampadas = math.ceil(potencia_necessaria / potencia_lampada)

print(f'Área: {area_comodo:.2f} m²')
print(f'Potência necessária: {potencia_necessaria:.2f} W')
print(f'Lâmpadas necessárias: {quantidade_lampadas}')
