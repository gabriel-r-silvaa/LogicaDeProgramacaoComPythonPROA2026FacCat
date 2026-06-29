primeiro_valor = float(input('Primeiro valor: '))
segundo_valor = float(input('Segundo valor: '))
terceiro_valor = float(input('Terceiro valor: '))

if primeiro_valor > segundo_valor:
    if primeiro_valor > terceiro_valor:
        maior_de_tres = primeiro_valor
    else:
        maior_de_tres = terceiro_valor
else:
    if segundo_valor > terceiro_valor:
        maior_de_tres = segundo_valor
    else:
        maior_de_tres = terceiro_valor

print(f'Maior valor: {maior_de_tres}')
