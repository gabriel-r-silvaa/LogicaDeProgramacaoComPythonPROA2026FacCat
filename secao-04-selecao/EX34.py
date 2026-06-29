estoque_atual = int(input('Quantidade atual em estoque: '))
estoque_maximo = int(input('Quantidade máxima em estoque: '))
estoque_minimo = int(input('Quantidade mínima em estoque: '))

quantidade_media = (estoque_maximo + estoque_minimo) / 2

print(f'Quantidade média: {quantidade_media}')

if estoque_atual >= quantidade_media:
    print('Não efetuar compra')
else:
    print('Efetuar compra')
