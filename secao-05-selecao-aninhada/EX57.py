posicao_alta = float(input('Primeiro valor: '))
posicao_media = float(input('Segundo valor: '))
posicao_baixa = float(input('Terceiro valor: '))

if posicao_alta < posicao_media:
    posicao_alta, posicao_media = posicao_media, posicao_alta

if posicao_alta < posicao_baixa:
    posicao_alta, posicao_baixa = posicao_baixa, posicao_alta

if posicao_media < posicao_baixa:
    posicao_media, posicao_baixa = posicao_baixa, posicao_media

print(f'Ordem decrescente: {posicao_alta}, {posicao_media}, {posicao_baixa}')
