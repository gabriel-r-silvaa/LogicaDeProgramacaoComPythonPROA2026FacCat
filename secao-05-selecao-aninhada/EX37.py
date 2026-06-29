primeiro_valor = float(input('Primeiro valor: '))
segundo_valor = float(input('Segundo valor: '))
terceiro_valor = float(input('Terceiro valor: '))

if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    menor_de_tres = primeiro_valor
elif segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor_de_tres = segundo_valor
else:
    menor_de_tres = terceiro_valor

soma_dois_maiores = primeiro_valor + segundo_valor + terceiro_valor - menor_de_tres

print(f'Soma dos dois maiores: {soma_dois_maiores}')
