angulo_um = float(input('Ângulo 1 (graus): '))
angulo_dois = float(input('Ângulo 2 (graus): '))
angulo_tres = float(input('Ângulo 3 (graus): '))

if angulo_um == 90 or angulo_dois == 90 or angulo_tres == 90:
    print('Triângulo Retângulo')
elif angulo_um > 90 or angulo_dois > 90 or angulo_tres > 90:
    print('Triângulo Obtusângulo')
else:
    print('Triângulo Acutângulo')
