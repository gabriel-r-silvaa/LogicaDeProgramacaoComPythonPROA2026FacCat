primeiro_valor = float(input('Primeiro valor: '))
segundo_valor = float(input('Segundo valor: '))

if primeiro_valor < segundo_valor:
    print(f'Ordem crescente: {primeiro_valor}, {segundo_valor}')
else:
    print(f'Ordem crescente: {segundo_valor}, {primeiro_valor}')
