posicao_baixa = float(input('Primeiro valor: '))
posicao_media = float(input('Segundo valor: '))
posicao_alta = float(input('Terceiro valor: '))

if posicao_baixa > posicao_media:
    posicao_baixa, posicao_media = posicao_media, posicao_baixa

if posicao_baixa > posicao_alta:
    posicao_baixa, posicao_alta = posicao_alta, posicao_baixa

if posicao_media > posicao_alta:
    posicao_media, posicao_alta = posicao_alta, posicao_media

print(f'Ordem crescente: {posicao_baixa}, {posicao_media}, {posicao_alta}')
