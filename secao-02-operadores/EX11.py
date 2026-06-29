total_eleitores = int(input('Total de eleitores: '))
votos_brancos = int(input('Votos brancos: '))
votos_nulos = int(input('Votos nulos: '))
votos_validos = int(input('Votos válidos: '))

percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

print(f'Brancos: {percentual_brancos:.2f}%')
print(f'Nulos: {percentual_nulos:.2f}%')
print(f'Válidos: {percentual_validos:.2f}%')
