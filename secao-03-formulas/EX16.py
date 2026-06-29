primeira_nota = float(input('Nota 1 (peso 2): '))
segunda_nota = float(input('Nota 2 (peso 3): '))
terceira_nota = float(input('Nota 3 (peso 5): '))
media_ponderada = (primeira_nota * 2 + segunda_nota * 3 + terceira_nota * 5) / 10

print(f'Média final: {media_ponderada:.2f}')
