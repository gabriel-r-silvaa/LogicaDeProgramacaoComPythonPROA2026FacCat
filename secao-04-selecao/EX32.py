salario_fixo = float(input('Salário fixo: R$ '))
total_vendas = float(input('Valor total das vendas: R$ '))

if total_vendas <= 1500:
    comissao_total = total_vendas * 0.03
else:
    comissao_total = 1500 * 0.03 + (total_vendas - 1500) * 0.05

salario_total = salario_fixo + comissao_total

print(f'Comissão: R$ {comissao_total:.2f}')
print(f'Salário total: R$ {salario_total:.2f}')
