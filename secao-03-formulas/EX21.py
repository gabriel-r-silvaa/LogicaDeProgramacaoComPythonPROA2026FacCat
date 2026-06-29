comprimento_pista_metros = float(input('Comprimento da pista (metros): '))
total_voltas_gp = int(input('Total de voltas no GP: '))
quantidade_reabastecimentos = int(input('Número de reabastecimentos: '))
consumo_km_l = float(input('Consumo do carro (Km/L): '))

segmentos_de_volta = quantidade_reabastecimentos + 1
voltas_ate_primeiro_abast = total_voltas_gp / segmentos_de_volta
distancia_primeiro_segmento = (comprimento_pista_metros / 1000) * voltas_ate_primeiro_abast
litros_minimos_necessarios = distancia_primeiro_segmento / consumo_km_l

print(f'Voltas até o 1º reabastecimento: {voltas_ate_primeiro_abast}')
print(f'Litros mínimos necessários: {litros_minimos_necessarios:.2f} L')
