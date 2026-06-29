lado_a = float(input('Lado a: '))
lado_b = float(input('Lado b: '))
lado_c = float(input('Lado c: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    if lado_a == lado_b == lado_c:
        mensagem = 'Triângulo Equilátero'
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        mensagem = 'Triângulo Isósceles'
    else:
        mensagem = 'Triângulo Escaleno'
else:
    mensagem = 'Não é possível formar um triângulo'

print(mensagem)
