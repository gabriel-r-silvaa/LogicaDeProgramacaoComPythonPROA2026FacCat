HORAS_SEMANAIS_NORMAIS = 40
SEMANAS_POR_MES = 4
LIMITE_HORAS_NORMAIS = HORAS_SEMANAIS_NORMAIS * SEMANAS_POR_MES

horas_trabalhadas_mes = float(input('Horas trabalhadas no mês: '))
valor_hora_normal = float(input('Salário por hora: R$ '))

if horas_trabalhadas_mes <= LIMITE_HORAS_NORMAIS:
    salario_total = horas_trabalhadas_mes * valor_hora_normal
else:
    horas_excedentes = horas_trabalhadas_mes - LIMITE_HORAS_NORMAIS
    valor_hora_extra = valor_hora_normal * 1.5
    salario_total = LIMITE_HORAS_NORMAIS * valor_hora_normal + horas_excedentes * valor_hora_extra

print(f'Salário total: R$ {salario_total:.2f}')
