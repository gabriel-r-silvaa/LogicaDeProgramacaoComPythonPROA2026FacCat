valor_x = float(input('X: '))
valor_y = float(input('Y: '))
resultado_z = (valor_x * valor_y) + 5

if resultado_z <= 0:
    categoria_resposta = 'A'
elif resultado_z <= 100:
    categoria_resposta = 'B'
else:
    categoria_resposta = 'C'

print(f'Z: {resultado_z} | Resposta: {categoria_resposta}')
