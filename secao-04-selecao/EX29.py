hora_inicio = int(input('Hora de início do jogo: '))
hora_fim = int(input('Hora de fim do jogo: '))

if hora_fim >= hora_inicio:
    duracao_partida = hora_fim - hora_inicio
else:
    duracao_partida = 24 - hora_inicio + hora_fim

print(f'Duração da partida: {duracao_partida} hora(s)')
