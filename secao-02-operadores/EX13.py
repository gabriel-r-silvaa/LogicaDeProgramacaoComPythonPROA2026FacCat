MARGEM_DISTRIBUIDOR = 0.28
ALIQUOTA_IMPOSTOS = 0.45

custo_fabrica = float(input('Custo de fábrica: R$ '))
margem_distribuidor = custo_fabrica * MARGEM_DISTRIBUIDOR
encargos_impostos = custo_fabrica * ALIQUOTA_IMPOSTOS
preco_final_consumidor = custo_fabrica + margem_distribuidor + encargos_impostos

print(f'Custo final ao consumidor: R$ {preco_final_consumidor:.2f}')
