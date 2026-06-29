nome_primeiro_time = input('Nome do 1º time: ')
nome_segundo_time = input('Nome do 2º time: ')
gols_primeiro_time = int(input(f'Gols do {nome_primeiro_time}: '))
gols_segundo_time = int(input(f'Gols do {nome_segundo_time}: '))

if gols_primeiro_time > gols_segundo_time:
    print(f'Vencedor: {nome_primeiro_time}')
elif gols_segundo_time > gols_primeiro_time:
    print(f'Vencedor: {nome_segundo_time}')
else:
    print('EMPATE')
