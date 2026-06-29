primeira_avaliacao = float(input('1ª avaliação: '))
segunda_avaliacao = float(input('2ª avaliação: '))
media_aritmetica = (primeira_avaliacao + segunda_avaliacao) / 2

if media_aritmetica >= 6.0:
    print('Você foi aprovado!')
else:
    print('Você NÃO foi aprovado.')

print(f'Média: {media_aritmetica:.2f}')
