primeira_avaliacao = float(input('Nota da 1ª avaliação: '))
segunda_avaliacao = float(input('Nota da 2ª avaliação: '))
nota_optativa = float(input('Nota da avaliação optativa (-1 se não fez): '))

nota_um = primeira_avaliacao
nota_dois = segunda_avaliacao

if nota_optativa != -1:
    if nota_um < nota_dois:
        nota_um = nota_optativa
    else:
        nota_dois = nota_optativa

media_semestral = (nota_um + nota_dois) / 2

print(f'Média semestral: {media_semestral:.2f}')

if media_semestral >= 6.0:
    print('Aprovado')
elif media_semestral < 3.0:
    print('Reprovado')
else:
    print('Em exame')
