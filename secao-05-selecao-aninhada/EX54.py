quantidade_lados = int(input('Número de lados (3, 4 ou 5): '))
medida_lado = float(input('Medida do lado (cm): '))

if quantidade_lados == 3:
    perimetro_triangulo = 3 * medida_lado
    print(f'TRIÂNGULO | Perímetro: {perimetro_triangulo:.2f} cm')
elif quantidade_lados == 4:
    area_quadrado = medida_lado * medida_lado
    print(f'QUADRADO | Área: {area_quadrado:.2f} cm²')
elif quantidade_lados == 5:
    print('PENTÁGONO')
