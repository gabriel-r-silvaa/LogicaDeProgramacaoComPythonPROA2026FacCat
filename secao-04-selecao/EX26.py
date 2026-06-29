ano_atual = int(input('Ano atual: '))
ano_nascimento = int(input('Ano de nascimento: '))
idade_calculada = ano_atual - ano_nascimento

if idade_calculada >= 18:
    print(f'Com {idade_calculada} anos, PODERÁ votar este ano.')
else:
    print(f'Com {idade_calculada} anos, NÃO poderá votar este ano.')
