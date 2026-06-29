primeira_avaliacao = float(input('Nota da 1ª avaliação: '))
segunda_avaliacao = float(input('Nota da 2ª avaliação: '))
media_semestral = (primeira_avaliacao + segunda_avaliacao) / 2

print(f'Média semestral: {media_semestral:.2f}')

if media_semestral >= 6.0:
    print('PARABÉNS! Você foi aprovado!')
else:
    print('Você foi REPROVADO! Estude mais...')
