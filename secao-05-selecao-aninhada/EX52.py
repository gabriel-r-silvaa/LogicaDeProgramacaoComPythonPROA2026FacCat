altura_pessoa = float(input('Altura (m): '))
codigo_sexo = int(input('Sexo (1-feminino, 2-masculino): '))

if codigo_sexo == 2:
    peso_ideal = (72.7 * altura_pessoa) - 58
else:
    peso_ideal = (62.1 * altura_pessoa) - 44.7

print(f'Peso ideal: {peso_ideal:.2f} kg')
