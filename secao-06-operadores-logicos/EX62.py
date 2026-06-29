nota_primeira_verificacao = float(input('Nota da 1ª verificação: '))
nota_segunda_verificacao = float(input('Nota da 2ª verificação: '))
nota_terceira_verificacao = float(input('Nota da 3ª verificação: '))
media_exercicios = float(input('Média dos exercícios: '))

media_aproveitamento = (
    nota_primeira_verificacao +
    nota_segunda_verificacao * 2 +
    nota_terceira_verificacao * 3 +
    media_exercicios
) / 7

if media_aproveitamento >= 9.0:
    conceito = 'A'
elif media_aproveitamento >= 7.5:
    conceito = 'B'
elif media_aproveitamento >= 6.0:
    conceito = 'C'
else:
    conceito = 'D'

print(f'Média de aproveitamento: {media_aproveitamento:.2f}')
print(f'Conceito: {conceito}')
