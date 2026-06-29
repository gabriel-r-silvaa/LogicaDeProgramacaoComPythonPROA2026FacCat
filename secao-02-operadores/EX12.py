salario_atual = float(input('Salário atual: R$ '))
percentual_reajuste = float(input('Percentual de reajuste (%): '))
incremento_salarial = salario_atual * (percentual_reajuste / 100)
novo_salario = salario_atual + incremento_salarial

print(f'Novo salário: R$ {novo_salario:.2f}')
