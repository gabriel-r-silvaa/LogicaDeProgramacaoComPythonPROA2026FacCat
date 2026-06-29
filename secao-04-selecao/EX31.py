nome_pessoa = input('Nome: ')
altura_pessoa = float(input('Altura (m): '))
sexo_pessoa = input('Sexo (M/F): ').upper()

if sexo_pessoa == 'M':
    peso_ideal = (72.7 * altura_pessoa) - 58
else:
    peso_ideal = (62.1 * altura_pessoa) - 44.7

print(f'Peso ideal de {nome_pessoa}: {peso_ideal:.2f} kg')
