quantidade_lados = int(input('Número de lados do polígono: '))
medida_lado = float(input('Medida do lado (cm): '))

if quantidade_lados < 3:
    print("NÃO É UM POLÍGONO")
elif quantidade_lados == 3:
    perimetro_triangulo = 3 * medida_lado
    print(f'TRIÂNGULO | Perímetro: {perimetro_triangulo:.2f} cm')
elif quantidade_lados == 4:
    area_quadrado = medida_lado * medida_lado
    print(f'QUADRADO | Área: {area_quadrado:.2f} cm²')
elif quantidade_lados == 5:
    print('PENTÁGONO')
else:
    print('POLÍGONO NÃO IDENTIFICADO')
