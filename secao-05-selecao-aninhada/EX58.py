lado_um = float(input('Lado A: '))
lado_dois = float(input('Lado B: '))
lado_tres = float(input('Lado C: '))

if lado_um == lado_dois == lado_tres:
    print('Triângulo Equilátero')
elif lado_um == lado_dois or lado_dois == lado_tres or lado_um == lado_tres:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')
