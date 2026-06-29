lado_a = float(input('Lado A: '))
lado_b = float(input('Lado B: '))
lado_c = float(input('Lado C: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo.')
