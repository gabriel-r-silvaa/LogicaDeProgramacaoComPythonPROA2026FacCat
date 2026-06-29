quantidade_veiculos_vendidos = int(input('Carros vendidos no mês: '))
valor_total_vendas = float(input('Valor total das vendas: R$ '))
salario_fixo_mensal = float(input('Salário fixo: R$ '))
bonificacao_por_veiculo = float(input('Valor recebido por carro vendido: R$ '))

comissao_unitaria = quantidade_veiculos_vendidos * bonificacao_por_veiculo
bonificacao_percentual = valor_total_vendas * 0.05
salario_final_vendedor = salario_fixo_mensal + comissao_unitaria + bonificacao_percentual

print(f'Salário final: R$ {salario_final_vendedor:.2f}')
