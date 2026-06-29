import math

AREA_POR_CAIXA = 1.5

comprimento_cozinha = float(input('Comprimento da cozinha (m): '))
largura_cozinha = float(input('Largura da cozinha (m): '))
altura_cozinha = float(input('Altura da cozinha (m): '))

area_paredes = 2 * (comprimento_cozinha + largura_cozinha) * altura_cozinha
caixas_necessarias = math.ceil(area_paredes / AREA_POR_CAIXA)

print(f'Área total das paredes: {area_paredes:.2f} m²')
print(f'Caixas de azulejos necessárias: {caixas_necessarias}')
